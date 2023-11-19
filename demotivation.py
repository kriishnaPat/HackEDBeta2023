# Print a random demotivational message
import random

demotivational_messages = [
    "Just because you're unique doesn't mean you are useful.",
    "The sooner you fall behind, the more time you'll have to catch up.",
    "Dream big, work hard, stay focused... for what? Life is short and then you die.",
    "If at first, you don't succeed, maybe skydiving isn't for you.",
    "You're not stupid; you just have bad luck thinking.",
    "Don't follow your dreams; chase them away.",
    "The glass is neither half-full nor half-empty; it's twice as large as it needs to be.",
    "Do what you love, and you'll never work a day in your life... because nobody will hire you.",
    "The early bird might get the worm, but the second mouse gets the cheese.",
    "Teamwork makes the dream work, but a nightmare's a dream too.",
    "Here's another demotivational message.",
    "This is just filler text for the example.",
    "You thought there'd be a motivational one here? Nope.",
    "You can't always get what you want, and you probably won't.",
    "This message is not inspiring in any way.",
    "Life is short. Smile while you still have teeth.",
    "Procrastination is the art of keeping up with yesterday.",
    "Some people are like clouds. When they go away, it's a brighter day.",
    "Don't aim for success if you want it; just do what you love, and success will follow. Or not.",
    "When nothing goes right, go left.",
    "Procrastination: because eventually is good enough."
    "Failure is the foundation of success, and the road to success is always under construction."
    "Ambition is a poor excuse for not having enough sense to be lazy."
    "If at first, you don't succeed, maybe this just isn't for you."
    "Dream big, work hard, fail miserably."
    "Effort is like toothpaste – you can always squeeze out just a little bit more."
    "Success is relative. The more success, the more relatives."
    "If opportunity doesn't knock, build a door. Then realize you're not a carpenter."
    "The only thing standing between you and your goal is the story you keep telling yourself."
    "Expect the worst, and you'll never be disappointed."
    "Success is for those who can tolerate the unbearable boredom of repetitive tasks."
    "Follow your dreams, except the one where you're naked in public – that's a nightmare."
    "Pro tip: Lower your expectations to increase your satisfaction."
    "The only thing that comes to those who wait is more waiting."
    "Motivation is like a cup of coffee – it wears off, and you're still left with the bitter taste of reality."
    "Perfection is overrated. Embrace your mediocrity; it's less stressful."
    "The harder you work, the luckier your lazier friend seems to get."
    "Life is like a rollercoaster: sometimes it's thrilling, but most of the time, you just want it to stop."
    "If life gives you lemons, just remember that life probably forgot to give you sugar and water too."
]

def return_demotivation():
    randsss = random.randint(0,len(demotivational_messages)-1)
    return demotivational_messages[randsss]