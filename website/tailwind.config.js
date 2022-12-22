/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      "./**/templates/*.html",
      "./**/static/*.js"
  ],
  theme: {
    extend: {
        colors: {
            "dark_mode":"#131414",
        },
        fontFamily: {
            kanit: ['Kanit', "sans-serif"],
        }
    },
  },
  plugins: [],
}
