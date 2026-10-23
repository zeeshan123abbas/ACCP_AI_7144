# ---- nvm: manage Node versions ----
nvm install 20        # install Node 20 LTS
nvm install 22
nvm use 20            # switch the active version
nvm ls                # list installed versions

# ---- npm: manage project packages ----
npm init -y                 # create package.json
npm install chalk           # add a dependency
npm install -D nodemon      # add a development-only dependency
npm ls --depth=0            # list top-level packages
npm outdated                # see which packages have updates
npm uninstall chalk         # remove a package
npx cowsay "Hello Node"     # run a tool without installing it globally
