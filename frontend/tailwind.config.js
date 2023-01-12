/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      backgroundImage: {
        'background': "url('/src/assets/lines.jpg')",
        'tree-leaves': "url('/src/assets/tree_leaves.jpg')",
      }
    }
  },
  plugins: [],
}
