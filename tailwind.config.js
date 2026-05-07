/** @type {import('tailwindcss').Config} */

module.exports = {

  content: [

    "./app/**/*.{js,ts,jsx,tsx,mdx}",

    "./components/**/*.{js,ts,jsx,tsx,mdx}",

    "./pages/**/*.{js,ts,jsx,tsx,mdx}"

  ],

  theme: {

    extend: {

      colors: {

        background: "#050816",

        card: "#0d1329",

        primary: "#00f0ff",

        secondary: "#7b2cff"

      },

      boxShadow: {

        glow: "0 0 30px rgba(0,240,255,0.3)"

      },

      borderRadius: {

        ultra: "30px"

      }

    }

  },

  plugins: []

}
