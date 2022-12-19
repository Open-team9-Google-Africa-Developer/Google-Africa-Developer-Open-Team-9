import Head from "next/head";
import Footer from "../components/footer";
import Hero from "../components/hero";
import Navbar from "../components/navbar";
import ComplaintList from "../components/complaintList";

export default function Home({ complaints }) {
  return (
    <>
      <Head>
        <title>Safeguard | Your Ultimate community Security system</title>
        <meta
          name="description"
          content="Your Ultimate community Security system"
        />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Navbar />
      <Hero />

      <div className="bg-white">
        <div className="mx-auto max-w-2xl py-16 px-4 sm:py-24 sm:px-6 lg:max-w-7xl lg:px-8">
          <h2 className="text-2xl font-bold tracking-tight text-gray-900">
            Recent Filed Complaints
          </h2>

          <ComplaintList complaints={complaints} />
        </div>
      </div>

      <Footer />
    </>
  );
}

export async function getStaticProps() {
  const res = await fetch("http://127.0.0.1:8000/api/complaints");
  const complaints = await res.json();

  return {
    props: { complaints },
  };
}
