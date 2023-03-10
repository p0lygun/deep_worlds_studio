/** @type {import('tailwindcss').Config} */
module.exports = {
    darkMode: 'class',
    content: [
      "./**/templates/*.html",
      "./**/templates/**/*.html",
      "./**/static/*.js",
  ],
  theme: {
    extend: {
        colors: {
            "dark_mode":"#131414",
            "light_mode": "#071D31"
        },
        fontFamily: {
            kanit: ['Kanit', "sans-serif"],
        },
        backgroundImage: {
            'home-banner': "url('/static/images/home_banner_bg.png')"
        },
        gridTemplateColumns: {
            'values-section': 'repeat(auto-fit, minmax(245px, max-content))'
        }
    },
  },
  plugins: [],
}
