<?php
// cart.php?action=list | add&id=1 | remove&id=1 | clear
session_start();
require __DIR__ . '/db.php';
header('Content-Type: application/json');

$_SESSION['cart'] ??= [];          // [productId => qty]
$id = (int) ($_GET['id'] ?? 0);

switch ($_GET['action'] ?? 'list') {
    case 'add':
        $_SESSION['cart'][$id] = ($_SESSION['cart'][$id] ?? 0) + 1; break;
    case 'remove':
        if (isset($_SESSION['cart'][$id]) && --$_SESSION['cart'][$id] <= 0) unset($_SESSION['cart'][$id]); break;
    case 'clear':
        $_SESSION['cart'] = []; break;
}

$items = []; $total = 0;
if ($_SESSION['cart']) {
    $ids = array_keys($_SESSION['cart']);
    $in  = implode(',', array_fill(0, count($ids), '?'));
    $stmt = $pdo->prepare("SELECT id, name, price FROM products WHERE id IN ($in)");
    $stmt->execute($ids);
    foreach ($stmt as $p) {
        $qty = $_SESSION['cart'][$p['id']];
        $items[] = $p + ['qty' => $qty, 'subtotal' => $qty * $p['price']];
        $total += $qty * $p['price'];
    }
}
echo json_encode(['items' => $items, 'count' => array_sum($_SESSION['cart']), 'total' => $total]);
