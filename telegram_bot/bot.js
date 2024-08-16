// Load environment variables from .env file
require('dotenv').config();

// Import the TelegramBot class
const TelegramBot = require('node-telegram-bot-api');

// Create a new bot instance with the token from the environment variable
const bot = new TelegramBot(process.env.TELEGRAM_BOT_TOKEN, { polling: true });

// Listen for messages
bot.on('message', (msg) => {
  const chatId = msg.chat.id;
  const text = msg.text;

  // Simple response to any message
  bot.sendMessage(chatId, `You said: ${text}`);
});
