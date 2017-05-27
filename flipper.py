# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from upsidedown import transform
from sopel.module import rule

@rule('^flips (.+)')
def flips(bot, trigger):
    bot.say("(╯°□°）╯︵ %s" % transform(trigger.group(1)))

@rule('^rolls (.+)')
def roll(bot, trigger):
    target = trigger.group(1)
    if target.endswith(' down a hill'):
        target = target[:-12]
        hill = True
    else:
        hill = False
    tegrat = transform(target)
    if hill:
        bot.say("%s %s %s %s %s (@_@;)" % (tegrat, target, tegrat, target, tegrat))
    else:
        bot.say(tegrat)
