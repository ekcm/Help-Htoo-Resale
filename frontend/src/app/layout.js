
import { Inter } from "next/font/google";
import "./globals.css";
import Body from "./Body";

const inter = Inter({ subsets: ["latin"] });

const onButtonClick = () => {
  console.log("Button clicked");
}


export const metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

export default function RootLayout() {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Body />
      </body>
    </html>
  );
}
