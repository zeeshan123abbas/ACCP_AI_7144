import nodemailer from "nodemailer";
import { config } from "../config.js";

let transporter;

async function getTransporter() {
  if (transporter) return transporter;
  if (config.smtp.host) {
    transporter = nodemailer.createTransport({
      host: config.smtp.host,
      port: config.smtp.port,
      auth: { user: config.smtp.user, pass: config.smtp.pass },
    });
  } else {
    // No SMTP configured: create a free Ethereal test account automatically
    const test = await nodemailer.createTestAccount();
    transporter = nodemailer.createTransport({
      host: "smtp.ethereal.email",
      port: 587,
      auth: { user: test.user, pass: test.pass },
    });
  }
  return transporter;
}

export async function sendWelcomeEmail(to, name) {
  const t = await getTransporter();
  const info = await t.sendMail({
    from: '"Course Portal" <no-reply@example.com>',
    to,
    subject: "Welcome to the MERN course",
    text: `Hi ${name}, your registration is confirmed.`,
    html: `<p>Hi <b>${name}</b>, your registration is confirmed.</p>`,
  });
  return nodemailer.getTestMessageUrl(info) || info.messageId; // preview link for Ethereal
}
