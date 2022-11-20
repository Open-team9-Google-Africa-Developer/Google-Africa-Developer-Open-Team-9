import Head from 'next/head'
import Footer from '../components/footer'
import Hero from '../components/hero'
import Navbar from '../components/navbar'

export default function Home() {
  return (
    <>
      <Head>
        <title>Safeguard | Your Ultimate community Security system</title>
        <meta name="description" content="Your Ultimate community Security system" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      
      <Navbar />
      <Hero />
      <Footer />

    </>
  )
}
