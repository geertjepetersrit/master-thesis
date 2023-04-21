label dilemma1:
    "You hear someone joking about ethnicities by using a derogatory term."
    show chad at above_right with moveinright
    c "\“Hehe, of course those {i}tacoheads{/i} take as much free food samples as possible.\”"
    hide chad with Dissolve(0.5)
    call show_npc
    if is_dutch:
        s "What’s so funny about it? I think it’s kinda offensive."
    else:
        j "What’s so funny about it? I think it’s kinda offensive."

    call hide_npc
    show chad at above_right with moveinright
    c "Whatever. I have friends who belong to this group, so I can do that. They don’t seem to mind it."

    "You decide that this is none of your business and try to ignore the conversation, but the person who confronted Chad earlier doesn’t buy it."
    "It looks like things are going south…"

    # Trivial choice
    label .confront_chad:
        menu:
            "What will you do?"

            "Wait until it passes over.":
                $renpy.fix_rollback()
                "You put in your earbuds and crank up the volume to 100. Bye outside world and its drama."

            "Try to cool it down.":
                $renpy.fix_rollback()
                "You attempt to break it off."
                if is_dutch:
                    j "Excuse me, but I would appreciate it if you would stop arguing. It stresses me out, please. Thank you."
                else:
                    s "Excuse me, but I would appreciate it if you would stop arguing. It stresses me out, please. Thank you."

    hide chad with Dissolve(0.5)
    "Unfortunately, your strategy doesn’t work and the two people continue disagreeing."
    "Hence, you try to distract yourself by texting your best friend, describing the situation you’re in."
    "They reply with: \“OK, yeah that sucks. I would try not to get involved in that, but what’s your own opinion about it?\”"

    # Consequential choice
    label .text_reply:
        menu:
            "\“Do you think that joke was appropriate?\”"

            "I don’t know, not enough context.":
                $answer1 = "idk"
                $renpy.fix_rollback()
                $send_to_file("choices.txt", "\nDilemma 1: " + answer1)
                if is_dutch:
                    j "\“I think I can’t be the judge of that. I don’t know these people at all.\”"
                else:
                    s "\“I think I can’t be the judge of that. I don’t know these people at all.\”"
            "No.":
                $answer1 = "no"
                $renpy.fix_rollback()
                $send_to_file("choices.txt", "\nDilemma 1: " + answer1)
                $score += 1
                if is_dutch:
                    j "\“Of course not. People shouldn’t make jokes about this and try to come up with lame excuses when others call them out.\”"
                else:
                    s "\“Of course not. People shouldn’t make jokes about this and try to come up with lame excuses when others call them out.\”"

    "You look up from your phone and notice the discussion has ended. At least verbally. "

    # Version A
    call switch_chad

    return

label dilemma2:
    menu:
        "What will you do?"

        "Dodge them and pretend it didn’t happen.":
            $answer2 = "dodge"
            $renpy.fix_rollback()
            $send_to_file("choices.txt", "\nDilemma 2: " + answer2)
        "Yell at them and get angry.":
            $answer2 = "yell"
            $renpy.fix_rollback()
            $score -= 1
            $send_to_file("choices.txt", "\nDilemma 2: " + answer2)
        "Stop and ask them where they are going.":
            $answer2 = "stop"
            $renpy.fix_rollback()
            $score += 1
            $send_to_file("choices.txt", "\nDilemma 2: " + answer2)

    return

label dilemma3A:
    "A group of students passes you. You hear them talking about pronouns."
    call hide_npc
    show carmen at above_right with moveinright
    carm "\“These non-binary pronouns don’t work for me. I find it too much effort, he’s not here and I don’t like him anyways.\”"
    carm "\“Plus, these pronouns don’t even exist in my native language. So I’ll just stick to using {i}him{/i}.\”"
    hide carmen with Dissolve(0.5)
    call show_npc
    if is_dutch:
        s "\“O my god. Did you hear that?\”"
        j "\“Yes.\”"
    else:
        j "\“O my god. Did you hear that?\”"
        s "\“Yes.\”"

    # Consequential choice
    menu:
        "\“What do you think about what Carmen said?\”"

        "I disagree.":
            $answer3a = "disagree"
            $renpy.fix_rollback()
            $score += 1
            $send_to_file("choices.txt", "\nDilemma 3A: " + answer3a)
            if is_dutch:
                j "\“If somebody explained their pronouns, I think you should try to use them. It could mean a lot to them.\”"
            else:
                s "\“If somebody explained their pronouns, I think you should try to use them. It could mean a lot to them.\”"
        "No opinion.":
            $answer3a = "no_opinion"
            $renpy.fix_rollback()
            $send_to_file("choices.txt", "\nDilemma 3A: " + answer3a)
            if is_dutch:
                j "\“To be honest, I don’t really have an opinion about it.\”"
            else:
                s "\“To be honest, I don’t really have an opinion about it.\”"
        "I could see why they would see it that way.":
            $answer3a = "agree"
            $renpy.fix_rollback()
            $send_to_file("choices.txt", "\nDilemma 3A: " + answer3a)
            if is_dutch:
                j "\“From their perspective, I could see why they would think like that.\”"
            else:
                s "\“From their perspective, I could see why they would think like that.\”"

    if is_dutch:
        s "\“Yeah, me too.\”"
    else:
        j "\“Yeah, me too.\”"

    if answer3a == "disagree":
        call hide_avatar
        show carmen at above_left with moveinleft
        if is_dutch:
            "Before you know it, Sam meddles in the conversation."
            s "\“You should respect somebody’s pronouns. Regardless of their presence and if you like them or not.\”"
            s "\“If you’re unsure how to refer to them in your native language, you could ask what their pronouns are.\”"
        else:
            "Before you know it, Jip meddles in the conversation."
            j "\“You should respect somebody’s pronouns. Regardless of their presence and if you like them or not.\”"
            j "\“If you’re unsure how to refer to them in your native language, you could ask what their pronouns are.\”"
    elif answer3a == "no_opinion":
        "You both don’t pay further attention to the conversation and wait until they pass by."
    else:
        call hide_avatar
        show carmen at above_left with moveinleft
        if is_dutch:
            "Before you know it, Sam meddles in the conversation."
            s "\“I understand your reasoning. Otherwise you have to invent a word that doesn’t even exist in your native language.\”"
        else:
            "Before you know it, Jip meddles in the conversation."
            j "\“I understand your reasoning. Otherwise you have to invent a word that doesn’t even exist in your native language.\”"

    # Version A
    call switch_carmen

    scene bg uithof_rainbow with Dissolve(0.5)
    if answer3a != "no_opinion":
        "Before you can think further about it, Carmen says:"
        show carmen at above_left with moveinleft
        if answer3a == "disagree":
            carm "\“I tried asking his pronouns once, but they just don’t stick with me. I can’t get used to it and I hardly find it the effort, since I rarely see that person.\”"
            if is_dutch:
                call show_npc
                s "\“OK, but I think you should give it another shot and ask again. It may not seem a big deal to you, but it can mean a lot to them.\”"
            else:
                call show_npc
                j "\“OK, but I think you should give it another shot and ask again. It may not seem a big deal to you, but it can mean a lot to them.\”"
            carm "\“Hmm, maybe you do have a point… I’ll think about it.\”"
        else:
            carm "\“Yep, you read my mind. Look, I'm not trying to be a bad person. In my native language, I’m just used to binary pronouns.\”"

    return

label dilemma3B:
    "In front of the stairs, someone approaches you. They seem to have some kind of paper in their hand."
    show leo at above_right with moveinright
    l "\“Hey, could I ask you something really quick?\”"
    if is_dutch:
        j "\“Of course.\”"
        j "{i}\“I hope they don’t want to sell me some kind of newspaper subscription. I have a hard time saying ‘No’ to those things.\”{/i}"
    else:
        s "\“Of course.\”"
        s "{i}I hope they don’t want to sell me some kind of newspaper subscription. I have a hard time saying ‘No’ to those things.{/i}"
    l "\“I’m Leo from the Diversity & Inclusion Committee here at Utrecht University. Next month we want to raise awareness for transgender and non-binary people, as they are often misgendered or misunderstood.\”"
    l "\“To estimate how to approach this campaign, I’m gauging the student’s feelings about this. Could I ask your opinion about this topic?\”"

    # Consequential choice
    menu:
        "\“What do you think of it?\”"

        "Support it.":
            $answer3b = "support"
            $renpy.fix_rollback()
            $send_to_file("choices.txt", "\nDilemma 3B: " + answer3b)
            $score += 1
            if is_dutch:
                j "\“I think it’s a good idea. I think equipping people with more knowledge about the topic will definitely help. It’ll hopefully solve a lot of misunderstandings.\”"
            else:
                s "\“I think it’s a good idea. I think equipping people with more knowledge about the topic will definitely help. It’ll hopefully solve a lot of misunderstandings.\”"
        "No opinion.":
            $answer3b = "no_opinion"
            $renpy.fix_rollback()
            $send_to_file("choices.txt", "\nDilemma 3B: " + answer3b)
            if is_dutch:
                j "\“To be honest, I don’t know, because it doesn’t cross my mind often.\”"
            else:
                s "\“To be honest, I don’t know, because it doesn’t cross my mind often.\”"
        "Be sceptical.":
            $answer3b = "sceptic"
            $renpy.fix_rollback()
            $send_to_file("choices.txt", "\nDilemma 3B: " + answer3b)
            if is_dutch:
                j "\“On the one hand I think it’s good, but on the other hand, making people aware of their marginalised positions could have negative consequences, especially if it’s not in their power to change it.\”"
                l "\“That’s true, I haven’t looked at it that way.\”"
                l "\“We have to approach it very carefully, the last thing we want is any backlash.\”"
            else:
                s "\“On the one hand I think it’s good, but on the other hand, making people aware of their marginalised positions could have negative consequences, especially if it’s not in their power to change it.\”"
                l "\“That’s true, I haven’t looked at it that way.\”"
                l "\“We have to approach it very carefully, the last thing we want is any backlash.\”"

    l "\“Thank you for your answer and your time!\”"
    l "\“Have a nice day!\”"
    if is_dutch:
        j "\“You too!\”"
    else:
        s "\“You too!\”"

    return

label dilemma4:
    scene bg kbg_door with Dissolve(0.5)
    call show_avatar
    show matilda at above_right with moveinright
    "While you are walking in the building, you see a girl who’s in a wheelchair."
    "Matilda’s struggling to open the door, but she hasn’t asked for any help."

    # Consequential choice
    menu:
        "What will you do?"

        "Pretend you don’t see her":
            $answer4 = "ignore"
            $renpy.fix_rollback()
            $score -= 1
            $send_to_file("choices.txt", "\nDilemma 4: " + answer4)
            "You pretend not to see Matilda’s struggle."
            "When she’s looking at you, you quickly look in another direction. This isn’t your finest moment."
        "Immediately help her":
            $answer4 = "help"
            $renpy.fix_rollback()
            $send_to_file("choices.txt", "\nDilemma 4: " + answer4)
            "You rush towards the door to hold it open."
            "Matilda looks at you with slight confusion, but quickly says:"
            m "\“I almost got it, but thanks!\”"
        "Ask if she needs any help":
            $answer4 = "ask"
            $renpy.fix_rollback()
            $score *= 2 # Double amount of points
            $send_to_file("choices.txt", "\nDilemma 4: " + answer4)
            if is_dutch:
                j "\“Hey, can I help you with that?\”"
                m "\“Actually yes! I didn’t want to ask anyone, thank my ego for that. But the door is too heavy.\”"

    # Version A
    if friends:
        call switch_matilda

    if answer4 != "ignore":
        "You wonder why Matilda is in a wheelchair."
        # Trivial choice
        menu:
            "Will you ask?"

            "No":
                $renpy.fix_rollback()
            "Yes":
                $renpy.fix_rollback()
                if is_dutch:
                    j "\“Hey, I hope you don’t mind that I ask this, but how did you end up in a wheelchair?\”"
                    m "\“No, it’s fine. I’ve been in a car accident that resulted in a spinal cord injury. So my legs and feet are paralysed.\”"
                    j "\“Oh… I’m very sorry to hear that.\”"
                    m "\“Thank you, but don’t be. It wasn’t your fault, right? \[laughs\]\”"
                    m "\“It also happened so long ago… I can handle myself in this wheelchair, but I still miss the things I did before the accident.\”"
                    j "\“What were those?\”"
                    m "\“Well, I used to take long walks through the parks. Utrecht has so many beautiful parks, but the {i}Máximapark{/i} is my absolute favourite.\”"
                    m "\“I can still visit the park in my wheelchair, but it’s just not the same.\”"
                    j "\“I see… I don’t know what else to say…\”"
                    m "\“It’s OK, talking about the {i}Máximapark{/i} brings up some good memories. I’m glad you asked, usually people just see me as kinda helpless and act awkward.\”"
                    m "\“I got to go now, but it was nice talking to you. Bye bye!\”"
                    j "\“I have to go too. See you later!\”"
                else:
                    s "\“Hey, I hope you don’t mind that I ask this, but how did you end up in a wheelchair?\”"
                    m "\“No, it’s fine. I’ve been in a car accident that resulted in a spinal cord injury. So my legs and feet are paralysed.\”"
                    s "\“Oh… I’m very sorry to hear that.\”"
                    m "\“Thank you, but don’t be. It wasn’t your fault, right? \[laughs\]\”"
                    m "\“It also happened so long ago… I can handle myself in this wheelchair, but I still miss the things I did before the accident.\”"
                    s "\“What were those?\”"
                    m "\“Well, I used to take long walks through the parks. Utrecht has so many beautiful parks, but the {i}Máximapark{/i} is my absolute favourite.\”"
                    m "\“I can still visit the park in my wheelchair, but it’s just not the same.\”"
                    s "\“I see… I don’t know what else to say…\”"
                    m "\“It’s OK, talking about the {i}Máximapark{/i} brings up some good memories. I’m glad you asked, usually people just see me as kinda helpless and act awkward.\”"
                    m "\“I got to go now, but it was nice talking to you. Bye bye!\”"
                    s "\“I have to go too. See you later!\”"

    "Matilda disappears and you continue your way towards the lecture room."

    return

label dilemma5:
    "The group continues their conversation about their evening plans."
    "Some students are talking about going to café {i}BodyTalk.{/i}"
    if is_dutch:
        j "\“What is that?\”"
    else:
        s "\“What is that?\”"
    show chloe at above_right with moveinright
    chloe "\“It’s a LGBTQ+-friendly café. I went there with my girlfriend last time.\”"
    "Suddenly, another student swamps Chloe with questions: Are you gay? Since when? How did you come out? How can you be so sure? Did you ever have a crush on one of your friends?"
    "The conversation abruptly seems to have turned into an interrogation."
    "You can see that Chloe doesn’t like it and shuts down."

    # Consequential choice
    menu:
        "What do you do?"

        "Switch the topic":
            $answer5 = "switch_topic"
            $renpy.fix_rollback()
            $send_to_file("choices.txt", "\nDilemma 5: " + answer5)
            "You try to change the topic."
            if is_dutch:
                j "\“Sooo, nice weather we’re having, right?\”"
            else:
                s "\“Sooo, nice weather we’re having, right?\”"
        "Say something about it.":
            $answer5 = "talk"
            $renpy.fix_rollback()
            $score += 1
            $send_to_file("choices.txt", "\nDilemma 5: " + answer5)
            "You let the person know that they are making Chloe uncomfortable with their questions and suggest they should stop."
            "You see that the girl is visibly relieved."
        "Wait until the topic switches, but talk later in private":
            $answer5 = "wait"
            $renpy.fix_rollback()
            $send_to_file("choices.txt", "\nDilemma 5: " + answer5)
            "You wait until the topic switches and talk to Chloe privately how she feels about it."
            chloe "\“I got myself back together and I’m OK now. Sorry you had to see my inner meltdown.\”"
            chloe "\“I just wish it wasn’t such a big deal every time I brought it up.\”"
            if is_dutch:
                j "\“Don’t be sorry. The one that should be, is that person who started those invasive and inappropriate questions.\”"
            else:
                s "\“Don’t be sorry. The one that should be, is that person who started those invasive and inappropriate questions.\”"
            chloe "\“You’re right.\”"

    # Version A
    if friends:
        call switch_chloe

    if answer5 == "switch_topic":
        "The group looks confused at you. However, they all sense the tense atmosphere, so they’re happy to switch the topic."
    if answer5 == "talk":
        chloe "\“Thanks so much for standing up for me! I’m so done with the fact that it’s such a big deal every time I bring it up.\”"
        chloe "\“As if my whole personality is reduced to having a girlfriend instead of a boyfriend and I owe everyone an explanation.\”"
        if is_dutch:
            j "\“Yeah, no problem! Glad I could help.\”"
            chloe "\“Are you also studying Artificial Intelligence?\”"
            j "\“Yes, I started today!\”"
            chloe "\“Cool, I tried Computing Science before, but that wasn’t really my thing. I hope this study will suit me better.\”"
            j "\“Maybe it will! It’s good that you try another study. I wouldn't know what else I would want to study besides AI.\”"
            chloe "\“You really don’t?\”"
            j "\“Hmm, thinking about it, maybe Gender Studies? But I never thought about it much further, I took a lot of science courses in high school instead of the humanities.\”"
            chloe "\“Sooo… what are you doing after class?\”"
            j "\“I’m going to the city centre. What about you?\”"
            chloe "\“Nothing much. But we can stay in touch if you’d like?\”"
            chloe "\“Can I get your number? Since you helped me, I want to take you out for a drink.\”"

            # Trivial choice
            call phone_nr
            if give_nr:
                j "\“Here it is. Maybe your girlfriend could join too? I would like to meet her.\”"
                chloe "\“Sure!\”"
            if not give_nr:
                j "\“Sorry, but I don’t know you that well. But thanks for offering.\”"
                chloe "\“No problem!\”"
        else:
            s "\“Yeah, no problem! Glad I could help.\”"
            chloe "\“Are you also studying Artificial Intelligence?\”"
            s "\“Yes, I started today!\”"
            chloe "\“Cool, I tried Computing Science before, but that wasn’t really my thing. I hope this study will suit me better.\”"
            s "\“Maybe it will! It’s good that you try another study. I wouldn't know what else I would want to study besides AI.\”"
            chloe "\“You really don’t?\”"
            s "\“Hmm, thinking about it, maybe Gender Studies? But I never thought about it much further, I took a lot of science courses in high school instead of the humanities.\”"
            chloe "\“Sooo… what are you doing after class?\”"
            s "\“I’m going to the city centre. What about you?\”"
            chloe "\“Nothing much. But we can stay in touch if you’d like?\”"
            chloe "\“Can I get your number? Since you helped me, I want to take you out for a drink.\”"

            # Trivial choice
            call phone_nr
            if give_nr:
                s "\“Here it is. Maybe your girlfriend could join too? I would like to meet her.\”"
                chloe "\“Sure!\”"
            if not give_nr:
                s "\“Sorry, but I don’t know you that well. But thanks for offering.\”"
                chloe "\“No problem!\”"

    hide chloe with Dissolve(0.5)

    return

label dilemma6:
    "Someone approaches you."
    show val at above_right with moveinright
    v "\“Hey, I’m Val. I studied at the {i}HU{/i} (Hogeschool Utrecht, which is the university of applied sciences) first.\”"
    v "\“I don’t know anyone here. Could I join your group?\”"

    # Consequential choice
    menu:
        "What is your response?"

        "Sorry, but no.":
            call dilemma6_no
        "Let me think about it.":
            $answer6 = "maybe"
            $renpy.fix_rollback()
            $send_to_file("choices.txt", "\nDilemma 6: " + answer6)
            "You are not sure yet."
            if is_dutch:
                j "\“Wait, let me check with this other person real quick.\”"
            else:
                s "\“Wait, let me check with this other person real quick.\”"
            v "\“OK, please let me know later.\”"
        "Sure!":
            call dilemma6_yes

    # Version A
    if friends:
        call switch_val

    # Consequential choice, second chance
    if answer6 == "maybe":
        if not friends:
            scene bg black with Dissolve(0.5)
            centered "A short moment later…"
            scene bg cosmos_lecture with Dissolve(0.5)
            call show_avatar
            show val at above_right with moveinright

        "Val approaches you again."
        v "\“Hey, so have you made up your mind?\”"
        menu:
            "Can I join your group?"

            "Sorry, but no.":
                call dilemma6_no
            "Sure!":
                call dilemma6_yes

    # Second chance to befriend NPC if player has accepted Val and not gotten angry in Dilemma #2
    if not friends and answer6 == "yes" and answer2 != "yell":
        hide val with Dissolve(0.5)
        call show_npc
        $friends = True
        "Another student approaches you."
        if is_dutch:
            s "\“Can I also join your group?\”"
            s "\“I just arrived in the Netherlands. Today is my first day on campus.\”"
            j "\“Of course!\”"
            call convo_befriend
        else:
            j "\“Can I also join your group?\”"
            j "\“Today is my first day on campus.\”"
            s "\“Of course!\”"
            call convo_befriend

    return

label dilemma7:
    # Consequential choice
    menu:
        "What do you do?"

        "Observe what will happen further":
            $answer7 = "observe"
            $renpy.fix_rollback()
            $score -= 1
            $send_to_file("choices.txt", "\nDilemma 7: " + answer7)
            "You stand still until the group finishes the song and walks away."
        "Ask in private if Shiro is OK":
            call dilemma7_ask
        "Walk past it":
            $answer7 = "ignore"
            $renpy.fix_rollback
            $send_to_file("choices.txt", "\nDilemma 7: " + answer7)
            "You find birthday songs silly anyway and walk away, while giving a quick side eye."

    # Version A
    if friends:
        call switch_shiro

    "Shiro walks away."
    hide shiro with Dissolve(0.5)

    return

label bonus_dilemma:
    if friends:
        call hide_npc
    show steph at above_right with moveinright
    st "\“In case you’re wondering, the Dom is actually 112 metres and 32 centimetres! To get to the top, you have to take 465 steps.\”"
    st "\“People even organise stair climbing matches. I like random facts, that's why I know. People find me a bit peculiar, and they might be right.\”"
    st "\“I’m Steph, by the way.\”"
    if is_dutch:
        j "“I’m Jip. And why is that so?”"
    else:
        s "“I’m Sam. And why is that so?”"
    st "\“Just between me and you, I’m diagnosed with autism, but I don’t know if I want to tell my friends about this.\”"
    st "\“I’m afraid I will be judged differently when I do. I don’t mind telling strangers though.\”"

    # Consequential choice
    menu:
        "What would you say to Steph?"

        "Play it down":
            $bonus_answer = "downplay"
            $renpy.fix_rollback()
            $send_to_file("choices.txt", "\nBonus dilemma: " + bonus_answer)
            if is_dutch:
                j "\“Everybody has some autistic traits and that it’s not a big deal in telling people.\”"
            else:
                s "\“Everybody has some autistic traits and that it’s not a big deal in telling people.\”"
            st "\“You’re probably right. But I’m still not sure if I’m ready for that.\”"
        "Thank and support":
            $bonus_answer = "thank_support"
            $renpy.fix_rollback()
            $score += 1
            $send_to_file("choices.txt", "\nBonus dilemma: " + bonus_answer)
            if is_dutch:
                j "\“I can’t make that choice for you, but I support you in whatever decision you take. Thanks a lot for sharing that with me.\”"
            else:
                s "\“I can’t make that choice for you, but I support you in whatever decision you take. Thanks a lot for sharing that with me.\”"
            st "\“Thank you.\”"

    # Version A
    if friends:
        #call switch_steph
        # Perspective switch
        scene bg black with Dissolve(0.5)
        centered "Oh, it’s happening again! What’s on their mind?"
        scene bg dom_square with Dissolve(0.5)
        show steph at above_left with moveinleft
        if bonus_answer == "downplay":
            st "{i}\“Why did I ask a random stranger for advice? Besides that, you probably think I’m blowing it up, but that’s not the case. I’m really struggling with it.\”{/i}"
        else:
            st "{i}\“They’re right, it’s my own decision to make. I guess I just needed to feel understood.\”{/i}"

        # Switch back
        scene bg black with Dissolve(0.5)
        centered "Back to hearing only your own thoughts."
        scene bg dom_square with Dissolve(0.5)
        call show_avatar
        show steph at above_right with moveinright

    "Steph smiles and walks away."
    hide steph with Dissolve(0.5)
    call show_all

    return

label dilemma8A:
    "The topic changes and you talk more about the {i}hospi{/i}."
    if is_dutch:
        "Sam says that they heard a story from a friend who joined a student house as the only international student."
    else:
        "Jip says that they heard a story from a friend who joined a student house as the only international student."
    "The house also has a group chat where they chat in Dutch. After the international student was added to the group chat, a few roommates were unsure whether to continue talking in Dutch or switch to English."

    # Consequential choice
    menu:
        "What would you do?"

        "Continue in Dutch, highlights in English":
            $answer8a = "both"
            $renpy.fix_rollback()
            $send_to_file("choices.txt", "\nDilemma 8A: " + answer8a)
            if is_dutch:
                j "\“I would continue casual communication in Dutch, but for important announcements I would switch to English.\”"
            else:
                s "\“I would continue casual communication in Dutch, but for important announcements I would switch to English.\”"
        "Stick to Dutch":
            $answer8a = "Dutch"
            $renpy.fix_rollback()
            $score -= 1
            $send_to_file("choices.txt", "\nDilemma 8A: " + answer8a)
            if is_dutch:
                j "\“As I see it, the majority of the house is Dutch. So I would stick to Dutch.\”"
            else:
                s "\“As I see it, the majority of the house is Dutch. So I would stick to Dutch.\”"
        "Switch to English":
            $answer8a = "English"
            $renpy.fix_rollback()
            $score += 1
            $send_to_file("choices.txt", "\nDilemma 8A: " + answer8a)
            if is_dutch:
                j "\“I would talk in English. So the international student can read the chat too.\”"
            else:
                s "\“I would talk in English. So the international student can read the chat too.\”"

    if is_dutch:
        s "\“OK, fair. Honestly, I wouldn’t know what I would do. I think it also depends how close the house is and if they’re used to speaking English in their daily lives.\”"
    else:
        j "\“OK, fair. Honestly, I wouldn’t know what I would do. I think it also depends how close the house is and if they’re used to speaking English in their daily lives.\”"

    return

label dilemma8B:
    "As you are enjoying your drink, you see some members of the study association {i}Sticky{/i} are sitting at a table next to you."
    "They’re busy chatting. One member is asked to make an announcement at the next activity."
    "They’re saying that they would rather make the announcement in Dutch, since they're much more comfortable speaking Dutch."
    "However, {i}Sticky{/i} has several international members."

    # Consequential choice
    menu:
        "If you were in their place, what would you do?"

        "English summary":
            $answer8b = "summary"
            $renpy.fix_rollback()
            $send_to_file("choices.txt", "\nDilemma 8B: " + answer8b)
            "You would perform the announcement in Dutch and give a highlighted summary in English at the end. That seems fair, right?"
        "Speak Dutch":
            $answer8b = "Dutch"
            $renpy.fix_rollback()
            $score -= 1
            $send_to_file("choices.txt", "\nDilemma 8B: " + answer8b)
            "You would perform the announcement in Dutch. That way you can express yourself better and that’s only fair, right?"
        "Speak English":
            $answer8b = "English"
            $renpy.fix_rollback()
            $score += 1
            $send_to_file("choices.txt", "\nDilemma 8B: " + answer8b)
            "You would perform the announcement in English. While it costs a little more effort from your side, it’s more important that everybody receives the message loud and clear."

    return

label dilemma9:
    if is_dutch:
        j "\“Hey, do you want to eat together? I'm making a [dinner].\”"
        s "\“Yes, I would like to! I like everything except goat cheese.\”"
        j "\“Don’t worry, this meal doesn’t have goat cheese.\”"
        s "\“Oh, and I only eat halal meat due to religious reasons.\”"
        j "\“Alright.\”"
    else:
        s "\“Hey, do you want to eat together? I'm making a [dinner].\”"
        j "\“Yes, I would like to! I like everything except carrots.\”"
        s "\“Don’t worry, this meal doesn’t have carrots.\”"
        j "\“Oh, and I only eat halal meat due to religious reasons.\”"
        s "\“Alright.\”"

    "You’re both at the supermarket buying ingredients for dinner. However, the halal meat is out of stock."

    # Consequential choice
    menu:
        "What now?"

        "Go to another store to buy it":
            $answer9 = "halal"
            $renpy.fix_rollback()
            $score +=1
            $send_to_file("choices.txt", "\nDilemma 9: " + answer9)
            "Your friend deserves a tasty meal too. You take the extra mile to buy halal meat at another store."
        "Buy regular meat, but pretend it’s halal":
            $answer9 = "lie"
            $renpy.fix_rollback()
            $score -=1
            $send_to_file("choices.txt", "\nDilemma 9: " + answer9)
            "You don’t take your friend's wishes into account. But they don’t need to know that."
        "Just skip the meat":
            $answer9 = "skip"
            $renpy.fix_rollback()
            $send_to_file("choices.txt", "\nDilemma 9: " + answer9)
            "You decide to make the dish with less ingredients."
            "If you don’t buy any ingredients that are not halal, they can’t cheat, right?"

    return

label dilemma10:
    "After paying for your groceries, you go home and eat dinner together."
    scene bg hostel_lobby with Dissolve(0.5)
    call show_all
    if is_dutch:
        s "\“Thanks for inviting me to your place! I’m staying in a hostel too currently.\”"
        j "\“Yeah, no problem! Wait, in which hostel are you staying?\”"
        s "\“At the {i}Student Hostel{/i} close to the city theatre. It’s actually not so far from the {i}Stayokay{/i} here at Neude.\”"
        s "\“By the way, can I complain about somebody to you?\”"
        j "\“Of course! Spill the tea.\”"
        s "\“OK, so my friend is vegan, but I just don’t understand why anybody would be vegan.\”"
        s "\“It feels like they do it to guilt-trip people that do eat meat and dairy products. I can’t wrap my head around it.\”"
    else:
        j "\“Thanks for inviting me to your place! I’m staying in a hostel too currently.\”"
        s "\“Yeah, no problem! Wait, in which hostel are you staying?\”"
        j "\“At the {i}Student Hostel{/i} close to the city theatre. It’s actually not so far from the {i}Stayokay{/i} here at Neude.\”"
        j "\“By the way, can I complain about somebody to you?\”"
        s "\“Of course! Spill the tea.\”"
        j "\“OK, so my friend is vegan, but I just don’t understand why anybody would be vegan.\”"
        j "\“It feels like they do it to guilt-trip people that do eat meat and dairy products. I can’t wrap my head around it.\”"
    "Their monologue of complaints continues for a while."

    # Consequential choice
    menu:
        "What do you do?"

        "Say nothing":
            $answer10 = "nothing"
            $renpy.fix_rollback()
            $send_to_file("choices.txt", "\nDilemma 10: " + answer10)
            "Although you don’t think the same about it, you wait until their rant is over."
            "While tempting, you don’t want to point them out that they have their dietary wishes too."
        "Pretend to agree.":
            $answer10 = "agree"
            $renpy.fix_rollback()
            $score -= 1
            $send_to_file("choices.txt", "\nDilemma 10: " + answer10)
            "You pretend to agree with them and also do your two cents by saying it’s only for the elite and pretentious ones."
            "Yet in reality, you don’t think that at all, but you don’t want a confrontation."

            if is_dutch:
                s "\“Glad you think the same about it. But you don’t have to agree just because we are friends.\”"
                j "\“I know…\”"
            else:
                j "\“Glad you think the same about it. But you don’t have to agree just because we are friends.\”"
                s "\“I know…\”"

            # Consequential choice, second chance
            menu:
                "What will you do next?"

                "Keep quiet":
                    $answer10 = "keep_quiet"
                    $renpy.fix_rollback()
                    $send_to_file("choices.txt", "\nDilemma 10: " + answer10)
                    "Although you don’t think the same about it, you decide to drop it and finish your plate."
                "Speak your mind":
                    $answer10 = "speak_up"
                    $renpy.fix_rollback()
                    $score += 1
                    $send_to_file("choices.txt", "\nDilemma 10: " + answer10)
                    if is_dutch:
                        j "\“Actually, I do disagree. People have their own reasons to be vegan. I think it’s unfair you criticise them for that.\”"
                    else:
                        s "\“Actually, I do disagree. People have their own reasons to be vegan. I think it’s unfair you criticise them for that.\”"
                    call dilemma10_disagree
        "Interrupt them by disagreeing":
            $answer10 = "disagree"
            $renpy.fix_rollback()
            $score += 1
            $send_to_file("choices.txt", "\nDilemma 10: " + answer10)
            "You interrupt them and explain the reasons why people could be vegan."
            "Your friend shouldn’t criticise them for that, that’s unfair."
            call dilemma10_disagree

    return