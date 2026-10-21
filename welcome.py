#!/usr/bin/env python3
"""
🔥 fire - Where It All Began
A commemorative script celebrating Evans Samwel's first GitHub repository.
Created: May 17, 2018
Branch: feature/hello-github
"""

import sys
import time
import random
from datetime import date

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
YELLOW = "\033[33m"
BRIGHT_RED = "\033[91m"
BRIGHT_YELLOW = "\033[93m"
CYAN = "\033[96m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"

GENESIS_DATE = date(2018, 5, 17)

def get_years_elapsed():
    today = date.today()
    return today.year - GENESIS_DATE.year - ((today.month, today.day) < (GENESIS_DATE.month, GENESIS_DATE.day))

FIRE_ART = f"""
{BRIGHT_RED}                 (        {RESET}
{BRIGHT_YELLOW}          )      )        {RESET}
{BRIGHT_RED}         (     (          {RESET}
{BRIGHT_YELLOW}   (     )     )          {RESET}
{RED}    )   (     (     (     {RESET}
{BRIGHT_YELLOW}   (     )     )     )    {RESET}
{BRIGHT_RED}    )   (  (  (     (     {RESET}
{YELLOW}   (     )(    )     )    {RESET}
{BRIGHT_YELLOW}  (     (  )  (     (  )  {RESET}
{BRIGHT_RED}   )  (  )(    )  (  )(   {RESET}
{RED}  (  (  (  )  (  (  (  )  {RESET}
{YELLOW} /========================\\{RESET}
{RED}|  🔥  F  I  R  E  . G I T  |{RESET}
{YELLOW} \\========================/{RESET}
"""

BANNER = f"""
{BOLD}{CYAN}╔══════════════════════════════════════════════════════════════════╗{RESET}
{BOLD}{CYAN}║{RESET}                 {BOLD}{BRIGHT_YELLOW}WELCOME TO GITHUB — THE GENESIS{RESET}                  {BOLD}{CYAN}║{RESET}
{BOLD}{CYAN}╠══════════════════════════════════════════════════════════════════╣{RESET}
{BOLD}{CYAN}║{RESET}  👤 Author:     {GREEN}Evans Samwel (@evanssamwel){RESET}                      {BOLD}{CYAN}║{RESET}
{BOLD}{CYAN}║{RESET}  📅 Inception:  {YELLOW}May 17, 2018{RESET}                                     {BOLD}{CYAN}║{RESET}
{BOLD}{CYAN}║{RESET}  🎯 Milestone:  {BRIGHT_RED}Repository #1 (Where It All Started){RESET}             {BOLD}{CYAN}║{RESET}
{BOLD}{CYAN}║{RESET}  🌿 Branches:   {CYAN}master | develop | feature/hello-github{RESET}          {BOLD}{CYAN}║{RESET}
{BOLD}{CYAN}╚══════════════════════════════════════════════════════════════════╝{RESET}
"""

QUOTES = [
    ("Zig Ziglar", "You don't have to be great to start, but you have to start to be great."),
    ("Linus Torvalds", "Talk is cheap. Show me the code."),
    ("Grace Hopper", "The most dangerous phrase in the language is, 'We've always done it this way.'"),
    ("Steve Jobs", "The only way to do great work is to love what you do."),
    ("Kent Beck", "Make it work, make it right, make it fast."),
]

def show_quote():
    author, text = random.choice(QUOTES)
    print(f"\n{BOLD}{YELLOW}💬 Developer Wisdom:{RESET}")
    print(f'   "{text}"')
    print(f"   — {BOLD}{CYAN}{author}{RESET}\n")

def run_flame_animation(frames=12):
    """Animates a warm flickering campfire in the terminal."""
    flame_variations = [
        f"{BRIGHT_RED}    (  .      )     \n   )           (    \n  (   .  )      )   \n   ) (   (   .  )   \n  (   )   ) (   )   \n   \\ (___/___) /    \n    `---------'     {RESET}",
        f"{BRIGHT_YELLOW}     .  )    (      \n   (          )     \n    )  . (   (      \n  (   )   ) (   )   \n   ) (   (   ) (    \n   \\ (___/___) /    \n    `---------'     {RESET}",
        f"{YELLOW}   (     (   .  )   \n    )     )     (   \n   (   . (   (   )  \n    ) (   )   ) (   \n  (   )  (   (   )  \n   \\ (___/___) /    \n    `---------'     {RESET}",
    ]
    print(f"\n{BOLD}{BRIGHT_YELLOW}🔥 Igniting the flame...{RESET}\n")
    try:
        for i in range(frames):
            frame = flame_variations[i % len(flame_variations)]
            sys.stdout.write(f"\r\033[K{frame}\n\033[7A")
            sys.stdout.flush()
            time.sleep(0.2)
        print("\n" * 7)
    except KeyboardInterrupt:
        print("\n")

def interactive_mode():
    """Generates a personalized welcome badge."""
    print(f"\n{BOLD}{CYAN}🎉 Welcome to GitHub — Personalized Badge Creator{RESET}")
    print("-" * 55)
    name = input(f"{BOLD}Enter your name (or GitHub handle): {RESET}").strip() or "Explorer"
    lang = input(f"{BOLD}Your favorite programming language: {RESET}").strip() or "Git & Code"
    year = input(f"{BOLD}What year did you join GitHub? {RESET}").strip() or "2018"
    
    badge = f"""
{BOLD}{MAGENTA}╔══════════════════════════════════════════════════════╗{RESET}
{BOLD}{MAGENTA}║{RESET}            {BOLD}{BRIGHT_YELLOW}✨ GITHUB DEVELOPER PASSPORT ✨{RESET}           {BOLD}{MAGENTA}║{RESET}
{BOLD}{MAGENTA}╠══════════════════════════════════════════════════════╣{RESET}
{BOLD}{MAGENTA}║{RESET}  🧑 Name:       {GREEN}{name:<36}{RESET}{BOLD}{MAGENTA}║{RESET}
{BOLD}{MAGENTA}║{RESET}  💻 Passion:    {CYAN}{lang:<36}{RESET}{BOLD}{MAGENTA}║{RESET}
{BOLD}{MAGENTA}║{RESET}  🚀 Explorer Since: {YELLOW}{year:<32}{RESET}{BOLD}{MAGENTA}║{RESET}
{BOLD}{MAGENTA}║{RESET}  🔥 Origin:     {BRIGHT_RED}{'fire (evanssamwel/fire)':<36}{RESET}{BOLD}{MAGENTA}║{RESET}
{BOLD}{MAGENTA}╚══════════════════════════════════════════════════════╝{RESET}
"""
    print(badge)
    print(f"{GREEN}Welcome to the world of open source, {name}! Never stop building.{RESET}\n")

def get_message():
    years = get_years_elapsed()
    return f"""
Over {years} years ago on May 17, 2018, this repository was created with
a single line: '# fire'. No complex build systems, no large pipelines —
just the pure curiosity of learning Git, making that first commit,
and joining the global GitHub developer community.

Every great engineering journey begins with a single commit.
This is where the spark caught fire!
"""

def main():
    if "--interactive" in sys.argv or "-i" in sys.argv:
        interactive_mode()
        return

    if "--flame" in sys.argv or "-f" in sys.argv:
        run_flame_animation()
        return

    if "--quote" in sys.argv or "-q" in sys.argv:
        show_quote()
        return

    print(FIRE_ART)
    print(BANNER)
    print(get_message().strip())
    print("\n" + "=" * 66)
    print(f"{BOLD}Feature branch enhancements available:{RESET}")
    print(f"  • Run with {CYAN}--interactive{RESET} to create your custom developer passport")
    print(f"  • Run with {BRIGHT_YELLOW}--flame{RESET}       to watch the fire animation")
    print(f"  • Run with {MAGENTA}--quote{RESET}       to read developer wisdom")
    print("=" * 66 + "\n")

if __name__ == "__main__":
    main()
