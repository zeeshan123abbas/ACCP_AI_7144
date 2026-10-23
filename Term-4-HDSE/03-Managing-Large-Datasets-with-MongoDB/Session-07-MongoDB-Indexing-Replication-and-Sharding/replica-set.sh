# Create data folders and start three mongod processes (each in its own terminal, or add --fork on Linux/macOS)
mkdir -p rs/1 rs/2 rs/3
mongod --replSet rs0 --port 27018 --dbpath rs/1 --bind_ip localhost
mongod --replSet rs0 --port 27019 --dbpath rs/2 --bind_ip localhost
mongod --replSet rs0 --port 27020 --dbpath rs/3 --bind_ip localhost

# Initiate the set from mongosh
mongosh --port 27018 --eval '
rs.initiate({ _id: "rs0", members: [
  { _id: 0, host: "localhost:27018" },
  { _id: 1, host: "localhost:27019" },
  { _id: 2, host: "localhost:27020" } ] })'

# Check status, then stop the primary and watch a new one being elected
mongosh --port 27018 --eval 'rs.status().members.forEach(m => print(m.name, m.stateStr))'

# Applications connect with all members listed:
# mongodb://localhost:27018,localhost:27019,localhost:27020/?replicaSet=rs0
