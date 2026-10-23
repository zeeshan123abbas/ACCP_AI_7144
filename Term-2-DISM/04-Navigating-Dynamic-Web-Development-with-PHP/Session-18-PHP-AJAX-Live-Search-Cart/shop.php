<?php
// shop.php
require __DIR__ . '/db.php';
$products = $pdo->query("SELECT id, name, price FROM products")->fetchAll();
?>
<!DOCTYPE html><html><head><title>Book Shop</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"></head>
<body class="container py-4">
<h3>Book Shop <span class="badge bg-primary" id="badge">0</span></h3>
<div class="row">
  <div class="col-md-7">
    <?php foreach ($products as $p): ?>
      <div class="d-flex justify-content-between border rounded p-2 mb-2">
        <span><?= e($p['name']) ?> — Rs <?= number_format($p['price']) ?></span>
        <button class="btn btn-sm btn-success" onclick="cart('add', <?= $p['id'] ?>)">Add to cart</button>
      </div>
    <?php endforeach; ?>
  </div>
  <div class="col-md-5">
    <h5>Your cart</h5>
    <table class="table table-sm" id="cartTable"></table>
    <p><b>Total: Rs <span id="total">0</span></b></p>
    <button class="btn btn-outline-danger btn-sm" onclick="cart('clear')">Clear</button>
    <button class="btn btn-primary btn-sm" onclick="alert('Checkout: order summary would be saved here (no payment).')">Checkout</button>
  </div>
</div>
<script>
async function cart(action = 'list', id = 0) {
  const res = await fetch(`cart.php?action=${action}&id=${id}`);
  const data = await res.json();
  document.getElementById('badge').textContent = data.count;
  document.getElementById('total').textContent = data.total.toLocaleString();
  const table = document.getElementById('cartTable');
  table.innerHTML = '';
  data.items.forEach(i => {
    const tr = table.insertRow();
    tr.insertCell().textContent = i.name;
    tr.insertCell().textContent = '× ' + i.qty;
    const btn = document.createElement('button');
    btn.className = 'btn btn-sm btn-link text-danger'; btn.textContent = 'remove';
    btn.onclick = () => cart('remove', i.id);
    tr.insertCell().appendChild(btn);
  });
}
cart();
</script>
</body></html>
