# I use Arch, FYI.

## Introduction
What is common in new parents and someone who installs
[Arch](https://archlinux.org/)?
A lot of things actually:
1. Both are sleepy as they had to stay up all night.
2. Both say "It's hard work, but it is totally worth it!"
3. Both can't wait to show the world the picture of their new baby!

Ok, so you installed Arch and have been
running [neofetch](https://archlinux.org/packages/?q=neofetch) again and
again to bask in your glory. Why not get **i-use-arch.fyi/yourname** and
tell the world!

## Rules

Rules are simple:
1. If a folder is not claimed, you can grab it.
2. You can always modify a folder that you have previously edited, as long
as your are using the same github username. Try to update your page once
every 3 months to keep it active (see below).
3. If a folder hasn't been edited for 3 months, you can claim it! No
notifications or emails would be sent to the existing user.
4. Only neofetch (or closely related) output from an Arch installation is
allowed. My ([sarvjeets](https://github.com/sarvjeets)) decision on what
is neofetch and what is not is final.
5. I ([sarvjeets](https://github.com/sarvjeets)) can modify these rules or
add new ones without notice.
6. Have fun and be nice!

## How to add your own page

1. Start by
[forking](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
[this](https://github.com/sarvjeets/i-use-arch) repository.
2. On your Arch computer:
~~~
# Make sure you have neofetch and python3 installed. Otherwise run:
# pacman -S python neofetch

$ git clone https://github.com/username/i-use-arch.git
$ cd i-use-arch
$ mkdir folder_of_your_choice  # Skip if you are updating an existing page
$ python3 ./scripts/plain-ascii.py > folder_of_your_choice/index.html
~~~
3. Create a
[pull request](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)
 for your changes.

