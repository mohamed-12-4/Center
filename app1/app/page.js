'use client';
import Image from 'next/image'
import Link from 'next/link'
import { useAuthContext } from '@/context/AuthContext';
import  logout  from '@/firebase/auth/signout'
export default function Home() {

  const { user } = useAuthContext()

  if ( user !== null ) {
    return (
      <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <h1>
        Hello { user?.email }
      </h1>
    </main>

    )
  }
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <h1>
        Hello { user?.email }
        <br />
        <Link href="/signup">
          Sign Up
        </Link>
        <Link href="login">
          Login
        </Link>
        <br />
      </h1>
    </main>
  )
}
