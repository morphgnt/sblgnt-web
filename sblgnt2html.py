#!/usr/bin/env python

print """
<!doctype html>
<html>
    <head>
        <title>Matthew</title>
        <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
        <style>
            body {
                font-family: sans-serif;
            }
            h1 {
                margin-top: 50px;
                margin-left: 210px;
            }
            .header {
                margin: 0;
                position: fixed;
                top: 0px;
            }
            .book {
                padding: 5px 10px;
                font-size: 12pt;
                font-weight: bold;
            }
            .nav {
                margin: 0;
                padding: 0;
                list-style: none;
                width: 140px;
                font-weight: 100;
                font-size: 10pt;
                text-align: right;
            }
            .nav li.active {
                font-weight: bold;
            }
            .nav a {
                padding: 5px 10px;
                display: block;
                text-decoration: none;
                color: black;
            }
            .nav a:hover {
                font-weight: bold;
            }
            .text {
                width: 450px;
                margin: 0 250px;
            }
            .gk {
                font-size: 16pt;
                color: #444;
                line-height: 32pt;
                font-family: sans-serif;
            }
            .word {
                text-decoration: none;
                color: inherit;
            }
            .lowlight {
                color: #999;
            }
            .highlight {
                color: black;
            }
            .verse_num {
                color: #999;
                font-size: 10pt;
                position: absolute;
                left: 200px;
                padding: 0 20px;
                text-decoration: none;
            }
            .verse_num:hover {
                color: #000;
            }
            
            .verse:target {
                background: #FF6;
            }
            .analysis {
                color: black;
                min-width: 200px;
                position: absolute;
                left: 750px;
                background: #F7F7F7;
                padding: 4px 8px;
            }
            .analysis .form {
                font-weight: bold;
                font-size: 16pt;
                line-height: 16pt;
            }
            .analysis .pos {
                color: #999;
                font-size: 10pt;
                line-height: 10pt;
            }
            .analysis .parse {
                color: #999;
                font-size: 10pt;
                line-height: 10pt;
                font-style: italic;
            }
            .analysis .lemma {
                font-size: 12pt;
                line-height: 16pt;
            }
            .word:hover {
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div id="chapter-nav" class="header">
            <ul class="nav">
"""

for i in range(1, 29):
    print """<li><a href="#chapter-{chapter}">{chapter}</a></li>""".format(chapter=i)

print """
            </ul>
        </div>
        <h1>Matthew</h1>
        <div class="text gk" id="text">
"""

last_verse = 0
last_chapter = 0

for line in open("61-Mt-morphgnt.txt"):
    bcv, pos, parse, text, norm, form, lemma = line.strip().split()
    pos = {
        "RA": "article",
        "A-": "adjective",
        "N-": "noun",
        "C-": "conjunction",
        "RP": "personal pronoun",
        "RR": "relative pronoun",
        "V-": "verb",
        "P-": "preposition",
        "D-": "adverb",
        "RD": "demonstrative",
        "RI": "interoggative/indefinite pronoun",
        "X-": "particle",
        "I-": "interjection",
    }[pos]
    person, tense, voice, mood, case, number, gender, degree = parse
    parse = []
    if pos == "verb":
        if mood == "P":
            parse.append({
                "P": "present",
                "A": "aorist",
                "X": "perfect",
                "F": "future",
            }[tense])
            parse.append({
                "A": "active",
                "M": "middle",
                "P": "passive",
            }[voice])
            parse.append("participle")
            parse.append({
                "N": "nominative",
                "A": "accusative",
                "G": "genitive",
                "D": "dative",
                "V": "vocative",
                "-": "",
            }[case])
            parse.append({
                "S": "singular",
                "P": "plural",
                "-": "",
            }[number])
            parse.append({
                "M": "masculine",
                "F": "feminine",
                "N": "neuter",
                "-": "",
            }[gender])
        elif mood == "N":
            parse.append({
                "P": "present",
                "A": "aorist",
                # "X": "perfect",
            }[tense])
            parse.append({
                "A": "active",
                "M": "middle",
                "P": "passive",
            }[voice])
            parse.append("infinitive")
        else:
            parse.append({
                "P": "present",
                "F": "future",
                "A": "aorist",
                "X": "perfect",
                "Y": "pluperfect",
                "I": "imperfect",
            }[tense])
            parse.append({
                "A": "active",
                "M": "middle",
                "P": "passive",
            }[voice])
            parse.append({
                "I": "indicative",
                "S": "subjunctive",
                "D": "imperative",
            }[mood])
            parse.append({
                "1": "1st person",
                "2": "2nd person",
                "3": "3rd person",
            }[person])
            parse.append({
                "S": "singular",
                "P": "plural",
                "-": "",
            }[number])
    else:
        parse.append({
            "N": "nominative",
            "A": "accusative",
            "G": "genitive",
            "D": "dative",
            "V": "vocative",
            "-": "",
        }[case])
        parse.append({
            "S": "singular",
            "P": "plural",
            "-": "",
        }[number])
        parse.append({
            "M": "masculine",
            "F": "feminine",
            "N": "neuter",
            "-": "",
        }[gender])
        parse.append({
            "C": "comparative",
            "S": "superlative",
            "-": "",
        }[degree])
    parse = " ".join(parse)
    chapter = int(bcv[2:4])
    verse = int(bcv[4:])
    cv = "{}-{}".format(chapter, verse)
    if chapter != last_chapter:
        if last_chapter:
            print """</span>"""
            print """</div>"""
        print """<div id="chapter-{chapter}" class="chapter">""".format(chapter=chapter)
        last_chapter = chapter
        last_verse = 0
    if verse != last_verse:
        if last_verse:
            print """</span>"""
        print """<a href="#verse-{cv}" class="verse_num" data-verse="{cv}">{verse}</a>""".format(verse=verse, cv=cv)
        last_verse = verse
        print """<span class="verse" id="verse-{cv}">""".format(cv=cv)
    print """<a href="#" class="word" data-form="{form}" data-pos="{pos}" data-parse="{parse}" data-lemma="{lemma}">{text}</a>""".format(
        text=text,
        form=form,
        pos=pos,
        parse=parse,
        lemma=lemma,
    )

print """
            </span>
            </div>
        </div>
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
        <script>
            $(function() {
                var positions = [];
                $(".chapter").each(function(i, e) {
                    positions[positions.length] = {
                        start: $(e).offset().top,
                        end: $(e).offset().top + $(e).height(),
                        id: $(e).attr("id"),
                        selected: null
                    }
                });
                function update() {
                    var window_start = $(window).scrollTop();
                    var window_end = window_start + $(window).height();
                    
                    for (var i=0; i<positions.length; i++) {
                        if (window_start <= positions[i].end && window_end >= positions[i].start) {
                            if (!positions[i].selected) {
                                $("a[href=#" + positions[i].id + "]").parent().addClass("active");
                                positions[i].selected = true;
                            }
                        } else {
                            if (positions[i].selected) {
                                $("a[href=#" + positions[i].selected + "]").parent().removeClass("active");
                                positions[i].selected = false;
                            }
                        }
                    }
                }
                $(window).bind("scroll", update);
                $(window).bind("resize", update);
                $(".verse_num").hover(
                    function() {
                        $("#text").addClass("lowlight");
                        var verse = $(this).data("verse");
                        $("#verse-" + verse).addClass("highlight");
                    },
                    function() {
                        $("#text").removeClass("lowlight");
                        var verse = $(this).data("verse");
                        $("#verse-" + verse).removeClass("highlight");
                    }
                );
                $(".word").hover(
                    function() {
                        var form = $(this).data("form");
                        var pos = $(this).data("pos")
                        var parse = $(this).data("parse");
                        var lemma = $(this).data("lemma");
                        $(this).after('<span class="analysis"><div class="form">' + form + '</div><div class="pos">' + pos + '</div><div class="parse">' + parse + '</div><div class="lemma">' + lemma + '</div></span>');
                    },
                    function() {
                        $(".analysis").remove();
                    }
                )
            });
        </script>
    </body>
</html>
"""
