#!/usr/bin/env python3
"""
🔥 fire - Where It All Began
A commemorative script celebrating Evans Samwel's first GitHub repository.
Created: May 17, 2018
"""

import sys
import time

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
YELLOW = "\033[33m"
BRIGHT_RED = "\033[91m"
BRIGHT_YELLOW = "\033[93m"
CYAN = "\033[96m"
GREEN = "\033[92m"

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

MESSAGE = """
Eight years ago, this repository was created with a single line: '# fire'.
No complex build systems, no large pipelines — just the pure curiosity
of learning Git, making that first commit, and joining the global GitHub
developer community.

Every great engineering journey begins with a single commit.
This is where the spark caught fire!
"""

def main():
    print(FIRE_ART)
    print(BANNER)
    print(MESSAGE.strip())
    print("\n" + "=" * 66 + "\n")

if __name__ == "__main__":
    main()
