import "./globals.css";

export const metadata = {

  title: "AI Command OS",

  description: "Built for Rehman Saifi",

};

export default function RootLayout({ children }) {

  return (

    <html lang="en">

      <body>

        {children}

      </body>

    </html>

  );

}
