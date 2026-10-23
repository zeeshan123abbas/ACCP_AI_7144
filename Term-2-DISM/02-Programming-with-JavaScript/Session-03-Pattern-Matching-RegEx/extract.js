// Run: node extract.js
const log = `
2026-03-01 10:15 ORDER #A1023 total Rs. 4,500 by ali@example.com
2026-03-01 11:02 ORDER #A1024 total Rs. 12,300 by sara@shop.pk
2026-03-02 09:40 REFUND #A1023 amount Rs. 4,500
`;

// 1. Named groups with matchAll
const orderRe = /(?<date>\d{4}-\d{2}-\d{2}) \d{2}:\d{2} ORDER #(?<id>A\d+) total Rs\. (?<amount>[\d,]+)/g;
const orders = [...log.matchAll(orderRe)].map(m => ({
  id: m.groups.id,
  date: m.groups.date,
  amount: Number(m.groups.amount.replace(/,/g, ""))
}));
console.table(orders);

// 2. All emails
console.log("Emails:", log.match(/[\w.+-]+@[\w-]+\.[\w.]+/g));

// 3. Reformat dates YYYY-MM-DD -> DD/MM/YYYY
console.log(log.replace(/(\d{4})-(\d{2})-(\d{2})/g, "$3/$2/$1").trim());

// 4. Replace with a function: mask emails
const masked = log.replace(/([\w.+-])[\w.+-]*@/g, (_, first) => `${first}***@`);
console.log(masked.trim());

// 5. Split on commas, semicolons or pipes with optional spaces
console.log("PHP, MySQL;Laravel | WordPress".split(/\s*[,;|]\s*/));

// 6. Greedy vs lazy
const html = "<b>bold</b> and <i>italic</i>";
console.log(html.match(/<.+>/)[0]);   // greedy: whole string
console.log(html.match(/<.+?>/g));    // lazy: each tag
