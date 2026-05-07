"use client";

import { motion } from "framer-motion";

export default function Header() {

    return (

        <motion.header

            initial={{
                opacity: 0,
                y: -30
            }}

            animate={{
                opacity: 1,
                y: 0
            }}

            transition={{
                duration: 0.5
            }}

            className="w-full border-b border-white/10 backdrop-blur-xl bg-white/5 sticky top-0 z-50"
        >

            <div className="max-w-7xl mx-auto px-6 py-5 flex items-center justify-between">

                {/* LEFT */}

                <div className="flex items-center gap-4">

                    <div className="
                        w-12
                        h-12
                        rounded-2xl
                        bg-gradient-to-r
                        from-cyan-400
                        to-violet-500
                        flex
                        items-center
                        justify-center
                        text-2xl
                        shadow-2xl
                        shadow-cyan-500/30
                    ">

                        🚀

                    </div>

                    <div>

                        <h1 className="
                            text-2xl
                            font-bold
                            tracking-wide
                        ">

                            AI Command OS

                        </h1>

                        <p className="
                            text-sm
                            text-gray-400
                        ">

                            Built for Rehman Saifi

                        </p>

                    </div>

                </div>

                {/* RIGHT */}

                <div className="
                    hidden
                    md:flex
                    items-center
                    gap-3
                ">

                    <button className="
                        px-5
                        py-2
                        rounded-2xl
                        bg-white/10
                        hover:bg-white/20
                        transition-all
                    ">

                        Research

                    </button>

                    <button className="
                        px-5
                        py-2
                        rounded-2xl
                        bg-white/10
                        hover:bg-white/20
                        transition-all
                    ">

                        Analyze

                    </button>

                    <button className="
                        px-5
                        py-2
                        rounded-2xl
                        bg-gradient-to-r
                        from-cyan-400
                        to-violet-500
                        hover:scale-105
                        transition-all
                        shadow-2xl
                        shadow-cyan-500/20
                    ">

                        Generate

                    </button>

                </div>

            </div>

        </motion.header>

    );

}
