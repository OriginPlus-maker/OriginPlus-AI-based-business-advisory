/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        origin: {
          green: {
            DEFAULT: '#1B4D3E',
            dark: '#12352B',
            light: '#276E59',
            surface: '#EBF4F0',
            border: '#B8D8CC',
          },
          navy: {
            DEFAULT: '#0B2545',
            dark: '#07182C',
            light: '#133E70',
            surface: '#EEF3F8',
          },
          saffron: {
            DEFAULT: '#D97706',
            dark: '#B45309',
            light: '#FBBF24',
            surface: '#FEF3C7',
          },
          canvas: '#FAF9F6',
          card: '#FFFFFF',
          border: '#E2E8F0',
          text: {
            primary: '#0F172A',
            secondary: '#475569',
            muted: '#64748B',
          }
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
      },
      boxShadow: {
        'gov': '0 1px 3px 0 rgba(0, 0, 0, 0.05), 0 1px 2px 0 rgba(0, 0, 0, 0.03)',
        'gov-card': '0 4px 6px -1px rgba(11, 37, 69, 0.06), 0 2px 4px -1px rgba(11, 37, 69, 0.03)',
        'gov-lg': '0 10px 25px -5px rgba(27, 77, 62, 0.1), 0 8px 10px -6px rgba(27, 77, 62, 0.05)',
      }
    },
  },
  plugins: [],
}

