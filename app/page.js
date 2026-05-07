export default function UltraAIUI() { return ( <div className="min-h-screen bg-[#050816] text-white flex flex-col"> {/* Header */} <header className="flex items-center justify-between px-6 py-5 border-b border-white/10 backdrop-blur-xl bg-white/5 sticky top-0 z-50"> <div className="flex items-center gap-3"> <div className="w-11 h-11 rounded-2xl bg-gradient-to-r from-cyan-400 to-violet-500 flex items-center justify-center text-2xl shadow-2xl shadow-cyan-500/30"> 🚀 </div>

<div>
        <h1 className="text-2xl font-bold tracking-wide">
          AI Command OS
        </h1>
        <p className="text-sm text-gray-400">
          Built for Rehman Saifi
        </p>
      </div>
    </div>

    <div className="hidden md:flex items-center gap-3">
      <button className="px-4 py-2 rounded-xl bg-white/10 hover:bg-white/20 transition-all">
        Research
      </button>

      <button className="px-4 py-2 rounded-xl bg-white/10 hover:bg-white/20 transition-all">
        Analyze
      </button>

      <button className="px-4 py-2 rounded-xl bg-gradient-to-r from-cyan-400 to-violet-500 shadow-lg shadow-cyan-500/20 hover:scale-105 transition-all">
        Generate
      </button>
    </div>
  </header>

  {/* Main */}
  <main className="flex-1 flex overflow-hidden">
    {/* Sidebar */}
    <aside className="hidden lg:flex w-80 border-r border-white/10 bg-white/5 backdrop-blur-xl flex-col p-5 gap-5">
      <div>
        <h2 className="text-lg font-semibold mb-3 text-cyan-400">
          AI Platforms
        </h2>

        <div className="space-y-3">
          {[
            'Reddit',
            'Quora',
            'StackOverflow',
            'Hacker News',
            'Dev.to',
            'Product Hunt'
          ].map((item) => (
            <div
              key={item}
              className="p-4 rounded-2xl bg-white/5 border border-white/10 hover:border-cyan-400/50 transition-all cursor-pointer"
            >
              {item}
            </div>
          ))}
        </div>
      </div>

      <div className="mt-auto p-5 rounded-3xl bg-gradient-to-r from-cyan-500/10 to-violet-500/10 border border-cyan-500/20">
        <h3 className="text-lg font-bold mb-2">
          Live AI Status
        </h3>

        <p className="text-gray-300 text-sm leading-7">
          Scanning real discussions...
          <br />
          Finding trending problems...
          <br />
          Generating human-like answers...
        </p>
      </div>
    </aside>

    {/* Chat Section */}
    <section className="flex-1 flex flex-col">
      {/* Chat Area */}
      <div className="flex-1 overflow-y-auto px-5 py-8 space-y-6">
        {/* AI Message */}
        <div className="flex items-start gap-4">
          <div className="w-12 h-12 rounded-2xl bg-gradient-to-r from-cyan-400 to-violet-500 flex items-center justify-center text-xl shadow-xl shadow-cyan-500/30">
            🤖
          </div>

          <div className="max-w-3xl p-6 rounded-3xl bg-white/5 border border-white/10 backdrop-blur-xl shadow-2xl">
            <h2 className="text-xl font-bold mb-3 text-cyan-400">
              AI Command Center
            </h2>

            <p className="text-gray-300 leading-8">
              Ask anything.
              <br />
              Research real platform data.
              <br />
              Analyze problems.
              <br />
              Generate human-like posts.
              <br />
              Build AI-powered systems.
            </p>
          </div>
        </div>

        {/* User Message */}
        <div className="flex items-start justify-end gap-4">
          <div className="max-w-2xl p-6 rounded-3xl bg-gradient-to-r from-cyan-500 to-violet-500 shadow-2xl shadow-cyan-500/20">
            <p className="leading-8">
              Find real AI automation problems from Reddit and Dev.to
            </p>
          </div>

          <div className="w-12 h-12 rounded-2xl bg-white/10 flex items-center justify-center text-xl border border-white/10">
            👤
          </div>
        </div>

        {/* AI Thinking */}
        <div className="flex items-start gap-4">
          <div className="w-12 h-12 rounded-2xl bg-gradient-to-r from-cyan-400 to-violet-500 flex items-center justify-center text-xl shadow-xl shadow-cyan-500/30 animate-pulse">
            ⚡
          </div>

          <div className="max-w-3xl p-6 rounded-3xl bg-white/5 border border-cyan-500/20 backdrop-blur-xl shadow-2xl">
            <p className="text-cyan-300 leading-8 animate-pulse">
              Scanning Reddit...
              <br />
              Reading Dev.to discussions...
              <br />
              Finding trending automation problems...
            </p>
          </div>
        </div>
      </div>

      {/* Input */}
      <div className="p-5 border-t border-white/10 bg-[#050816]/80 backdrop-blur-2xl sticky bottom-0">
        <div className="max-w-5xl mx-auto flex items-center gap-4 p-4 rounded-3xl border border-white/10 bg-white/5 shadow-2xl">
          <button className="w-14 h-14 rounded-2xl bg-white/10 hover:bg-white/20 transition-all text-2xl">
            +
          </button>

          <input
            type="text"
            placeholder="Ask AI anything or give commands..."
            className="flex-1 bg-transparent outline-none text-lg placeholder:text-gray-500"
          />

          <button className="px-8 py-4 rounded-2xl bg-gradient-to-r from-cyan-400 to-violet-500 hover:scale-105 transition-all shadow-2xl shadow-cyan-500/20 font-bold">
            Run AI
          </button>
        </div>
      </div>
    </section>
  </main>
</div>

) }
