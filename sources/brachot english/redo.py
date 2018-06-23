# -*- coding: utf-8 -*-
import json
import os
import sys
import pprint
import pdb
import urllib
import urllib2
from urllib2 import URLError, HTTPError
sys.path.insert(0, '../Match/')
from match import Match
import re
p = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, p)
os.environ['DJANGO_SETTINGS_MODULE'] = "sefaria.settings"
from local_settings import *

sys.path.insert(0, SEFARIA_PROJECT_PATH)

from sefaria.model import *
from sefaria.model.schema import AddressTalmud	

def post_text(ref, text):
    textJSON = json.dumps(text)
    ref = ref.replace(" ", "_")
    url = 'http://dev.sefaria.org/api/texts/'+ref
    values = {'json': textJSON, 'apikey': API_KEY}
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    try:
        response = urllib2.urlopen(req)
        print response.read()
    except HTTPError, e:
        print 'Error code: ', e.code
        print e.read()
        
berakhot_array = [

        [

            "From what time may the Shema'[1] be read in the evening? ", 

            "From the time the priests[2] enter [the Temple] to partake of their Terumah, until the end of the first watch[3]. These are the words of R. Eliezer;", 

            " but the Sages[4] say:", 

            " Until midnight. ", 

            "Rabban Gamaliel says: ", 

            "Until the rise of dawn[5]. ", 

            "It once happened that his sons returned from a feast [after midnight] and said to him,", 

            " \"We have not read the Shema' !\" ", 

            "He told them,", 

            " \"If the dawn has not yet risen, you are still under the obligation of reading it. ", 

            "And not only in this connection do they so decide; but wherever the Sages use the expression 'Until midnight,' the obligation continues until the rise of dawn.\"", 

            " The duty of burning the fat and parts of the animal[6] continues until the rise of dawn. Likewise with all offerings which have to be eaten the same day [they are sacrificed][7], the duty continues until the rise of dawn. If so, why do the Sages say \"Until midnight\"?", 

            " In order to keep a man far from transgression. ", 

            "GEMARA  What authority has the Tanna [that the Shema' is to be read at all] that he raises the question: From what time?[8]", 

            "Further, on what ground does he first deal with the evening ?", 

            " Let him first deal with [the Shema'] of the morning ! ", 

            "The Tanna bases his authority on Scripture ; for it is written, \"When thou liest down and when thou risest up\" (Deut. vi. 7)[1].", 

            " His statement in the Mishnah is to be understood thus :", 

            " When is the time for reading the Shema' which is to be recited when lying down? From the time the priests enter [the Temple] to partake of their Terumah. ", 

            "Or if thou wilt,", 

            " I can say that he derives [his reason for commencing with the evening] from the account of the Creation ; for it is written : \"It was evening and it was morning, one day\" (Gen, i. 5)[2]. ", 

            "If this be so, in the sequel where he teaches : In the morning [the reading of the Shema'] is preceded by two benedictions and followed by one; in the evening it is preceded by two and followed by two[3], let him likewise treat of the evening first !", 

            " The Tanna commenced with the evening and then treats of the morning[4]; but while on the subject of the morning, he explains matters connected with the morning, and afterwards explains matters connected with the evening. ", 

            "The teacher stated :", 

            " From the time the priests enter [the Temple] to partake of their Terumah. ", 

            "Yes, but when do the priests partake of their Terumah ? From the time the stars appear.  Then let him explicitly teach : \"From the time of the appearance of the stars\" !", 

            " He wishes to tell us something incidentally : When do the priests partake of their Terumah ? From the time the stars appear[5]. He thereby informs us ", 

            "that [the omission of] the sin-offering does not prevent [the priest from partaking of the Terumah]. ", 

            "This is in agreement with the teaching :", 

            " \"When the sun is down and it is clean\" (Lev. xxii. 7)[6] — i.e. the setting of the sun[7] prevents him from partaking of the Terumah, but not [his failure to bring] his sin-offering. ", 

            "How is it to be known, however, that the phrase \"When the sun is down\" means the [complete] setting of the sun[1], and the phrase \"It is clean\" means the day is clean? "

        ], 

        [

            "Perhaps the former signifies the setting of its light[2], and the latter the man shall be clean !", 

            " Rabbah b. Rab Shela answered : ", 

            "In that case the text should have read weyithar[3] ; what means wetaher? The day is clean [of light]; ", 

            "as people commonly say, \"When the sun has set, the day is cleansed.\" ", 

            "In the West[4], this explanation of Rabbah b. Rab Shela had not been heard by them, and they raised the question: ", 

            "The phrase \"When the sun is down\" means the [complete] setting of the sun, and the phrase \"It is clean\" means the day is clean ; but perhaps the former signifies the setting of its light, and the latter the man shall be clean ! ", 

            "They then solved it from a Baraita ; for it is taught in a Baraita : The sign for the matter[5] is the appearance of the stars.", 

            " Conclude from this that the [complete] setting of the sun is intended ; and what means \"It is clean\" ? The day is clean. ", 

            "The teacher stated :", 

            " From the time the priests enter [the Temple] to partake of their Terumah. ", 

            "Against this I quote:", 

            " From what time may the Shema' be read in the evening ? ", 

            "From the time when the poor man[6] goes home to eat his bread with salt, until such time as he usually stands up to leave his meal ! ", 

            "The latter part of this passage is certainly at variance with our Mishnah[7] ; ", 

            "but is it to be said that the first part is also at variance with it ? ", 

            "No ; the poor man and the priest have the one standard of time. ", 

            "I quote the following against our Mishnah : ", 

            "From what time may we begin to read the Shema' in the evening? ", 

            "From the time that people go home to eat their bread on the Sabbath-eve[1]. These are the words of R. Meir ; ", 

            "but the Sages say :", 

            " From the time the priests[2] are entitled to partake of their Terumah. A sign for the matter is the appearance of the stars, ", 

            "and although there is no proof of this[3], yet is there some indication ; as it is said, \"So we wrought in the work : and half of them held the spears from the rising of the morning till the stars appeared\" (Neh. iv. 15), and it continues \"That in the night they may be a guard to us, and may labour in the day\" (ibid. v. 16). What is the meaning of this latter verse? ", 

            "Shouldest thou say that immediately the sun set it was reckoned to be night, but they worked late and started early[4] — come and hear[5] :", 

            " \"That in the night they may be a guard to us, and may labour in the day.\" ", 

            "The thought has occurred to thee that the poor man and people generally have the same standard of time[6]. ", 

            "Shouldest thou, however, maintain that the poor man and the priest have the same standard of time, then the opinion of the Sages and R. Meir would be identical[7] !", 

            " Is it then to be concluded ", 

            "that the poor man and the priest have each a different standard of time ?", 

            " No ; the poor man and the priest have the same standard of time, but the poor man and people generally have a different standard. ", 

            "The poor man and the priest have the same standard of time ! ", 

            "Against this I quote : ", 

            "From what time do we begin to read the Shema' in the evening ?", 

            " From the time that the day becomes hallowed on the Sabbath-eve. These are the words of R. Eliezer. ", 

            "R. Joshua says : ", 

            "From the time the priests become ritually clean to partake of their Terumah. ", 

            "R. Meir says: ", 

            "From the time the priests bathe so as to be able to partake of their Terumah. ", 

            "(R. Judah asked him,", 

            " \"But do not the priests bathe while it is yet day[1] ?\") ", 

            "R. Hannina says : ", 

            "From the time the poor man goes home to eat his bread with salt.", 

            " R. Ahai (another version : R. Aha) says :", 

            " From the time when the majority of people go home to have their evening repast. ", 

            "Shouldest thou maintain that the poor man and the priest have the same standard of time, then R. Hannina and R. Joshua hold the same opinion[2] ! ", 

            "Must it not therefore be concluded ", 

            "that each of them has a different standard ? Yes, draw that conclusion. ", 

            "Which of the two[3] is later[4]?", 

            " It is more probable that the poor man is later ; for shouldest thou maintain that he is earlier, then R. Hannina and R. Eliezer would hold the same opinion[5] ! Must it not therefore be concluded that the poor man is later? Yes, draw that conclusion. ", 

            "The teacher stated above : ", 

            "\"R. Judah asked him,", 

            " 'But do not the priests bathe while it is yet day?'\"", 

            " R. Judah's question to R. Meir is a forcible one ! ", 

            "But R. Meir answered him thus : ", 

            "Dost thou think that I agree with thy opinion of \"twilight[6]\" ?", 

            " I agree with R, Jose's opinion.", 

            " For R. Jose said : ", 

            "The twilight is like a flicker of the eye ;", 

            " the night comes on and the day passes without anyone being able to perceive it[7].  "

        ], 

        [

            " R. Meir has contradicted himself[1]!", 

            " There are two Tannaim in the sense of R. Meir[2].", 

            " R. Eliezer has contradicted himself[3] ! ", 

            "There are two Tannaim in the sense of R. Eliezer.", 

            " Or if thou wilt,", 

            " I can say that the first part of the Mishnaic statement is not R. Eliezer's[4]. ", 

            "Until the end of the first watch.  What is R. Eliezer's view ?", 

            " If he holds that the night is divided into three watches, let him say explicitly [in the Mishnah] \"until the end of the fourth hour[5].\"", 

            " If, on the other hand, he holds that the night is divided into four watches[6], let him say explicitly \"until the end of the third hour.\" ", 

            "His opinion is certainly that there are three watches in the night ; but his intention is to inform us", 

            " that there are watches in heaven as on earth[7]. For there is a teaching[8] : ", 

            "R. Eliezer says :", 

            " There are three watches in the night, and at each watch, the Holy One, blessed be He, sits enthroned and roars like a lion ; as it is said,", 

            " \"The Lord doth roar from on high, and utter His voice from His holy habitation ; He doth mightily roar[9] because of His fold \" (Jer. xxv. 30).  A sign for the matter [of the three earthly night-watches] is : ", 

            "at the first watch, the ass brays ; at the second, dogs bark ; and at the third, the babe sucks at the breast of its mother and a woman converses with her husband. ", 

            "Of what is R. Eliezer thinking ?", 

            " If he is thinking of the commencement of the watches, what need is there for a sign of the beginning of the first watch, ", 

            "since it is dusk ? ", 

            "Should he be thinking of the end of the watches, what need is there for a sign of the end of the last watch, ", 

            "since it is day ? ", 

            "Nay, ", 

            "he must be thinking of the end of the first watch, the beginning of the last watch, and the middle of the central watch. ", 

            "Or if thou wilt, I can say that in every case he is thinking of the end of the watches ; and shouldest thou urge", 

            " that a sign of the end of the last watch is unnecessary,", 

            "and ask what is its purpose ? It is for the reading of the Shema' on the part of one who sleeps in a dark room[1] and does not know when is the time for reading the Shema'. Therefore, when the woman converses with her husband and the child sucks at the breast of its mother, let him get up and read it. ", 

            "R. Isaac b. Samuel[2] said in the name of Rab[3]: ", 

            "The night is divided into three watches[4], and at each watch the Holy One, blessed be He, sits enthroned, roars like a lion and exclaims,", 

            " \"Alas for My children, for whose iniquities I destroyed My house, burnt My Temple, and exiled them among the nations of the world ! \" ", 

            "There is a teaching : R. Jose said :", 

            " Once I was journeying by the way, and I entered one of the ruins of Jerusalem to pray.", 

            " Elijah[5] — may he be remembered for good ! — came, waited at the entrance for me, and stayed until I had concluded my prayer[6]. ", 

            "After I had finished my prayer he said to me,", 

            " \" Peace be to thee, my master.\"", 

            " I responded,", 

            "\"Peace be to thee, my master and teacher.\"", 

            " Then he said to me,", 

            " \"My son, why didst thou enter this ruin ?\"", 

            " I answered,", 

            " \"To pray.\"", 

            " He said to me, ", 

            "\"Thou shouldest have prayed by the roadside.\"", 

            " I said, ", 

            "\"I feared lest passers-by interrupt me.\" ", 

            "Then said he to me,", 

            " \" Thou shouldest have offered an abbreviated prayer[1].\"", 

            " On that occasion I learnt three things from him : ", 

            "first, one should not enter ruins ; second, it is permissible to pray by the roadside ; third, one who prays by the roadside should offer an abbreviated prayer. ", 

            "Then he said to me,", 

            " \"My son, what sound didst thou hear in that ruin ?\"", 

            " I answered,", 

            " \"I heard a Bat Kol moaning like a dove[2], crying, ", 

            "'Alas for My children for whose iniquities I destroyed My house[3], burnt My Temple, and exiled them", 

            " among the nations ! '\" ", 

            "He said to me,", 

            " \"By thy life and the life of thy head, not only at this hour does it so cry, but thrice daily it exclaims thus.", 

            " Moreover, whenever the Children of Israel enter their", 

            " Synagogues and Houses of Study and respond 'Let His great Name be blessed[4],' the Holy One, blessed be He, shakes His head[5] and exclaims,", 

            " 'Happy the King Who is so praised in His house ! Alas[6] for the Father Who has banished His children ! And alas for the children who have been banished from their Father's table ! '\" ", 

            "Our Rabbis have taught : For three reasons one should not enter ruins : ", 

            "on account of suspicion[7], of falling fabric and evil spirits[8]. ", 

            "[Why mention] on account of suspicion, since thou canst derive [a sufficient reason] from the danger of falling fabric ? "

        ], 

        [

            " They might be new ruins[9]. ", 

            "Then derive it from the danger of evil spirits ! ", 

            "This would not apply when two men entered a ruin. But should there be two men, there would likewise be no ground for suspicion[10] ! ", 

            "There would be in the case of two men of ill-repute.", 

            " [Why mention] on account of falling fabric, since thou canst derive [a sufficient reason] from the grounds of suspicion and evil spirits ? ", 

            "No, not in the case of two men of good repute. ", 

            "[Why mention] on account of evil spirits, since thou canst derive [a sufficient reason] from the grounds of suspicion and falling fabric ? ", 

            "No, not in the case of new ruins and two men of good repute.", 

            " Is there no fear of evil spirits also when there are two men ?", 

            " In such places where evil spirits resort", 

            " there is occasion for fear.", 

            "Or if thou wilt, I can say that even in the case of a person alone and new ruins situated in a wild place[1] there is no ground for suspicion, because a woman does not frequent such a spot ; but the fear of evil spirits remains. ", 

            "Our Rabbis have taught : ", 

            "The night is divided into four watches. These are the words of Rabbi[2].", 

            " R. Nathan says :", 

            " Three. ", 

            "What is R. Nathan's reason ? ", 

            "Because it is written, \"So Gideon, and the hundred men that were with him, came unto the outermost part of the camp in the beginning of the middle watch \" (Judges vii 19). Hence he teaches that", 

            " there cannot be a \"middle watch\" unless one precedes and follows. ", 

            "How does Rabbi explain the phrase \"middle watch\" ? ", 

            "He takes it to mean one of the middle watches. ", 

            "What reply does R. Nathan make to this? He asks, ", 

            "Does Scripture state \"one of the two middle watches\"? ", 

            "No; the \"middle watch\" is explicitly mentioned[3]. ", 

            "What is Rabbi's reason [for declaring there are four watches] ? ", 

            "R. Zerika stated that R. Ammi said in the name of[4] R. Joshua b. Levi : ", 

            "One verse states, \"At midnight I will rise to give thanks unto Thee because of Thy righteous ordinances\" (Ps. cxix. 62) and another verse states, ", 

            "\"Mine eyes forestalled the night-watches\" (ibid. V. 148). How is this? ", 

            "There must be four watches in the night[5]. ", 

            "How does R. Nathan answer this argument?", 

            " He agrees with the opinion of R. Joshua ; for there is a Mishnaic teaching[6] : ", 

            "R. Joshua says : ", 

            "Until the third hour [in the day may the morning Shema' be read], for so is the custom of kings to rise at the third hour.", 

            " Six hours of the night and two of the day make two watches[1]. ", 

            "Rab Ashe said: ", 

            "A watch and a half are also referred to as \"watches[2].\" ", 

            "R. Zerika also stated that R. Ammi said in the name of[3] R. Joshua b. Levi : ", 

            "In the presence of the dead, we should only speak of matters relating to the dead. ", 

            "R. Abba b. Kahana said :", 

            " This applies only to words of Torah ; but as for worldly matters we can have no objection[4]. ", 

            "Another version is : R. Abba b. Kahana said : ", 

            "This applies even to words of Torah ; how much more so to worldly matters ! ", 

            "How David rose at midnight ! ", 

            "He rose at eventide ; ", 

            "as it is written, ", 

            "\"I arose early beneshef[5] and cried\" (Ps. cxix. 147). Whence is it learnt that neshef means evening ? Because it is written, \"In the twilight [beneshef], in the evening of the day, in the blackness of night and the darkness\" (Prov. vii. 9). ", 

            "R. Osha'ya said in the name of R. Aha[6] : Thus declared David, ", 

            "\"Midnight never passed me by in my sleep[7].\"", 

            " R. Zera said :", 

            " Until midnight ", 

            "David used to slumber like a horse[8], ", 

            "but from thence he grew strong like a lion[9]. ", 

            "Rab Ashe said :", 

            " Until midnight he was occupied with words of Torah, but from thence with psalms and praises. ", 

            "Neshef means evening !", 

            " Lo, it means the morning ; for it is written, ", 

            "\"And David smote them from the neshef even unto the evening ['ereb] of the next day\" (I Sam. xxx. 17). Is this not to be understood to mean from the morning unto the evening? ", 

            "No, from evening unto evening.", 

            " If so, the text should have read \"from the neshef unto the neshef\" or \"from the 'ereb unto the 'ereb\" ! ", 

            "But, says Raba[1], ", 

            "there are two occasions in the day called neshef; there is the neshef of the night followed by day, and the neshef of the day followed by night. ", 

            "Did David know when it was [exactly] midnight,", 

            " since even Moses our teacher was not certain ; as it is written, \"About mid-night will I go out into the midst of Egypt\" (Exod. xi. 4) ? What means \"about midnight\" ? ", 

            "Are we to suppose that the Holy One, blessed be He, used the phrase \"about midnight\" to Moses ?  Can there be any doubt in the mind of God ?", 

            " Nay ; God told him \"At midnight[2]\"; but Moses came and said", 

            " \"about midnight.\" Hence it is to be understood that Moses was in doubt, but David did know it !", 

            " He had a sign. For R. Hannah b. Bizna[3] said in the name of R. Simeon Hasida : ", 

            "There was a harp hanging above David's bed, and when the time of midnight arrived a North wind came and blew upon it, so that it produced melody[4]. He used immediately to rise and occupy himself with Torah until the break of dawn. ", 

            "At the rise of dawn, the wise men of Israel entered his presence and said to him,", 

            " \"Our lord, the king, thy people Israel are in need of sustenance.\" ", 

            "He answered them,", 

            " \"Go, let each sustain himself from the other[5].\" ", 

            "They said to him,", 

            " \"A handful cannot", 

            " satisfy a lion, nor can a pit be filled with its own clods[6].\"", 

            " He said to them,", 

            " \"Go, stretch forth your hands with the army[7].\" ", 

            "At once they took counsel with Ahitophel, consulted the Sanhedrin[8], and inquired of the Urim and Tummim[1].", 

            " Rab Joseph asked : ", 

            "What is the Scriptural authority for this?", 

            " \"And after Ahitophel was Benaiah the son of Jehoiada[2], and Abiathar ; and the captain of the king's host was Joab\" (I Chron. xxvii. 34) —", 

            " \"Ahitophel \" was the counsellor, for thus it is stated, \"Now the counsel of Ahitophel, which he counselled in those days, was as if a man inquired of the word of God\" (2 Sam. xvi. 23). "

        ], 

        [

            "\"Benaiah the son of Jehoiada\" refers to the Sanhedrin ; \"Abiathar[3]\" denotes the Urim and Tummim[4]. For so the Scriptures declare, ", 

            " \"And Benaiah the son of Jehoiada was over the Cherethites and over the Pelethites\" (2 Sam. xx. 23).  ", 

            " Why were the members of the Sanhedrin called Kereti and Peleti ?", 

            " They were called Kereti because they were concise [koretim] with their words, and Peleti because they were \"distinguished\" [muflaim] with their words[5]. ", 

            "After them came \"the captain of the king's host, Joab[6].\"", 

            "Rab Isaac b. Adda[7] (another version : Rab Isaac b. Rab Iddi) said : ", 

            "What Scriptural authority is there for the story of David's harp? \"Awake, my glory ; awake, psaltery and harp; I will awake the dawn\" (Ps. lvii. 9). ", 

            "R. Zera said :", 

            " Moses certainly knew [the exact time of midnight], and David also knew it. ", 

            "Since David knew it, why did he require a harp ?", 

            " In order that he may be aroused from his sleep. ", 

            "And since Moses knew it, what object had he in saying \"About mid-night\" ? ", 

            "Moses thought", 

            " that perhaps Pharaoh's astrologers would err[8] and say, \"Moses is a liar.\" ", 

            "For a teacher has said : ", 

            "Teach thy tongue to say, \"I do not know,\" lest thou be led to falsehoods and be apprehended. ", 

            "Rab Ashe said : ", 

            "It[1] happened in the middle of the night of the thirteenth [of the first month] which is the beginning of the fourteenth ; and thus spake Moses to Israel,", 

            " \"The Holy One, blessed be He, said, 'To-morrow, like the time of midnight, as it is now, I will go forth in the midst of Egypt.'\" ", 

            "David prayed, \"Keep my soul, for I am godly\" (Ps. Ixxxvi. 2). [R.] Levi[2] and R. Isaac differ in their interpretation.", 

            " One explains : ", 

            "Thus spake David before the Holy One, blessed be He, ", 

            "\"Lord of the Universe, am I not godly, ", 

            "seeing that all the kings of the East and West sleep unto the third hour of the day, but as for me, 'At midnight I rise to give thanks unto Thee' (Ps. cxix. 62)?\" ", 

            "The other explains : ", 

            "Thus spake David before the Holy One, blessed be He,", 

            " \"Lord of the Universe, am I not godly,", 

            " seeing that all the kings of the East and West sit in companies[3] in all their pomp, whereas my hands are stained with the blood of a foetus or with the placenta[4] in order to pronounce a woman clean to her husband ? ", 

            "Moreover, ", 

            "whatever I do I discuss with my teacher Mephibosheth[5], saying to him,", 

            " 'Mephibosheth, my teacher, ", 

            "have I decided well ? ", 

            "Have I convicted correctly", 

            " or acquitted correctly ? ", 

            "Did I rightly pronounce clean", 

            " or rightly pronounce unclean?' ", 

            "And I was not ashamed [so to do].\" ", 

            "R. Joshua b. Rab Iddi[6] asked :", 

            " What is the Scriptural authority for this ? \"I will also speak of Thy testimonies", 

            " before kings, and will not be ashamed\" (Ps. cxix. 46). ", 

            "It has been taught: ", 

            "His name was not Mephibosheth but Ishbosheth. Why, then, was he called Mephibosheth? ", 

            "Because he used to put David to shame[7] on questions of Halakah.", 

            " On that account David merited that Chileab[8] should issue from him;", 

            " and R. Johanan said: ", 

            "His pame was not Chileab but Daniel[1]. Why, then, was he called Chileab? Because he put Mephibosheth to shame[2] on questions of Halakah; and concerning him Solomon said in his wisdom, ", 

            "\"My son, if thy heart be wise, my heart will be glad, even mine\" (Prov. xxiii. 15), and ", 

            "\"My son, be wise, and make mine heart glad, that I may answer him that taunteth me\" (ibid, xxvii. 11). ", 

            "But how could David describe himself as \"godly[3]\"?", 

            " For behold it is written, \"If I had not [lule'] believed to look upon the goodness of the Lord in the land of the living\" (Ps. xxvii. 13); and it has been taught in the name of R. Jose : ", 

            "Why are there dots over the word lule'[4]?", 

            " David spake before the Holy One, blessed be He,", 

            " \"Lord of the Universe,", 

            " I am confident that Thou repayest a good reward to the righteous in the hereafter, but I know not whether I have a portion among them or not[5]. ", 

            "Perhaps my sin will cause [me not to[6]].\"", 

            " This is like the teaching of R. Jacob b. Iddi who asked: It is written, ", 

            "\"Behold, I am with thee, and will keep thee whithersoever thou goest\" (Gen. xxviii. 15), and then it is written, ", 

            "\"Jacob was greatly afraid\" (ibid, xxxii. 8)!", 

            " But Jacob said,", 

            " \"Perhaps sin will cause [His protection to be withheld].\" This is like the teaching:", 

            " \"Till Thy people pass over, O Lord, till the people pass over that Thou hast gotten\" (Exod. xv. 16).", 

            " — \"Till Thy people pass over, O Lord\" refers to the first entry [into Canaan]; \"till the people pass over that Thou hast gotten\" refers to the second entry[7]. ", 

            "Hence the Sages said : ", 

            "The Israelites were worthy that a miracle should be performed for them in the days of Ezra", 

            " in the same way that it was performed for them in the days of Joshua, the son of Nun; but sin caused [the miracle to be withheld][1]. ", 

            "But the Sages say: Until midnight. ", 

            "With whose opinion do the Sages agree?", 

            " If with R. Eliezer's, let them express themselves like R. Eliezer;"

        ], 

        [

            "if with Rabban Gamaliel's, let them express themselves like Rabban Gamaliel[2]!", 

            " They certainly agree with Rabban Gamaliel, and the reason they say Until midnight is to keep a man far from transgression. ", 

            "This is like the teaching:", 

            " The Sages made a \"fence[3]\" to their words, so that a man shall not come from the field[4] in the evening and say,", 

            " \"I will go home, eat a little, drink a little, sleep a little, and after that I will read", 

            " the Shema' and say the Tefillah\"; ", 

            "for slumber may overcome him and as a result he may sleep through all the night[5]. ", 

            "Rather should a man come from the field in the evening and enter a Synagogue ; if he is accustomed to read [the Scriptures], let him read; if he is accustomed to study[6], let him study. Then let him read the Shema' and say the Tefillah; after that he should eat his meal and say Grace. ", 

            "Whosoever transgresses the words of the Sages [in this matter] is worthy of death. ", 

            "Why is it not stated in any other place that whosoever transgresses the words of the Sages is worthy of death, but here a distinction is made and it is so stated?", 

            " If thou wilt, I can say", 

            " that here there is the danger of the overpowering force of sleep[1];", 

            " or if thou wilt, I can say ", 

            "that it is intended to exclude the opinion of those who maintain that the evening prayer is voluntary[2]; and hence we are informed that it is an obligation. ", 

            "The teacher stated above :", 

            " \"Then let him read the Shema' and say the Tefillah.\" ", 

            "This supports the view of R. Johanan who declared : ", 

            "Who will inherit the world to come? ", 

            "He who joins the Ge'ullah to the evening Tefillah[3].", 

            " R. Joshua b. Levi said : ", 

            "The Tefillot were arranged in the middle[4]. ", 

            "What is the point on which they differ?", 

            " If thou wilt, I can say [they differ in the interpretation of] a Scriptural passage; or if thou wilt, I can say [they differ] in their reasoning.", 

            " If thou wilt, I can say [they differ] in their reasoning : for R. Johanan holds", 

            " that the deliverance [from Egypt] began also at night[5], but the complete deliverance did not take place until the morning. ", 

            "R. Joshua b. Levi holds", 

            " that since the deliverance did not take place until the morning, [what happened in the night] is not to be considered a proper deliverance. ", 

            "Or if thou wilt, I can say [they differ in the interpretation of] a Scriptural passage; and they both expound the same verse, viz.", 

            " \"When thou liest down and when thou risest up\" (Deut. vi. 7). R. Johanan holds that ", 

            "an analogy is here to be drawn between \"lying down\" and \"rising up\" in this sense: as with \"rising up\" the order is the reading of the Shema' and then the Tefillah, so also with \"lying down\" the order is the reading of the Shema' and then the Tefillah. ", 

            "R. Joshua b. Levi, however, thinks that ", 

            "the analogy is to be drawn between \"lying down\" and \"rising up\" in this sense : as with \"rising up\" the reading of the Shema' is nearer to his contact with the bed[1], so with \"lying down\" the reading of the Shema' must be nearer to his contact with the bed. ", 

            "Mar b. Rabina quoted in objection :", 

            " In the evening [the reading of the Shema'] is both preceded and followed by two benedictions[2].", 

            " If, then, thou sayest that the Ge'ullah must be joined to the Tefillah, behold that condition is not fulfilled because one is required to say the prayer \"Cause us, O Lord our God, to lie down[3]!", 

            "\" They answer: ", 

            "Since the Rabbis instituted the prayer \"Cause us, etc.,\" it is to be considered part of the Ge'ullah[4].", 

            " If thou dost not admit this, ", 

            "how is it possible to affect the same union in the morning service ; ", 

            "for lo, R. Johanan has said : Before the Tefillah one says,", 

            " \"O Lord, open Thou my lips\" (Ps. li. 17)[5], and at its conclusion, ", 

            "\"Let the words of my mouth... be acceptable\" (ibid. xix. 15) !", 

            " In this case, ", 

            "since the Rabbis instituted the saying of ", 

            "\"O Lord, open Thou my lips,\" it is considered part of the Tefillah ; so likewise in the evening prayer, the Rabbis having instituted the saying of \"Cause us, etc.,\" it is considered part of the Ge'ullah. ", 

            "R. Eleazar b. R. Abina[6] said: ", 

            "Whoever recites Psalm cxlv. thrice[7] daily may be assured that he is a son of the world to come. ", 

            "What is the reason? ", 

            "Is it to be supposed because the initial letter of the verses follows the alphabetical order? Then let him recite Psalm cxix. which contains an eight-fold alphabetical order!", 

            " No, the reason is that it contains the verse, \"Thou openest Thy hand and satisfiest every living thing with favour\" (Ps. cxlv. 16)[8]. Then let him say the Great Hallel[9] which includes", 

            " \"Who giveth food to all flesh\" (ibid. cxxxvi. 25)! ", 

            "But [Psalm cxlv. is selected] because it contains both features. ", 

            "R. Johanan[1] said:", 

            " Why is there no verse beginning with the letter N in that Psalm ? ", 

            "Because it would refer to the downfall of Israel's enemies[2]; as it is written,", 

            " \"Fallen (Naphelah) is the virgin of Israel, she shall no more rise\" (Amos v. 2).", 

            " In the West[3] they interpret the verse thus: ", 

            "\"She is fallen, but she shall no more fall; rise, O virgin of Israel.\" ", 

            "Rab Nahman b. Isaac said :", 

            " Even so, David refers to it and finds support for Israel in the Holy Spirit; as it is said, \"The Lord upholdeth all that fall\" (Ps. cxlv. 14). ", 

            "R. Eleazar b. Abina [also] said : ", 

            "What is declared of [the angel] Michael is greater than what is declared of Gabriel ; for of Michael it is written, \"Then flew unto me one of the Seraphim\" (Is. vi. 6), but of Gabriel it is written,", 

            " \"The man Gabriel whom I had seen in the vision at the beginning, being caused to fly swiftly[4], approached close to me about the time of the evening offering\" (Dan. ix. 21). ", 

            "How is it to be inferred that \"one of the Seraphim\" means Michael ?", 

            " R. Johanan said : ", 

            "By comparing the occurrence of the word \"one\"[5] in the following passages: In Isaiah it is written, \"Then flew unto me one of the Seraphim,\" and elsewhere it is written, \"But, lo, Michael, one of the chief princes, came to help me\" (ibid. x. 13). ", 

            "It has been taught : ", 

            "Michael flew in one flight, Gabriel in two, Elijah in four, and the Angel of Death in eight; but in the time of plague [the Angel of Death flies] in one. ", 

            "R. Joshua b. Levi said : ", 

            "Although a man has read the Shema' in the Synagogue, it is a pious act to read it again upon his bed. ", 

            "R. Assi[6] said : ", 

            "What is the Scriptural authority for this ? \"Tremble and sin not ; commune with your own heart upon your bed, and [[fol. 5a.]] be still. Selah \" (Ps. iv. 5). ", 

            "Rab Nahman added : "

        ], 

        [

            "In the case of a disciple of the wise[7], this is not necessary. ", 

            "But Abbai said: ", 

            "Even the disciple of the wise should recite a verse of supplication; for instance, \"Into Thy hand I commit my spirit. Thou hast redeemed me, O Lord, Thou God of truth\" (ibid. xxxi. 6). ", 

            "R. Levi b. Hamma[1] said in the name of R. Simeon b. Lakish: ", 

            "A man should always oppose [yargiz] the good impulse to the evil impulse[2] ; as it is said : \"Tremble [rigzu] and sin not\" (ibid. iv. 5).", 

            " If he conquer it, well and good ; but if not, let him occupy himself with Torah ; as it is said,", 

            " \"Commune with your own heart\" (ibid.)[3].", 

            " Should this gain him the victory, well and good; but if not, let him read the Shema' ; as it is said, ", 

            "\"Upon your bed[4].\"", 

            " If he conquer it, well and good ; but if not, let him reflect ", 

            "upon the day of death; as it is said, ", 

            "\"And be still[5]. Selah.\" ", 

            "R. Levi ", 

            "b. Hamma also said in the name of R. Simeon b. Lakish : ", 

            "What means that which is written,", 

            " \"And I will give thee the tables of stone, and the law and the commandment, which I have written, that thou mayest teach them\" (Exod. xxiv. 12)? \"Tables of stone,\" i.e. the Decalogue: \"law,\" i.e. the Pentateuch; \"commandment,\" i.e. the Mishnah ; \"which I have written,\" i.e. the Prophets and Hagiographa; \"that thou mayest teach them,\" i.e. the Gemara[6]. ", 

            "The verse teaches that all of them were given to Moses on Sinai[7]. ", 

            "R. Isaac[8] said :", 

            " Whoever reads the Shema' upon his bed is as though he holds a two-edged sword in his hand[9]; as it is said, \"Let the high praises of God be in their mouth, and a two-edged sword in their hand\" (Ps. cxlix. 6). ", 

            "How is this inferred ? ", 

            "Mar Zotra (another version : Rab Ashe) said :", 

            " From what precedes ; for it is written, \"Let the saints exult in glory, let them sing for joy upon their beds\" (ibid. v. 5), and this is followed by ", 

            "\"Let the high praises of God be in their mouth, and a two-edged sword in their hand.\" ", 

            "R. Isaac also said : Whoever reads the Shema' upon his bed, the evil spirits flee from him ; as it is said, \"And the sons of Reshef[1] fly upwards ['uf] \" (Job v. 7). ", 

            "'Uf means nothing else than Torah ; as it is said,", 

            " \"Wilt thou set [hata'if][2] thine eyes upon it? It is gone\" (Prov. xxiii. 5). ", 

            "And Reshef means nothing else than \"evil spirits\"; as it is said, \"The wasting of hunger, and the devouring of the fiery bolt [Reshef] and bitter destruction\" (Deut. xxxii. 24)[3]. ", 

            "R. Simeon b, Lakish said : Whoever occupies himself with Torah, sufferings depart from him ; as it is said, ", 

            "\"And the sons of Reshef fly upwards ['uf].\"", 

            " 'Uf means nothing else than Torah; as it is said, ", 

            "\"Wilt thou set thine eyes upon it? It is gone.\" ", 

            "And Reshef means nothing else than \"sufferings\"; as it is said,", 

            " \"The wasting of hunger, and the devouring of the fiery bolt.\" ", 

            "R. Johanan said to him : ", 

            "Why, even school-children know that[4]; as it is stated, ", 

            "\"And He said, If thou wilt diligently hearken to the voice of the Lord thy God, and wilt do that which is right in His eyes, and wilt give ear to His commandments, and keep all His statutes, I will put none of the diseases upon thee, which I have put upon the Egyptians ; for I am the Lord that healeth thee \" (Exod. xv. 26) ! ", 

            "But[5], everyone who is able to occupy himself with Torah and does not do so, the Holy One, blessed be He, brings upon him dreadful sufferings to stir him ; as it is said,", 

            " \"I was dumb with silence, I held my peace, had no comfort [tob] ; and my pain was stirred\" (Ps. xxxix. 3). \"Comfort\" means nothing else than Torah; as it is said, ", 

            "\"For I give you good [tob] doctrine; forsake ye not My teaching \" (Prov. iv. 2). ", 

            "R. Zera (another version : R. Hannina b. Pappa)[6] said : ", 

            "Come and see that the attribute of a human being differs from that of the Holy One, blessed be He. What is the attribute of a human being ? When a man sells a valued article to his fellow, the seller grieves[1] and the purchaser rejoices. ", 

            "But with the Holy One, blessed be He, it is not so. He gave the Torah to Israel and rejoiced[2]; as it is said,", 

            " \"For I give you good doctrine ; forsake ye not My teaching.\" ", 

            "Raba (another version : Rab Hisda)[3] said :", 

            " Should a man see sufferings come upon him, let him scrutinise his actions ; as it is said, \"Let us search and try our ways, and return unto the Lord\" (Lam. iii. 40).", 

            " If he has scrutinised his actions without discovering the cause, let him attribute them to neglect of Torah; as it is said,", 

            " \"Happy is the man whom Thou chastenest, and teachest out of Thy law\" (Ps. xciv. 12). ", 

            "If he attributed them to neglect of Torah without finding any justification, it is certain that his sufferings are chastenings of love ; as it is said,", 

            "\"For whom the Lord loveth He correcteth\" (Prov. iii. 12)[4]. ", 

            "Raba stated that Rab Sahorah said in the name of Rab Huna : ", 

            "Him in whom the Holy One, blessed be He, delighteth He crusheth with sufferings ; as it is said, ", 

            "\"Yet it pleased the Lord to crush him by disease\" (Is. liii. 10). ", 

            "It is possible to think that this is so even with one who does not receive the chastenings in a spirit of love : therefore there is a teaching to say, \"To see if his soul would offer itself in restitution\" (ibid.). Just as the trespass-offering[5] is brought voluntarily, so are the sufferings voluntarily received. ", 

            "If he accept them, what is his reward? \"He will see his seed, prolong his days\" (ibid.). ", 

            "More than that, his study [of Torah] will endure with him; as it is said, ", 

            "\"The purpose of the Lord will prosper in his hand\" (ibid.). ", 

            "R. Jacob b. Iddi and Rab Aha b. Hannina [differ in opinion]. One of them says :", 

            " Those are to be considered chastenings of love which do not involve neglect of Torah; as it is said,", 

            " \" Happy is the man whom Thou chastenest, O Lord, and teachest him out of Thy law \" (Ps. xciv. 12). ", 

            "The other declares : ", 

            "Those are to be considered chastenings of love which do not involve neglect of prayer; as it is written, ", 

            "\"Blessed be God, Who hath not turned away my prayer, nor His mercy from me\" (Ps. lxvi. 20)[1] ", 

            "R. Abba the son of R. Hiyya b. Abba said to them : Thus declared R. Hiyya b. Abba in the name of R. Johanan : ", 

            "Both of them are to be considered chastenings of love ; as it is said, ", 

            "\"For whom the Lord loveth He correcteth\" (Prov. iii. 12). ", 

            "But what does the phrase \"and teachest him out of Thy law\" (Ps. xciv, 12) intend to convey to us ?", 

            " Read not telammedennu \"and teachest him\" but telammedennu \"and teachest us[2]\"; i.e., Thou teachest us this matter out of Thy law", 

            " as a deduction[3] from the ordinance ", 

            "concerning \"the tooth and eye[4].", 

            "\" Should the tooth or eye of a slave be injured, which is only one of the members of a man's body, he thereby obtains his freedom, how much more so with the sufferings which afflict the whole body of a man[5] ! This is in accord with the statement of R. Simeon b. Lakish who said: ", 

            "The word berit \"covenant\" is mentioned in connection with salt and also with chastenings. ", 

            "With salt, as it is written, \"Thou shalt not suffer the salt of the covenant of Thy God to be lacking\" (Lev. ii. 13); ", 

            "and with chastenings, as it is written, ", 

            "\"These are the words of the covenant\" (Deut. xxviii. 69)[6]. ", 

            "As with the \"covenant\" mentioned in connection with salt, it is salt which sweetens meat, so with the \"covenant\" mentioned in connection with chastenings, they are chastenings which purge all the iniquities of man. ", 

            "There is a teaching : R. Simeon b. Johai said :", 

            " Three precious gifts did the Holy One, blessed be He, give to Israel, and all of them He gave only through the medium of suffering ;", 

            " they are : Torah, the land of Israel, and the world to come. ", 

            "Whence is it deduced that Torah [was given through the medium of suffering]?  As it is said :", 

            " \"Happy is the man whom Thou chastenest, O Lord, and teachest him out of Thy law \" (Ps. xciv. 12). ", 

            "And the land of Israel ? For it is written, \"As a man chasteneth his son, so the Lord thy God chasteneth thee\" (Deut. viii. 5), which is followed by ", 

            "\"For the Lord thy God bringeth thee into a good land\" (ibid. V. 7).", 

            " And the world to come ? For it is written, \"For the commandment is a lamp, and the teaching is light, and reproofs of instruction' are the way of life\" (Prov. vi. 23). [1]", 

            "A Tanna taught in the presence of R. Johanan : ", 

            "whoever occupies himself with Torah and benevolent acts, "

        ], 

        [

            "or who buries his children, all his sins are forgiven him. ", 

            "R. Johanan said to him : ", 

            "It is quite right with Torah and benevolent acts ; for it is written,  \"By mercy and truth iniquity is expiated\" (Prov. xvi. 6) ", 

            "\"mercy\" means benevolent acts, as it is said, \"He that followeth after righteousness and mercy findeth life, prosperity and honour\" (ibid. xxi. 21), and \"truth\" means Torah, as it is said, ", 

            "\"Buy the truth, and sell it not\" (ibid, xxiii. 23); ", 

            "but how know we that this is true of one who buries his children? ", 

            "A certain Elder taught in the name of R. Simeon b. Johai[2] : ", 

            "It is to be derived from the occurrence of the same word 'awon \"iniquity\" in the following passages : ", 

            "\"By mercy and truth iniquity is expiated\" (ibid. xvi. 6) ", 

            "and \"Who recompensest the iniquity of the fathers into the bosom of their children\" (Jer. xxxii. 18)[3]. ", 

            "R. Johanan said :", 

            " Plagues and childlessness are not to be considered chastenings of love. ", 

            "Are not plagues to be so considered?", 

            " Lo, there is a teaching :", 

            " Whoever is afflicted with any of four plague-symptoms[4] is to regard them as nothing but an altar of atonement[5] !", 

            " Yes, they may be considered an altar of atonement, but not chastenings of love. ", 

            "Or if thou wilt,", 

            " I can say this is our teaching and that is theirs[6]. ", 

            "Or if thou wilt, ", 

            "I can say the latter teaching refers to when the plague affects a hidden part of the body and the other to the case where an exposed part is affected[1]. Is not childlessness to be considered [chastenings of love] ? ", 

            "What is meant [by childlessness] ?", 

            " Is it to be supposed to refer to a man who had children but they died ? Lo, R. Johanan himself said, ", 

            "\"This is the bone of my tenth son[2]!\"", 

            " Nay, ", 

            "the latter teaching refers to one who never had children, the other to one who has been bereft of his children. ", 

            "R. Hiyya b. Abba was ill and R. Johanan went in to visit him. ", 

            "He said to him, ", 

            "\"Are thy sufferings dear to thee ?\"", 

            " \"No,\" he replied,", 

            " \"neither they nor the reward they bring.\"", 

            " R. Johanan said to him,", 

            " \"Give me thy hand.\" ", 

            "He gave him his hand and R. Johanan raised him[3]. ", 

            "R. Johanan was ill and R. Hannina went in to visit him. ", 

            "He said to him, ", 

            "\"Are thy sufferings dear to thee?\" ", 

            "\"No,\" he replied, ", 

            "\"neither they nor the reward they bring.\"", 

            "R. Hannina said to him, ", 

            "\"Give me thy hand.\"", 

            "He gave him his hand and R. Hannina raised him. ", 

            "", 

            "Why did not R. Johanan raise himself ? ", 

            "They answer :", 

            " A prisoner does not release himself from the dungeon. ", 

            "R. Eleazar[4] was ill ", 

            "and R. Johanan went in to visit him. ", 

            "He saw that he was lying in a dark room, so he bared his arm and a brightness was radiated therefrom[5]. ", 

            "He then noticed that R. Eleazar was weeping.", 

            " He said to him,", 

            " \"Why weepest thou?", 

            " Is it because thou hast not applied thyself sufficiently to the study of Torah ? We have learnt that", 

            " it matters not whether one does much or little, so long as he directs his heart to Heaven !", 

            " Is it because of [the lack of] food[6]? Not everyone has the merit of two tables[7]!", 

            " Is it because of childlessness? This is the bone of my tenth son!\" ", 

            "R. Eleazar answered him,", 

            " \"I weep because of this beauty[1] which will decay in the earth.\"", 

            " R. Johanan said to him, ", 

            "\"Well dost thou weep on that account\" ; and they both wept. ", 

            "After a while, he said to him,", 

            " \"Are thy sufferings dear to thee?\" ", 

            "He replied, ", 

            "\"Neither they nor the reward they bring.\" ", 

            "He said to him,", 

            " \"Give me thy hand.\" He gave him his hand and R. Johanan raised him. ", 

            "It happened to Rab Huna that four hundred flasks of wine turned sour. ", 

            "There visited him Rab Judah the brother of Rab Sala Hasida and other Rabbis. ", 

            "(Another version : Rab Adda b. Ahaba and other Rabbis.) They said to him, ", 

            "\"The master[2] should look into his actions[3].\" ", 

            "He answered them, ", 

            "\"Have I aroused suspicion in your eyes?\" ", 

            "They retorted,", 

            " \"Is the Holy One, blessed be He, to be suspected of passing an unjust judgment?\" ", 

            "He said to them,", 

            " \"If there be anyone who has heard aught against me, let him speak out.\" ", 

            "They replied, ", 

            "\"Thus have we heard, that our master has not given the vine-tendrils to his labourer[4].\" ", 

            "He said to them, ", 

            "\"Has he left me any of them ? ", 

            "He has stolen the lot!\"", 

            " They replied,", 

            " \"That is what the proverb tells : ", 

            "'Steal from a thief and thou also hast a taste of it'[5].\" ", 

            "He said to them,", 

            " \"I undertake to give him what is due.\" ", 

            "Some declare ", 

            "that thereupon the vinegar turned back into wine, ", 

            "but others say ", 

            "that vinegar became very dear and was sold at the price of wine. ", 

            "There is a teaching : Abba Benjamin said : ", 

            "Throughout my life I was most anxious about two things, viz., that my Tefillah should be recited before my bed, and that my bed should be placed between North and South.", 

            " \"That my Tefillah should be recited before my bed.\" ", 

            "What means \"before my bed\" ? Is it to be supposed that it was actually in front of the bed? But Rab Judah has said in the name of Rab (another version : R. Joshua b. Levi)[6]: ", 

            "Whence do we learn that when one prays, there should be nothing intervening between him and the wall? As it is said,", 

            " \"Then Hezekiah turned his face to the wall and prayed\" (Is. xxxviii. 2)[2]!", 

            " Do not read \"before my bed\" but", 

            " \"near my bed[2].\" ", 

            "\"And that my bed should be placed between North and South[3]\" ; for R. Hamma b. R. Hannina said in the name of[4] R. Isaac :", 

            " Whoever places his bed between North and South will have male children[5] born to him ; as it is said, \"And whose belly Thou fillest with Thy treasure[6], who have sons in plenty\" (Ps. xvii. 14).", 

            " Rab Nahman b. Issac said : Also, his wife will not miscarry;", 

            " for it is here written, ", 

            "\"Thou fillest with Thy treasure,\" and elsewhere it is written, \"And when her days to be delivered were fulfilled, behold, there were twins in her womb\" (Gen. xxv. 24). ", 

            "There is a teaching : Abba Benjamin said : ", 

            "Should two enter a Synagogue[7] to pray, and one of them finishing before the other does not wait for him but goes out, his prayer is torn in his face ; as it is said, ", 

            "\"Thou tearest thy soul[8] in thine anger, shall the earth be forsaken for thee ?\" (Job xviii. 4). ", 

            "More than that, he causes the Shekinah to depart from Israel ; as it is said, ", 

            "\"Shall the Rock be removed out of its place?\" (ibid.)", 

            " \"Rock\" means nothing else than the Holy One, blessed be He; as it is said, \"Of the Rock that begat thee thou wast unmindful\" (Deut. xxxii. 18)[9]. [[fol. 6 a.]] ", 

            "Should he, however, wait for him, what is his reward ?  "

        ], 

        [

            "R. Jose b. Hannina answered :", 

            " He is worthy of the following blessings ; as it is said,]", 

            " \"Oh that thou wouldst hearken to My commandments! Then would thy peace be as a river, and thy righteousness as the waves of the sea ; thy seed also would be as the sand, and the offspring of thy body like the grains thereof ; his name would not be cut off nor destroyed from before Me\" (Is. xlviii. 18 f.). ", 

            "There is a teaching : Abba Benjamin said : ", 

            "Had the human eye been given the power of seeing them, no person could endure because of the evil spirits. ", 

            "Abbai[1] said : ", 

            "They outnumber us, and surround us like the ridge round a field. ", 

            "Rab Huna said : Every one of us has a thousand on his left hand and myriads on his right[2]. ", 

            "Raba[3] said : ", 

            "The crush at the public discourses[4] is due to them ;", 

            "the knees grow fatigued because of them ; ", 

            "the wearing out of the clothes of the Rabbis is the consequence of their rubbing against them ;", 

            " the feet are bruised by them. ", 

            "Who wishes to perceive their footprints[5] should take sifted ashes and sprinkle them around his bed. In the morning he will see something resembling the footprints of a cock[6]. ", 

            "Who wishes to see them should take the after-birth of a black she-cat[7], the offspring of a black she-cat, the first-born of a first-born, roast it in the fire, pulverise it, then fill his eyes with it, and he will see them.", 

            " He must pour the powder into an iron tube and seal it with an iron signet, lest the evil spirits steal it. ", 

            "He must also seal its mouth,", 

            " lest he come to harm. ", 

            "Rab Bebai b. Abbai did this ; he saw the evil spirits and was injured. ", 

            "The Rabbis prayed for him and he was cured. ", 

            "There is a teaching : Abba Benjamin said : ", 

            "A man's prayer is only", 

            " heard [by God]  when offered in a Synagogue[1] ; as it is said,", 

            " \"To hearken unto the song and to the prayer\" (I Kings viii. 28) — where there is song, let there be prayer. ", 

            "Rabin b. Adda said in the name of R. Isaac : ", 

            "Whence is it that the Holy One, blessed be He, is found in the Synagogue ? As it is said, ", 

            "\"God standeth in the godly congregation \" (Ps. Ixxxii. 1 ). ", 

            "And whence is it that when ten assemble for prayer, the Shekinah is in their midst ? As it is said, ", 

            "\"God standeth in the godly congregation[2].\" ", 

            "And whence is it that when three sit and judge, the Shekinah is in their midst? As it is said, ", 

            "\"In the midst of the judges[3] He judgeth\" (ibid.).", 

            " And whence is it that when two sit and occupy themselves with Torah, the Shekinah is in their midst ? As it is said, ", 

            "\"Then they that feared the Lord spoke one with another[4]; and the Lord hearkened and heard, and a book of remembrance was written before Him for them that feared the Lord and that thought upon His name\" (Mal. iii. 16). ", 

            "What means \"and that thought upon His name\"? ", 

            "Rab Assi[5] said :", 

            " If a man contemplated fulfilling a commandment, and through compulsion did not perform it, the verse ascribes it to him as though he had done it. ", 

            "And whence is it that even if an individual sits and occupies himself with Torah, the Shekinah is with him ? As it is said, ", 

            "\"In every place where I cause My name to be remembered I will come unto thee and will bless thee\" (Exod. xx. 24). ", 

            "Since [the Shekinah is] even with one, why mention two ?", 

            " With two, their words are written in the book of remembrance, but the words of an individual are not so recorded. ", 

            "Since [the Shekinah is] even with two, ", 

            "why mention three? ", 

            "Thou mightest argue that since the act of judging is merely for the sake of peace[6], the Shekinah does not come [in their midst], therefore he informs us that the administration of justice is equal to being occupied with Torah. ", 

            "Since [the Shekinah is] even with three, why mention ten ? ", 

            "With ten, the Shekinah precedes them[1] ; with three, it waits until they are seated [to try cases]. ", 

            "Rab Abin b. Rab Adda said in the name of R. Isaac[2] : ", 

            "Whence is it that the Holy One, blessed be He, lays Tefillin[3] ? As it is said, \"The Lord hath sworn by His right hand, and by the arm of His strength\" (Is. Ixii. 8). ", 

            "\"By His right hand\" means Torah ; as it is said, ", 

            "\"At His right hand was a fiery law unto them\" (Deut. xxxiii. 2); ", 

            "\"by the arm of His strength\" means Tefillin, as it is said, ", 

            "\"The Lord will give strength unto His people\" (Ps. xxix. 11). ", 

            "But whence is it that the Tefillin are a strength to Israel? As it is written, ", 

            "\"And all the peoples of the earth shall see that the name of the Lord is called upon thee, and they shall he afraid of thee\" (Deut. xxviii. 10); and there is a teaching: R. Eliezer the Elder says : ", 

            "This refers to the Tefillin worn on the head[4]. ", 

            "Rab Nahman b. Isaac asked Rab Hiyya b. Abin : ", 

            "What is written in the Tefillin of the Lord of the Universe ?", 

            " He answered,", 

            " \"And who is like Thy people Israel, a nation one in the earth?\" (I Chron. xvii 21).", 

            " Does, then, the Holy One, blessed be He, glory in the praises of Israel ?", 

            " Yes, for it is written,", 

            " \"Thou hast avouched the Lord this day\" (Deut. xxvi. 17) ", 

            "and \"The Lord hath avouched thee this day \" (ibid. v. 18). ", 

            "The Holy One, blessed be He, said to Israel, ", 

            "\"You have made Me the only object of your love[5] in the world, so I shall make you the only object of My love in the world.\"", 

            " \"You have made Me the only object of your love in the world\" — as it is said,", 

            " \"Hear O Israel, the Lord our God, the Lord is one\" (ibid. vi. 4).", 

            " \"I shall make you the only object of My love in the world\" — as it is said, ", 

            "\"And who is like Thy people Israel, a nation one in the earth?\" (I Chron. xvii. 21). ", 

            "Rab Aha b. Raba said to Rab Ashe : ", 

            "This is all very well with one case of the Tefillin ; what, however, of the other[6]? ", 

            "He answered :", 

            " [It contains the following[1] :] \"For what great nation is there,\" etc. (Deut. iv. 7), \"And what great nation is there,\" etc. (ibid, v. 8), \"Happy art thou, O Israel \" etc. (ibid, xxxiii. 29), \"Or hath God assayed to go\" etc. (ibid. iv. 34), and \"To make thee high above all nations\" etc. (ibid. xxvi. 19).", 

            " If so, it will have too many partitions[2] ! ", 

            "Nay, \"For what great nation is there\" and \"And what great nation is there,\" which are very similar, are in one partition; \"Happy art thou, O Israel\" and \"Who is like Thy people Israel\" in one ; \"Or hath God assayed to go\" in one ; and \"To make thee high above all nations\" in one[3].  "

        ], 

        [

            "[not translated: and they are all (the verses mentioned there) written on His arm]", 

            "Rabin b. Rab Adda said in the name of R. Isaac :", 

            "If one is accustomed to attend the Synagogue regularly and absents himself one day, the Holy One, blessed be He, makes inquiry about him ; as it is said, ", 

            "\"Who is among you that feareth the Lord, that obeyeth the voice of His servant, that walketh in darkness and hath no light?\" (Is. 1. 10).", 

            " If [his absence is because] he went to perform a religious duty, he will have light ; but if he went to attend to some secular business, he will have no light.", 

            " \"Let him trust in the name of the Lord\" (ibid.). For what reason [is the light denied him][4] ? Because he should have trusted in the name of the Lord, but did not[5]. ", 

            "R. Johanan said :", 

            " When the Holy One, blessed be He, enters a Synagogue and does not find there ten[6]. He is immediately filled with wrath ; as it is said, ", 

            "\"Wherefore, when I came, was there no man ? When I called, was there none to answer ?\" (ibid. v. 2)[7]. ", 

            "R. Helbo said in the name of Rab Huna : ", 

            "Whoever fixes a place for his prayer has the God of Abraham for his help : ", 

            "and on his death, it is said of him, ", 

            "\"Where is the humble and pious man, of the disciples of our father Abraham !\"", 

            " Whence do we learn that our father Abraham fixed a place for his prayer ?", 

            " For it is written, ", 

            " (Gen. xix. 27)", 

            "\"And Abraham got up early in the morning to the place where he had stood\". \"Stood\" means nothing else than prayer ; as it is said, ", 

            "\"Then stood up Phineas and prayed\" (Ps. cvL 30)[1]. ", 

            "R. Helbo [also] said in the name of Rab Huna : ", 

            "When leaving the Synagogue, one should not take large steps[2]. ", 

            "Abbai said: ", 

            "This refers only to leaving ; but to enter a Synagogue it is praise-worthy to hasten ; as it is said, \"Let us eagerly strive to know the Lord\" (Hos. vi. 3). ", 

            "R. Zera said :", 

            " At first when I saw the Rabbis hastening to the study-session on the Sabbath,", 

            " I thought they were desecrating the holy day[3]; ", 

            "but when I heard the statement of R. Tanhum, in the name of R. Joshua b. Levi : ", 

            "A man should always run to hear the Halakah discussed, even on the Sabbath, as it is said, \"They shall walk after the Lord, who shall roar like a lion, for He shall roar, and the children shall come hurriedly from the West\" (ibid. xi. 10), I also hastened. ", 

            "R. Zera said : ", 

            "The merit of attending the study-session lies in hastening thereto[4]. ", 

            "Abbai said : ", 

            "The merit of attending the discourse lies in the crush[5]. ", 

            "Raba said:", 

            " The merit of studying [Torah] lies in the reasoning thereon[6].", 

            " Rab Pappa said: ", 

            "The merit of attending a house of mourning lies in maintaining silence[7]. ", 

            "Mar Zotra said : ", 

            "The merit of a fast consists in dispensing charity[8].", 

            " Rab Sheshet[9] said : ", 

            "The merit of listening to a funeral oration lies in raising [the voice in lamentation][10]. ", 

            "Rab Ashe[11] said : ", 

            "The merit of attending a wedding lies in addressing words [of felicitation to the bride and bridegroom]. ", 

            "Rab Huna said[1] :", 

            " Whoever prays at the rear of a Synagogue is called wicked ; as it is said,", 

            " \"The wicked walk on every side\" (Ps. xii. 9). ", 

            "Abbai said :", 

            " This applies only to one who does not turn his face towards the Synagogue[2] ; but if he does that, we can have no objection. ", 

            "Once a man prayed at the rear of a Synagogue and did not turn his face in its direction. ", 

            "Elijah passed by, and seeing him thought that he was an Arab[3].", 

            " He said to him, ", 

            "\"With thy back [to the Synagogue][4] standest thou before thy Master? \" ", 

            "And drawing his sword, he slew him. ", 

            "One of the Rabbis said to Rab Bebai b. Abbai (another version : Rab Bebai said to Rab Nahman b. Isaac)[5] : ", 

            "What means, \"When vileness is exalted [kerum] among the sons of men\" (ibid.)?", 

            " He answered :", 

            " This refers to the things that stand in the height [rum] of the world[6] which are despised by men.", 

            " R. Johanan and R. Eleazar [offer another explanation]. They both say : ", 

            "As soon as a man stands in need of the help of his fellow-creatures, his face changes like a Kerum ; as it is said, ", 

            "\"Kerum is vileness to the sons of men.\" ", 

            "What is Kerum? ", 

            "When Rab Dimai came [from Palestine] he said[7], ", 

            "\"There is a bird in the coast-towns[8] called Kerum[9], and when the sun shines, it changes into many colours.\"", 

            " R. Ammi and R. Assi both say : ", 

            "[The man who needs help from his fellow-creatures] is as though he were sentenced to two penalties, viz., fire and water; as it is said, ", 

            "\"Thou hast caused men to ride over our heads, we went through fire and water\" (ibid. lxvi. 12)[1]. ", 

            "R. Helbo also said in the name of Rab Huna : ", 

            "A man should always be careful with the afternoon prayer, for behold, Elijah was only answered in the afternoon[2] prayer; as it is said,", 

            " \"And it came to pass at the time of the offering of the afternoon offering, that Elijah the prophet came near and said, O Lord, the God of Abraham.... ", 

            "Hear me, O Lord, hear me\" (I Kings xviii. 36 f.). ", 

            "The first \"Hear me\" means : that fire may descend from heaven ; the second \"hear me\" means : that they may not say it is due to sorcery. ", 

            "R. Johanan[3] said : ", 

            "Also with the evening prayer [must a man be careful] ; as it is said, ", 

            "\"Let my prayer be set forth as incense before Thee, the lifting up of my hands as the evening sacrifice\" (Ps. cxli. 2). ", 

            "Rab Nahman b. Isaac said :", 

            " Also with the morning prayer [must a man be careful] ; as it is said,", 

            " \"O Lord, in the morning shalt Thou hear my voice ; in the morning will I order my prayer unto Thee, and will look forward\" (ibid. v. 4). ", 

            "R. Helbo also said in the name of Rab Huna : ", 

            "Whoever partakes of the festivity of a bridegroom without felicitating him transgresses the five \"voices\" ; as it is said,", 

            " \"The voice of joy and the voice of gladness, the voice of the bridegroom and the voice of the bride, the voice of them that say. Give thanks to the Lord of Hosts\" (Jer. xxxiii. 11).", 

            " If he does felicitate him, what is his reward ?", 

            " R. Joshua b. Levi said : ", 

            "He is worthy of Torah which was given amidst five \"voices\"; as it is said,", 

            " \"And it came to pass on the third day, when it was morning, that there were thunders[4] and lightnings and a thick cloud upon the mount, and the voice of a horn exceeding loud... and when the voice of the horn waxed louder and louder, Moses spoke, and God answered him by a voice\" (Exod. xix. 16 ff.). ", 

            "But it is not so; ", 

            "for it is written, \"And all the people perceived the thunderings\" (Exod. XX. 18)[1]! ", 

            "The \"voices\" referred to are those before the giving of the Torah. ", 

            "R. Abbahu said :", 

            " [If he felicitates the bridegroom] it is as though he had brought a thanksgiving offering ; as it is said,", 

            " \"Even of them that bring offerings of thanksgiving into the house of the Lord\" (Jer. l.c.). ", 

            "Rab Nahman b. Isaac said :", 

            " It is as though he had rebuilt one of the ruins of Jerusalem ; as it is said, ", 

            "\"For I will cause the captivity of the land to return as at the first, saith the Lord\" (ibid.). ", 

            "R. Helbo also said in the name of Rab Huna :", 

            " Every man in whom is the fear of God, his words are heard ; as it is said,", 

            " \"The end of the matter, all having been heard, fear God, and keep His commandments, for this is the whole man\" (Eccles. xii. 13). ", 

            "What means \"for this is the whole man\"? ", 

            "R. Eleazar[2] answered :", 

            " The Holy One, blessed be He, said, The whole universe was only created for his sake. ", 

            "R. Abba b. Kahana said : ", 

            "Such a man is equal in worth to the whole world. ", 

            "R. Simeon b. 'Azzai (another version: R. Simeon b. Zoma) said : ", 

            "The whole world has only been created to be subservient[3] to him. ", 

            "R. Helbo also said in the name of Rab Huna : ", 

            "Whoever is in the habit of greeting his neighbour, and omits to do so a single day, transgresses the injunction", 

            " \"Seek peace and pursue it\" (Ps. xxxiv. 15)[4].  Should his neighbour greet him and he does not respond, he is called a robber ; as it is said,", 

            " \"It is ye that have eaten up the vineyard ; the spoil of the poor is in your houses\" (Is. iii. 14).  "

        ], 

        [

            " R. Johanan said in the name of R. Jose[5] :  ", 

            "Whence is it that the Holy One, blessed be He, prays[6]? ]", 

            "As it is said, \"Even them will I bring to My holy mountain, and make them joyful in My house of prayer [lit. the house of My prayer]\" (ibid. Ivi. 7). It is not said \"their prayer\" but \"My prayer\" ; hence we infer that the Holy One, blessed be He, prays. ", 

            "What does He pray?", 

            " Rab Zotra b. Tobiah said in the name of Rab :", 

            " \"May it be My will that My mercy may subdue My wrath ; and may My mercy prevail over My attributes[1], so that I may deal with My children in the quality of mercy and enter on their behalf within the line of strict justice.\" ", 

            "There is a teaching :", 

            " R. Ishmael b. Elisha said : ", 

            "Once I entered [the Holy of Holies][2] to offer incense in the innermost part of the Sanctuary, and I saw Okteriel[3], Jah, the Lord of Hosts, seated upon a high and exalted throne. He said to me, ", 

            "\"Ishmael, My son, bless Me.\"", 

            " I replied,", 

            " \"May it be Thy will that Thy mercy may subdue Thy wrath ; and may Thy mercy prevail over Thy attributes, so that Thou mayest deal with Thy children in the quality of mercy and enter on their behalf within the line of strict justice.\" And He nodded His head towards me[4]. ", 

            "We are thus informed that the blessing of a common person should not be esteemed lightly in thine eyes[5]. ", 

            "R. Johanan also said in the name of R. Jose : ", 

            "Whence is it that we should not try to appease a man in the time of his wrath[6]? As it is written, ", 

            "\"My face shall go[7] and I will give thee rest\" (Exod. xxxiii. 14). ", 

            "The Holy One, blessed be He, said to Moses,", 

            " \"Wait for Me until My wrathful countenance shall have passed away, then I will give thee rest.\" ", 

            "Is there ever anger before the Holy One, blessed be He?", 

            " Yes ; as there is a teaching :", 

            " \"A God that hath indignation every day\" (Ps. vii, 12). ", 

            "But how long does His anger last ? ", 

            "A moment. ", 

            "And how long is a moment? ", 

            "A moment is one 58,888th[1] part of an hour ; and nobody has ever been able to fix upon just that moment with the exception of the wicked Balaam, of whom it is written,", 

            " \"He knoweth the knowledge of the Most High\" (Num. xxiv. 16). ", 

            "Was Balaam, then, ignorant of the mind of his ass, and yet acquainted with the knowledge of the Most High?", 

            " Nay; ", 

            "it teaches that he knew how to fix upon that moment in which the Holy One, blessed be He, is wrathful. This is the intention of the statement which the prophet made to Israel : ", 

            "\"O My people, remember now what Balak king of Moab devised, and what Balaam the son of Beor answered him . . .that ye may know the righteous acts of the Lord\" (Micah vi. 5). ", 

            "What means \"that ye may know the righteous acts of the Lord\" ? ", 

            "R. Eleazar answered : ", 

            "The Holy One, blessed be He, said to Israel, ", 

            "\"Know ye how many are the righteous acts which I have wrought on your behalf, that I was not wrathful in the days of the wicked Balaam ; for had I been wrathful, there would not have been left any remnant of the enemies of Israeli[2].\" ", 

            "That is the meaning of what Balaam said to Balak, ", 

            "\"How shall I curse, whom God hath not cursed ? And how shall I execrate, whom the Lord hath not execrated?\" (Num. xxiii. 8). This teaches that during all those days He did not execrate. ", 

            "How long does His execration last? ", 

            "A moment. ", 

            "And how long is a moment?", 

            " R. Abin (another version : R. Abina) said : ", 

            "The moment lasts as long as it takes to utter the word. ", 

            "Whence do we know that He is angry but for a moment?", 

            " As it is said,", 

            " \"For His anger is but for a moment, His favour is for a life-time\" (Ps. XXX. 6). ", 

            "Or if thou wilt, I can say it may be deduced from the following :", 

            "\"Hide thyself for a moment until the indignation be overpast\" (Is. xxvi. 20). ", 

            "When is God angry? ", 

            "Abbai said : ", 

            "During the first three hours of the day when the comb of the cock is white and it stands on one foot. ", 

            "But[3] the comb is white at all times !", 

            "During the rest of the day there are many red streaks in it, but not at the afore-mentioned time. ", 

            "A certain Min[1], who lived in the neighbourhood of R. Joshua b. Levi, used to plague him with questions about [the interpretation of] the Scriptures.", 

            " One day R. Joshua took a cock and placed it between the feet of his bed and watched [the comb] closely. ", 

            "His intention was to curse the heretic when the moment arrived [in which God was wrathful] ; ", 

            "but when the moment arrived, he was sleeping. ", 

            "On waking up[2] he said ;", 

            " Learn from this that it is not proper to act thus ; for it is written, \"His tender mercies are over all His works\" (Ps. cxlv. 9), and ", 

            "\"To punish is also not good for the righteous\" (Prov. xvii. 26). ", 

            "It has been taught in the name of R. Meir : ", 

            "At the hour when the sun shines forth and all the kings of the East and West place their crowns upon their heads and worship it, at once the Holy One, blessed be He, is filled with wrath.", 

            "Further said R. Johanan in the name of R. Jose : ", 

            "One chastisement in the heart of a man[3] is better than many lashes ; as it is said,", 

            " \"And she shall run after her lovers, but she shall not overtake them, and she shall seek them, but shall not find them ; then shall she say [in her heart], I will go and return to my first husband ; for then was it better with me than now \" (Hos. ii. 9).", 

            " R. Simeon b. Lakish said : ", 

            "It is better than a hundred lashes ; as it is said,", 

            "\"A rebuke entereth deeper into a man of understanding than a hundred stripes into a fool\" (Prov. xvii. 10). ", 

            "R. Johanan also said in the name of R. Jose : ", 

            "Three things Moses sought of the Holy One, blessed be He, and He granted them. ", 

            "He sought that the Shekinah should rest upon Israel, and He granted it ; as it is said, ", 

            "\"Is it not in that Thou goest with us?\" (Exod. xxxiii. 16). He sought that the Shekinah should not rest upon the other peoples of the world[4], and He granted it ; as it is said, ", 

            "\"So that we are distinguished, I and Thy people \" (ibid.). He sought that God should show him His ways, and He granted it ; as it is said, ", 

            "\"Show me now Thy ways\" (ibid. V. 13). ", 

            "Moses said before Him[1], ", 

            "\"Lord of the Universe, ", 

            "why is there a righteous man enjoying prosperity and a righteous man afflicted with adversity ? Why is there a wicked man enjoying prosperity and a wicked man afflicted with adversity?\"", 

            "He answered him, ", 

            "\"Moses, the righteous man who enjoys prosperity is the son of a righteous father ; the righteous man who is afflicted with adversity is the son of a wicked father ; the wicked man who enjoys prosperity is the son of a righteous father ; the wicked man who is afflicted with adversity is the son of a wicked father.\" ", 

            "The teacher stated above: ", 

            "\"The righteous man who enjoys prosperity is the son of a righteous father ; the righteous man who is afflicted with adversity is the son of a wicked father.\" ", 

            "But it is not so ; ", 

            "for lo, it is written,", 

            " \"Visiting the iniquity of the fathers upon the children\" (Exod. xxxiv. 7) and it is also written,", 

            " \"The children shall not be put to death for the fathers\" (Deut. xxiv. 16)! ", 

            "We set these verses one against the other and conclude there is no contradiction ; because the former passage refers to those children who continue in their fathers' ways[2], and the latter to those who do not continue in their fathers' ways. ", 

            "But [we may suppose that] God answered Moses thus wise, ", 

            "\"The righteous man who enjoys prosperity is perfectly righteous ; the righteous man who is afflicted with adversity is not perfectly righteous ; the wicked man who enjoys prosperity is not perfectly wicked ; the wicked man who is afflicted with adversity is perfectly wicked[3].\" ", 

            "This[4] is opposed to the teaching of R. Meir ; ", 

            "for R. Meir said that God granted two of Moses' requests and refused one. As it is said, ", 

            "\"I will be gracious to whom I will be gracious\" (Exod. xxxiii. 19), i.e. although he may not be deserving; \"And I will show mercy on whom I will show mercy\" (ibid.), i.e. although he may not be deserving[5]. ", 

            "\"And He said, Thou canst not see My face\" (ibid. v. 20). It has been taught in the name of R. Joshua b. Karhah : Thus spake the Holy One, blessed be He, to Moses,", 

            " \"When I was willing [that thou shouldest see My face] thou wert not willing[1] ; so now that thou art willing, I am not willing.\"", 

            " This disagrees with the teaching of R. Samuel b. Nahmani in the name of R. Jonathan[2], ", 

            "viz. By virtue of three [meritorious acts] Moses became worthy of three [favours]. ", 

            "By virtue of \"Moses hid his face\" (Exod. iii. 6), he was granted the shining of his countenance (cf.ibid. xxxiv. 29 f.). ", 

            "By virtue of \"For he was afraid\" (ibid. iii. 6), he merited \"And they were afraid to come nigh him\" (ibid, xxxiv. 30). By virtue of \"[He was afraid] to behold God\" (ibid. iii. 6), he merited \"The similitude of the Lord doth he behold\" (Num. xii. 8). ", 

            "\"And I will take away My hand, and thou shalt see My back\" (Exod. xxxiii. 23). Rab Hanna[3] b. Bizna said in the name of R. Simeon Hasida : ", 

            "This teaches that the Holy One, blessed be He, showed Moses the knot of the Tefillin[4]. ", 

            "R. Johanan also said in the name of R. Jose :", 

            " Any propitious utterance which issues from the mouth of the Holy One, blessed be He, though it be conditional, He does not retract [though the condition be not fulfilled]. ", 

            "Whence do we learn this ? ", 

            "From Moses our teacher; as it is said,", 

            " \"Let Me alone, that I may destroy them, and blot out their name from under heaven ; and I will make of thee a nation mightier and greater than they\" (Deut. ix. 14).", 

            " Although Moses supplicated God against this decree and averted it, nevertheless He fulfilled [the blessing contained therein] in his seed ; as it is said, \"The sons of Moses : Gershom and Eliezer\" (I Chron. xxiii. 15), ", 

            "and then \"And the sons of Eliezer were : Rehabiah the chief. And Eliezer had no other sons ; but the sons of Rehabiah were very [lema'alah] many\" (ibid. v. 17). ", 

            "On this Rab Joseph taught : ", 

            "They were upwards of [lema'alah] sixty myriads. One draws an analogy from the occurrence of the word rabah \"many\" in the following passages : here it is written, \"they were very many,\" and elsewhere it is written, \"And the children of Israel were fruitful, and increased abundantly, and became very many\" (Exod. i. 7)[5].  "

        ], 

        [

            "R. Johanan said in the name of R. Simeon b. Johai : ", 

            "From the day that the Holy One, blessed be He, created the Universe, nobody called Him \"Lord[1]\" until Abraham came and so called Him ; as it is said,", 

            " \"And he said, O Lord God, whereby shall I know that I shall inherit it?\" (Gen. xv. 8). ", 

            "Rab said : ", 

            "Also, Daniel was only answered because of Abraham ; as it is said,", 

            " \"Now therefore, O our God, hearken unto the prayer of Thy servant, and to his supplications, and cause Thy face to shine upon Thy sanctuary that is desolate, for the Lord's sake\" (Dan. ix. 17).", 

            " It should have read \"for Thy sake\" !", 

            " But [he means] \"for the sake of Abraham, who called Thee 'Lord'.\" ", 

            "R. Johanan also said in the name of R. Simeon b. Johai:", 

            " Whence is it that we should not try to appease a man in the time of his wrath?", 

            " As it is said,", 

            " \"My face shall go, and I will give thee rest\" (Exod. xxxiii. 14)[2]. ", 

            "R. Johanan also said in the name of R. Simeon b. Johai: ", 

            "From the day that the Holy One, blessed be He, created the Universe, nobody praised Him until Leah came and praised Him ; as it is said, \"This time will I praise the Lord\" (Gen. xxix. 35). ", 

            "\"Reuben\" — [what means \"Reuben\"][3]? R. Eleazar answered :", 

            " Leah said,", 

            " \"See the difference between[4] my son and the son of my father-in-law ; ", 

            "for the son of my father-in-law, although he voluntarily sold his birthright — as it is written, 'And he sold his birthright unto Jacob' (ibid. xxv. 33) — see what is written of him,", 

            " 'And Esau hated Jacob' (ibid, xxvii. 41)", 

            " and 'Is not he rightly called Jacob? for he hath supplanted me these two times' (ibid. V. 36). ", 

            "But as for my son, although Joseph forcibly deprived him of his birthright — as it is written, ", 

            "'But, forasmuch as he defiled his father's couch, his birthright was given unto the sons of Joseph' (I Chron. v. 1 )[6] — ", 

            "nevertheless he was not jealous of him; for it is written,", 

            " 'And Reuben heard it, and delivered him out of their hand' (Gen. xxxrii. 21).\" ", 

            "\"Ruth\" — what means \"Ruth\"? ", 

            "R. Johanan said: ", 

            "Because she was worthy that David should issue from her, who delighted[1] the Holy One, blessed be He, with songs and praises. ", 

            "Whence do we learn that the name of a person affects his life[2]? ", 

            "R. Eleazar[3] said :", 

            "Because the Scriptures declare,", 

            " \"Come, behold the works of the Lord, Who hath made shammot ['desolations'] in the earth\" (Ps. xlvi. 9). Read not shammot but shemot \"names.\" ", 

            "R. Johanan also said in the name of R. Simeon b. Johai : ", 

            "More painful is filial impiety in a man's house than the wars of Gog and Magog[4]; as it is said,", 

            " \"A Psalm of David, when he fled from Absalom his son\" (ibid. iii. 1), after which it is written,", 

            " \"Lord, how many are mine adversaries become ! Many are they that rise up against me\" (ibid. v. 2), ", 

            "But in connection with the wars of Gog and Magog it is written, ", 

            "\"Why are the nations in an uproar? And why do the peoples mutter in vain?\" (ibid. ii. 1); but it is not written, \"How many are mine adversaries become!\" ", 

            "\"A Psalm of David, when he fled from Absalom his son\" (ibid. iii. 1). \"A Psalm of David\"! ", 

            "Rather should we have expected \"A Lament of David\"! ", 

            "R. Simeon b. Abishalom said :", 

            " A parable : To what is it like ? ", 

            "To a man to whom it is said, \"To-morrow a bill of debt will be issued against thee.\" Before he sees it, he worries; but having seen it, he rejoices[5]. So was it likewise with David. When the Holy One, blessed be He, said to him, \"Behold, I will raise up evil against thee out of thine own house\" (II Sam. xii. 11), he grieved; for he said,", 

            " \"Perhaps it refers to a slave or illegitimate child who will have no pity on me.\" ", 

            "When, however, he found that it was Absalom, he rejoiced; and therefore he uttered a Psalm. ", 

            "R. Johanan also said in the name of R. Simeon b. Johai : ", 

            "It is permissible to contend with the wicked[6] in this world; as it is said, ", 

            "\"They that forsake the law praise the wicked, but such as keep the law contend with him\" (Prov. xxviii, 4). ", 

            "There is a teaching to the same effect : R. Dostai b. R. Mattun said :", 

            " It is permissible to contend with the wicked in this world ; as it is said,", 

            " \"They that forsake the law praise the wicked,\" etc. ", 

            "Should a man try to mislead thee, saying,", 

            " Lo, it is written, \"Contend not with evil-doers, neither be thou envious against them that work unrighteousness\" (Ps. xxxvii 1),", 

            "answer him, ", 

            "Only he whose conscience pricks him[1] speaks thus.", 

            " Nay, \"Contend not with evil-doers\" means, to emulate them; \"be not envious against them that work unrighteousness\" means, to be like them. And so it is stated, ", 

            "\"Let not thy heart envy sinners, but be in the fear of the Lord all the day\" (Prov. xxiii. 17). ", 

            "But it is not so ! ", 

            "For behold, R. Isaac has said :", 

            " If thou seest a wicked man upon whom fortune smiles[2], do not contend with him ; as it is said,", 

            " \"His ways prosper at all times\" (Ps. x. 5).", 

            " More than that, [if thou contendest with him] he will be justified, in judgment; as it is said,", 

            " \"Thy judgments are far above out of his sight\" (ibid.). ", 

            "More even than that, he will see his desire on his enemies[3]; as it is said,", 

            " \"As for his enemies, he puffeth at them\" (ibid.)!", 

            " There is no contradiction :", 

            " R. Isaac speaks of one who is wicked in his personal affairs, the other[4] of one who is wicked in religious matters[5]. ", 

            "Or if thou wilt, ", 

            "I can say that both refer to religious matters, and still there is no contradiction ; ", 

            "for R. Isaac may be taken to mean the wicked upon whom fortune smiles, and the other the wicked upon whom fortune does not smile.", 

            " Or if thou wilt,", 

            " I can say that both refer to the wicked upon whom fortune smiles, and still there is no contradiction; for R. Johanan may be understood as speaking of a perfectly righteous man [contending with the wicked], and the other of one who is not perfectly righteous. For Rab Huna said : ", 

            "What means that which is written, \"Wherefore lookest Thou, when they deal treacherously, and holdest Thy peace, when the wicked swalloweth up the man that is more righteous than he\"? (Hab. i. 13). Does, then, the wicked swallow up the righteous?", 

            " And lo, it is written,", 

            " \"The Lord will not leave him in his hand\" (Ps. xxxvii. 33) and ", 

            "\"There shall no mischief befall the righteous\" (Prov. xii. 21)!", 

            " Nay;", 

            " \"the wicked swalloweth up the man that is more righteous than he,\"", 

            " but a perfectly righteous man he doth not swallow up. ", 

            "Or if thou wilt, I can say that", 

            " when fortune smiles upon him, it is different[1]. ", 

            "R. Johanan also said in the name of R. Simeon b. Johai :", 

            " Whoever fixes a place for his prayer[2], his enemies fall beneath him; as it is said :", 

            " \"And I will appoint a place for My people Israel, and will plant them, that they may dwell in their own place, and be disquieted no more ; neither shall the children of wickedness afflict them any more as at the first\" (II Sam. vii. 10). ", 

            "Rab Huna asked :", 

            " It is written here \"to afflict them,\" but in the parallel passage (I Chron. xvii. 9) it is written \"to exterminate them[3]\"! The answer is: At first \"to afflict them\" and finally \"exterminate them.\" ", 

            "R. Johanan also said in the name of R. Simeon b. Johai : ", 

            "Greater is the service of Torah[4] than its study : as it is said,", 

            " \"Elisha the son of Shaphat is here, who poured water on the hands of Elijah\" (II Kings iii. 11). It is not mentioned that he studied [with Elijah] but that he poured water. ", 

            "That teaches that its service is greater than its study. ", 

            "Rab Isaac asked Rab Nahman,", 

            " \"Why does not the master[5] come to the Synagogue to pray ?\" ", 

            "He answered,", 

            " \"I am not able [through indisposition].\"", 

            " He said to him, ", 

            "\"Then the master should gather ten together and pray [with a quorum].\" ", 

            "He replied, ", 

            "\"It is too great a trouble for me.\"", 

            " \"Then the master should tell the messenger of the congregation at the time when the congregation prays to come and inform him[6].\" ", 

            "He asked him,", 

            " \"But why all this?\"", 

            " He answered,", 

            " \"Because R. Johanan said in the name of R. Simeon b. Johai :  "

        ], 

        [

            " What means that which is written, 'But as for me, let my prayer be unto Thee, O God, in an acceptable time' (Ps. Ixix. 14)?", 

            " When is an 'acceptable time'? At the time when the congregation prays.\"", 

            " R. Jose b. R. Hannina derived it from the following :", 

            " \"Thus saith the Lord, In an acceptable time have I answered thee\" (Is. xlix. 8). ", 

            "R. Aha b. R. Hannina[7] derived it from the following : ", 

            "\"Behold, God despiseth not the mighty\" (Job xxxvi. 5)[1]; and it is written, ", 

            "\"He hath redeemed my soul in peace so that none came nigh me ; for they were many with me\" (Ps. Iv. 19)[2]. ", 

            "There is a teaching to the same effect : R. Nathan said : ", 

            "Whence is it that the Holy One, blessed be He, does not reject the prayer offered by many[3]? As it is said, ", 

            "\"Behold, God despiseth not the mighty\"; and it is written, ", 

            "\"He hath redeemed my soul in peace so that none came nigh me ; for they were many with me.\" ", 

            "The Holy One, blessed be He, said, \"Whoever occupies himself with Torah, practises benevolent acts and prays with the congregation, I ascribe it to him as though he had redeemed Me and My son [Israel] from [exile] among the peoples of the world.\" ", 

            "R. Simeon b. Lakish said : ", 

            "Whoever has a Synagogue in his town, and does not enter it to pray, is called \"an evil neighbour\"; as it is said,", 

            " \"Thus saith the Lord, As for all Mine evil neighbours, that touch the inheritance which I have caused My people Israel to inherit\" (Jer. xii. 14). ", 

            "More than that, he causes exile to come upon himself and his sons ; as it is said, ", 

            "\"Behold, I will pluck them up from off their land, and will pluck up the house of Judah from among them\" (ibid.). ", 

            "It was said to R. Johanan[4], ", 

            "\"There are old men to be found in Babylon.\" ", 

            "He was astonished and exclaimed,", 

            " \"It is written 'that your days may be multiplied, and the days of your children, upon the land' (Deut. xi. 21); but not outside the land [of Israel] !\"", 

            " When they told him ", 

            "[that the old men are in the Synagogue early and late,] he said, ", 

            "\"It is this which helps them [to live long].\" ", 

            "This is like what R. Joshua b. Levi said to his sons :", 

            " Rise early and stay up late to enter the Synagogue, so that you may prolong your life. ", 

            "R. Aha b. R. Hannina[5] asked, ", 

            "What is the Scriptural authority for this ? \"Happy is the man that hearkeneth to Me, watching daily at My gates, waiting at the posts of My doors\" (Prov. viii. 34), after which it is written, ", 

            "\"For whoso findeth me findeth life\" (ibid. v. 35). ", 

            "Rab Hisda said : ", 

            "A man should always enter two doors in the Synagogue and then pray ; as it is said, \"Waiting at the posts of My doors[1].\"", 

            " \"Two doors\" [literally], dost imagine !", 

            " But say [the meaning is],", 

            " A man should penetrate into the Synagogue a distance which equals the width of two doors, and then offer prayer[2]. ", 

            "\"For this let every one that is godly pray unto Thee in the time of finding\" (Ps. xxxii. 6). R. Hannina said:", 

            " \"In the time of finding\" refers to [the choice of] a wife ; as it is said,", 

            " \"Whoso findeth a wife findeth a great good\" (Prov. xviii. 22).", 

            " In the West[3] when a man marries, they say to him, ", 

            "\"Masa' or Mose' ?\" — ", 

            "Masa', as it is written, \"Whoso findeth [masa'] a wife findeth a great good\"; Mose', as it is written,", 

            " \"And I find [mose'] more bitter than death the woman\" etc. (Eccles. vii. 26). ", 

            "R. Nathan[4] said :", 

            " \"In the time of finding\" refers to Torah; as it is said, ", 

            "\"For whoso findeth me findeth life, and obtaineth favour of the Lord\" (Prov. viii. 35). ", 

            "Rab Nahman b. Isaac said :", 

            " \"In the time of finding [meso']\" refers to death ; as it is said, \"The issues [tosa'ot] of death\" (Ps. Ixviii. 21). ", 

            "There is a teaching to the same effect : ", 

            "Nine hundred and three varieties of death have been created in the world ; as it is said, ", 

            "\"The issues of death.\" Tosa'ot has that numerical value[5]. ", 

            "The severest of them all is croup, and the lightest is the kiss of death. ", 

            "Croup is like a thorn in a ball of clipped wool which tears backwards[6]. Others say", 

            " it is like the whirling waters at the entrance of a canal[7]. ", 

            "The kiss of death is like taking a hair out of milk[8]. ", 

            "R. Johanan said :", 

            " \"In the time of finding\" refers to burial. ", 

            "R. Hannina' said: ", 

            "What is the Scriptural authority for this? \"Who rejoice unto exultation and are glad, when they can find the grave\" (Job iii. 22).", 

            " Rabbah b. Rab Shela said : Hence the popular saying : ", 

            "\"Let a man pray for peace even to the last shovelful of earth[2].\" ", 

            "Mar Zotra said :", 

            " \"In the time of finding\" refers to a privy[3]. ", 

            "In the West, they said that", 

            " the interpretation of Mar Zotra was the best of all. ", 

            "Raba said to Rafram b. Pappa :", 

            " Let the master tell us some of those excellent things which thou reportest in the name of Rab Hisda, relating to the Synagogue.", 

            " He replied, Thus said Rab Hisda : ", 

            "What means that which is written, \"The Lord loveth the gates of Zion [Siyyon] more than all the dwellings of Jacob\" (Ps. Ixxxvii. 2)? The Lord loveth the gates distinguished [mesuyyanim] for Halakah more than Synagogues and Houses of Study. ", 

            "That agrees with what R. Hiyya b. Ammi said in the name of 'Ulla :", 

            " Since the day the Temple was destroyed, there is left to the Holy One, blessed be He, in His Universe the four cubits of Halakah alone[4]. ", 

            "And Abbai said ; ", 

            "At first I used to study at home and pray in Synagogue, but after hearing the statement of R. Hiyya b. Ammi in the name of 'Ulla — ", 

            "\"Since the day the Temple was destroyed, there is left to the Holy One, blessed be He, in His Universe the four cubits of Halakah alone\" I only pray where I study. ", 

            "R. Ammi and R. Assi, although there were thirteen[5] Synagogues in Tiberias[6], used to pray only between the pillars where they studied. ", 

            "R. Hiyya b. Ammi said in the name of 'Ulla : ", 

            "Greater is he who enjoys the fruit of his labour than the fearer of Heaven ; for with regard to the fearer of Heaven it is written,", 

            " \"Happy is the man that feareth the Lord\" (ibid. cxii. 1), but with regard to him who enjoys the fruit of his labour it is written, ", 

            "\"When thou eatest the labour of thy hands, happy shalt thou be, and it shall be well with thee\" (ibid, cxxviii. 2) — \"happy shalt thou be\" in this world, \"and it shall be well with thee\" in the world to come[1]. It is not written, \"and it shall be well with thee\" about the fearer of Heaven. ", 

            "R. Hiyya b. Ammi also said in the name of 'Ulla :", 

            " A man should always reside in the same place as his teacher, for so long as Shimei the son of Gera[2] lived, Solomon did not marry the daughter of Pharaoh. ", 

            "But there is a teaching : ", 

            "A man should not reside [in the same place as his teacher]! ", 

            "There is no contradiction ;", 

            " the former referring to the pupil who submits to his master, the latter to him who does not[3]. ", 

            "Rab Huna b. Judah stated that R. Menahem said in the name of R. Ammi : ", 

            "What means that which is written, \"They that forsake the Lord shall be consumed\" (Is. i. 28)?  This refers to one who leaves a Scroll of the Law [unrolled][4] and goes out [from the Synagogue]. ", 

            "R. Abbahu used to go out between man and man[5]. ", 

            "Rab Pappa asked : ", 

            "How is it between verse and verse [may one go out]?", 

            " The question remains [unanswered]. ", 

            "Rab Sheshet used to turn his face [away from the Scroll] and study, saying,", 

            " \"We with ours, they with theirs[6].\" ", 

            "Rab Huna b. Judah stated that R. Menahem said[7] in the name of R. Ammi : ", 

            "A man should always finish his Parashah with the congregation, twice the Hebrew text and once the Targum[8] — "

        ], 

        [

            "Even", 

            " \"Ataroth and Dibon\" (Num. xxxii. 3)[1] — for whoever finishes his Parashah with the congregation, his days and years are prolonged. ", 

            "Rab Bebai b. Abbai thought to complete the Parashot of the whole year on the eve of the Day of Atonement; ", 

            "but Hiyya b. Rab of Difti[2] taught him :", 

            " It is written, \"Ye shall afflict your souls, in the ninth day of the month at even\" (Lev, xxiii. 32). Do we fast on the ninth ? ", 

            "Surely it is on the tenth that we fast ! ", 

            "But the intention is to tell thee that ", 

            "whoever eats and drinks on the ninth, the Scriptures ascribe it to him as though he fasted on the ninth and tenth[3]. ", 

            "He then thought to anticipate [the reading of the Parashot]; but a certain Elder said to him ; We have learnt that ", 

            "one should neither anticipate nor postpone [the reading of the Parashot]; ", 

            "as R. Joshua b. Levi said to his sons, ", 

            "\"Finish your Parashot with the congregation, twice the Hebrew text and once the Targum; and also be careful to sever the jugular vein [of a bird when slaughtering] in accord with the opinion of R. Judah —", 

            " for there is a Mishnaic teaching : ", 

            "R. Judah says : ", 

            "[One must cut] until he severs the jugular vein — ", 

            "and be careful [to honour] an old man, who has forgotten his learning involuntarily[4]: for we say that ", 

            "both the whole tables of stone and the pieces of the broken tables were placed in the Ark[5].\" ", 

            "Raba said to his sons :", 

            " When you cut meat, do not cut it upon your hand — ", 

            "some say, ", 

            "on account of danger[6],", 

            " others, ", 

            "on account of spoiling the meal[7] — ", 

            "and do not sit upon the bed of an Aramaean[8] woman ; and do not pass behind a Synagogue[9] at the time when the congregation is at prayer.", 

            " [He advised them] not to sit upon the bed of an Aramaean woman[1]. ", 

            "Some say he meant,", 

            " Do not lie down to sleep without first reading the Shema'[2]; ", 

            "others explain he meant, ", 

            "Do not marry a proselyte; ", 

            "but others declare that ", 

            "he really meant an Aramaean woman, because of what happened to Rab Pappa. ", 

            "For Rab Pappa went to the house of an Aramaean woman, who brought out a couch for him and told him", 

            " to be seated.", 

            " He said to her,", 

            " \"I will not sit down until thou raisest up the couch.\" ", 

            "They lifted it up and found a dead child there. ", 

            "On this account the Sages say :", 

            " It is forbidden to sit upon the bed of an Aramaean woman.", 

            " [His advice] \"Do not pass behind a Synagogue at the time when the congregation is at prayer\" supports the teaching of R. Joshua b. Levi who said[3]:", 

            " It is forbidden a man to pass behind a Synagogue at the time when the congregation is at prayer,", 

            " Abbai said: ", 

            "This only applies when the building has no other entrance ; but should it have another entrance, we can have no objection ; ", 

            "further it applies only when there is no other Synagogue [in the town], but should there be another Synagogue, we can have no objection ; ", 

            "further it applies only to one who is not carrying a load, or is not running, or is not wearing Tefillin ; but in any of such cases, we can have no objection[4]. ", 

            "There is a teaching : R. 'Akiba said : ", 

            "For three things I admire the Medes : ", 

            "When they cut up meat, they only do so upon the table ; when they kiss, they only kiss on the hand ; and when they hold a consultation, they only do so in a field[5]. ", 

            "R. Adda b. Ahabah said : ", 

            "What Scriptural authority is there for this ? \"And Jacob sent and called Rachel and Leah to the field\" (Gen. xxxi. 4). ", 

            "There is a teaching : Rabban Gamaliel[6] said :", 

            " For three things I admire the Persians : ", 

            "They are temperate with their food, modest in the privy, and modest in another matter[7]. ", 

            "\"I have commanded My consecrated ones\" (Is. xiii. 3). ", 

            "Rab Joseph taught :", 

            " These are the Persians who are consecrated and destined for Gehinnom[8]. ", 

            "Rabban Gamaliel said : Until the rise of dawn. ", 

            "Rab Judah said in the name of Samuel : ", 

            "The Halakah is in accord with Rabban Gamaliel.", 

            " There is a teaching : R. Simeon b. Johai said :", 

            " There are times when a man reads the Shema twice in a night, once before the rise of dawn and once after the rise of dawn, and thereby fulfils his obligation both for the day and night.", 

            " This is self-contradictory !", 

            " Thou sayest, \"There are times when a man reads the Shema' twice in a night\"; consequently, after the rise of dawn is still night ! And it continues,", 

            " \"The man thereby fulfils his obligation both for the day and night\" ; consequently, it is day !", 

            " No ; it is certainly still night ; and that he calls it \"day\" is because there are people who rise at that early hour[1]. ", 

            "Rab Aha b. Hannina said in the name of R. Joshua b. Levi :", 

            " The Halakah is in accord with R. Simeon b. Johai. ", 

            "There are some who apply the statement of Rab Aha b. Hannina to the following : There is a teaching : R. Simeon b. Johai said in the name of R. 'Akiba : ", 

            "There are times when a man reads the Shema' twice in a day, once before sunrise and once after sunrise, and thereby fulfils his obligation both for the day and night. ", 

            "This is self-contradictory !", 

            " Thou sayest, \"There are times when a man reads the Shema' twice in a day\"; consequently, before sunrise is day ! And it continues, ", 

            "\"The man thereby fulfils his obligation [[fol. 9a.]] both for the day and night\" ; consequently it is still night !  "

        ], 

        [

            "No ; it is certainly day, and that he calls it \"night\" is because there are people who retire to rest at that hour[2]. ", 

            "Rab Aha b. R. Hannina said in the name of R. Joshua b. Levi : ", 

            "The Halakah is in accord with R. Simeon who spoke in the name of R. 'Akiba. ", 

            "R. Zera said : ", 

            "This is so, only one does not say, \"Cause us, O Lord our God, to lie down[3].\" ", 

            "When Rab Isaac b. Joseph came [from Palestine], he said :", 

            " The statement of Rab Aha b. R. Hannina in the name of R. Joshua b. Levi was not explicitly said but was inferred. ", 

            "For it happened that two Rabbis became intoxicated at the marriage feast of R. Joshua b. Levi's son, and they omitted to read the Shema'[4]. They came before R. Joshua b. Levi who said : ", 

            "R. Simeon is worthy that one should rely upon bis opinion in a time of emergency. ", 

            "It once happened that his sons returned from a feast, etc. ", 

            "Before then, had they never heard this teaching of Rabban Gamaliel ?", 

            " But they spoke to him thus : ", 

            "The Rabbis differ from thee, and where an individual differs", 

            "from the many, the Halakah is in accord with the many. Or perhaps, the Rabbis agree with thee, and the reason that they declare [that the evening Shema' may be read] \"Until midnight\" is in order to keep a man far from transgression ? ", 

            "He answered them. ", 

            "The Rabbis hold the same view as myself, and you are under the obligation [to read the Shema']; ", 

            "and the reason they say \"Until midnight\" is to keep a man far from transgression. ", 

            "And not only in this connection do they so decide. ", 

            "But did Rabban Gamaliel say \"Until midnight\" that he teaches \"and not only in this connection do they so decide[1]\"?", 

            " Nay, thus spake Rabban Gamaliel to his sons : ", 

            "Even according to the Rabbis who say \"Until midnight,\" the obligation continues until the rise of dawn ; and the reason they say \"Until midnight\" is to keep a man far from transgression. ", 

            "The duty of burning the fat, etc. ", 

            "But he does not mention the eating of the Paschal offering[2]! ", 

            "And I quote against the Mishnah: ", 

            "The reading of the evening Shema', and Hallel on the Passover night, and the eating of the Paschal offering — their obligation continues until the rise of dawn ! ", 

            "Rab Joseph said : There is no contradiction ; the statement of the Mishnah being the view of R. Eleazar b. 'Azariah, the other the view of R. 'Akiba. ", 

            "For there is a teaching :", 

            " \"And they shall eat the flesh in that night\" (Exod. xii. 8). R. Eleazar b. 'Azariah said, ", 

            "\"Here it is stated, 'in that night' and the same phrase occurs in 'For I will go through the land of Egypt in that night' (ibid. V. 12) ; as in the latter passage it means 'until midnight', so also in the former it means 'until midnight'.\" ", 

            "R. 'Akiba said to him,", 

            "\"But has it not already been stated, 'Ye shall eat it in haste' (ibid. v. 11) — i.e. until the time of hastening[3]?\" ", 

            "R. Eleazar b. 'Azariah asked[4], \"If so, why is there a teaching to state 'in that night'?\" R. 'Akiba answered[1], \"One might otherwise have thought that the Paschal offering could be eaten like the other holy offerings during the day ; therefore there is a teaching to state 'in that night,' meaning", 

            " it must be eaten at night, not during the day.\" ", 

            "According to R. Eleazar b. 'Azariah who uses the argument of Gezerah Shawah[2], it is quite right that it was necessary to state \"in that night\"; but how does R. 'Akiba explain the word \"that[3]\"?", 

            " [He declares] that its purpose is to exclude the following night ;", 

            " for it might have occurred to thee to say that since the Paschal offering belongs to the class of things holy in a minor degree[4], and peace offerings are in the same category, as the peace offerings might be eaten within two days and a night, so also the Paschal offering might be eaten two nights instead of two days, and therefore might be eaten any time during two nights and one day ! Therefore it informs us \"in that night,\" i.e. it must be eaten that night and no other. ", 

            "And R. Eleazar b. 'Azariah[5]? He deduces that from", 

            " \"And ye shall let nothing of it remain until the morning\" (Exod. xii. 10). ", 

            "And R. 'Akiba[6]? ", 

            "If one deduced it from this passage, I might have said, ", 

            "Which \"morning\"? The second morning ! ", 

            "And R. Eleazar[7]?", 

            " He would answer thee, ", 

            "\"Morning,\" used generally, means only the first morning. ", 

            "These Tannaim are like those other Tannaim[8]; for there is a teaching : ", 

            "\"There shalt thou offer the Passover-offering at even, at the going down of the sun, at the season that thou camest forth out of Egypt\" (Deut. xvi. 6).", 

            " R. Eliezer said : ", 

            "\"At even\" thou shalt sacrifice ; \"at the going down of the sun\" thou shalt eat it ; \"at the season that thou camest forth out of Egypt\" thou shalt burn [the remainder][9].", 

            " R. Joshua said: ", 

            "\"At even\" thou shalt sacrifice ; \"at the going down of the sun\" thou shalt eat it ; and how long mayest thou continue eating it? Until \"the season that thou camest forth out of Egypt[1].\" ", 

            "R. Abba[2] said : ", 

            "Everybody admits that the Israelites were only redeemed from Egypt at even ; as it is said, \"The Lord thy God brought thee forth out of Egypt by night\" (ibid. v. I); but they actually left Egypt by day ; as it is said, \"On the morrow after the Passover, the children of Israel went out with a high hand \" (Nam. xxxiii. 3). ", 

            "What is the point of disagreement? The time of \"hastening.\"", 

            " R. Eleazar b. 'Azariah holds that", 

            " it refers to the haste of the Egyptians[3]; but R. 'Akiba holds that", 

            " it refers to the haste of the Israelites[4].", 

            " There is a teaching to the same effect :", 

            " \"The Lord thy God brought thee forth out of Egypt by night\" (Deut. xvi. 1). Was it in the night they went out?", 

            " Surely they went out during the day ; as it is said,", 

            " \"On the morrow after the Passover the children of Israel went out with a high hand\" (Num. xxxiii. 3) ! ", 

            "But", 

            "this teaches that the redemption began for them at even. ", 

            "\"Speak now [na'] in the ears of the people\" etc. (Exod. xi. 2). In the school of R. Jannai they said : ", 

            "The word [na'] always expresses a request. The Holy One, blessed be He, said to Moses,", 

            " \"I request thee. Go and say to the Israelites :", 

            " I beg of you to ask of the Egyptians vessels of silver and vessels of gold, so that the righteous one[5] shall not say, "

        ], 

        [

            "[the righteous one]", 

            "'And they shall serve them, and they shall afflict them' (Gen. xv. 13) He did fulfil in them, but 'and afterward shall they come out with great substance' (ibid. v. 14) He did not fulfil in them.\"", 

            " They answered Moses,", 

            " \"Would that we could escape with our lives!\" ", 

            "A Parable: [It may be likened] to a man who was imprisoned in a dungeon, and people came to tell him, ", 

            "\"To-morrow thou wilt be released from the dungeon and be presented with a large sum of money.\" He replies to them,", 

            " \"I beg of you to release me to-day, and I ask for nothing more.\" ", 

            "\"They let them have what they asked\" (Exod. xii. 36). ", 

            "R. Ammi said : ", 

            "This teaches that they let them have what they asked against their will. ", 

            "Some explain :", 

            " Against the will of the Egyptians; ", 

            "but others explain ;", 

            " Against the will of the Israelites.", 

            " Those who say it was against the will of the Egyptians,", 

            " because it is written, \"And she that tarrieth at home divideth the spoil\" (Ps. Ixviii. 13)[1]. ", 

            "Those who say it was against the will of the Israelites, because of the burden[2]. ", 

            "\"And they despoiled Egypt\" (Exod. xii. 36). ", 

            "R. Ammi said :", 

            " This teaches that they made it like a fort without provisions[3], ", 

            "R. Simeon b. Lakish said : ", 

            "They made it like a pond without fish. ", 

            "\"I am that I am\" (ibid. iii. 14).", 

            " R. Ammi said[4]: The Holy One, blessed be He, spake to Moses,", 

            " \"Go, say to the Israelites,", 

            " I was with you in this servitude, and I will be with you in the servitude of the kingdoms[5].\" ", 

            "He said before Him,", 

            " \"Lord of the Universe, ", 

            "sufficient is the evil in its time[6].\" ", 

            "The Holy One, blessed be He, said to him, ", 

            "\"Go say to them, I am[7] hath sent me unto you\" (ibid.). ", 

            "\"Hear me, O Lord, hear me \" (I Kings xviii. 37)[8]. ", 

            "R. Abbahu said: ", 

            "Why did Elijah exclaim \"Hear me\" twice? ", 

            "This teaches that Elijah spake before the Holy One, blessed be He,", 

            " \"Lord of the Universe, ", 

            "hear me, that fire may descend from heaven and consume all that is upon the altar; and hear me, that Thou mayest divert their mind so that they say not it was the effect of sorcery; as it is said, ", 

            "'For Thou didst turn their heart backward' (ibid.).\" ", 

            "MISHNAH  II From what time may the Shema' be read in the morning ? ", 

            "From the time that one can distinguish between blue and white[1]. ", 

            "R. Eliezer says : ", 

            "Between blue and green. And he may finish it any time until sunrise. ", 

            "R. Joshua says : ", 

            "Until the third hour, for so is the custom of kings to rise at the third hour.", 

            " He who reads from that time onward incurs no loss, for he is to be regarded as one reading in the Torah[2]. ", 

            "GEMARA What is to be understood by \"between blue and white\"?", 

            " Is it to be supposed between a lump of white wool and a lump of blue wool ? That can be distinguished also at night ! ", 

            "But it means, ", 

            "between the blueness in it and the whiteness in it[3]. ", 

            "There is a teaching : R. Meir says : ", 

            "[The morning Shema' is to be read] from the time one can distinguish between a wolf and a dog. ", 

            "R. 'Akiba says : ", 

            "Between an ass and a wild ass. ", 

            "Others say : ", 

            "When he can see an associate of his at a distance of four cubits[4] and recognise him.", 

            " Rab Huna said : ", 

            "The Halakah is in accord with the \"others.\"", 

            " Abbai said:", 

            " [The Halakah is] in accord with the \"others\" with respect to the Tefillah[5]; but with respect to the Shema' it is in accord with the Wetikin[6]. For R. Johanan said: ", 

            "The Wetikin used to conclude it with the sunrise.", 

            " There is a teaching to the same effect : ", 

            "The Wetikin used to conclude it with the sunrise in order to unite the Geullah with the Tefillah[7], and consequently pray in the day. ", 

            "R. Zera said : ", 

            "What is the Scriptural authority foe this? \"They shall fear Thee with the sun[1], and before the moon, throughout all generations\" (Ps. Ixxii. 5). ", 

            "R. Jose b. Eliakim testified in the name of the Holy Congregation of Jerusalem[2]: ", 

            "Whoever unites the Ge'ullah with the Tefillah will meet with no mishap all that day. ", 

            "R. Zera exclaimed,", 

            " \"But it is not so! ", 

            "For lo, I united them but mishap befel me!\"", 

            " He asked him, ", 

            "\"What was the mishap?", 

            " That thou didst carry myrtle into the king's palace[3]? Why, thou shouldest even have offered some reward to be privileged to behold a king. For R. Johanan has said :", 

            " A man should always be eager to run to meet a king of Israel ; and not only to meet an Israelite king, but even a king of the other nations, for if he be worthy, he will distinguish[4] between the kings of Israel and the kings of other peoples.\" ", 

            "R, El'ai[5] said to 'Ulla :", 

            " When thou goest up there [to Palestine], make inquiries about the welfare of my brother, Rab Berona, in the presence of the whole college ; for he is a great man and rejoices in [the performance of] the commandments. ", 

            "On one occasion he united the Ge'ullah with the Tefillah, and laughter did not cease from his mouth all that day. ", 

            "How was he able to unite them? ", 

            "For lo, R, Johanan has said : ", 

            "At the commencement of the Tefillah one should say", 

            " \"O Lord, open Thou my lips\" (Ps. li. 17) and at the conclusion \"Let the words of my mouth etc.\" (ibid. xix. 15)[6] !", 

            " R. Eleazar said :", 

            " [R. Johanan's statement] refers to the Tefillah of the evening.", 

            " But R. Johanan has said : ", 

            "Who will inherit the world to come? He who unites the Ge'ullah of the evening to the Tefillah of the evening[7]!", 

            " R. Eleazar said :", 

            " Then it must refer to the Tefillah of the afternoon service. ", 

            "Rab Ashe[8] said :", 

            " Thou mayest even suppose that it refers to all of them ; for, since the Rabbis instituted it[1] in the Tefillah it is to be considered as part thereof. If thou dost not admit this, how could one unite them in the evening, ", 

            "since one has to say the prayer \"Cause us, O Lord our God, to lie down[2]\"! ", 

            "But since the Rabbis instituted that prayer, it is considered part of the Ge'ullah ; and so here also, since the Rabbis instituted \"O Lord, open etc.\" in the Tefillah, it is to be considered part thereof. ", 

            "Since the verse : \"Let the words of my mouth be acceptable before Thee\" might with equal propriety be said at the conclusion or the commencement [of the Tefillah], ", 

            "why did the Rabbis institute it at the end of the Eighteen Benedictions? ", 

            "Let it be said at the commencement! ", 

            "R. Judah, the son of R. Simeon b. Pazzi, answered : ", 

            "Since David only says this verse after eighteen Psalms, therefore the Rabbis arranged it at the end of the Eighteen Benedictions. ", 

            "How so eighteen Psalms — there are nineteen[3]!", 

            " \"Happy is the man\" (Ps. i. 1) and \"Why are the nations in an uproar\" (ibid. ii. 1) form one Psalm[4]. ", 

            "For R. Judah, the son of R. Simeon b. Pazzi, has said : ", 

            "David composed one hundred and three Psalms, and did not say Hallelujah until he had seen the overthrow of the wicked ; as it is said, ", 

            "\"Let sinners cease out of the earth, and let the wicked be no more. Bless the Lord, O my soul. Hallelujah\" (ibid, civ, 35). ", 

            "How so one hundred and three Psalms — there are one hundred and four!", 

            " But infer from this that ", 

            "\"Happy is the man\" and \"Why are the nations in an uproar\" are one Psalm.", 

            " For R. Samuel b. Nahmani said in the name of R. Jonathan[5]:  "

        ], 

        [

            "Every Psalm which was dear to David he opened with \"Happy\" and concluded with \"Happy.\" ", 

            "He opened with \"Happy\" as it is written, \"Happy is the man\" (ibid. i. 1 ) and concluded with \"Happy\" as it is written, \"Happy are all they that take refuge in Him\" (ibid. ii. 12). ", 

            "There were some lawless men[6] living in the neighbourhood of R. Meir, and they used to vex him sorely. Once R. Meir prayed that they should die.", 

            " His wife, Beruriah[7], exclaimed, ", 

            "\"What thinkest thou?", 

            " Is it because it is written,", 

            " 'Let sinners cease out of the earth'?  But has the text hoteim? ", 

            "It is written hata'im[1]. ", 

            "Glance also at the end of the verse,", 

            " 'And let the wicked be no more' — i.e. when 'sins will cease,' then 'the wicked will be no more.'", 

            " Rather shouldest thou pray that they repent and they be no more wicked.\" ", 

            "R. Meir offered prayer on their behalf and they repented. ", 

            "A Min said to Beruriah ", 

            ": It is written, \"Sing, O barren, thou that didst not bear\" (Is. liv. 1 ). Is the woman to sing because she did not bear?", 

            " She answered him, ", 

            "\"Fool, ", 

            "glance at the end of the verse ; for it is written,", 

            " 'For more are the children of the desolate than the children of the married wife, saith the Lord[2].' ", 

            "But what means, 'barren woman, thou that didst not bear '? Sing, O community of Israel, who art like a barren woman that hath not borne children for Gehinnom — like you.\" ", 

            "A Min said to R. Abbahu : It is written \"A Psalm of David, when he fled from Absalom his son\" (Ps. iii. 1)", 

            " and also \"Of David, Michtam ; when he fled from Saul, in the cave\" (ibid. Ivii. 1). Which incident happened first? ", 

            "Surely the incident of Saul happened first ; then he should record it first !", 

            " He replied : ", 

            "For you who do not use the rule of juxtaposition[3] it is a difficulty, but not for us who do make use of it. For R. Johanan[4] said : ", 

            "Whence is the rule of juxtaposition derived from the Torah? As it is said :", 

            " \"Semukim[5] for ever and ever, they are done in truth and righteousness\" (ibid. cxi. 8). ", 

            "Why, then, is the Psalm concerning Absalom (Ps. iii) next to the Psalm concerning Gog and Magog (Ps. ii)[6]? So that should anybody ask thee,", 

            " \"Is there a slave that rebels against his master[7]?\" ", 

            "do thou ask him,", 

            " \"Is there a son who rebels against his father?\" ", 

            "The latter has happened, and similarly will the former happen. ", 

            "R. Johanan said in the name of R. Simeon b. Johai : What means that which is written,", 

            " \"She openeth her mouth with wisdom, and the law of kindness is on her tongue\" (Prov. xxxi. 26) ? Of whom does Solomon say this? ", 

            "He said it of no one else than David his father, who dwelt in five worlds and composed songs [in each]. ", 

            "He dwelt in the womb of his mother and composed a song ; as it is said,", 

            " \"Bless the Lord, O my soul, and all that I am within[1], bless His holy name\" (ibid. ciii. 1).", 

            " He issued forth into the air of the world, gazed at the stars and planets, and composed a song; as it is said, ", 

            "\"Bless the Lord, ye angels of His, ye mighty in strength, that fulfil His word, hearkening unto the voice of His word. Bless the Lord, all ye His hosts, etc.\" (ibid. vv. 20 f.). ", 

            "He sucked at his mother's breast, gazed at her nipples, and composed a song ; as it is said, ", 

            "\"Bless the Lord, O my soul, and forget not all His benefits\" (ibid. v. 2).", 

            " What means \"all His benefits[2]\"? ", 

            "R. Abbahu said : ", 

            "[It means] that He placed her breast in the place of understanding[3]. ", 

            "For what reason? ", 

            "Rab Judah said : ", 

            "So that [the child] may not gaze at the place of nakedness. ", 

            "Rab Mattena said : ", 

            "So that it should not have to suck from a part of the body which is foul. ", 

            "David looked upon the overthrow of the wicked and composed a song ; as it is said,", 

            " \"Let sinners cease out of the earth, and let the wicked be no more. Bless the Lord, O my soul. Hallelujah\" (ibid. civ. 35).", 

            " He reflected on the day of death and composed a song ; as it is said, \"Bless the Lord, O my soul : O Lord my God, Thou art very great, Thou art clothed with glory and majesty\" (ibid. v. 1). ", 

            "How is it understood that this verse speaks of the day of death?", 

            " Rabbah b. Rab Shela answered : ", 

            "From the continuation ; as it is written,", 

            " \"Thou hidest Thy face, they vanish ; Thou withdrawest their breath, they perish, and return to the dust\" (ibid. v. 29). ", 

            "Rab Shimi b. 'Ukba (another version : Mar 'Ukba) was frequently in the company of R. Simeon b. Pazzi who[4] used to arrange the Aggadah in the presence of R. Joshua b. Levi[5]. ", 

            "He asked him : ", 

            "What means that which is written, \"Bless the Lord, O my soul, and all that is within me, bless His holy name\" (ibid. ciii. I)? ", 

            "He replied : Come and see that the attribute of man is not like the attribute of the Holy One, blessed be He.", 

            " It is an attribute of man to draw a figure on a wall, but he is unable to endow it with breath and soul, with inward parts and bowels. ", 

            "But with the Holy One, blessed be He, it is not so. He draws a figure within a figure, and endows it with breath and soul, with inward parts and bowels. ", 

            "That is what Hannah said,", 

            " \"There is none holy as the Lord, for there is none beside Thee ; neither is there any rock like our God\" (I Sam. ii, 2). ", 

            "What means \"there is no rock [sur] like our God\"?", 

            " [It means] \"there is no designer [sayyar] like our God.\"", 

            " What means \"for there is none beside Thee\"? ", 

            "R. Judah b. Menasya said : ", 

            "Read not en bilteka\" there is none beside Thee,\" but en Ieballoteka \"there is none to outlast Thee.\" For not like the attribute of the Holy One, blessed be He, is the attribute of the human being. ", 

            "With the human being, his works outlast him ; but the Holy One, blessed be He, outlasts His works. ", 

            "He said to him[1] :", 

            " I tell thee as follows : ", 

            "These five \"Bless the Lord, O my soul\" — with reference to whom did David compose them ?", 

            " He composed them with reference to none other than the Holy One, blessed be He, and the soul. ", 

            "As the Holy One, blessed be He, fills the whole world, so also the soul fills the whole body. ", 

            "As the Holy One, blessed be He, sees but cannot be seen, so also the soul sees but cannot be seen. ", 

            "As the Holy One, blessed be He, nourishes the whole world, so also the soul nourishes the whole body. ", 

            "As the Holy One, blessed be He, is pure, so also the soul is pure. ", 

            "As the Holy One, blessed be He, dwells in the inmost part [of the Universe], so also the soul dwells in the inmost part [of the body][2].", 

            " Let him in whom are these five qualities come and praise Him Who possesses these five qualities. ", 

            "Rab Hamnuna said : ", 

            "What means that which is written,", 

            " \"Who is as the wise man? and who knoweth the interpretation [pesher] of a thing?\" (Eccles. viii. 1)?", 

            " [It means]. Who is like the Holy One, blessed be He, Who knows how to make a reconciliation [pesharah] between the two righteous men, Hezekiah and Isaiah.", 

            " Hezekiah said, ", 

            "\"Let Isaiah come to me, for so we find that Elijah went to Ahab ; as it is said,", 

            " 'And Elijah went to show himself unto Ahab' (I Kings xviii. 2).\"", 

            " Isaiah said,", 

            " \"Let Hezekiah come to me, for so we find that Jehoram, son of Ahab, went to Elisha\" (II Kings iii. 12). ", 

            "What did the Holy One, blessed be He, do? He brought sufferings upon Hezekiah and said to Isaiah,", 

            " \"Go and visit the sick[1]\" ;", 

            " as it is said,", 

            " \"In those days was Hezekiah sick unto death. And Isaiah, the prophet, the son of Amoz came to him and said to him. ", 

            "Thus saith the Lord, Set thy house in order; for thou shalt die, and not live\" (Is. xxxviii. 1). ", 

            "What means \"For thou shalt die, and not live\"? — \"for thou shalt die\" in this world, \"and not live\" in the world to come. ", 

            "He asked him, \"Why all this [severe punishment]?\" ", 

            "He replied,", 

            " \"Because thou hast not performed the duty of begetting children[2].", 

            "\" Hezekiah said to him,", 

            " \"The reason is that I have seen by the aid of the Holy Spirit[3], that worthless children will issue from me.\"", 

            " Isaiah asked him,", 

            " \"What hast thou to do with the secrets of the All-merciful? ", 

            "What thou hast been commanded thou shouldest perform, and let the Holy One, blessed be He, do whatever is pleasing to Him.\" ", 

            "Hezekiah said to him,", 

            " \"Then give me thy daughter; perhaps my merit and thine will have effect, and worthy children will issue from me.\"", 

            " He replied, ", 

            "[\"Lo, I have brought thee the message 'Set thy house in order' and thou sayest to me 'Give me thy daughter'!][4] The verdict [of death] has already been decreed against thee!\" ", 

            "He said to him,", 

            " \"Son of Amoz, end thy prophecy and go! ", 

            "For thus has it been handed down to me from my forefather[5]: Even if a sharp sword be laid upon a man's neck, let him not despair of [the divine] mercy.\"", 

            " It has been similarly reported : R. Johanan and R. Eleazar[6] both said : ", 

            "Even if a sharp sword be laid upon a man's neck, let him not despair of [the divine] mercy, as it is said, ", 

            "\"Though He slay me, yet will I trust in Him\" (Job xiii. 15). "

        ], 

        [

            "R. Hanan said :", 

            " Even if the lord of dreams[7] inform a man that he will die on the morrow, he should not despair of [the divine] mercy; as it is said,", 

            " \"For through the multitude of dreams and vanities there are also many words ; but fear thou God\" (Eccles. v. 6)[1],", 

            " Immediately, ", 

            "\"Then Hezekiah turned his face to the wall [kir] and prayed unto the Lord\" (Is. xxxviii. 2).", 

            " What means kir?", 

            " R. Simeon b. Lakish said: ", 

            "[He prayed][2] from the chambers [kirot] of his heart; as it is said, ", 

            "\"My bowels, my bowels! I writhe in pain! the chambers of my heart, etc.\" (Jer. iv. 19). ", 

            "R. Levi[3] declared : ", 

            "[He prayed][2] in connection with the \"wall,\" ", 

            "saying before Him, ", 

            "\"Lord of the Universe, if Thou didst bring back to life the child of the Shunammite woman who but made 'a little chamber on the roof[4],' how much more so [shouldest Thou spare my life], seeing that my forefather Solomon overlaid the whole Temple with silver and gold!\" ", 

            "\"Remember now, O Lord, I beseech Thee, how I have walked before Thee in truth and with a whole heart, and have done that which is good in Thy sight\" (Is. xxxviii. 3). What means \"I have done that which is good in Thy sight\"?", 

            " Rab Judah said in the name of Rab :", 

            " He joined the Ge'ullah to the Tefillah[5]. ", 

            "R. Levi said : ", 

            "He hid the Book of Remedies[6]. ", 

            "The Rabbis have taught : ", 

            "Six acts did King Hezekiah perform ; of three [the Rabbis] approved, and of three they disapproved.", 

            " Of three they approved,", 

            " viz. he hid the Book of Remedies, and they approved; he broke the brazen serpent[7], and they approved; he dragged his father's bones upon a bed of ropes[8], and they approved. ", 

            "But of three of his acts they disapproved, ", 

            "viz. he stopped up the waters of Gihon[9], and they disapproved ; he cut down the doors of the Temple and sent them to the King of Assyria[10], and they disapproved ; he intercalated Nisan in Nisan[1], and they disapproved. ", 

            "Did not Hezekiah know of the teaching,", 

            " \"This month shall be unto you the beginning of months\" (Exod. xii, 2), i.e. this month and none other shall be Nisan[2]? ", 

            "But he erred in the teaching of Samuel ", 

            "who said : ", 

            "We do not intercalate the year on the 30th day of Adar, since that day may possibly be fixed as Nisan. Hezekiah thought ", 

            "that we do not say \"since that day may possibly be fixed as Nisan[3].\" ", 

            "R. Johanan said in the name of R. Jose b. Zimra :", 

            " Whoever refers to his own merit [when praying], the merit of others is referred to [in the answer to the petition]; and whoever refers to the merit of others, his own merit is referred to. ", 

            "Moses referred to the merit of others; as it is said,", 

            " \"Remember Abraham, Isaac and Israel, Thy servants\" (ibid, xxxii. 13),", 

            " and his own merit was referred to ; as it is said,", 

            " \"Therefore He said that He would destroy them, had not Moses His chosen stood before Him in the breach, to turn back His wrath, lest He should destroy them\" (Ps. cvi. 23).", 

            " Hezekiah referred to his own merit; as it is written, ", 

            "\"Remember now, O Lord, I beseech Thee, how I have walked before Thee\" (Is. xxxviii. 3), and the merit of others was referred to ; as it is said,", 

            " \"For I will defend this city, for Mine own sake, and for My servant David's sake\" (ibid, xxxvii. 35). ", 

            "This agrees with the statement of R. Joshua b. Levi ", 

            "who said : What means that which is written,", 

            "\"Behold, for my peace I had great bitterness\" (Is. xxxviii. 17)? ", 

            "Even when the Holy One, blessed be He, sent him peace, it was bitter for him[1].", 

            "\"Let us make, I pray thee, a little chamber on the roof\" (II Kings iv. 10)[2].", 

            " Rab and Samuel [discuss its meaning]. One says :", 

            "It was an open chamber which they roofed in ; the other says : ", 

            "It was a large verandah' which they divided into two [by erecting a wall]. ", 

            "This is all very well according to him who says it was a verandah, since it is written kir \"a wall\" ; but for him who says it was an upper chamber, what means kir?", 

            " He takes it to mean \"they roofed it.\"", 

            " It is all very well according to him who says it was an upper chamber, since it is written 'aliyyah \"upper chamber\" ; but for him who says it was a verandah, what means 'aliyyah? ", 

            "He takes it to mean the finest [me'ullah] of the rooms. ", 

            "\"And let us set for him there a bed, and a table, and a stool and a candlestick\" (ibid.). ", 

            "Abbai (another version : Rab Isaac[4]) said : ", 

            "Whoever wishes to take advantage [of an offer of hospitality] may do so like Elisha ; and whoever does not wish to accept may do so[5] like Samuel of Ramah ;", 

            " as it is said, ", 

            "\"And his return was to Ramah, for there was his house\" (I Sam. vii. 17)[6], ", 

            "and R. Johanan[7] said :", 

            " Wherever he went, he took his house with him. ", 

            "\"And she said to her husband. Behold now, I perceive that this is a holy man of God\" (II Kings iv. 9). ", 

            "R. Jose b. R. Hannina said : ", 

            "From here [we learn] that a woman can better estimate [the character of] a guest than a man. ", 

            "\"A man of God[8].\" How did she know it?", 

            " Rab and Samuel [offer explanations]. One says: ", 

            "She never saw a fly pass over his table[1]; ", 

            "the other says:", 

            "She spread a linen sheet upon his bed and never found it stained with seminal emission. ", 

            "\"A holy man.\" R. Jose b. R. Hannina said : ", 

            "He is holy, but not his servant : as it is said,", 

            " \"Gehazi came near to thrust her away\" (ibid. v. 27). ", 

            "R. Simeon b. Lakish[2] said: ", 

            "He seized her by the breast[3]. ", 

            "\"That passeth by us continually\" (ibid. v. 9). R. Jose b. R. Hannina said in the name of R. Eliezer b. Jacob : ", 

            "Whoever invites a disciple of the wise as a guest to his house and lets him enjoy his possessions, the Scriptures ascribe it to him as though he had brought continual offerings[4]. ", 

            "R. Jose b. R. Hannina also said in the name of R. Eliezer b. Jacob :", 

            " Let not a man stand on an elevated place and pray, but let him pray in a lowly place[5]; ", 

            "as it is said, \"Out of the depths have I called Thee, O Lord\" (Ps. cxxx. 1 ). ", 

            "There is a teaching to the same effect :", 

            " Let not a man stand upon a chair, or a stool, or any elevated place to pray, but let him pray in a lowly place, because there can be no haughtiness before the Omnipresent ; as it is said, \"Out of the depths have I called Thee, O Lord,\" and it is said, ", 

            "\"A prayer of the afflicted, when he fainteth\" (ibid. cii. 1). ", 

            "R. Jose b. R. Hannina also said in the name of R. Eliezer b. Jacob :", 

            " Whoever prays must direct his feet ; as it is said,", 

            " \"And their feet were straight feet\" (Ezek. i. 7)[6]. ", 

            "[7]R. Jose b. R. Hannina also said in the name of R. Eliezer b. Jacob : ", 

            "What means that which is written, ", 

            "\"Ye shall not eat with the blood\" (Lev. xix, 26)? [It means], Ye shall not eat before you have prayed for your life'.", 

            " There are some who declare that R. Isaac stated that R. Johanan said^ in the name of R. Eliezer b. Jacob : ", 

            "Whoever eats and drinks and afterwards otFers his prayers, concerning him the Scriptures say, ", 

            "\"Thou hast cast Me behind thy back\" (I Kings xiv. 9). Read not geweka \"thy back,\" but geeka \"thy pride.\" ", 

            "The Holy One, blessed be He, says, ", 

            "\"After this person has exalted himself, he receives upon himself the kingdom of Heaven[3].\" ", 

            "R. Joshua said : Until the third hour. ", 

            "Rab Judah said in the name of Samuel :", 

            " The Halakah is in accord with R. Joshua. ", 

            "He who reads from that time onward incurs no loss. ", 

            "Rab Hisda said in the name of Mar 'Ukba : Provided he does not say \"Blessed... Who formest light[4].\" ", 

            "Against this view I quote : He who reads [the Shema'] from that time onward incurs no loss ; he is regarded as one reading in the Torah, but he must precede it with two benedictions and follow it with one ! This refutation of Rab Hisda's view remains unshaken. ", 

            "Some declare: ", 

            "Rab Hisda said in the name of Mar 'Ukba : ", 

            "What means he incurs no loss? He loses none of the benedictions[5]. ", 

            "There is a teaching to the same effect : ", 

            "He who reads [the Shema'] from that time onward incurs no loss ; he is regarded as one reading in the Torah, but he must precede it with two benedictions and follow it with one. ", 

            "R. Manni said :", 

            " Greater is he who reads the Shema' in its proper time than one who occupies himself with Torah ; for the Mishnah states :", 

            " He who reads from that time onward incurs no loss, he is regarded as one reading in the Torah ; hence it is to be deduced that he who reads [the Shema'] in its proper time is superior. ", 

            "MISHNAH III  Bet Shammai say :", 

            " In the evening a man should recline and read [the Shema'], and in the morning he should stand up [to read it] ; as it is said,", 

            " \"When thou liest down and when thou risest up\" (Deut. vi. 7). ", 

            "But Bet Hillel say : ", 

            "A man reads it after his own manner[1]; as it is said,", 

            " \"And when thou walkest by the way\" (ibid.).", 

            " If so, why is it said,", 

            " \"When thou liest down and when thou risest up\" ? ", 

            "[That means], At the time when people lie down and rise up.", 

            " R. Tarphon said : ", 

            "I was once journeying by the way and I reclined to read [the Shema'], according to the view of Bet Shammai, and I placed myself in danger on account of robbers.", 

            " They said to him : ", 

            "Thou didst justly incur a penalty for thyself, in that thou didst transgress the view of Bet Hillel.  "

        ], 

        [

            "GEMARA It is all very well that Bet Hillel explain their reasons and the reason of Bet Shammai ; but why do not Bet Shammai agree with Bet Hillel? ", 

            "Bet Shammai would tell thee :", 

            " In that case[2], the text should read, \"In the morning and at even\" ; what means \"When thou liest down and when thou risest up\" ? At the time of lying down, there should be actual lying down [to read the Shema'], and at the time of rising up, there should be actual rising up. ", 

            "What, then, do Bet Shammai make of the phrase \"and when thou walkest by the way\"? ", 

            "This is required in accordance with the teaching : \"", 

            "When thou sittest in thy house\" excludes one occupied with a religious duty; \"and when thou walkest by the way\" excludes a bridegroom[3]. Hence they say :", 

            " He who takes a virgin to his house as wife is exempt [from the obligation of reading the Shema' on the night of his marriage] ; but if he marry a widow, he has that obligation. ", 

            "How is this demonstrated[4]? ", 

            "Rab Pappa said: ", 

            "Because [the text uses the word] \"way\" [we argue], Just as the way is voluntary, so all is voluntary[5]. ", 

            "Are we not here dealing with one who is on his way to perform a religious duty, and even so, the All-merciful requires of him the reading [of the Shema'][1]?", 

            " In that case, the All-merciful should have written \"when sitting and when walking.\" What means \"when thou sittest and when thou walkest\"?", 

            " When sitting for thine own purpose and when walking for thine own purpose, thou art under the obligation [to read the Shema'] ; ", 

            "but when it is the performance of a religious duty, thou art exempt. ", 

            "If so, even one who takes a widow as wife should also [be exempt][2] ! ", 

            "The man [who marries a virgin] is anxious[3]; the other is not. ", 

            "Should the reason [of exemption] be on account of anxiety, then it ought also to apply to one whose ship has sunk at sea ! ", 

            "Shouldest thou say that he likewise is exempt, why does R. Abba b. Zabda declare in the name of Rab :", 

            " A mourner[4] is under the obligation to observe all the commandments mentioned in the Torah except Tefillin, because they are called an adornment ; as it is said, ", 

            "\"Bind thine adornment upon thee\" (Ezek. xxiv. 17)?", 

            " [No, there is a difference]; the former is troubled by the anxiety of a religious duty; but as for the latter, his anxiety is caused by some voluntary affair. ", 

            "And Bet Shammai[5]?", 

            " They require it for the exclusion of messengers sent out in connection with a religious duty[6]. ", 

            "And Bet Hillel[7]?", 

            " They answer that it is self-evident that they may read [the Shema'] while even on a journey. ", 

            "The Rabbis have taught : Bet Hillel say : ", 

            "When standing they may read [the Shema'], when sitting they may read, when reclining they may read, when walking by the way they may read, when doing work they may read.", 

            " It once happened that R. Ishmael and R. Eleazar b. 'Azariah were dining in a certain place, the former reclining and the latter sitting upright.", 

            " When the time for reading the Shema' arrived, R. Eleazar reclined[1] and R. Ishmael sat up. ", 

            "R. Eleazar b. 'Azariah said to R. Ishmael, ", 

            "\"[Ishmael] My brother, I will narrate a parable for thee. To what is this like?", 

            " To one", 

            " who is told 'Thy beard is well grown[2]' and he answers, ", 

            "'Then it shall be taken in hand by the barbers[3].", 

            "' So art thou ; all the time that I was sitting up thou wert reclining, but now that I have reclined[4] thou hast sat up !\"", 

            " He replied,", 

            " \"I have acted according to the teaching of Bet Hillel, and thou according to the teaching of Bet Shammai. ", 

            "Not only that, [I sat up] lest the disciples see this[5] and fix the Halakah for future generations.\" ", 

            "What means \"not only that\"? ", 

            "Shouldest thou say, \"Bet Hillel also hold [that the Shema' may be read] in a reclining position!\" that is so, but only when one was reclining from the first ; but in thy case, since hitherto thou has been sitting up and now thou reclinest, they will say, \"We have to infer that [our teachers] agree with the opinion of Bet Shammai,\" and there is a fear, that the disciples seeing this, will fix the Halakah accordingly for future generations. ", 

            "Rab Ezekiel taught :", 

            " If a man acted in accordance with the view of Bet Shammai, he has done [rightly] ; if in accordance with the view of Bet Hillel, he has done [rightly].", 

            " Rab Joseph said : If he acted in accordance with the view of Bet Shammai, he has done nothing at all. For there is a Mishnaic teaching :", 

            " If the head and greater part of a man's body be in a Sukkah and his table inside his house[6], Bet Shammai pronounce it invalid, but Bet Hillel declare it valid. ", 

            "Bet Hillel said to Bet Shammai,", 

            " \"It once happened that the Elders of Bet Shammai and the Elders of Bet Hillel went to visit R. Johanan b. ha-Horanit ", 

            "and they found him with his head and the greater part of his body in the Sukkah and his table inside his house, but they said nothing to him.\"", 

            " They asked them[7],", 

            " \"Is proof to be drawn from this?", 

            " They certainly told him, ", 

            "'If this be thy practice, never hast thou in thy life-time properly observed the commandment of Sukkah!' \" ", 

            "Rab Nahman b. Isaac said :", 

            "If one acted according to the view of Bet Shammai, he is worthy of death ; for we have learnt in our Mishnah: R. Tarphon said:", 

            " I was once journeying by the way and I reclined to read [the Shema'] according to the view of Bet Shammai, and I placed myself in danger on account of robbers. ", 

            "They said to him :", 

            " Thou didst justly incur a penalty for thyself, in that thou didst transgress the view of Bet Hillel. ", 

            "MISHNAH IV  In the morning [the reading of the Shema'] is preceded by two benedictions and followed by one[1] ; in the evening it is preceded by two and followed by two[2], one long and one short. Where [the Rabbis] order to say a long benediction, it is not permissible to say a short one ;", 

            " [where they order] to say a short benediction, it is not permissible to say a long one. [Where they order] to \"seal \" a benediction[3], it is not permissible not to \"seal\" ; [where they order] not to \"seal,\" it is not permissible to \"seal.\" ", 

            "GEMARA  Which benedictions does one say [in the morning]? ", 

            "R. Jacob[4] [[fol. 11b.]] said in the name of R. Osha'ya :  "

        ], 

        [

            "\"[Blessed].... Who formest light and createst darkness[5].\" ", 

            "Surely one ought rather to say : \"Who formest light and createst brightness\"! ", 

            "As it is written[6], so we say it. ", 

            "But in the case of the words ", 

            "\"I make peace and create evil\" (Is. xlv. 7), do we say them as they are written?", 

            " It is written \"evil,\" but [in the prayer] we say \"all things[7]\" ! It is an euphemism. Then in the former instance, let us [in the prayer] also use \"brightness\" [instead of \"darkness\"] as an euphemism ! ", 

            "Raba[8] answered : ", 

            "The purpose is to mention the characteristic of day at night and the characteristic of night in the day. ", 

            "It is quite right [about mentioning] the characteristic of night in the day, since we say ", 

            "\"Who formest light and createst darkness\" ; but where is [the mention of] the characteristic of day at night?", 

            " Abbai answered : ", 

            "[We say] \"Thou rollest away the light from before the darkness, and the darkness from before the lights[1].\" ", 

            "Which is the other [blessing to be recited before the morning Shema']?", 

            " Rab Judah said in the name of Samuel :", 

            " \"With abounding love[2]\" ; ", 

            "and so R. Eleazar taught his son R. Pedat to say ", 

            "\"With abounding love.\" ", 

            "There is a teaching to the same effect :", 

            " We do not say \"With everlasting love[3],\" but \"With abounding love.\" ", 

            "But the Rabbis declare that", 

            " \"With everlasting love\" [is to be recited] ; for so it is said, \"Yea, I have loved thee with an everlasting love ; therefore with affection have I drawn thee\" (Jer. xxxi. 3). ", 

            "Rab Judah said in the name of Samuel : ", 

            "When one rises early to study [Torah], if he had not yet read the Shema', he must utter a benediction [prefatory to study] ; but should he have read the Shema', it is not necessary to utter a benediction, for he has freed himself from the obligation by having recited \"With abounding love[4].\" ", 

            "Rab Huna said : ", 

            "For the study of the Scriptures a benediction is necessary, but not for the study of Midrash. ", 

            "R. Eleazar said : ", 

            "For the study of the Scriptures and Midrash a benediction is required, but not for the study of the Mishnah. ", 

            "R. Johanan said : ", 

            "For the Mishnah it is also required, but not for the study of Talmud.", 

            " Raba said : ", 

            "Also for the study of Talmud it is necessary to recite a benediction[5].", 

            " For Rab Hiyya b. Ashe said : ", 

            "On many occasions have I stood before Rab to study the chapters of the Sifra debe Rab[6] ; he first washed his hands, uttered a benediction, and then taught us the chapters. ", 

            "What was the benediction ?", 

            " Rab Judah said in the name of Samuel:", 

            " \"[Blessed art Thou, O Lord our God, King of the Universe], Who hast sanctified us by Thy commandments and commanded us to occupy ourselves with the words of Torah[1].\" ", 

            "R. Johanan used to conclude thus : ", 

            "\"Make pleasant, therefore, we beseech Thee, O Lord our God, the words of Thy Torah in our mouth and in the mouth of Thy people, the house of Israel, so that we with our offspring and the offspring of Thy people, the house of Israel, may all know Thy name and occupy ourselves with Thy Torah. Blessed art Thou, O Lord, Who teachest Torah to Thy people Israel[2].\"", 

            " Rab Hamnuna[3] said : \"[Blessed]... Who hast chosen us from all nations and given us Thy Torah.", 

            " Blessed art Thou, O Lord, Who givest the Torah[4].\" ", 

            "Rab Hamnuna said :", 

            " This is the choicest of benedictions.", 

            " Rab Pappa said[5] : Therefore let one say them all.", 

            "We have learnt elsewhere in the Mishnah : The Temple-super-intendent[6] said [to the priests]", 

            " \"Utter one benediction,\" ", 

            "and they did so. They then read the Decalogue, \"Hear, O Israel\" etc. (Deut. vi. 4 ff.), \"And it shall come to pass if ye shall hearken diligently\" etc. (ibid. xi. 13 ff.), \"And the Lord said\" etc. (Num. xv, 37 ff.)[7]. After that they uttered with the people three benedictions, ", 

            "viz, \"True and firm[8],\" \"Accept, O Lord our God[9]\" and the Priestly Benediction[10]. On the Sabbath they added a benediction for the outgoing guard[11].", 

            "Which is the one benediction[12]? ", 

            "It so happened that R. Abba and R.Jose b. Abba[13] came to a certain place and were asked : ", 

            "Which is the one benediction? ", 

            "They were unable to answer ;", 

            " so they went and questioned Rab Mattena, and he could not answer.", 

            " They thereupon asked Rab Judah. He replied :", 

            " Thus said Samuel : It is \"With abounding love.\" ", 

            "But R. Zerika stated that R. Ammi said in the name of R. Simeon b. Lakish : ", 

            "It is \"Who formest light.\" ", 

            "When Rab Isaac b. Joseph came [from Palestine], he said : ", 

            "The statement of R. Zerika was not explicitly made but was inferred ; for what R. Zerika stated that R. Ammi said in the name of R. Simeon b. Lakish was : ", 

            "This teaches that the benedictions do not invalidate one another[1].", 

            " Now it is quite right if thou maintainest that [the priests] recited \"Who formest light\" ;", 

            " then it would follow that the benedictions do not invalidate one another, for they omitted \"With abounding love.\" "

        ], 

        [

            " Shouldest thou, on the other hand, maintain that they recited \"With abounding love,\" how would it follow that the benedictions do not invalidate one another? ", 

            "Perhaps the reason they omitted \"Who formest light\" was because it was not yet time for that prayer[2], and when the proper time arrived, they said it!", 

            " And if this be an inference, what then[3]? ", 

            "It might have been inferred that it was certainly \"With abounding love\" that [the priests] recited, and when the proper time for reciting \"Who formest light\" arrived, they said it; and what means \"The benedictions do not invalidate one another\"?", 

            " The order of the benedictions[4]. ", 

            "[The Mishnah quoted above states :] Then they read the Decalogue, \"Hear, O Israel,\" \"And it shall come to pass, if ye shall hearken diligently,\" \"And the Lord said,\" \"True and firm,\" \"Accept, O Lord our God,\" and the Priestly Benediction.", 

            " Rab Judah said in the name of Samuel : ", 

            "Also beyond the confines of the Temple they wished to read [the Decalogue with the Shema'] but it had long been abolished because of the murmuring of the Minim[5]. ", 

            "There is a teaching to the same effect : R. Nathan said :", 

            " Outside the Temple they wished to read [the Decalogue with the Shema'] but it had long been abolished because of the murmuring of the Minim.", 

            " Rabbah b. Rab Huna[6] thought to establish it in Sura[1] ; but Rab Hisda told him", 

            " it had been previously abolished because of the murmuring of the Minim. ", 

            "Amemar thought to establish it in Nehardea[2]; but Rab Ashe told him", 

            " it had previously been abolished because of the murmuring of the Minim. ", 

            "[The Mishnah-quotation continues :] On the Sabbath they added a benediction for the outgoing guard. ", 

            "Which is this benediction ? ", 

            "R. Helbo said : ", 

            "The outgoing guard said to the incoming guard, ", 

            "\"May He Who caused His name to dwell in this house make love and brotherhood, peace and comradeship, to abide amongst you.\" ", 

            "Where [the Rabbis] order to say a long benediction, it is not permissible to say a short one. ", 

            "It is evident that one who took a cup of wine, and thinking that it was beer, commenced saying the benediction on the supposition that it was beer, and then concluded the benediction for wine, has complied with the requirements of the law ; because even if he had said \"[Blessed]... by Whose word all things exist[3],\" he would also have complied with the requirements of the law. For there is a Mishnaic teaching :", 

            "[not translated.]", 

            " If one has uttered the benediction \"By Whose word all things exist\" over any kind of liquor, he has fulfilled his obligation.", 

            " But if one took a cup of beer, and thinking it was wine began the benediction for wine and concluded with the benediction for beer, how is it then ? ", 

            "Do we follow the main theme of the benediction or its conclusion ? ", 

            "Come and hear[4]:", 

            " In the morning service, if one commences with \"Who formest light\" but concludes with \"Who bringest on the evening twilight[5],\" he has not complied with the requirements of the law. If he opened with \"[ Blessed] . . . Who at Thy word bringest on the evening twilight\" and concluded with \"Creator of the luminaries[6],\" he has so complied.", 

            " In the evening service, if he opened with \"Who at Thy word bringest on the evening twilight\" and concluded with \"Creator of the luminaries[7],\" he has not so complied. If he opened with \"Who formest light\" and concluded with \"Who bringest on the evening twilight[1],\" he has so complied.", 

            " The general rule in this matter is, therefore,", 

            " that it depends upon the conclusion of the benediction[2]. ", 

            "But it is different here, because he has said", 

            " \"Blessed art Thou, O Lord, Creator of the luminaries[3].\"", 

            " That is quite right according to Rab who declares that a benediction which does not contain the Divine Name is no benediction. But, according to R. Johanan who holds that", 

            " a benediction which does not contain a reference to the Divine Kingship is no benediction, what is there to say[4]?", 

            " But since Rabbah b. 'Ulla has declared :", 

            " \"The purpose is to mention the characteristic of day at night and the characteristic of night in the day[5],\" having uttered the benediction and the reference to the Divine Kingship from the commencement, he said them of both[6]. ", 

            "Come and hear : From the latter clause [of the quoted Baraita]", 

            " \"The general rule in this matter is that it depends upon the conclusion of the benediction\" — ", 

            "what does \"the general rule in this matter\" intend to include? Is it not to include what we have mentioned[7]?", 

            " No ;  it is to include the instance of bread and dates. ", 

            "How is this to be understood ? ", 

            "Are we to suppose that it refers to one who ate bread and thinking that it was dates he had eaten, commences the benediction on the supposition it was dates, but concludes with the benediction for bread ? This is the same as the last-mentioned case[1]!", 

            " No, [the \"general rule\"] is necessary for the following : ", 

            "If, for instance, one ate dates, and thinking it was bread, commenced with the benediction for bread but concluded with the benediction for dates, he has complied with the requirements of the law ; for even if he had concluded with the benediction for bread, he would also have so complied.", 

            " What is the reason ? Because dates likewise nourish[2]. ", 

            "Rabbah", 

            " b. Hinnana[3] the Elder said in the name of Rab :", 

            " Whoever does not recite \"True and firm\" in the morning and \"True and trustworthy[4]\" in the evening has not fulfilled his obligation ; as it is said,", 

            " \"To declare Thy lovingkindness in the morning and Thy faithfulness in the night-seasons\" (Ps. xcii. 3)[5]. ", 

            "Rabbah b. Hinnana [the Elder] also said in the name of Rab :", 

            " When one prays [the Tefillah] and has to bow[6], he should bow at the word \"Blessed\" ; and when returning to the erect position, he should do so on mentioning the Divine Name.", 

            " Samuel asked : ", 

            "What is Rab's reason ? Because it is written,", 

            "\"The Lord raiseth up them that are bowed down\" (ibid, cxlvi. 8)[7]. ", 

            "Against this is quoted,", 

            " \"And from before My name he is afraid\" (Mal. ii. 5)[8]!", 

            " Is it written \"at My name[9]\"? ", 

            "No, \"from before My name\" is written. ", 

            "Samuel said to Hiyya b. Rab : ", 

            "O son of the Law, come and let me tell thee an excellent thing which thy father once said. ", 

            "Thus spake thy father : ", 

            "When one bows, he should do so at the word \"Blessed\" ; and when he returns to the erect position, he should do so on mentioning the Divine Name. "

        ], 

        [

            "When Rab Sheshet bowed, he did so like a twig[10] ; but when he returned to the erect position, he did so like a snake. ", 

            "Rabbah b. Hinnana the Elder also said in the name of Rab :", 

            " During the whole year, one should in the Tefillah use the phrases \"The holy God\" and \"King Who lovest righteousness and judgment[1]\" ; except during the ten days from the New Year until the Day of Atonement, when he should substitute \"The holy King\" for the former and \"King of judgment\" for the latter.", 

            " R. Eliezer said : ", 

            "Even if he used the phrase \"holy God,\" he has complied with the requirements of the law ; as it is said, ", 

            "\"But the Lord of hosts is exalted through justice, and the holy God is sanctified through righteousness\" (Is. v. 16). ", 

            "When is \"the Lord of hosts exalted through justice\"? During the ten days from the New Year until the Day of Atonement, and yet it is stated thereby \"the holy God\" ! ", 

            "How is it, then, in this matter?", 

            " Rab Joseph declared : ", 

            "\"The holy God\" and \"King Who lovest righteousness and judgment\" should be said[2]: ", 

            "Rabbah declared:", 

            "\"The holy King\" and \"King of judgment\" should be said ;", 

            " and the Halakah is in accord with Rabbah's view. ", 

            "Rabbah b. Hinnana the Elder also said in the name of Rab : ", 

            "Whoever has it in his power to pray\" on behalf of his neighbour and fails to do so is called a sinner ; ", 

            "as it is said, ", 

            "\"Moreover as for me, far be it from me that I should sin against the Lord in ceasing to pray for you\" (I Sam. xii. 23). ", 

            "Raba[3] said :", 

            " If [the neighbour] be a disciple of the wise, then it is necessary to grieve on his behalf [should he be in trouble]. ", 

            "What is the reason ? ", 

            "Are we to suppose it is because it is written, \"There is none of you that is sorry for me or discloseth unto me\" (ibid. xxii. 8)? Perhaps it is different in the case of a king[4]! Nay, ", 

            "[derive the reason] from the following : ", 

            "\"But as for me, when they were sick, my clothing was sackcloth, I afflicted my soul with fasting ; and my prayer, may it return into mine own bosom\" (Ps. xxxv. 13)[5]. ", 

            "Rabbah b. Hinnana the Elder also said in the name of Rab :", 

            " Whoever commits a transgression and is filled with shame thereby, all his sins are forgiven him; as it is said, ", 

            "\"That thou mayest remember and be confounded, and never open thy mouth any more, because of thy shame; when I have forgiven thee all that thou hast done, saith the Lord God\" (Ezek. xvi. 63).", 

            " Perhaps it is different with a community[1]? Nay,", 

            " [derive the reason] from the following:", 

            " \"And Samuel said to Saul, Why hast thou disquieted me, to bring me up? And Saul answered, I am sore distressed ; for the Philistines make war against me, and God is departed from me, and answereth me no more, neither by prophets, nor by dreams; therefore I have called thee, that thou mayest make known unto me what I shall do\" (I Sam. xxviii. 15). Saul did not mention [having inquired through] the Urim and Tummim[2], because he put Nob, the city of the priests, to the sword[3]. ", 

            "Whence do we know that he was forgiven by God ? As it is said, \"(And Samuel said unto Saul)[4], Tomorrow shalt thou and thy sons be with me\" (ibid. V. 19); upon which R. Johanan comments, ", 

            "\"with me\" i.e. in my division[5]. ", 

            "The Rabbis [find that Saul was forgiven] in the following :", 

            " \"We will hang them up unto the Lord in Gibeah of Saul, the chosen of the Lord[6]\" (II Sam. xxi. 6). A Bat Kol issued forth and proclaimed", 

            " \"The chosen of the Lord.\" ", 

            "R. Abbahu b. Zutarti said in the name of R. Judah b. Zebida[7]:", 

            " It was sought to include the Parashah of Balak[8] in the reading of the Shema'. Why did they not do so? Because of the trouble [its length would cause] to the congregation. ", 

            "On what ground [did they wish to include it] ? ", 

            "Was it because it is written therein, ", 

            "\"God Who brought them forth out of Egypt\" (Num. xxiii. 22) ? Then let one say the Parashah of usury[9] or of weights[10] which likewise contains a reference to the exodus from Egypt ! ", 

            "Nay ; R. Jose b. Abin said :", 

            " [The reason is] because it is written therein,", 

            " \"He couched, he lay down as a lion, and as a lioness ; who shall rouse him up?\" (ibid. xxiv. 9)[1]. ", 

            "Then let him say that verse and no more", 

            " [if the whole is too lengthy] ! ", 

            "We have a tradition that any Parashah which Moses our teacher divided off, we may divide off; but a Parashah which he had not divided off, we may not. ", 

            "Why was the Parashah of Fringes[2] included [in the Shema']? ", 

            "R. Judah b. Habiba[3] said : ", 

            "Because there are five things contained therein :", 

            " the command of fringes ; the exodus from Egypt ; the yoke of the commandments ; [a warning against] heretical opinions [Minut] ; lustful imagination and idolatrous longing. ", 

            "Quite right that three of these are explicitly stated therein ;", 

            " viz. : the yoke of the commandments, as it is written,", 

            " \"That ye may look upon it and remember all the commandments of the Lord\" (ibid. xv. 39) ; the command of Fringes, as it is written, ", 

            "\"That they make for themselves fringes\" (ibid. v. 38) ; the exodus from Egypt, as it is written,", 

            " \"I am the Lord your God, Who brought you out of the land of Egypt to be your God ; I am the Lord your God\" (ibid. V. 41). But where is there reference to heretical opinions and lustful imagination and idolatrous longing ? ", 

            "There is a teaching[4] : ", 

            "\"After your heart\" (ibid. v. 39) means heresy; for thus the Scriptures state, ", 

            "\"The fool hath said in his heart, There is no God\" (Ps. xiv, 1). \"After your own eyes\" (Num. I.c.) means lustful imagination ; as it is said,", 

            " \"And Samson said unto his father. Get her for me, for she is pleasing in my eyes\" (Judg. xiv. 3). \"After which ye use to go astray\" (Num. I.c.) means idolatrous longing; ", 

            "for thus the Scriptures state, \"The children of Israel again went astray after the Baalim \" (Judg. viii. 33). ", 

            "MISHNAH V  The exodus from Egypt must be mentioned at night[5]. ", 

            "R. Eleazar b. 'Azariah said :", 

            " Behold I am like one seventy years old[6], and I have never been worthy [to hear the reason] why the exodus from Egypt should he mentioned at night, until Ben Zoma expounded it [as follows].", 

            " It is said, ", 

            "\"That thou mayest remember the day when thou camest forth out of the land of Egypt all the days of thy life\" (Deut. xvi. 3). ", 

            "[Had the Scriptures stated] \"the days of thy life\" [it would have meant] the days only ; but \"all the days of thy life\" [must be intended to include] the nights.", 

            " The Sages explain the verse thus :", 

            " \"The days of thy life\" signifies [thy life-time] in this world; \"all\" is to include the days of the Messiah. ", 

            "GEMARA There is a teaching : Ben Zoma said to the Sages :", 

            " Will the exodus from Egypt be mentioned in the days of the Messiah ? ", 

            "Has it not long ago been declared,", 

            " \"Therefore behold, the days come, saith the Lord, that they shall no more say. As the Lord liveth, that brought up the children of Israel out of the land of Egypt ; but, as the Lord liveth, that brought up and that led the seed of the house of Israel out of the north country, and from all the countries whither I had driven them\" (Jer. xxiii. 7f.)? ", 

            "They answered him :", 

            " [This passage does not mean] that the memory of the exodus from Egypt is to be obliterated, but that [the memory of the release from] the servitude of the kingdoms will be fundamental and the exodus of Egypt secondary to it. ", 

            "Take the following as an analogy:", 

            " \"Thy name shall no more be called Jacob, but  Israel shall be thy name\" (Gen. xxxv. 10). "

        ], 

        [

            " It is not intended that the name Jacob shall be obliterated[1], but that Israel will be fundamental and Jacob secondary.", 

            " Similarly the Scriptures state,", 

            " \"Remember ye not the former things, neither consider the things of old\" (Is. xliii. 18) — \"Remember ye not the former things,\" i.e. the servitude of the kingdoms, \"neither consider the things of old,\" i.e. the exodus from Egypt. \"Behold I will do a new thing ; now shall it spring forth\" (ibid. V. 19). Rab Joseph taught : ", 

            "This refers to the war of Gog and Magog[2]. ", 

            "A parable : to what is this like ? To a man walking by the way, when a wolf attacked him and he was rescued from it ; then he is fond of relating his adventure with the wolf.", 

            "[Later on] a lion attacked him and he was rescued from it ; so he is fond of relating his adventure with the lion. ", 

            "[After that] a serpent attacked him and he was rescued from it ; so he forgets his two previous adventures, and relates the incident of the serpent. ", 

            "So is it also with Israel ; later troubles cause the former to be forgotten. ", 

            "\"Abram, the same is Abraham\" (I Chron. i. 27). At first he was made the father of Aram, but subsequently the father of all the universe[1]. ", 

            "Sarai, the same is Sarah. At first she was made princess of her own people, but subsequently princess of all the universe[2] ", 

            "Bar Kappara taught :", 

            " Whoever calls Abraham \" Abram \" transgresses a command ; as it is said,", 

            " \"Thy name shall be Abraham\" (Gen. xvii. 5). ", 

            "R. Eliezer says: ", 

            "He transgresses a prohibition ; as it is said, ", 

            "\"Thy name shall no more be called Abram\" (ibid.).", 

            " But now, can this also apply to one who calls Sarah \"Sarai[3]\"?", 

            " In her case the Holy One, blessed be He, said to Abraham,", 

            " \"As for Sarai thy wife, thou shalt not call her name Sarai, but Sarah shall her name be\" (ibid. v. 15)[4]. ", 

            "Does it likewise apply to one who calls Jacob \"Jacob\"? ", 

            "No; it is different here, because the Scriptures afterwards repeat [his old name] ; as it is written, \"And God spoke unto Israel in the visions of the night, and said, Jacob, Jacob\" (ibid. xlvi. 2). ", 

            "R. Jose b. Abin (others declare it was R. Jose b. Zebida) quoted in objection : ", 

            "\"Thou art the Lord the God, Who didst choose Abram\" (Neh. ix. 7) ! ", 

            "He was answered :", 

            " In this passage the prophet narrates the praise of the All-merciful by reviewing what had happened from the beginning[5]. ", 

            "May we return to thee : From what time[6]. ", 

            "MISHNAH  Should a man be reading in the Torah [the section of the Shema'] and the time of reciting the Shema' arrived, if he directed his heart[1], he has fulfilled his obligation. ", 

            "Between the sections, he may greet a man out of respect for him and return a salutation ; but in the middle [of the sections] he may greet a man because of fear for him[2] and return a salutation. These are the words of R. Meir.", 

            " R. Judah says: ", 

            "In the middle, he may greet a man because of fear for him, and return a salutation out of respect ; and between the sections, he may greet a man out of respect for him and return the salutation of any person. ", 

            "II. The following are \"between the sections\" : ", 

            "Between the first benediction and the second[3] ; between the second and \"Hear, O Israel\" ; between \"Hear, O Israel\" and \"And it shall come to pass if ye shall hearken\" ; between \"And it shall come to pass if ye shall hearken\" and \"And the Lord spake\" ; between \"And the Lord spake\" and \"True and firm.\" ", 

            "R. Judah says : ", 

            "One must make no interruption between \"And the Lord spake\" and \"True and firm.\" ", 

            "R. Joshua b. Karhah said: ", 

            "Why does the section \"Hear, O Israel\" precede \"And it shall come to pass if ye shall hearken\"? So that a man shall first receive upon himself the yoke of the kingdom of heaven, and afterwards receive upon himself the yoke of the commandments. ", 

            "And why does \"And it shall came to pass if ye shall hearken\" precede \"And the Lord spake\" ? Because the former applies both during the day and night, but the latter during the day only[4]. ", 

            "GEMARA Is the conclusion to be drawn [from the opening sentence of the Mishnah] that ", 

            "the performance of the commandments requires Kawwanah[1]? ", 

            "No; for] what means If he directed his heart to read ? ", 

            "Just to read [in the Torah for the sake of study]. ", 

            "But he was reading[2]!", 

            " [It is to differentiate him] from one who is reading [the Torah] for the purpose of correcting[3]. ", 

            "Our Rabbis have taught : ", 

            "The Shema' must be read as it is written[4]: These are the words of Rabbi[5]; ", 

            "but the Sages say : ", 

            "may be read] in any language[6]. ", 

            "What is Rabbi's reason ? ", 

            "The text states, \"And these words shall be\" (Deut. vi. 6); i.e. as they are, so must they remain. ", 

            "And what is the reason of the Sages? ", 

            "The text states,", 

            " \"Hear, O Israel\" (ibid. v. 4); i.e. in any language which thou hearest. ", 

            "But for Rabbi also it is written \"Hear, O Israel[7]\" ! ", 

            "He requires it to establish the rule.", 

            " Cause thine ear to hear what thou utterest with thy lips[8]. ", 

            "And the Sages ?", 

            "They agree with him who says that ", 

            "if one does not read [the Shema'] audibly, he has still fulfilled his obligation. ", 

            "But for the Sages also it is written \"And these words shall be\" !", 

            " They require it to establish the rule that one must not read [the sentences of the Shema'] out of order.", 

            " Whence does Rabbi find authority for the rule that the Shema' may not be read out of order[9]?", 

            " He derives it from the fact that the text states \"these words shall be\" and not \"the words shall be.\" ", 

            "And the Sages", 

            " [what do they make of this distinction between \"these words\" and \"the words\"]? ", 

            "They draw no conclusion from it at all. It is possible to say that Rabbi holds that the whole Torah can be read in any language. For if thou maintainest that it may be read only in the holy tongue, what are we to make of the phrase \"and these words shall be\" which the All-merciful wrote?", 

            " It is necessary because it is written \"Hear, O Israel[1].\"", 

            " It is likewise possible to say that the Sages hold that the whole Torah must be read in the holy tongue. For if thou maintainest that it can be read in any language, what are we to make of the phrase \"Hear, O Israel\" which the All-merciful wrote?", 

            " It is necessary because it is written \"And these words shall be.\" ", 

            "Our Rabbis have taught :", 

            " \"And these words shall be\" means that one must not recite [the sentences of the Shema'] out of order. ", 

            "\"These words... upon thine heart\" — one might suppose that the whole Parashah requires Kawwanah; therefore there is a teaching to state, \"These words... [shall be upon thine heart],\" that is to say,", 

            " up to this point Kawwanah is required, but from this point onward it is not necessary. These are the words of R. Eliezer. [[fol. 13 b.]] R. 'Akiba said to him :", 

            " Behold it states,  "

        ], 

        [

            "\"Which I command thee this day... upon thine heart.\" Hence thou learnest that the whole Parashah requires Kawwanah !", 

            " Rabbah b. Bar Hannah said in the name of R. Johanan:", 

            " The Halakah is in accord with R. 'Akiba. ", 

            "There are some who connect [the statement of Rabbah b. Bar Hannah] with the following. There is a teaching : ", 

            "Who recites the Shema' must direct his heart thereto.", 

            " R. Aha[2] says in the name of R. Judah :", 

            " If one directed his heart in the first paragraph, it is no longer necessary [in the succeeding paragraphs]. ", 

            "Rabbah b. Bar Hannah said in the name of R. Johanan : ", 

            "The Halakah is in accord with the view of R. Aha which he reported in the name of R. Judah. ", 

            "There is a further teaching:", 

            " \"And these words... shall be\" means one must not read [the sentences of the Shema'] out of order. \"Upon thine heart\" — R. Zotra[3] says: ", 

            "Up to here[4] the law of Kawwanah applies, but from here onward the commandment to recite applies. ", 

            "R. Josiah[5] says : ", 

            "Up to here the commandment to recite applies, but from here onward the law requiring Kawwanah applies.", 

            " What is the distinction that from here onward the commandment to recite applies ? Because it is written, \"talking of them[1].\" But in the first Parashah it is likewise written \"and shalt talk of them\" ! ", 

            "What he means to say is,", 

            " Up to here the law of Kawwanah and reciting applies, but from here onward, reciting without Kawwanah is sufficient. ", 

            "And what is the distinction that up to [the end of the first paragraph] the law of Kawwanah and reciting applies ? Because it is written \"upon thine heart\" and \"and shalt talk of them.\" But in the next paragraph it is likewise written \"Upon your heart\" and \"talking of them\" !", 

            " That", 

            " is required for that which R. Isaac said : ", 

            "\"Therefore shall ye lay up these My words upon your heart\" (Deut. xi. 18) is necessary [to teach that the Tefillin] must be placed over against the heart[2]. ", 

            "The teacher stated above : \"R. Josiah says : ", 

            "Up to here the commandment to recite applies, but from here onward the law requiring Kawwanah applies.", 

            "\" What is the distinction that from here onward the law requiring Kawwanah applies ? Because it is written \"upon your heart.\" But in the first Parashah it is likewise written \"upon thine heart\" !", 

            " What he means to say is,", 

            " Up to here the law of reciting and Kawwanah applies, but from here onward Kawwanah without reciting is sufficient. ", 

            "And what is the distinction that up to [the end of the first paragraph] the law of reciting and Kawwanah applies ? Because it is written \"upon thine heart\" and \"thou shalt talk of them.\" But in the next paragraph it is likewise written \"upon your heart\" and \"talking of them\"! ", 

            "That refers to the words of ", 

            "Torah[3]; and thus spake the All-merciful,", 

            " \"Teach your children Torah so that they can read therein.\" ", 

            "Our Rabbis have taught : ", 

            "\"Hear, O Israel, the Lord our God, the Lord is one\" (Deut. vi. 4) — up to here Kawwanah[4] is required. These are the words of R. Meir. ", 

            "Raba said :", 

            " The Halakah is in accord with R. Meir.", 

            " There is a teaching : Symmachus[1] says : ", 

            "Whoever prolongs the pronunciation of the word ehad \"one[2],\" his days and years are prolonged for him. ", 

            "Rab Aha b. Jacob said :", 

            " Especially the letter ", 

            "D. Rab Ashe said:", 

            " Only he must not slur over the letter H. R. ", 

            "Jeremiah was sitting in the presence of R. Hiyya b. Abba[3], and noticed that he prolonged [the word ehad] exceedingly. ", 

            "He said to him : ", 

            "So long as thou hast proclaimed His Kingship above and below and the four winds of heaven[4], more than that is not required of thee. ", 

            "Rab Nathan b. Mar 'Ukba said in the name of Rab Judah :", 

            " \"Upon thine heart\" [should be recited] standing. ", 

            "Dost thou imagine that applies only to the words \"Upon thine heart\"?", 

            " No ; but say,", 

            " [From the commencement of the Shema'] up to \"upon thine heart\" is to be recited standing, but not from there onward.", 

            " R. Johanan said : ", 

            "The whole paragraph should be recited standing ; ", 

            "and R. Johanan hereby follows out his opinion [expressed in the statement ;] Rabbah b. Rab Hannah said in the name of R. Johanan : ", 

            "The Halakah is in accord with the view of R. Aha which he reported in the name of R. Judah[5]. ", 

            "Our Rabbis have taught[6]: ", 

            "\"Hear, O Israel, the Lord our God, the Lord is one\" — that was the reading of the Shema' of R. Judah ha-Nasi'. ", 

            "Rab said to R. Hiyya,", 

            " \"I have never seen Rabbi receive the yoke of the kingdom of heaven upon himself[7].\"", 

            " He replied to him,", 

            " \"Son of princes[8],", 

            " at the time when he passed his hands across his face[1], he received upon himself the yoke of the kingdom of heaven.\" ", 

            "Did he afterwards finish the Shema' or did he not? ", 

            "Bar Kappara says : ", 

            "He did not afterwards finish it.", 

            " R. Simeon b. Rabbi says : ", 

            "He did afterwards finish it. ", 

            "Bar Kappara said to R. Simeon b. Rabbi ;", 

            " It is quite right according to me when I declare he did not afterwards finish it, because Rabbi used [every day] to deal with a theme in which the exodus from Egypt was mentioned[2]; but according to thee who sayest that he did afterwards finish it, why did he [daily] deal with such a theme?", 

            " [He replied] : For the purpose of mentioning the exodus from Egypt in its proper time[3]. ", 

            "R. Ila[4] b. Rab Samuel b. Marta said in the name of Rab:", 

            " [If one recited only the verse] \"Hear, O Israel, the Lord our God, the Lord is one\" and was then overcome by sleep, he has fulfilled his obligation. ", 

            "Rab Nahman[5] said to Daro his servant :", 

            " With the first verse worry me [to keep awake], but do not so after that. ", 

            "Rab Joseph asked Rab Joseph b. Raba[6], ", 

            "\"How used thy father to do ?\"", 

            "He replied, ", 

            "\"With the first verse he took pains [to keep awake], but he did not so after that.\" ", 

            "Rab Joseph said : ", 

            "One who lies on his back should not read the Shema'. ", 

            "Is it only he may not read [the Shema' in this position] ; but is it right for him to sleep [in this position]?", 

            " For lo, R. Joshua b. Levi cursed anyone who slept lying on his back[7] ! ", 

            "They answered : ", 

            "To sleep thus is right if he incline a little to one side, ", 

            "but to read the Shema' is forbidden, though he incline to one side. ", 

            "But R. Johanan inclined to one side and read the Shema' !", 

            " It is different with him, because he was corpulent. ", 

            "Between the sections he may greet a man out of respect for him and return a salutation. ", 

            "He may return a salutation ; but on what ground ? If it is supposed out of respect, since he is allowed to greet, surely he ought to be permitted to respond ! ", 

            "But [the meaning is],", 

            " He greets a man out of respect, and returns a salutation to any person. ", 

            "Consider the sequel : ", 

            "In the middle [of the sections] he may greet a man because of fear for him and return the salutation. On what ground may he respond ? ", 

            "If it is supposed because of fear, since he is allowed to greet, surely he ought to be permitted to respond ! But [the meaning is. ", 

            "He may return the salutation] out of respect.", 

            " But that is the view of. R. Judah[1]! ", 

            "For our Mishnah states: ", 

            "R. Judah says : In the middle of a section, he may greet a man because of fear for him and return a salutation out of respect ; and between the sections, he may greet a man out of respect and return the salutation of any person! ", 

            "[The text of the Mishnah] is defective and should read thus :", 

            " \"Between the sections, he may greet a man out of respect for him, and there is no need to state that he may return the salutation ; and in the middle [of the sections], he may greet a man because of fear for him, and there is no need to state that he may return a salutation. These are the words of R. Meir. ", 

            "R. Judah says : ", 

            "In the middle, he may greet [[fol. 14a.]] because of fear and return a salutation out of respect;  "

        ], 

        [

            "and between the sections he may greet out of respect and return the salutation of any person.\" ", 

            "There is a teaching to the same effect :", 

            " If one is reading the Shema', and his teacher or one greater than himself meet him, between the sections he may greet him out of respect, and there is no need to state that he may return a salutation; and in the middle [of the sections], he may greet one because of fear, and there is no need to state that he may return a salutation. These are the words of R. Meir. ", 

            "R. Judah says :", 

            " In the middle, he may greet because of fear and return a salutation out of respect ; and between the sections, he may greet out of respect and return the salutation of any person.", 

            " Ahi [asked of him]  ", 

            "a Tanna of the school of R. Hiyya, asked R. Hiyya :", 

            " May one interrupt the Hallel or the Megillah [to greet a person] ? ", 

            "Do we argue a fortiori :", 

            " If with the reading of the Shema', which is an ordinance of the Torah, one may interrupt, how much more so should it be permitted in the case of the Hallel or the Megillah[2], which is only a Rabbinical ordinance ! Or is it perhaps that the proclamation of a miracle[3] is superior [to the reading of the [Shema'] ? ", 

            "He replied : ", 

            "One may interrupt, and there is nothing in that [point you raise]. ", 

            "Rabbah' said : ", 

            "On those days when the individual [2] completes the Hallel, he may interrupt between the paragraphs, but in the middle of a paragraph he may not interrupt ; ", 

            "and on the days when the individual does not complete the Hallel[3], he may interrupt even in the middle of a paragraph. ", 

            "But it is not so ! For behold, Raba b. Rab Shaba[4] visited Rabina[5] on one of those days when the individual does not[6] complete the Hallel, and Rabina did not interrupt [to greet him]!", 

            " It is different with Raba b. Shaba, since he was not highly esteemed by Rabina. ", 

            "[He asked of him]", 

            "Ashyan[7], a Tanna of the school of R. Ammi, asked R. Ammi : ", 

            "May one who is undergoing a fast[8] taste anything?", 

            " If he has taken upon himself [to abstain from] eating and drinking, it comes under the heading of neither ; or is it that he has taken upon himself [to abstain from] any kind of gratification, and [tasting] is to be so regarded? ", 

            "He replied : ", 

            "He may taste and there is nothing in that [point you raise]. ", 

            "There is a teaching to the same effect : ", 

            "A woman who tastes [her cooking] is not required to utter a benediction, and she who is undergoing a fast may taste and there is nothing in it. ", 

            "What is the maximum quantity [he may taste]? ", 

            "R. Ammi and R. Assi tasted up to a fourth [of a log]. ", 

            "Rab said :", 

            " Whoever greets his neighbour before he prays[9] is as though he accounted him as an idolatrous altar [bamah][10] ; as it is said, ", 

            "\"Cease ye from man, in whose nostrils is a breath[11] ; for how little [bammeh] is he to be accounted\" (Is. ii. 22). Read not bammeh but bamah[1]. ", 

            "But Samuel said[2] :", 

            " Why do you esteem this person [whom you greet first] and not God ? ", 

            "Rab Sheshet[3] quoted the following in objection ;", 

            " Between the sections one may greet out of respect and return a salutation[4] !", 

            " R. Abba explained ", 

            "[the statements of Rab Samuel to refer] to one who goes first to the door of his neighbour[5]. ", 

            "R. Jonah said in the name of R. Zera: ", 

            "Whoever attends to ", 

            "his personal affairs before offering his prayers is as though he had erected an idolatrous altar. ", 

            "He was asked : ", 

            "Dost thou say \"an idolatrous altar\"? ", 

            "He answered : ", 

            "No, I only mean it is prohibited[6]; and it is in accordance with the statement of Rab Iddi b. Abin ", 

            "who said in the name of Rab Isaac b. Ashyan :", 

            " It is forbidden a man to attend to his personal affairs before offering his prayers ; as it is said, ", 

            "\"Righteousness shall go before him[7], and shall make his footsteps a way\" (Ps. Ixxxv. 14). ", 

            "Rab Iddi b. Abin also said in the name of Rab Isaac b. Ashyan : ", 

            "Whoever prays and afterwards goes on his way [to attend to his affairs], the Holy One, blessed be He, attends to them for him ; as it is said, ", 

            "\"Righteousness shall go before him, and He shall make his footsteps a way.\" ", 

            "R. Jonah also said in the name of R. Zera :", 

            " Whoever sleeps for seven nights without a dream is called evil[8]; as it is said,", 

            " \"He shall abide satisfied [sabea'] he shall not he visited with evil\" (Prov. xix. 23). Read not sabea', but sheba' \"seven[9].\" ", 

            "R. Abba[10], son of R. Hiyya b. Abba, said to him : Thus declared R. Hiyya[11] in the name of R. Johanan :", 

            " Whoever satisfies[12] himself with words of Torah and then sleeps will not receive evil tidings [in a dream]; as it is said, ", 

            "\"He shall abide satisfied [with Torah], he shall not be visited with evil.\" ", 

            "The following are between the sections, etc. ", 

            "R. Abbahu said in the name of R. Johanan :", 

            " The Halakah is in accord with R. Judah who maintains that one may not interrupt between \"I am the Lord your God\" and \"True and firm[1].\"", 

            " R. Abbahu [also] said in the name of R. Johanan:", 

            " What is R. Judah's reason? Because it is written, "

        ], 

        [

            " \"The Lord God is the true God\" (Jer. x. 10). ", 

            "Should one repeat the word \"true\" or not[2]?", 

            " R. Abbahu said in the name of R. Johanan:", 

            " He must repeat the word \"true.\" ", 

            "Rabbah[3] said : ", 

            "He does not repeat it. ", 

            "Somebody descended[4] in the presence of Rabbah ; and when the latter heard him say emit \"true\" twice, ", 

            "He [Rabbah] exclaimed, ", 

            "\"Every emet has seized hold of this fellow !\" ", 

            "Rab Joseph said : ", 

            "How excellent is the teaching which, when Rab Samuel b. Judah came [from Palestine], he reported, viz. :", 

            " In the West they say in the evening, \"Speak unto the children of Israel and say unto them I am the Lord your God. True[5].\" ", 

            "Abbai said to him :", 

            " What is there excellent in this? ", 

            "Behold, Rab Kahana has said in the name of Rab : ", 

            "One need not commence [the third paragraph at all] ; but if he has commenced it, he must finish it ! ", 

            "Shouldest ", 

            "thou argue that [to say the words] \"And thou shalt say unto them\" is not commencing[6], behold Rab Samuel b. Isaac has declared in the name of Rab[7] : ", 

            "\"Speak unto the children of Israel\" is not considered a commencement, but \"And thou shalt say unto them\" is to be so regarded ! ", 

            "Rab Pappa replied : ", 

            "In the West they hold that \"And thou shalt say unto them\" is likewise not considered a commencement, until one adds \"And they shall make for themselves fringes.\" ", 

            "Abbai said :", 

            " Therefore we[1] commence as they commence in the West, and since we have commenced, we also complete it ; for Rab Kahana said in the name of Rab : ", 

            "One need not commence it ; but if he has commenced it, he must finish it. ", 

            "Hiyya b. Rab declared:", 

            " If one has said \"I am the Lord your God,\" he must continue \"True\" ; if he has not said \"I am the Lord your God,\" it is not necessary to add \"True[2].\" ", 

            "Yes; but he is required to mention the exodus from Egypt[3]!", 

            " Let him say the following :", 

            " \"We give thanks unto Thee, O Lord our God, that Thou hast brought us forth from the land of Egypt and redeemed us from the house of bondage, and performed miracles and mighty deeds for us by the Red Sea ; to thee do we sing[4].\" ", 

            "R. Joshua b. Karhah said: Why does the section \"Hear O Israel\" precede \"And it shall come to pass if ye shall hearken\"?", 

            "There is a teaching : R. Simeon b. Johai says : ", 

            "It is right that precedence should be given to \"Hear O Israel\" over \"And it shall come to pass,\" because the former speaks of learning, the latter of teaching;", 

            " and to \"It shall come to pass\" over \"And the Lord spake,\" because the former speaks of teaching[5] and the latter of performing. ", 

            "Do you mean to say that in \"Hear O Israel\" there is a reference to learning, but not to teaching and performing? ", 

            "Behold it is written,", 

            " \"Thou shalt teach them diligently... thou shalt bind them... thou shalt write them\"! ", 

            "And further [do you mean to say that] \"And it shall come to pass\" contains a reference to teaching, but not to performing?", 

            " Behold it is written,", 

            " \"Ye shall bind... ye shall write\"! ", 

            "Nay; but this is what he means to say :", 

            " It is right that precedence should be given to \"Hear O Israel\" over \"And it shall come to pass,\" because the former contains a reference to learning, teaching and performing ; and to \"And it shall come to pass\" over \"And the Lord spake,\" because the former contains a reference to teaching and performing, whereas \"And the Lord spake\" refers only to performing. ", 

            "But derive the reason [for the order of the paragraphs] from the statement of R. Joshua b. Karhah[6]! ", 

            "[He gave] one reason and now another is added; viz. :", 

            " [the first is] in order that a man shall first receive upon himself the yoke of the kingdom of heaven and afterwards receive upon himself the yoke of the commandments ; and the second reason is because the first paragraph contains these other references. ", 

            "Rab washed his hands, read the Shema', put on the Tefillin and then offered his prayers.", 

            " How could he act thus[1]?", 

            " For lo, there is a teaching :", 

            " One who is digging a cavity for a corpse[2] is exempt from the obligation of reading the Shema', the Tefillah, Tefillin and all the commandments mentioned in the Torah[3] ; but when the time of reading the Shema' arrives, he ascends, washes his hands, puts on the Tefillin, reads the Shema' and offers his prayers? ", 

            "Here is a self-contradiction !", 

            " The first clause declares such a man to be exempt from the obligation, and the latter imposes the obligation upon him !", 

            " There is no contradiction : ", 

            "the latter clause referring to where there are two[4], the former to one.", 

            " Nevertheless it presents a difficulty to Rab.", 

            " [The solution is :] Rab holds the view of R. Joshua b. Karhah who says : ", 

            "First there must be the yoke of the kingdom of heaven, and afterwards the yoke of the commandments[5]. ", 

            "R. Joshua b. Karhah certainly said that the reading [of the yoke of heaven, i.e. \"Hear O Israel\"] is to precede the reading [of the yoke of the commandments, i.e. \"And it shall come to pass\"] ; but hast thou heard him say that the reading [of the Shema'] should precede the performance [of the duty of Tefillin] ? ", 

            "Further, how could Rab be considered as holding the same opinion as R. Joshua b. Karhah ? ", 

            "For Rab Hiyya b. Ashe has said : ", 

            "On many occasions have I stood before Rab[6], who first washed his hands, uttered the benediction[7], taught us the chapters, laid Tefillin, and after that read the Shema' ! ", 

            "Shouldest thou argue that the time for reading the Shema' had not yet arrived, in that case what purpose is there in the testimony of Rab Hiyya b. Ashe? ", 

            "[The object was] to refute him who declared that it is unnecessary to utter a benediction over the study of the Mishnah ; hence we are informed that likewise for the Mishnah it is necessary to utter a benediction[1]. ", 

            "Still the difficulty against Rab remains! ", 

            "His messenger was at fault[2]. ", 

            "'Ulla said : ", 

            "Whoever reads the Shema' without Tefillin is as though he spoke false testimony against himself[3]. ", 

            "R. Hiyya b. Abba said in the name of R. Johanan : It is as though he had offered a burnt-offering without a meal-offering (cf. Num. xxviii. 5) and a sacrifice without drink-offerings (ibid. v. 14).  ", 

            "R. Johanan also said[4]: ", 

            "Whoever wishes to receive upon himself the yoke of the kingdom of heaven in perfection"

        ], 

        [

            "should first have evacuation[5], then wash his hands, lay Tefillin, read the Shema' and offer his prayers — that is receiving the kingdom of heaven in perfection. ", 

            "R. Hiyya b. Abba said in the name of R. Johanan : ", 

            "Whoever has evacuation, washes his hands, lays Tefillin, reads the Shema' and offers his prayers, the Scriptures ascribe it to him as though he had erected an altar and brought a sacrifice thereon ; as it is written, ", 

            "\"I will wash my hands in cleanliness ; so will I compass Thine altar, O Lord\" (Ps. xxvi. 6).", 

            " Rabbah[6] said to him : ", 

            "Does not the master think that it is as though he had bathed his whole body[7]? ", 

            "[Yes]; for it is written,", 

            " \"I will wash [in cleanliness][8]\" not simply \"I will cause [mine hands] to be washed.\" ", 

            "Rabina said to Raba[1] :", 

            " Has the master seen the Rabbinical scholar who has come from the West and said,", 

            " \"Who has no water wherewith to wash his hands should rub them with earth or pebbles or sawdust[2]\"?", 

            " He answered : ", 

            "Well has he spoken ; for is it written, \"I will wash with water\"? ", 

            "No; it is written, \"I will wash in cleanliness,\" i.e. with anything that cleanses.", 

            " And lo, Rab Hisda cursed anyone who went about in search of water at the time of prayer[3]. This, however, applies only to the reading of the Shema', but for the Tefillah one may go for water[4]. ", 

            "How far may one go for it ?", 

            " A Parsah. ", 

            "But this applies only in front of him ; in the rear he may not go even a Mil, ", 

            "[from which it is to be deduced] he may not go in the rear a Mil, but less than that distance is permissible. ", 

            "MISHNAH  Who reads the Shema' without making it audible to his ear has complied with the requirements of the law[5]. ", 

            "R. Jose says : ", 

            "He has not so complied.", 

            " If he read it without distinctly pronouncing its letters — R. Jose says :", 

            " He has complied with the requirements of the law ; ", 

            "but R. Judah says : ", 

            "He has not. ", 

            "If one reads it in the wrong order of its paragraphs, he has not complied with the requirements of the law.", 

            " If one has read it but made a mistake, he returns to the place where he erred. ", 

            "GEMARA What is R. Jose's reason [for declaring that unless the Shema' is read audibly the requirements of the law have not been fulfilled]? Because it is written,", 

            " \"Hear O Israel,\" i.e. let thine ear hear what thou issuest from thy mouth. ", 

            "And the first Tanna[6] ? He holds that", 

            " \"Hear\" [means that the Shema' may be read] in any language which thou hearest. ", 

            "And R. Jose [ — where does he find a basis in the Torah for this regulation] ? Both are to be derived from the word \"Hear.\"", 

            " We have learnt elsewhere in the Mishnah : ", 

            "A deaf man who speaks but cannot hear may not separate the Terumah[1] ; but if he has done so, his Terumah is valid. ", 

            "Who is the authority for the teaching : [The Terumah separated by] a deaf man who speaks but cannot hear is post factum valid, but not ab initio[2]? ", 

            "Rab Hisda said : ", 

            "It is R. Jose ; because we have learnt in our Mishnah : ", 

            "Who reads the Shema' without making it audible to his ear has complied with the requirements of the law. These are the words of R. Judah[3].", 

            " R. Jose says: ", 

            "He has not so complied.", 

            "[not translated]", 

            " Only in the matter of the reading of the Shema, which is an ordinance of the Torah, does R. Jose say that the man has not fulfilled his obligation ; but in the matter of Terumah [the deaf man would have fulfilled it], because it is a question of saying the benediction and the saying of the benediction is ordained by the Rabbis, and [the validity of the Terumah] is not dependent upon the benediction[4]. ", 

            "But how [do we know that the teaching in the quoted Mishnah] is R. Jose's? ", 

            "Perhaps it is R. Judah's, ", 

            "and he means to say with reference also to the reading of the Shema' that having read it inaudibly he has complied with the requirements of the law, ", 

            "but ab initio he should not read it so ? ", 

            "Thou mayest find proof for this in the fact that he states Who reads[5] [the Shema' without making it audible], i.e. post factum it is valid, but not ab initio ! ", 

            "They answer ", 

            "that the fact that our Mishnah states Who reads is intended to show how extreme is the view of R. Jose, for he means to say ", 

            "that even post factum it is not valid; since were it R. Judah, even ab initio it would still be valid. ", 

            "Having demonstrated that [the Mishnah about Terumah] is in accord with R. Jose, what, however, of the following ? There is a teaching: ", 

            "A man must not say the Grace after meals", 

            " in his heart [inaudibly] ; but if he has done so, he has fulfilled his obligation. Whose view is this?", 

            " It can be neither R. Jose's nor R. Judah's. ", 

            "For were it R. Judah's, if the man had said [Grace inaudibly] ", 

            "ab initio he would also have fulfilled his duty ; if R. Jose's, even post factum it cannot be considered that he has done so[1]. How is it then?", 

            " It must be R. Judah's, and [his opinion is] post factum it is allowed, but not ab initio. ", 

            "What, however, of the following? R. Judah, the son of R. Simeon b. Pazzi, taught : ", 

            "A deaf person who can speak but cannot hear may separate the Terumah ab initio. In accordance with whose view is this ?", 

            " It can be neither R. Judah's nor R. Jose's.", 

            " If R. Judah's, he permits it ", 

            "post factum, but not ab initio; if R. Jose's, ", 

            "he does not allow it even post factum.", 

            " It is certainly in agreement with R. Judah, even though it be ab initio ; and there is no contradiction[2].", 

            " The latter[3] is his own opinion, the other[4] the opinion of his teacher.  For there is a teaching[5] : R. Judah says in the name of R. Eleazar b. 'Azariah :", 

            " When one reads the Shema' he must make it audible to his ear ; as it is said, ", 

            "\"Hear, O Israel, the Lord our God, the Lord is one\" (Deut. vi. 4). ", 

            "R. Meir said to him : ", 

            "Behold the Scriptures state, \"And these words which I command thee this day shall be upon thy heart\" (ibid. v. 6), i.e. the words depend on the Kawwanah of the heart[6]. Since thou hast reached so far[7], thou mayest even suppose that ", 

            "R. Judah agrees with his teacher's opinion, and there is no contradiction, one being R. Meir's view[8] and the other R. Judah's[9]. ", 

            "We have learnt elsewhere in the Mishnah :", 

            " All are fit and proper persons to read the Megillah, except a deaf person, a mentally defective, and a minor[1]. R. Judah allows a minor to read. ", 

            "Who is the authority for the teaching that if a deaf person has read it[2], his recital is even post factum invalid? ", 

            "Rab Mattenah declared ", 

            "that it is R. Jose ; for we have learnt in our Mishnah :", 

            " Who reads the Shema' without making it audible to his ear has complied with the requirements of the law. These are the words of R. Judah. ", 

            "R. Jose says: ", 

            "He has not so complied. ", 

            "How can we know that [this quoted Mishnah] is R. Jose's view [and means that the reading of the Megillah by a deaf person] is also invalid post factum ; "

        ], 

        [

            "perhaps it is R. Judah's view and ab initio it is not permitted, but post factum it is valid ?", 

            " This cannot enter thy mind ; because the Mishnah refers to a deaf person exactly as to the mentally defective and minor ; ", 

            "and therefore, as in the case of a mentally defective and minor even post factum [the reading of the Megillah] is invalid, ", 

            "so also if a deaf person has read it, it is likewise invalid.", 

            " But perhaps the two have to be kept distinct[3]!", 

            " Still thou canst not possibly maintain that it is in accord with R. Judah ; because from what is stated in the sequel,", 

            " \"R. Judah allows a minor to read [the Megillah]\" it is to be inferred that the first part is not R. Judah's view ! ", 

            "But perhaps the whole of it is R. Judah's view, there being two kinds of \"minor,\" and [the wording of the Mishnah] is defective and should read thus :", 

            " \"All are fit and proper persons to read the Megillah except a deaf person, a mentally defective person and a minor. Of whom does this speak ? Of a minor who has not yet reached Initiation[4]; but a minor who has reached Initiation is fit to read it even ab initio. These are the words of R. Judah, for R. Judah permits a minor to read.\" ", 

            "Having demonstrated that [the Mishnah about the reading of the Megillah] is in accord with R. Judah and post factum it is permissible, but not ab initio, what, however, of the teaching of R. Judah, the son of R. Simeon b. Pazzi : ", 

            "A deaf person who speaks but cannot hear may separate the Terumah ab initio ? Whose view is that?", 

            " It cannot be R. Judah's, nor R. Jose's.", 

            " If R. Judah's, post factum it should be allowed, but not ab initio; if R. Jose's, even post factum it should be invalid. Whose view is it then ?", 

            " R. Judah's and even ab initio it is permissible. ", 

            "What, however, of the following ? There is a teaching :", 

            " A man must not say Grace after meals in his heart ; but if he has done so, he has complied with the requirements of the law. Whose view is that ?", 

            " It is not R. Judah's, nor R. Jose's. ", 

            "If R. Judah's, he would allow that to act thus ab initio likewise complies with the requirements of the law ; if R. Jose's, even post factum it is not valid.", 

            " It is certainly R. Judah's view, and even ab initio it is valid. Nor is there any contradiction[1] ; ", 

            "the latter[2] being R. Judah's own opinion, the other that of his teacher[3]. For there is a teaching : R. Judah says in the name of R. Eleazar b. 'Azariah :", 

            " He who reads the Shema' must make it audible to his ear ; as it is said,", 

            " \"Hear O Israel.\" ", 

            "R. Meir said to him : Behold the Scriptures state,", 

            " \"And these words which I command thee this day shall be upon thy heart,\" i.e. the words depend upon the Kawwanah of the heart. ", 

            "Since thou hast reached so far, thou mayest even suppose that ", 

            "R. Judah agrees with his teacher's opinion ; and there is no contradiction, one being R. Judah's view, the other R. Meir's[4]. ", 

            "Rab Hisda said in the name of Rab Shela[5]: ", 

            "The Halakah is in accord with R. Judah's view which he reported in the name of R. Eleazar b. 'Azariah, and the Halakah is in accord with R. Judah.", 

            " It is necessary [to state it in this way] ; for if he had informed us only that the Halakah is in accord with R. Judah, I might have supposed", 

            " [the Shema' need not be read audibly] ab initio ; therefore he tells us that ", 

            "the Halakah is in accord with R. Judah's view which he reported in the name of R. Eleazar b. 'Azariah[6]. ", 

            "And if he had informed us only that the Halakah is in accord with R. Judah's view which he reported in the name of R. Eleazar b. 'Azariah, I might have supposed ", 

            "that it is essential [for the Shema' to be read audibly ab initio] and there was no rectification [if this had not been done]. Therefore he informs us that", 

            " the Halakah is in accord with R. Judah[7]. ", 

            "Rab Joseph said :", 

            " The dispute is only over the reading of the Shema', but with other commandments[1] all agree that [if inaudible] he has not complied with the requirements of the law ; for it is written, ", 

            "\"Attend and hear, O Israel\" (Deut. xxvii. 9). ", 

            "But it is quoted in objection :", 

            " One may not say the Grace after meals in his heart ; but if he has done so, he has complied with the requirements of the law !", 

            " But if [the statement of Rab Joseph] was reported, it must have been reported as follows :", 

            "[Rab Joseph said] :", 

            " The dispute is only over the reading of the Shema' ; for it is written,", 

            " \"Hear O Israel\" ; but with other commandments all agree that [if inaudible] he has complied with the requirements of the law. ", 

            "But it is written, \"Attend and hear, O Israel[2]\" ! ", 

            "That refers to reading the Scriptures[3]. ", 

            "If he had read it without distinctly pronouncing its letters. ", 

            "R. Tabi said in the name of R. Josiah : The Halakah is in accord with the more lenient view in both instances[4]. ", 

            "R. Tabi also said in the name of R. Josiah : What means that which is written, ", 

            "\"There are three things that are never satisfied... the grave, and the barren womb,\" etc. (Prov, xxx. 15 f.) — what is the connection between \"the grave\" and \"the barren womb\"?", 

            " Its intention is to tell thee that", 

            " as the womb receives and yields up, so the grave receives and yields up. ", 

            "And may we not use the a fortiori argument ? ", 

            "As the womb receives [the seed] in silence and yields up [the child] with loud cries, how much more so will the grave, which receives [the body] with loud cries [of lament], yield up with loud cries !", 

            " Hence a refutation of those who assert that the resurrection of the dead is not taught in the Torah[5]. ", 

            "Rab Josiah[6] taught in the presence of Raba :", 

            " \"And thou shalt write them\" (Deut. vi. 9) means that the whole [of the first two paragraphs of the Shema'] must be written [in the Tefillin], even the words of the commands[7]. ", 

            "Raba said to him :", 

            " Should one ask thee whose teaching this is, it is R. Judah's; for he stated with reference to the woman suspected of adultery : One writes the curses but not the words of the command, ", 

            "because in this connection it is written, ", 

            "\"And the priests shall write these curses in a scroll\" (Num. v. 23), but here [in connection with Tefillin] it is written, \"And thou shalt write them,\" i.e. even the words of the command. ", 

            "Dost thou suppose that R. Judah's reason is because the text states, \"[And the priest] shall write\"?", 

            " His reason is because the text states, \"[And the priest shall write] these curses,\" i.e. the curses shall be written, but not the words of the command.", 

            " It is necessary [to mention this point] ; ", 

            "because it might have entered thy mind that I mean we can draw an analogy from the use of the verb \"to write\" in the former instance, thus : As there [with reference to the woman suspected of adultery] the curses were to be written and not the words of the command, so here likewise [with the Tefillin] the words of the command were not to be written[1]! Therefore the All-merciful wrote, \"And thou shalt write them\" i.e. even the words of the command. ", 

            "Rab Obadiah taught in the presence of Raba :", 

            " \"And ye shall teach\" (Deut. xi. 19), i.e. let thy teaching be perfect[2] — let one make a brief pause between words which are liable to be jumbled together[3], ", 

            "Raba added to this observation : ", 

            "For instance 'al lebabeka \"upon thy heart\" ; 'al lebabekem \"upon your heart\" ; bekol lebabeka \"with all thy heart\" ; bekol lebabekem \"with all your heart\" ; 'eseb besadeka \"grass in thy field\" ; wa'abadtem meherah \"and ye will perish speedily\" ; hakkanaph petil \"the corner, a thread\" ; etkem me'eres \"you from the land[4].\" ", 

            "R. Hamma b. R. Hannina said : ", 

            "Whoever reads the Shema' with distinct pronunciation of its letters, Gehinnom is cooled for him ; as it is said,", 

            " \"When the Almighty scattereth kings therein, it snoweth in Zalmon\" (Ps. Ixviii. 15). Read not bephares \"[When the Almighty] scattereth,\" but read bepharesh \"When one uttereth [the name of the Almighty] distinctly\" ; and read not beZalmon \"in Zalmon,\" but besalmawet \"in the shadow of death[1].\" ", 

            "R. Hamma b. R. Hannina also said : ", 

            "Why are there found associated "

        ], 

        [

            " \"tents\" and \"streams\" — for it is written,", 

            " \"As streams  stretched out, as gardens by the river-side, as tents[2] planted by the Lord, as cedars beside the waters\" (Num. xxiv. 6)[3]? Its intention is to tell thee that", 

            " as streams bring a man up from impurity to purity, so do \"tents\" bring a man up from the scale of guilt to the scale of merit. ", 

            "If one read it in the wrong order of its paragraphs, he has not complied with the requirements of the law. ", 

            "R. Ammi and R. Assi were once decorating the bridal-chamber for R.Eleazar. He said to them,", 

            " \"In the meanwhile I will go and listen to the teaching in the House of Study, and will come back and report it to you.\" ", 

            "He went and found a Tanna expounding in the presence of R. Johanan: ", 

            "Should one have read the Shema' and erred without knowing for certain where he made the mistake, if this occurred in the middle of the first paragraph he must return to the commencement ; if between two paragraphs, he must return to the first of them ; if between \"and thou shalt write them\" and \"ye shall write them[4],\" he must return to the first. ", 

            "R. Johanan said to him : ", 

            "This latter only applies if he has not started \"That your days may be multiplied\" ; but should he have commenced that sentence, [he may assume that] he followed on from force of habit[5]. ", 

            "[R. Eleazar] returned and reported it to them. ", 

            "They said to him : ", 

            "\"If we had come for nothing else than to hear this, it would be sufficient for us.\" ", 

            "MISHNAH Workmen may read the Shema' on the top of a tree or on top of scaffolding, but this they may not do with the Tefillah. ", 

            "A bridegroom is exempt from the obligation of reading the Shema' on the first night [of his marriage], ", 

            "and until the termination of the ensuing Sabbath, if he has not consummated the marriage. ", 

            "It happened that when Rabban Gamaliel married, he read the Shema' on the first night.", 

            " His disciples said to him,", 

            " \"Our teacher ! thou hast taught us that a bridegroom is exempt from the obligation of reading the Shema'[1].\" ", 

            "He replied, ", 

            "\"I will not hearken to you to annul the kingdom of heaven from myself even a single hour.\" ", 

            "GEMARA Our Rabbis have taught : ", 

            "Workmen may read [the Shema'] on the top of a tree or on the top of scaffolding. They may likewise say the Tefillah on top of an olive-tree or fig-tree[2] ; but with all other trees they must descend to the ground to say the Tefillah. ", 

            "The employer must in every instance descend to the ground to say the Tefillah, because his mind is not settled[3]. ", 

            "Rab Mari, the son of Samuel's daughter[4], asked Raba : Our Mishnah states : ", 

            "Workmen may read [the Shema'] on the top of a tree or on the top of scaffolding ; hence it is to be inferred that", 

            " it does not require Kawwanah.", 

            " I quote in refutation[5]: ", 

            "Who reads the Shema' must direct his heart; as it is said,", 

            " \"Hear, O Israel\" (Deut. vi. 4) and elsewhere, ", 

            "\"Attend and hear, O Israel \" (ibid, xxvii. 9) ; as here \"attention\" is required so also there[6] ! ", 

            "[Raba] remained silent ; ", 

            "so he asked him : ", 

            "Hast thou heard anything on this point ?", 

            " He replied : ", 

            "Thus said Rab Sheshet[7]: ", 

            "[Kawwanah is demanded of workmen] only if they stop their work to read it. ", 

            "But lo, there is a teaching : Bet Hillel say :", 

            " Workmen may remain at their work and read it !", 

            " There is no contradiction ;", 

            "the former refers to the first paragraph [of the Shema'], the latter to the second. ", 

            "Our Rabbis have taught: ", 

            "Labourers who are working for an employer should read the Shema', say the benedictions before and after, eat their meal with Grace before and after, and then pray the Eighteen Benedictions[1]; but they cannot descend before the Ark[2] nor raise their hands[3]. ", 

            "But lo, there is a teaching:", 

            " [Such men are to say] an abstract of the Eighteen Benedictions[4]! ", 

            "Rab Sheshet said : There is no contradiction ;", 

            " the first being Rabban Gamaliel's view, the latter R. Joshua's[5]. ", 

            "If it be R. Joshua's view, why does he mention labourers specially, since it holds good of anybody ?", 

            " But [we have to assume that] both are Rabban Gamaliel's,", 

            " and there is no contradiction;", 

            "the latter treating of one who works for a wage[6], the former of one who works for his keep.", 

            " And so there is a teaching :", 

            " Labourers who are working for an employer should read the Shema' say the Tefillah, then eat their meal, but should not say Grace before it[7], only two benedictions after it. How is this meant[8]? The first benediction as ordained[9]; the second commences with the benediction of \"the land,\" and they include \"Who... rebuildest Jerusalem\" in the benediction of \"the land[10].\" ", 

            "To whom does this apply ? To those who work for a wage ; but should they work for their keep or their employer take his meals with them[11], they say the [entire] Grace after meals as ordained. ", 

            "A bridegroom is exempt from the obligation of reading the Shema'. ", 

            "Our Rabbis have taught :", 

            " \"When thou sittest in thy house\" (Deut. vi. 7) excludes one occupied with a religious duty ; \"and when thou walkest by the way\" (ibid.) excludes a bridegroom. Hence they say : ", 

            "He who takes a virgin to his house as wife is exempt ; but if he marry a widow, he has that obligation. ", 

            "How is that demonstrated ? ", 

            "Rab Pappa said : ", 

            "Because [the text uses the word] \"way\" [we argue]: Just as the way is voluntary, so all is voluntary[1]. ", 

            "Are we not here dealing with one who is on his way to perform a religious duty, and even so the All-merciful requires of him the reading [of the Shema'] ? ", 

            "In that case, the All-merciful should have written \"when walking.\" What means \"when thou walkest\"? Deduce from this, [it means]", 

            " when walking for thine own purpose thou art under the obligation [to read the Shema'] ; but when it is the performance of a religious duty, thou art exempt. "

        ], 

        [

            "If so,  why especially mention, \"He who takes a virgin to his house as wife\" ? Even one who takes a widow to wife should also [be exempt] !", 

            " The man [who marries a virgin] is anxious ; the other is not. ", 

            "Should the reason [of exemption] be on account of anxiety, then it ought to apply also to one whose ship has sunk at sea ! ", 

            "Why, then, does R. Abba b. Zabda declare in the name of Rab :", 

            "A mourner is under the obligation to observe all the commandments mentioned in the Torah except Tefillin, because they are called an adornment; as it is said,", 

            " \"Bind thine adornment upon thee\" (Ezek. xxiv. 17)? ", 

            "The answer is : [There is a difference] ;.", 

            " the latter being troubled by anxiety of some voluntary matter, whereas the former has anxiety in connection with a religious duty. ", 

            "MISHNAH [Rabban Gamaliel] bathed on the first night of his wife's death. His disciples said to him,", 

            " \"Our master! Thou hast taught us[2] that a mourner is forbidden to bathe !\" ", 

            "He replied,", 

            " \"I am not like other men ; I am in delicate health.\" ", 

            "When his slave, Tabi, died, lie accepted condolence on his behalf. ", 

            "His disciples said to him,", 

            " \"Our master ! Thou hast taught us that one may not accept condolence on the death of slaves\" !", 

            " He replied, ", 

            "\"My slave, Tabi, was not like other slaves; he was a worthy man.\" ", 

            "If a bridegroom wishes to read the Shema' on the first night [of his marriage], he may do so. ", 

            "Rabban Simeon b. Gamaliel says :", 

            " \"Not everybody who wishes to assume the name[1] may do so.\" ", 

            "GEMARA What was Rabban Gamaliel's reason[2]? ", 

            "He was of the opinion that the application of the laws of mourning in the night is a Rabbinical injunction; for it is written, ", 

            "\"And the end thereof as a bitter day\" (Amos viii. 10)[3]; and in the case of a person in delicate health, the Rabbis do not so decree. ", 

            "When his slave, Tabi, died, etc. ", 

            "Our Rabbis have taught : ", 

            "[At the burial of] male and female slaves, we do not stand in a row[4] for them, nor do we pronounce ", 

            "over them the benediction of mourners[5] and the condolence of mourners[6].", 

            " It happened that R. Eliezer's female slave died and his disciples went in to comfort him. ", 

            "When he saw them, he ascended to an upper room, but they ascended after him.", 

            " He went into the court-way[7], but they went after him. He entered the guest-chamber, but they entered after him.", 

            " He said to them :", 

            " I imagined you would be scalded with tepid water[8]; but now you are not scalded even with hot water. ", 

            "Have I not taught you :", 

            " [On the death of] male and female slaves, we do not stand in a row for them, nor do we pronounce over them the benediction of mourners and the condolence of mourners? ", 

            "What, however, do we say over them ? As we say to a man on the death of his ox or ass,", 

            " \"May the Omnipresent repair thy loss,\" so do we say to a man on the death of his slaves,", 

            " \"May the Omnipresent repair thy loss.\" ", 

            "There is a further teaching : ", 

            "We do not speak a funeral oration over male and female slaves. ", 

            "R. Jose said :", 

            " If he was a worthy man, we say of him, ", 

            "\"Alas, the good and faithful man who derived pleasure from his work !\" ", 

            "They said to him, ", 

            "\"In that case, what hast thou left to be said over worthy men [who are not slaves][1]?\" ", 

            "Our Rabbis have taught :", 

            " We restrict the name \"Patriarch\" to three[2], and \"Matriarch\" to four[3]. ", 

            "Why is the name \"Patriarch\" [restricted to three][4]? ", 

            "Is it because we are not certain whether we are descended from Reuben or Simeon ? If so, in the case of the Matriarchs we are not certain whether we are descended from Rachel or Leah ! ", 

            "But", 

            " up to here they were esteemed sufficiently [to be called \"Patriarchs\"] ; their successors were not so esteemed. ", 

            "There is a further teaching :", 

            " We do not call male and female slaves \"Father so-and-so\" or \"Mother so-and-so.\" But Rabban Gamaliel's [slaves] used to be called in this manner.", 

            " This is an actual fact to upset [the teaching just quoted] !", 

            " [No; it is different with them,] because they were highly esteemed. ", 

            "R. Eleazar said : ", 

            "what means that which is written, ", 

            "\"So will I bless Thee as long as I live ; in Thy name will I lift up my hands\" (Ps. Ixiii. 5)? \"So will I bless Thee as long as I live\" refers to the reading of the Shema' ; \"in Thy name will I lift up my hands\" refers to Tefillah.", 

            " If one act thus, of him the text saith, ", 

            "\"My soul is satisfied as with marrow and fatness\" (ibid. v. 6) ; and not only that, but he will inherit two worlds, this world and the world to come, as it is said, ", 

            "\"And my mouth will praise Thee with joyful lips\" (ibid.)[5]. ", 

            "R. Eleazar used to add at the conclusion of his prayer[6] : ", 

            "May it be Thy will, O Lord our God, to cause love and brotherhood, peace and comradeship, to abide in our lot[7], to enlarge our border with disciples, to prosper our goal with a [happy] end and with hope, to set our portion in the Garden of Eden[1], and fortify us with good companionship and the good impulse in Thy universe, so that we rise up and find the longing of our heart to fear Thy name ; and may the satisfaction of our soul come before Thee for good.", 

            "R. Johanan used to add at the conclusion of his prayer: ", 

            "May it be Thy will, O Lord our God, to glance at our shame and look upon our evil plight ; and do Thou clothe Thyself in Thy mercy, cover Thyself with Thy might, enfold Thyself with Thy piety and gird Thyself with Thy grace, and may Thy attribute of goodness and gentleness come before Thee[2]. ", 

            "R. Zera used to add at the conclusion of his prayer : ", 

            "May it be Thy will, O Lord our God, that we sin not ; neither may we be put to shame nor be confounded before our fathers. ", 

            "R. Hiyya[3] used to add at the conclusion of his prayer : ", 

            "May it be Thy will, O Lord our God, that Thy Torah be our occupation ; and let not our heart grow faint nor our eyes dim. ", 

            "Rab used to add at the conclusion of his prayer : ", 

            "May it be Thy will, O Lord our God, to grant us long life, a life of peace, a life of good, a life of blessing, a life of sustenance, a life of bodily vigour, a life marked by the fear of sin, a life free from shame and reproach, a life of prosperity and honour, a life in which the love of Torah and the fear of Heaven shall cleave to us, a life wherein Thou fulfillest all the desires of our heart for good[4]. ", 

            "Rabbi used to add at the conclusion of his prayer :", 

            " May it be Thy will, O Lord our God and God of our fathers, to deliver me from arrogant men and from arrogance, from a bad man, and from any mishap, from the evil impulse, from a bad companion, from a bad neighbour, and from the adversary that destroyeth ; from a hard judgment, and from a hard opponent, whether he be a son of the covenant or be not a son of the covenant[5]. ", 

            "[Thus did Rabbi pray], although eunuchs were standing by him[6]. ", 

            "Rab Saphra used to add at the conclusion of his prayer : ", 

            "May it be Thy will, O Lord our God, to grant peace "

        ], 

        [

            " in the household above[1] and the household below, and among the students who occupy themselves with Thy Torah, whether they devote themselves thereto for its own sake or not for its own sake[2]; and as for them that devote themselves thereto not for its own sake, may it be Thy will that they do devote themselves thereto for its own sake. ", 

            "R. Alexander used to add at the conclusion of his prayer : ", 

            "May it be Thy will, O Lord our God, to place us in a corner of light and not in a corner of darkness ; and may not our heart grow faint nor our eyes dim. ", 

            "There are some who say ", 

            "this was Rab Hamnuna's prayer ; and R. Alexander used to add at the conclusion of his prayer : ", 

            "Lord of the universe ! It is revealed and known before Thee that it is our will to perform Thy will ; but what stands in the way?", 

            " The leaven that is in the dough[3] and the servitude of the kingdoms[4]. ", 

            "May it be Thy will to deliver us from their hand[5], so that we may again perform the statutes of Thy will with a perfect heart. ", 

            "Raba used to add at the conclusion of his prayer : ", 

            "O my God, before I was formed I was nothing worth, and now that I have been formed I am but as though I had not been formed. Dust am I in my life ; how much more so in my death. Behold I am before Thee like a vessel filled with shame and confusion. O may it be Thy will, O Lord my God, that I may sin no more; and as to the sins I have committed, purge them away in Thine abounding compassion though not by means of affliction and sore diseases.", 

            " That is the confession of[6] Rab Hamnuna Zuta on the Day of Atonement[7]. ", 

            "Mar b. Kabina used to add at the conclusion of his prayer : ", 

            "O my God ! (Guard my tongue from evil and my lips from speaking guile ; and to such as curse me let my soul be dumb, yea, let my soul be unto all as the dust. Open my heart to Thy Torah, and let my soul pursue Thy commandments. And do Thou deliver me from mishap, from the evil impulse, and from an evil woman and all evil which breaks forth to come upon the world[1]. If any design evil against me, speedily make their counsel of none effect, and frustrate their designs[2]. Let the words of my mouth and the meditation of my heart be acceptable before Thee, O Lord my Rock and Redeemer. ", 

            "Rab Sheshet, when observing a fast, used to add at the conclusion of his prayer :", 

            " Lord of the universe ! It is revealed before Thee that when the Sanctuary was in existence, a man sinned and brought an offering, of which they sacrificed only the fat and the blood, and atonement was made for him. ", 

            "But now, I observe a fast, and my fat and blood are diminished. May it be Thy will, that my fat and blood which have been diminished may be accounted as though I had offered them before Thee upon the altar, and do Thou favour me[3]. ", 

            "R. Johanan said : R. Meir[4], on concluding the reading of the Book of Job, used to say:", 

            " It is the fate of man to die and of cattle to be slaughtered, and all are destined to die. ", 

            "Happy is he who has grown in Torah and whose labour has been in Torah ; who has caused tranquillity of spirit to his Creator, advanced in good repute, and departed from the world with a good name. Of him said Solomon, \"A good name is better than precious oil, and the day of death than the day of one's birth \" (Eccles. vii. 1). ", 

            "It was a favourite saying of R. Meir : ", 

            "Learn with all thy heart and with all thy soul to know My ways and watch at the doors of My Torah. Guard My Torah in thy heart and let the fear of Me be before thine eyes. Keep thy mouth from all sin, and purify and sanctify thyself from all guilt and iniquity. Then shall I be with thee everywhere. ", 

            "It was a favourite saying of the Rabbis of Jabneh[1] :", 

            " I am a creature [of God] and my neighbour is also His creature ; my work is in the city and his in the field ; I rise early to my work and he rises early to his. As he cannot excel in my work, so I cannot excel in his work. But perhaps thou sayest, ", 

            "\"I do great things and he small things\"! We have learnt that [it matters not whether]", 

            " one does much or little, if only he direct his heart to Heaven. ", 

            "It was a favourite saying of Abbai: ", 

            "A man should always be cunning[2] in the fear [of God], giving the soft answer that turneth away wrath (cf. Prov. xv. 1), increasing peace with his brethren and relatives and with all men[3], even the heathen in the street ; so that he may be beloved above and popular on earth, and acceptable to his fellow-creatures.", 

            " They say of Rabban Johanan b.", 

            " Zakkai that nobody ever greeted him first, not even the heathen in the street. ", 

            "It was a favourite saying of Raba : ", 

            "The goal of wisdom is repentance and good works; ", 

            "so that a man shall not read [Torah] and study [Mishnah] and then contradict his father or mother or teacher or anybody greater than he in knowledge and number [of years]; as it is said,", 

            " \"The fear of the Lord is the beginning of wisdom, a good understanding have all that do thereafter\" (Ps. cxi. 10). ", 

            "\"All that learn[4]\" is not said here, but \"all that do thereafter,\" i.e. they that practise Torah for its own sake, but not they that practise Torah not for its own sake[5]. ", 

            "As for him who does not fulfil the Torah for its own sake, it were better had he never been created[1]. ", 

            "It was a favourite saying of Rab :", 

            " Not like this world is the world to come. In the world to come there is neither eating nor drinking; no procreation of children[2] or business transactions; no envy or hatred or rivalry ; but the righteous sit enthroned, their crowns on their heads, and enjoy the lustre of the Shekinah; as it is said, ", 

            "\"And they beheld God, and did eat and drink\" (Exod. xxiv. ll)[3]. ", 

            "Our Rabbis have taught[4] : Greater is the promise given by the Holy One, blessed be He, to women than to men ; as it is said, \"Rise up, ye women that, are at ease, and hear My voice ; ye confident daughters, give ear unto My speech\" (Is. xxxii. 9)[5].", 

            " Rab asked R. Hiyya : ", 

            "Wherewith do women acquire merit[6]? By sending their children to learn [Torah] in the Synagogue and their husbands to study in the schools of the Rabbis, and waiting for their husbands until they return from the schools of the Rabbis[7]. ", 

            "As the Rabbis departed[8] from the school of R. Ammi[9] (another version: R. Hannina's school), they said to him:", 

            " Mayest thou see thy world in thy life-time[10], and may thine end be in the life of the world to come and thy hope throughout the generations. ", 

            "May thy heart meditate in understanding, thy mouth speak wisdom, thy tongue abound in joyful songs, thine eyelids set thy glance straight before thee[11], thine eyes be illumined with the light of the Torah, thy countenance shine like the splendour of the firmament, thy lips utter knowledge, thy reins exult with up-rightness, and thy feet run to hear the words of the Ancient of days. ", 

            "As the Rabbis departed from the school of Rab Hisda (another version : the school of R. Samuel b. Nahmani) they said to him :", 

            " \"Our leaders[1] are well laden ; with no breach, and no going forth, and no outcry in our broad places\" (Ps. cxliv. 14).", 

            " \"Our leaders are well laden\" — Rab and Samuel (another version : R. Johanan and R. Eleazar) [differ in interpretation] ; one says, ", 

            "\"Our leaders\" in Torah \"are well laden\" with religious duties ;", 

            " the other says,", 

            " \"Our leaders\" in Torah and religious duties \"are well laden\" with sufferings. "

        ], 

        [

            " \"With no breach\" — may not our company be like the company of David from which issued Ahitophel ; \"and no going forth\" — may not our company be like the company of Saul from which issued Doeg the Edomite; \"and no outcry\" — may not our company be like the company of Elisha from which issued Gehazi ; \"in our broad places\" — that we may not have a son or disciple who spoiled his food in public, like the Nazarene[2]. ", 

            "\"Hearken unto Me, ye stout-hearted, that are far from righteousness\" (Is. xlvi. 12). ", 

            "Rab and Samuel (another version : R. Johanan and R. Eleazar) [differ in interpretation]. One says : ", 

            "The whole world is nourished through righteousness, but the \"stout-hearted\" are nourished by the arm[3].", 

            " The other says :", 

            " The whole world is nourished through their merit, but they are not nourished even by their own merit. ", 

            "This is like the statement of Rab Judah who says in the name of Rab : ", 

            "Every day a Bat Kol issues from Mount Horeb[4] and proclaims : ", 

            "\"All the world is nourished for the sake of My son, Hannina[5], but My son, Hannina, is satisfied with a Kab of locusts[6] from the Sabbath-eve to the next Sabbath-eve.\" ", 

            "This contradicts the statement of Rab Judah who says : ", 

            "Who are the \"stout-hearted\"? They are the foolish Gobeans[1]. ", 

            "Rab Joseph[2] said : ", 

            "Thou canst know [that the \"stout-hearted\" are the Gobeans] because not one of them has ever been made a proselyte. ", 

            "Rab Ashe said : ", 

            "[The \"stout-hearted\" are] the inhabitants of Mata Mehasya[3], for they beheld the glory of the Torah twice yearly, but not one of them has ever been made a proselyte. ", 

            "If a bridegroom wishes to read the Shema', etc. ", 

            "It is to be inferred that Rabban Simeon b. Gamaliel is concerned lest a charge of presumption [be brought against a bridegroom who reads the Shema' on the first night of his marriage and therefore forbids it], whereas the Rabbis have no such concern [and permit it]. But we understood just the opposite of them ! ", 

            "For there is a Mishnaic teaching :", 

            " In a place where they are accustomed to work on the ninth of Ab[4], we may work ; but in a place where they are not accustomed to work, we may not. Disciples of the wise must cease work in every place.", 

            " Rabban Simeon b. Gamaliel says :", 

            " Everyone should regard himself as a disciple of the wise[5]. ", 

            "Here is an inconsistency of the Rabbis and an inconsistency of Rabban Simeon b. Gamaliel ! ", 

            "R. Johanan said :", 

            " The statement must be reversed[6]; ", 

            "but Rab Shesha b. Rab Iddi said : ", 

            "Thou hast surely no need to reverse the statement, because the Rabbis do not here contradict themselves.", 

            " In the case of the reading of the Shema' which everybody reads, if [the bridegroom] also reads it, it would not seem presumptuous ; but in the latter instance, since everybody works [on the ninth of Ab] and he does not, it would appear presumptuous. ", 

            "Likewise, Rabban Simeon b. Gamaliel does not contradict himself.", 

            " In the case of the reading of the Shema', its validity depends on Kawwanah, and we testify that [the bridegroom] would not be able to concentrate his mind ; ", 

            "but here, if one saw [a man not working on the ninth of Ab] he would merely say", 

            " \"He has no work to do.\" Go out and see how many idle men there are in the street[1]. ", 

            "May we return to thee : Who reads. ", 

            "MISHNAH  He whose dead is lying before him [unburied] is exempt from the reading of the Shema', from Tefillah, Tefillin and all the commandments mentioned in the Torah. ", 

            "The bearers of the bier and they who relieve them, and they who relieve these latter — such as are before the bier[1] and such as are behind it[2] — ", 

            "they who are before it, whose services will be required, are exempt ; but they who are behind it, whose services may still be required, are under the obligation. But both are exempt from the Tefillah. ", 

            "Having buried the dead and returned [from the grave], if they have sufficient time to begin and finish [the Shema'] before arriving at the row[3], they should commence it ; but if they have not sufficient time, they should not commence it. ", 

            "As for those who stand in the row, the inner line is exempt, the outer line under the obligation[4]. ", 

            "[not translated]", 

            "GEMARA When the body is lying before him, he is exempt; [it is consequently to be inferred that] when it is not lying before him, he is not exempt ! ", 

            "I quote in objection : ", 

            "He whose dead is lying", 

            " before him should eat his meal in another room, and if he has no other room he should eat in a neighbour's house ; if such be not available, he should put up a partition and have his meal ; if he has nothing wherewith to make a partition, he should turn his face away [from the body] and eat. But he must not have his meal in a reclining position[5], or partake of meat or drink wine ; nor does he say Grace or arrange Zimmun, \n"

        ], 

        [

            "nor do others say Grace on his behalf or include him for Zimmun. He is likewise exempt from the reading of the Shema', from Tefillah, Tefillin, and all the commandments mentioned in the Torah. ", 

            "On the Sabbath, however, he may recline at his meal, eat meat and drink wine, say Grace and arrange Zimmun, and others may say Grace on his behalf and include him for Zimmun ; and he is under the obligation of reading the Shema' and Tefillah[1], and all the commandments mentioned in the Torah. ", 

            "Rabban Simeon b. Gamaliel[2] says :", 

            " Since he is under the obligation of these[3], he has obviously the obligation of them all ! ", 

            "And R. Johanan asked : ", 

            "What is the point of divergence between them[4]? The question of connubial intercourse[5]. ", 

            "It is here at any rate taught that [the mourner, although he is not in the same room as the body[6],] is exempt from reading the Shema', from Tefillah, Tefillin, and all the commandments mentioned in the Torah ! ", 

            "Rab Pappa replied :", 

            " [The Baraita] is to be interpreted as referring to one who turns his face from the body and eats[7]. ", 

            "Rab Ashe said : ", 

            "Since the duty of burying rests upon him, it is to be regarded as though the body was lying before him[8]; as it is said,", 

            " \"And Abraham rose up from before his dead\" (Gen. xxiii. 3) and it is said ", 

            "\"That I may bury my dead from before me\" (ibid. v. 4)[9], i.e. so long as the duty of burial rested upon him, it was as though the body was actually before him. ", 

            "He whose dead [is lying before him] is exempt, but [so it may The be inferred,] not the watcher[10]. But lo, there is a teaching : ", 

            "Who watches the body, although it is not his dead, is exempt from reading the Shema', from Tefillah, Tefillin, and all the commandments mentioned in the Torah ! ", 

            "\"Who watches the body, although it is not his dead\" [so stated the Baraita ; therefore it is to be inferred] if it is his dead, although he does not watch the body, [he is exempt].", 

            " If it be his dead or if he watches it, he is exempt ; but [so it may be inferred] one who walks in a cemetery is not ! But lo, there is a teaching :", 

            " A man must not walk in a cemetery with his Tefillin on his head or holding a scroll of the Torah and reading therein ; should he do so, he commits a transgression because of the injunction : \"Whoso mocketh the poor blasphemeth his Maker\" (Prov. xvii. 5)[1] !", 

            " In this latter case, within four cubits [of the grave] it ", 

            "is forbidden, but beyond that limit, he is under the obligation ; for the teacher has said : ", 

            "A dead body affects four cubits with regard to the reading of the Shema'. But here [in the case of a mourner or watcher], even beyond the limit of four cubits he is exempt. ", 

            "It was stated above [in the Baraita] :", 

            " \"Who watches the body, although it is not his dead, is exempt from reading the Shema', from Tefillah, Tefillin, and all the commandments mentioned in the Torah.\" ", 

            "Should there be two [watchers], they take it in turn to watch and read. ", 

            "Ben  Azzai says :", 

            " Should they be bringing the body in a boat, they place it in one corner and they both pray in another corner[2] ! ", 

            "What is the point of divergence between them ? ", 

            "Rabina said : ", 

            "They differ whether we have fear of mice [gnawing the body] ;", 

            " the former holds", 

            " there is such fear, the other ", 

            "there is not. ", 

            "Our Rabbis have taught :", 

            " He who is removing bones from one place to another must not put them into a saddle-bag and set them upon an ass and ride upon them, because this is disrespectful treatment ; ", 

            "but if he is afraid of heathens or robbers, he may do so[3]. What they say of bones applies also to a scroll of the Torah. ", 

            "To which [clause in this teaching does this last statement refer] ?", 

            " If to the first clause, it is self-evident ; for is a scroll of the Torah less than bones? ", 

            "Nay; it refers to the second clause[4]. ", 

            "Rahbah said in the name of R. Judah : ", 

            "Whoever sees a body [being conveyed to burial] and does not accompany it[5] commits a transgression because of [the injunction] \"Whoso mocketh the poor blasphemeth his Maker\" (Prov. xvii. 5). ", 

            "If he accompany it, what is his reward ? ", 

            "Rab Assi said : Of him the Scriptures state,", 

            " \"He that is gracious to the poor lendeth unto the Lord\" (ibid. xix. 17) and \"he that is gracious unto the needy honoureth Him\" (ibid. xiv. 31)[1].", 

            "R. Hiyya and R. Jonathan were conversing as they walked in a cemetery, and the \"fringes\" belonging to R. Jonathan fell upon the graves[2]. ", 

            "R. Hiyya said to him,", 

            "\"Lift them up, so that [the dead] shall not say, 'To-morrow they will come to us, but to-day they revile us'.\"", 

            " He asked him,", 

            " \"Do they know all that ; ", 

            "for lo, it is written,", 

            " 'The dead know not anything' (Eccles. ix. 5)?\" ", 

            "He answered,", 

            " \"If thou hast read [this verse], thou hast not read it a second time ; if a second time, then not a third time ; and if a third time, its meaning has not been explained to thee.", 

            " 'For the living know that they shall die' (ibid.) — this refers to the righteous who are called living even in their death ; as it is said, ", 

            "'And Benaiah the son of Jehoiada, the son of a living man[3] of Kabzeel, who had done mighty deeds, he smote the two altar-hearths of Moab ; he went down also and slew a lion in the midst of a pit in time of snow' (II Sam. xxiii. 20). "

        ], 

        [

            " — 'Son of a living man !' Are there, then, in the whole world sons [born of! dead men ?", 

            " But, 'son of a living man' [means] even in his death he is called 'living.' ", 

            "'Of Kabzeel, who had done mighty deeds' — [he is so described] because he multiplied and gathered labourers for the Torah[4].", 

            " 'He smote the two altar-hearths of Moab[5]' — i.e. he left nobody like him, neither [in the time of] the first Temple nor the Second Temple. 'He went down also and slew a lion in the midst of a pit in time of snow' — some say : ", 

            "He cut a hole in the ice into which he descended to bathe[6]; others say : He learnt the Sifra debe Rab[7] in a winter's day. ", 

            "'But the dead know not anything' — this refers to the wicked who are called dead in their life-time; as it is said,", 

            " 'And thou, O wicked one, thou art slain, the prince of Israel' (Ezek. xxi. 30)[1].\" ", 

            "Or if thou wilt, derive it from the following :", 

            "\"At the mouth of two witnesses, or three witnesses, shall the dead be put to death\" (Deut. xvii. 6). ", 

            "But he is alive !", 

            " Nay, ", 

            "he is accounted as dead from the beginning. ", 

            "The sons of R. Hiyya[2] went out on to the land[3]; their studies had been difficult for them, and they had had considerable trouble to remember them. ", 

            "One said to the other, ", 

            "\"Does our father[4] know of this trouble?\"", 

            " The other replied,", 

            " \"How should he know ? ", 

            "Lo, it is written, ", 

            "'His sons come to honour him, and he knoweth it not' (Job xiv. 21)!\" ", 

            "The first said to him, ", 

            "\"But does he not know ; ", 

            "for behold it is written,", 

            " 'But his flesh grieveth for him, and his soul mourneth over him' (ibid. v. 22)? And R. Isaac has said : ", 

            "The worm is as painful to the flesh of the dead as a needle in the flesh of the living !\" ", 

            "Some answer : ", 

            "The dead know of their own troubles, but not of the troubles of others. ", 

            "Do they not [know of the troubles of others]?", 

            " Lo, there is a teaching :", 

            " It once happened that a pious man gave a denarius[5] to a beggar on the New Year's eve in a time of drought. His wife upbraided him ; so he went and spent the night in the cemetery[6]. ", 

            "He heard two spirits conversing. One said to the other,", 

            " \"Come, friend, let us wander in the world and hear behind the curtain[7] what visitation is to come upon the world.\"", 

            "The other spirit replied, ", 

            "\"I cannot, because I am buried in a matting of reeds[8]; but go thou and report to me what thou hearest.\" ", 

            "She[9] went, and having wandered about returned. ", 

            "The other asked, ", 

            "\"What didst thou hear, friend, behind the curtain ?\" ", 

            "She replied,", 

            " \"I heard that if one sows in the first rainfall[10], the hail will smite it.\" ", 

            "This man thereupon went and sowed in the second rainfall. ", 

            "[The hail] destroyed everybody's crops but not his. ", 

            "The following year, he again spent the [New Year's] night in the cemetery, and heard the same two spirits conversing. ", 

            "One said to the other, ", 

            "\"Come, let us wander in the world and hear behind the curtain what visitation is to come upon the world.\" ", 

            "The other spirit replied,", 

            " \"Have I not told thee, friend,", 

            " that I cannot, because I am buried in a matting of reeds? ", 

            "But go thou and come and tell me what thou hearest.\" ", 

            "She went, and wandered about and returned. ", 

            "The other spirit asked, ", 

            "\"What didst thou hear behind the curtain ?\" ", 

            "She replied,", 

            " \"I heard that if one sows in the second rainfall, it will be smitten by the blast.\" ", 

            "This man went and sowed in the first rainfall. ", 

            "What everybody else sowed was smitten by the blast, but not his. ", 

            "His wife asked him, ", 

            "\"How is it that last year everybody's crop was destroyed by hail, but not thine ; and this year everybody's crop was blasted except thine ?\"", 

            " He told her the whole story. ", 

            "It is related ", 

            "that very soon afterwards a quarrel broke out between the wife of that pious man and the mother of the girl[1]. ", 

            "The former said to the other,", 

            " \"Come, I will show thee that thy daughter is buried in reed-matting.\" ", 

            "The following year the same man went and spent the [New Year's] night in the cemetery, and he heard those spirits conversing. ", 

            "One said,", 

            "\"Come, friend, let us wander in the world and hear behind the curtain what visitation is to befall the world.\"", 

            " The other replied,", 

            " \"Leave me alone, friend ; what has passed between me and thee has been overheard by the living.\" ", 

            "Infer from this that the dead do know !", 

            " [No ;] it is possible that some other person[2] died and went and informed them. ", 

            "Come and hear :", 

            " Ze'iri left a sum of money in charge of his landlady[3]. During the time he went to the school of his master and returned, she died. ", 

            "He followed her to the court of death[4]", 

            " and asked her,", 

            " \"Where is the money?\"", 

            " She replied, ", 

            "\"Go and take it from beneath the door-socket in such and such a place ; and tell my mother to send me my comb and tube of eye-paint[5] through so-and-so who will arrive here to-morrow,\" ", 

            "Conclude from this that the dead do know ! ", 

            "[No;] perhaps Dumah[1] informed [the dead] beforehand[2]. ", 

            "Come and hear :", 

            " The father of Samuel was entrusted with some money belonging to orphans. At the time that he passed away, Samuel was not with him. ", 

            "People afterwards called him, \"Son of the consumer of the orphans' money.\" ", 

            "He went after his father to the court of death ", 

            "and said to them[3], ", 

            "\"I want Abba.\"", 

            " They replied,", 

            " \"There are many of that name here.\" ", 

            "not translated. [He said to them]", 

            "\"I want Abba b. Abba.\" ", 

            "They answered, ", 

            "\"There are also many of that name here.\" ", 

            "He said to them,", 

            " \"I want Abba b. Abba, the father of Samuel ; where is he?\"", 

            " They answered, ", 

            "\"He has gone up to the heavenly seminary[4].\"", 

            " In the meantime he noticed Levi[5] who was seated apart.", 

            " He asked him, ", 

            "\"Why sittest thou apart? Why hast thou not gone up [to the heavenly seminary]?\"", 

            " He replied,", 

            " \"I was told, ", 

            "'The number of years thou didst not attend the seminary of R. Aphes and didst grieve him on that account, we will not permit thee to ascend to the heavenly seminary'.\"", 

            " In the meantime his father arrived ; and Samuel noticed that he wept and laughed.", 

            " He said to him, ", 

            "\" Why weepest thou?\"", 

            " He answered, ", 

            "\"Because thou wilt soon come here.\"", 

            " \"And why dost thou laugh?\"", 

            " \"Because thou art very highly thought of in this world.\" Samuel said to him,", 

            " \"If I am so esteemed, let them allow Levi to enter\" ; and they permitted him to enter. ", 

            "He asked him,", 

            "\"Where is the orphans' money ?\"", 

            " He answered, ", 

            "\"Go, take it from the enclosure of the mill. The upper and lower sums of money belong to us, the middle sum belongs to the orphans.\" ", 

            "He asked his father,", 

            " \"Why didst thou act in this manner?\"", 

            " He replied, ", 

            "\"Should thieves come to steal, they would steal ours ; should the earth destroy[6], it would destroy ours.\" ", 

            "Conclude from this that the dead do know[7]! ", 

            "[No ;] perhaps it was different with Samuel ; being a man so highly esteemed, it may have been announced in advance \"Make way for him.\" ", 

            "R. Jonathan likewise retracted[1]; for R. Samuel b. Nahmani said in the name of R. Jonathan :", 

            " Whence do we learn that the dead converse one with the other? ", 

            "As it is said, ", 

            "\"And the Lord said unto him[2], This is the land which I swore unto Abraham, unto Isaac, and unto Jacob, saying\" (Deut. xxxiv. 4). What means \"saying\"? The Holy One, blessed be He, spake to Moses,", 

            " \"Go, tell Abraham, Isaac and Jacob, The oath which I swore unto you have I fulfilled for your children.\" "

        ], 

        [

            " If thou shouldest imagine that they were not cognisant [of what transpires on earth], what use would it be to tell them ?", 

            " On the other hand,", 

            " if they were cognisant, what need was there for him to inform them ? ", 

            "To give the credit to Moses.  ", 

            "R. Isaac said : ", 

            "Whoever speaks [evil] of the dead is as though he spoke it of a stone. ", 

            "Some say that", 

            " they are not aware [of what is spoken], ", 

            "while others say ", 

            "they are aware but it does not trouble them. ", 

            "But it is not so ! ", 

            "For Rab Pappa[3] spoke ", 

            "[evil] of Mar Samuel [after his death], and a pole fell from the roof and split his skull !", 

            " It is different with a Rabbinical scholar, because the Holy One, blessed be He, defends his honour. ", 

            "R. Joshua b. Levi said :", 

            " Whoever talks [evil] after the bier of disciplas of the wise will fall into Gehinnom ; as it is said, ", 

            "\"But as for such as turn aside unto their crooked ways, the Lord will lead them away with the workers of iniquity. Peace be upon Israel\" (Ps. cxxv. 5) — i.e. even at a time when \"there is peace upon Israel,\" \"the Lord will lead them away with the workers of iniquity.\" ", 

            "It was taught by the school of R. Ishmael : ", 

            "If thou seest a scholar committing an offence at night, do not criticise him for it by day ; perhaps he has repented by then.", 

            " Dost thou imagine perhaps he has repented?", 

            " Nay, ", 

            "he has certainly repented. ", 

            "This refers[4] only to an offence concerned with his person ; but in a matter involving money, [he may be criticised] until he refunds it to its owner. ", 

            "R. Joshua b. Levi also said :", 

            " In twenty-four places [it is taught] that the Bet Din excommunicates a man for [lack of] respect to a teacher, and we learn them all in our Mishnah[1].", 

            " R. Eleazar asked him : ", 

            "Where [are they to be found]? ", 

            "He replied : ", 

            "Search and thou wilt find them. ", 

            "He accordingly went and searched and found three — ", 

            "Who despises the washing of the hands[2], who talks [evil] after the bier of the disciples of the wise, and who acts arrogantly towards the Most High. ", 

            "\"Who talks after the bier of disciples of the wise\" ; where is this to be found ? ", 

            "There is a Mishnaic teaching :", 

            " ['Akabya b. Mahalalel] used to say : We may not administer the waters of a woman suspected of adultery[3] to a female proselyte or freed woman ; ", 

            "but the Sages say : ", 

            "We may do so. ", 

            "And they said to him,", 

            " \"It happened with Karkemit, a [handmaid]", 

            "freed handmaid of Jerusalem, and Shemayah and Abtalion did administer the waters to her!\" ", 

            "'Akabya said to them,", 

            " \"It was for show that they made her drink[4].\"", 

            " Thereupon the Sages excommunicated him and he died under the ban, and the Bet Din stoned his coffin. ", 

            "\"Whoever despises the washing of the hands\" ; where is this found ?", 

            " There is a Mishnaic teaching : R. Judah said :", 

            " God forbid that we should suppose that 'Akabya b. Mahalalel was excommunicated, for the Temple-court[5] was not locked upon any man of Israel equal to him in knowledge, purity and fear of sin. But who was it they excommunicated? It was Eleazar b. Hanok, because he made light of the washing of the hands ; ", 

            "and when he died the Bet Din sent and placed a large stone upon his coffin,", 

            " to teach ", 

            "that whoever is excommunicated and dies under the ban, the Bet Din stones his coffin. ", 

            "\"Who acts arrogantly towards the Most High\" ; where is this to be found? ", 

            "There is a Mishnaic teaching : Simeon b. Shetah sent to Honi Hamme'aggel[6] : ", 

            "\"Thou art deserving of excommunication, and wert thou not Honi, I would pronounce the ban against thee ; but what can I do seeing that thou art petulant with the Omnipresent, and nevertheless He fulfils thy desires as a father gratifies a petulant child ; and concerning thee the Scriptures state, 'Let thy father and thy mother be glad, and let her that bore thee rejoice ' (Prov. xxiii. 25).\" Is there no other instance [of arrogance towards God]? ", 

            "Yes, there is;", 

            " for Rab Joseph has taught[1] :", 

            " Theodosius of Rome accustomed the Jews in Rome to eat kids roasted in their entirety[2] on the Passover night. ", 

            "They[3] sent him [the message] : ", 

            "\"If thou wert not Theodosius, I would have issued a ban against thee, for thou hast induced Israelites to eat the holy things outside [Jerusalem][4].\"", 

            " But we are speaking of instances mentioned in our Mishnah ; and this is a Baraita ! ", 

            "Is there none in the Mishnah ?", 

            " Yes, there is ; for there is a Mishnaic teaching : ", 

            "If one has cut [a portable earthenware oven] into layers and placed sand between each layer[5], R. Eliezer declares it clean, but the Sages declare it unclean ; and this is what is known as \"the oven of the serpent[6].\"", 

            " Why \"serpent\"?", 

            " Rab Judah said in the name of Samuel :", 

            " This teaches that the Sages wound it round with discussions as a serpent [winds itself round something] and proved that the oven was unclean. ", 

            "And there is a teaching :", 

            " That day they brought everything that R. Eliezer had proclaimed clean[7] and burnt it in his presence, and finally they excommunicated[8] him. ", 

            "Despite this, we have not learnt a case of excommunication in the Mishnah ! ", 

            "And where are the twenty-four places to be found[1]? ", 

            "R. Joshua b. Levi compares one thing with another[2], but R. Eleazar does not. ", 

            "The bearers of the bier and they who relieve them. ", 

            "Our Rabbis have taught :", 

            " We should not carry out a body [for burial] near the time of reading the Shema'[3] ; but if they have commenced to do so, we should not stop them. ", 

            "But it is not so ' ", 

            "For lo, Rab Joseph was borne out near the time of reading the Shema' ! ", 

            "With a highly esteemed man it is different ", 

            "Such as are before the bier and stich as are behind it. ", 

            "Our Rabbis have taught :", 

            " Those who are occupied with the funeral oration at the time when the body is lying before them should slip away one by one and read the Shema'; but if the body is not present, they sit and read the Shema' and the orator sits in silence ; they stand and say the Tefillah, and he justifies the divine decree, saying : ", 

            "\"Lord of the Universe, I have often sinned before Thee, and Thou hast not exacted punishment from me for one in a thousand. May it be Thy will, O Lord our God, to repair our breaches and the breaches of all Thy people, the house of Israel, in mercy.\"", 

            " Abbai said :", 

            " A man ought not to speak thus ; for R. Simeon b. Lakish said, and it has been similarly taught in the name of R. Jose : ", 

            "A man should not open his mouth to Satan[4]. ", 

            "Rab Joseph said : ", 

            "What is the Scriptural authority for this ? As it is said, ", 

            "\"We should have been as Sodom\" (Is. i. 9) ; and what did the prophet reply to them? \"Hear the word of the Lord, ye rulers of Sodom\" (ibid. v. 10). ", 

            "Having buried the dead and returned, etc. ", 

            "If they are able to begin and finish the whole, yes ; but if only one paragraph", 

            " or one verse, are they not [to commence it]?", 

            " Against this conclusion I quote :", 

            " Having buried the dead and returned, if they are able to begin and complete even one paragraph or one verse [they should commence it] ! ", 

            "Here likewise[5] it means that ...", 

            "if they are able to begin and finish one paragraph or even one verse, before reaching the row, they should begin ; but if not, they should not commence it.  "

        ], 

        [

            "As for those who stand in the row, etc. ", 

            "Our Rabbis have taught :", 

            " The row which looks upon the inner  space[1] is exempt [from reading the Shema']; but the row which does not look upon the inner space is under the obligation. R. Judah says : ", 

            "Those who come out of regard for the mourner are exempt ; but those who come on their own account[2] are under the obligation. ", 

            "Rab Judah said in the name of Rab : ", 

            "Who finds diverse kinds[3] in his garment must divest himself thereof even in the street. What is the reason ? [As it is said,] \"There is no wisdom nor understanding nor counsel against the Lord\" (Prov. xxi. 30) — i.e. wherever the Divine Name is liable to be profaned, we pay no respect to a teacher. ", 

            "Against this teaching is quoted : ", 

            "Having buried the dead, and on returning there are two paths before them one clean, the other unclean[4], if [the mourner] enters the clean path, they follow him there, and if he enters the unclean path, they follow him there out of respect for him[5]! ", 

            "Why should this be so? ", 

            "Let one say, ", 

            "\"There is no wisdom nor understanding nor counsel against the Lord\"!", 

            " R. Abba explained that it speaks here of a Bet Peras[6] which is declared unclean by the Rabbis[7]. ", 

            "For Rab Judah said in the name of Samuel : ", 

            "One may blow upon a Bet Peras [to see whether there are any bones ; and if there are none] he may walk on it[8]. ", 

            "And Rab Judah b. Ashe said in the name of Rab[9] :", 

            " A Bet Peras which has been much trodden under foot is to be regarded as clean. ", 

            "Come and hear : R. Eleazar b. Sadok[10] said : ", 

            "We used to leap upon the coffins of the dead to meet the kings of Israel[11], and not only to meet kings of Israel do they so permit, but even to meet the kings of other nations[1] ; for if he be worthy, he will discern between the kings of Israel and the kings of other nations.", 

            " Why should this be so?", 

            " Let one say,", 

            " \"There is no wisdom nor understanding nor counsel against the Lord\" !", 

            " It is in accord with the opinion of Raba[2], who said : ", 

            "According to the teaching of the Torah, \"a tent\" — i.e. anything which contains a hollow space at least a handbreadth in extent — forms a partition against uncleanness, but if it does not contain a hollow space at least a handbreadth in extent it does not form such a partition ; and most coffins have a hollow space a handbreadth in extent. But the Rabbis decreed that even those which have this hollow space [should defile] because of those which have it not ; but for the purpose of paying honour to royalty, the Rabbis do not enforce this decree. ", 

            "Come and hear : ", 

            "Great is the duty of honouring one's fellow-creatures, since it sets aside a prohibition enjoined by the Torah. ", 

            "Why should this be so?", 

            " Let one say, ", 

            "\"There is no wisdom nor understanding nor counsel against the Lord\" !", 

            " Rab b. Shaba explained it in the presence of Rab Kahana as referring to the prohibition, \"Thou shalt not turn aside from the sentence which they shall declare unto thee\" (Deut. xvii. 11).", 

            " They laughed at him,", 

            " for is not the prohibition, \"Thou shalt not turn aside\" enjoined by the Torah\" ! ", 

            "Rab Kahana said to them :", 

            " A great man having expressed an opinion, you should not laugh at him. We base the authority for all the dicta of the Rabbis upon the prohibition, \"Thou shalt not turn aside\" ; but for the duty of honouring a fellow-creature the Rabbis give permission[4]. ", 

            "Come and hear: ", 

            "[It is written :] \"And hide thyself from them\" (ibid. xxii. 1)[5]; i.e. there are times when thou mayest hide thyself from them, and times when thou must not hide thyself from them. ", 

            "How can this be? If he was a Kohen[1] and [the straying animal] was in a cemetery ; or he was an Elder and it was derogatory to his dignity [to be seen leading the animal back] ; or his work was more important than his neighbour's[2] — therefore it is said, ", 

            "\"And hide thyself.\" ", 

            "Why should this be so ? ", 

            "Let one say, ", 

            "\"There is no wisdom nor understanding nor counsel against the Lord[3]\"! ", 

            "It is different here ; for it is written,", 

            " \"And hide thyself from them[4].\"", 

            " May one, then, conclude from this[5]?", 

            " We cannot draw an inference about a prohibition from a case involving only financial loss[6]. ", 

            "Come and hear:", 

            " [It is written,] \"Or for his sister\" (Num. vi. 7)[7]. What has this teaching to tell us ? ", 

            "Supposing he[8] were on his way to sacrifice the Paschal lamb or circumcise his son[9], and he heard that one of his relatives had died, it is possible [to think] that he should turn back and render himself unclean ; say, then, he shall not make himself unclean. ", 

            "It is possible [to think] that in the same way that [under these conditions] he may not make himself unclean for his relatives, he may not make himself unclean for a Met Miswah,", 

            " therefore there is a teaching to tell us", 

            " \"or for his sister\" ; i.e. \"for his sister\" he may not render himself unclean, \n"

        ], 

        [

            "but for a Met Miswah he must defile himself. Why should this be so?", 

            " Let one say, ", 

            "\"There is no wisdom nor understanding nor counsel against the Lord[1]\"! ", 

            "It is different here; because it is written \"for his sister[2].\" May one, then, conclude from this ?", 

            " Sit and do nothing is different[3]. ", 

            "Rab Pappa asked Abbai : ", 

            "How were our predecessors different from us that miracles occurred for them but not for us? ", 

            "Is it a question of learning ? In the time of Rab Judah, their whole study was limited to the Order \"Damages[4],\" whereas we study the six Orders; ", 

            "and when Rab Judah reached", 

            " the paragraph in Mishnah 'Uksin[5] : \"If a woman presses vegetables in a pot\" (some declare it was the paragraph : \"Olives which are pressed with their leaves are clean\"), he said,", 

            " \"We see here the conflicts of Rab and Samuel[6],\" whereas we study 'Uksin in thirteen lessons[7] ! ", 

            "Yet, with respect to Rab Judah, when he took off one of his shoes[8], the rain descended ; but we afflict our souls and cry aloud and there is none that takes notice of us !", 

            " He replied : ", 

            "Our predecessors jeopardised their lives for the sanctification of the Name, but we do not. ", 

            "As it once happened with Rab Adda b. Ahabah who noticed a heathen woman[9] wearing a karbalta[10] in the street; thinking that she was an Israelite, he went up to her and tore it from off her.", 

            " It was then discovered that she was a heathen, and they fined him four hundred Zuzim.", 

            " He said to her,", 

            " \"What is thy name ?\" ", 

            "She replied, ", 

            "\"Matun.\"", 

            " He said, ", 

            "\"Matun, Matun, is worth four hundred Zuzim[1].\" ", 

            "Rah Giddel had the habit of going and sitting at the gate of the baths[2], saying [to the women as they entered],", 

            " \"Bathe thus and thus.\" ", 

            "The Rabbis said to him,", 

            "\"Is not the master afraid of [the promptings of] the evil impulse ?\"", 

            " He replied, ", 

            "\"They are in my eyes like white geese.\" ", 

            "R. Johanan had the habit", 

            " of going and sitting at the gates of the baths, saying, ", 

            "\"When the daughters of Israel leave, let them gaze upon me, and they will have children as beautiful as I[3].\"", 

            " The Rabbis said to him,", 

            " \"Art thou not afraid of the Evil Eye[4]?\" ", 

            "He answered,", 

            "\"I am come from the seed of Joseph against whom the Evil Eye had no power ; for it is written,", 

            " 'Joseph is a fruitful vine, a fruitful vine by a fountain' (Gen. xlix. 22) ; and R. Abbahu said: ", 

            "Read not 'ale 'ayin 'by a fountain' but 'ole 'ayin 'overcoming the [Evil] Eye'.\" ", 

            "R. Jose b. Hannina said : From the following passage [did R. Johanan derive his reason] :", 

            " \"And let them grow [weyidgu] into a multitude in the midst of the earth\" (ibid. xlviii. 16) ; i.e. as the fishes [dagim] in the sea are covered by the water and the Evil Eye has no power over them, ", 

            "in similar manner ", 

            "the Evil Eye has no power over the seed of Joseph. Or if thou wilt, say that the eye which desired not to partake of what did not belong to it[5] cannot be influenced by the Evil Eye. ", 

            "MISHNAH Women, slaves and minors are exempt from reading the Shema' "

        ], 

        [

            " and from Tefillin; but they are under the obligation of Tefillah, Mezuzah and Grace after meals. ", 

            "GEMARA Why are the reading of the Shema' and Tefillin different [from the others] ? ", 

            "Because they are commands[1] the observance of which depends upon a certain point of time, and women are exempt from all commands of this class. Tefillah, Mezuzah and Grace after meals, being commands the observance of which does not depend upon a certain point of time, are obligatory upon women[2]. That the reading of the Shema' [is not obligatory upon women] is self-evident, because it is a command the observance of which depends upon a certain point of time, and women are exempt from all commands of this class!", 

            " [Why, then, does the Mishnah mention it ?]", 

            " Thou mightest say that since it contains a reference to the Kingdom of Heaven [it should be read by women] ; therefore it informs us [they are exempt]. ", 

            "And from Tefillin. ", 

            "This too is evident !", 

            " Thou mightest say ", 

            "that since Tefillin are to be compared with Mezuzah[3] [they should be obligatory upon women] ; therefore it informs us [they are exempt]. ", 

            "But they are under the obligation of Tefillah ; ", 

            "[obviously] because this is prayer!", 

            "[not translated]", 

            " But thou mightest say that since it is written thereby, \"Evening and morning and at noonday\" (Ps. lv. 18), it is like a command the observance of which depends upon a certain point of time [and women are exempt]; therefore it informs us [the obligation is theirs]. ", 

            "And Mezuzah. This is evident !", 

            " But thou mightest say that", 

            " since it is to be compared with the study of Torah[4], [being exempt from the latter they are likewise exempt from the former] ; therefore it informs us [that women have the duty of fixing the Mezuzah]. ", 

            "And Grace after meals. ", 

            "This too is evident ! ", 

            "But thou mightest say that", 

            "since it is written thereby, \"When the Lord shall give you in the evening flesh to eat and in the morning bread to the full\" (Exod. xvi. 8), it is like a command the observance of which depends upon a certain point of time [and women are exempt]; therefore it informs us [that it is obligatory]. ", 

            "Rab Adda b. Ahabah said : ", 

            "Women are under the obligation to recite the Sanctitication [1] of the [Sabbath] day by the ordinance of the Torah. ", 

            "But why,", 

            " since it is a command the observance of which is dependent upon a certain point of time, and women are exempt from all commands of this class ! ", 

            "Abbai answered : ", 

            "[The Sanctification by women] is a Rabbinical ordinance. ", 

            "Rab said to him : ", 

            "But lo, [Rab Adda] mentioned it was \"by the ordinance of the Torah\" ! ", 

            "And further, let us make all commands [of this class] obligatory upon women by Rabbinic authority ! ", 

            "But, said Raba,", 

            " [the correct reason why they have to \"sanctify\" the Sabbath is because] the Scriptures declare, \"Remember the Sabbath day to keep it holy\" (Exod. xx. 8) and \"Observe the Sabbath to keep it holy\" (Deut. v. 12) — everyone who has to \"observe[2]\" must likewise \"remember[3]\"; and since women must \"observe,\" so must they \"remember.\" ", 

            "Rabina asked Raba :", 

            "Is the recital of the Grace after meals by women an ordinance from the Torah or the Rabbis ?", 

            " What is the point at issue ? It is whether they have the power of exempting others[4].", 

            " It is quite right if thou sayest it is from the Torah ; then one who is enjoined by the Torah [to keep the observance] comes and exempts one [whose observance is likewise commanded] by the Torah. But if thou sayest it is from the Rabbis, then it is not a compulsory observance, and one who is not under the obligation [to keep the observance] cannot exempt others. ", 

            "How is it then ?", 

            " Come and hear : It has indeed been stated : ", 

            "A son [who is a minor] may say Grace for his father, a slave for his master, and a woman for her husband ; ", 

            "but the Sages declare : ", 

            "May a curse alight upon the man for whom his wife or his son says Grace ! ", 

            "This[5] is quite right if thou sayest that it is from the Torah; then one who is enjoined by the Torah [to keep the observance] comes and exempts one [whose observance is likewise commanded] by the Torah. But if thou sayest it is from the Rabbis, then one who is enjoined by the Rabbis [to keep the observance] comes and exempts one [whose observance is commanded] by the Torah ! ", 

            "Also, according to thy reason, is a minor under the obligation [to say Grace][6] ? ", 

            "Nay, with what case are we here dealing ? With one who, for instance, has eaten the minimum quantity ordained by the Rabbis [as making the saying of Grace necessary][1] ; and thus one who is enjoined by the Rabbis [to say Grace][2] comes and exempts one [whose observance is likewise commanded] by the Rabbis[3]. ", 

            "Rab 'Awira expounded (sometimes he said it in the name of R. Ammi and sometimes in the name of R. Assi) :", 

            " The ministering angels spake before the Holy One, blessed be He,", 

            " \"Lord of the universe ! It is written of Thee in Thy Torah, 'Who regardeth not persons[4] nor taketh reward' (Deut. x. 17); but dost Thou not regard the person of Israel, for it is written, ", 

            "'The Lord lift up His countenance upon thee' (Num. vi. 26)?\" ", 

            "He replied to them, ", 

            "\"And should I not regard the person of Israel, ", 

            "for whom I wrote in the Torah, 'And thou shalt eat and be satisfied and bless the Lord thy God' (Deut. viii. 10), but they are strict with themselves [and bless] even with a quantity of food equal in size to an olive or an egg?\" ", 

            "MISHNAH A Ba'al Keri meditates upon [the wording of the Shema'] in his heart and says neither the benediction before nor after[5].", 

            " At his meal, he says the Grace after [in his heart] but not the Grace before.", 

            " R. Judah declares : ", 

            "He says Grace before and after. ", 

            "GEMARA Rabina said :", 

            " [The statement of the Mishnah] means to say that meditation is the equivalent of speech ;", 

            " for if it enter thy mind that it is not the equivalent of speech, ", 

            "why should he meditate! How is it then? Meditation is the equivalent of speech. Let him, then, utter the words with his lips !", 

            " No ; it is as we find at Mount Sinai[6]. ", 

            "But Rab Hisda said : ", 

            "Meditation is not the equivalent of speech ; ", 

            "for if it enter thy mind that it is the equivalent of speech, let him utter the words with his lips ! ", 

            "How is it then ? Meditation is not the equivalent of speech. Why, then, should he meditate? ", 

            "R. Eleazar said : ", 

            "So that the whole world should not be engaged upon the reading of the Shema', whereas he sits idle. ", 

            "Then let him read some other chapter !", 

            " Rab Adda b. Ahabah replied : ", 

            "With that wherewith the Community is engaged [should he like-wise be engaged].  "

        ], 

        [

            "But Tefillah is also a matter with which the  Community is engaged, and there is a Mishnaic teaching:", 

            " If he was standing in the Tefillah and recollected that he is a Ba'al Keri, he should not interrupt [his prayer] but shorten it[1]. The reason is because he had already commenced it ; hence, if he had not commenced it, he should not do so !", 

            " It is different with Tefillah, because it contains no reference to the Kingdom of Heaven. But in the Grace after meals there is also no reference to the Kingdom of Heaven, and yet our Mishnah declares : ", 

            "At his meal, he says the Grace after but not the Grace before ! ", 

            "Quite so ; ", 

            "but the reading of the Shema' and the Grace after meals are ordained by the Torah, whereas Tefillah is ordained by the Rabbis. ", 

            "Rab Judah said[2] : ", 

            "Whence is it that Grace after meals is ordained by the Torah? As it is said, ", 

            "\"And thou shalt eat and be satisfied and bless the Lord thy God\" (Deut. viii. 10). ", 

            "Whence is it that the benediction to be uttered before reading the Torah is ordained by the Torah[3]? As it is said,", 

            " \"For I will proclaim the name of the Lord : ascribe ye greatness unto our God\" (ibid. xxxii. 3)[4]. ", 

            "R. Johanan said : ", 

            "We derive the injunction to utter a benediction after reading the Torah from the Grace after meals by a fortiori argument, and the injunction to say Grace before meals from the benediction over the reading of the Torah by a similar method of reasoning. ", 

            "We derive the injunction to utter a benediction after reading the Torah from the Grace after meals by a fortiori argument :", 

            " If a meal which requires no benediction before it requires one after it, is it not right that the reading of the Torah, which does require a benediction before it, should require one after it ! ", 

            "And we derive the injunction to say Grace after meals from the benediction over the reading of the Torah by a similar method of reasoning : ", 

            "If the reading of the Torah, which requires no benediction after it[1], requires one before it, is it not right that a meal, which does require a benediction after it, should require one before it ! ", 

            "One can, however, object to this reasoning :", 

            " Why is Grace answered squired after a meal? Because it has been enjoyed[2]. Why is a benediction required over the reading of the Torah ? Because it is life eternal. ", 

            "Moreover there is a teaching in our Mishnah: ", 

            "At his meal, he says the Grace after but not the Grace before !", 

            " The refutation [remains unanswered]. ", 

            "Rab Judah said[3] :", 

            " If one is in doubt whether he has read the Shema' or not, he does not repeat it ; if he is in doubt whether he said \"True and firm[4]\" or not, he does repeat it.", 

            " What is the reason ? Because the reading of the Shema' is ordained by the Rabbis, but saying \"True and firm\" by the Torah. ", 

            "Rab Joseph quoted in objection :", 

            " \"When thou liest down and when thou risest up\" (Deut. vi. 7)[5]!", 

            " Abbai answered him: ", 

            "That is written with reference to words of Torah[6]. ", 

            "We have a teaching in our Mishnah : ", 

            "A Ba'al Keri meditates upon [the wording of the Shema'] in his heart and says neither the benediction before nor after. At his meal, he says the Grace after [in his heart] but not the Grace before. ", 

            "But if it enter thy mind that \"True and firm\" is ordained by the Torah, then he should say the benediction after the Shema' ! ", 

            "And for what reason should he say this benediction ? If because it contains a reference to the Exodus from Egypt[7], he has already mentioned that in the Shema'[8] !", 

            " Then let him say this benediction and there will be no necessity for the other[9] ! ", 

            "The reading of the Shema' is more important because it contains two things[10]. ", 

            "R. Eleazar said :", 

            " If one is in doubt whether he has read the Shema' or not, he should repeat it ; but if he is in doubt whether he has said the Tefillah or not, he need not repeat it. ", 

            "But R. Johanan said: ", 

            "Would that a man could pray all day[1]. ", 

            "Rab Judah also said in the name of Samuel :", 

            " If a man was standing in the Tefillah and recollected that he had already said it, he must stop even in the middle of a benediction. ", 

            "But it is not so ! ", 

            "For lo, Rab Nahman has said :", 

            " When we were at the school of Rabbah b. Abbuha we asked him, \"How is it with those young disciples who made a mistake and said the week-day Tefillah on the Sabbath, should they finish it[2]?\" ", 

            "And he replied, ", 

            "\"They should finish the whole of that benediction[3]\" !", 

            " Now is this analogy correct?", 

            " In the latter instance[4], he was at any rate under the obligation [to say the Tefillah] and the Rabbis did not trouble him out of regard for the Sabbath ; but in the former case[5], he had already said the prayer. ", 

            "Rab Judah also said in the name of Samuel : ", 

            "Should one have already said the Tefillah and then enter a Synagogue and find the Congregation saying it, if he is able to add anything new to the prayer, he may repeat it ; but if not, he should not repeat it.", 

            " It was necessary [to have both this and the former teaching of Rab Judah in the name of Samuel] ; ", 

            "for if he had given us only the first teaching, [we might have argued,] To whom does this apply ? To a person who said the Tefillah alone and is repeating it alone ;\n"

        ], 

        [

            " or to a person who said the Tefillah with the Congregation and is repeating it with the Congregation ; but having said it alone, he is like one who has not prayed when he finds himself with a Congregation ! Therefore he informs us [that having once said the Tefillah in private, there is no need to say it a second time with a Congregation], And if he had only given us the latter teaching,", 

            " [we might have supposed that he does not say the Tefillah a second time with the Congregation] because he has not actually commenced it; but in the former circumstance[6], having commenced it, therefore he should not [interrupt it on discovering his error] ! Consequently it was necessary [to have the first teaching of Rab Judah][1]. ", 

            "Rab Huna said : ", 

            "Should one enter a Synagogue and find the Congregation saying the Tefillah, if he is able to commence and finish before the Precentor reaches the words \"We give thanks unto Thee[2],\" he should say the Tefillah; but if not, he should not say it[3].", 

            " R. Joshua b. Levi said :", 

            " If he is able to commence and finish before the Precentor reaches the \"Sanctification[4],\" he should say the Tefillah ; but if not, he should not say it.", 

            " In what do they differ ?", 

            " The former is of the opinion", 

            " that the individual says the \"Sanctification[5],\" ", 

            "whereas the other is of the opinion", 

            " that the individual does not say it[6]. ", 

            "And similarly said Rab Adda b. Ahabah : ", 

            "Whence is it that the individual does not say the \"Sanctification\"? As it is said, ", 

            "\"But I will be hallowed among the children of Israel\" (Lev. xxii. 32) — i.e. anything which comes under the heading of \"Sanctification\" cannot be without a minimum of ten. ", 

            "How is this implied?", 

            " As Rabbanai, the brother of R. Hiyya b. Abba, taught : ", 

            "We draw an analogy from the occurrence of the word \"among[7].\"", 

            " It is written here,", 

            " \"But I will be hallowed among the children of Israel\" and it is written elsewhere", 

            " \"Separate yourselves from among this congregation\" (Num. xvi. 21). As in the latter circumstance there were ten[8], so here also there must be", 

            " ten. ", 

            "But everybody agrees that a man must not interrupt [the Tefillah in order to make the responses to the \"Sanctification\" or \"We give thanks\"].", 

            " The question was raised : ", 

            "May one interrupt [the Tefillah] to respond, \"Let His great name be blessed[9]\"? ", 

            "When Rab Dimai came [from Palestine] he reported that R. Judah and R. Simeon[1], disciples of R. Johanan, said: ", 

            "For no response may we interrupt [the Tefillah] except for \"Let His great name be blessed\"; for even one engaged with the study of the Ma'aseh Merkabah[2] must interrupt [to make this response]. ", 

            "But the Halakah is not in accord with their view. ", 

            "R. Judah declares : He says Grace before and after. ", 

            "That is to say that R. Judah is of the opinion that a Ba'al Keri is permitted to study Torah[3].", 

            " But lo, R. Joshua b. Levi has said :", 

            " Whence is it that a Ba'al Keri is forbidden to study Torah? As it is said, ", 

            "\"Thou shalt make them known unto thy children and thy children's children\" (Deut. iv. 9) ", 

            "and it continues,", 

            " \"The day that thou stoodest before the Lord thy God in Horeb\" (ibid. v. 10) — as those who were Ba'al Keri were forbidden [in the assembly at Horeb][4], so are they forbidden [to occupy themselves with Torah]. ", 

            "Shouldest thou say that ", 

            "R. Judah does not draw deductions from juxtaposition[5], but Rab Joseph has said : ", 

            "Even one who does not draw deductions from juxtaposition in any other part of the Torah does so in the Book of Deuteronomy; ", 

            "and R. Judah who does not draw deductions from juxtaposition in any other part of the Torah does so in the Book of Deuteronomy. ", 

            "How do we know that he does not use this method in any other part of the Torah ? For there is a teaching : Ben 'Azzai said :", 

            " It is stated, \"Thou shalt not suffer a sorceress to live\" (Exod. xxii. 17)[6] and it continues, ", 

            "\"Whosoever lieth with a beast shall surely be put to death\" (ibid. v. 18); ", 

            "[the Rabbis] connect the two laws to infer that as the one who lieth with a beast is put to death by stoning[7], so also is the sorceress put to death by stoning.", 

            " R. Judah said to him : ", 

            "Because the two matters are in juxtaposition, shall we inflict stoning upon the person [condemned for sorcery[8]] ! ", 

            "[No;] but ", 

            "they that divine by a ghost or a familiar spirit come under the category of sorcerers; and why are they particularised[1]? To draw an analogy and teach thee", 

            " that as these are punished by stoning, so also is the sorceress[2]. ", 

            "How do we know that R. Judah does draw deductions from juxta-position in the Book of Deuteronomy? For there is a teaching[3]: R. Eliezer says : ", 

            "A man may marry one outraged or seduced by his father, or one outraged or seduced by his son.", 

            " R. Judah prohibits a man to marry one outraged or seduced by his father. ", 

            "Rab Giddel asked in the name of Rab : ", 

            "What is R. Judah 's reason? Because it is written, ", 

            "\"A man shall not take his father's wife and shall not uncover his father's skirt\" (Deut. xxiii. 1) — i.e. the skirt which his father had seen shall he not uncover. But how do we know that this refers to one outraged by his father ? ", 

            "Because it is written in the preceding verse,", 

            " \"The man that lay with her shall give unto the damsel's father fifty shekels of silver\" (ibid. xxii. 29). ", 

            "They said : ", 

            "Yes, in the Book of Deuteronomy R. Judah does use this method of deduction[4]; ", 

            "but the consecutive verses [quoted above] are required for another teaching of R. Joshua b. Levi who says : ", 

            "Whoever teaches his son Torah, the Scriptures ascribe it to him as though he had received it from Mount Horeb ; as it is said, ", 

            "\"Thou shalt make them known unto thy children and thy children's children\" (Deut. iv. 9) and it continues,", 

            " \"The day that thou stoodest before the Lord thy God in Horeb\" (ibid. v. 10)[5]. ", 

            "There is a Mishnaic teaching : ", 

            "A man with a running issue who has experienced emission, a menstruous woman from whom the semen has escaped and a woman who during intercourse experiences the menstrual flow require immersion[6] ; ", 

            "but R. Judah exempts them therefrom.", 

            " Only in the case of a roan with a running issue who has experienced emission does R. Judah grant exemption, because he was not originally under the obligation to bathe ; but [it may be argued] a man who is merely a Ba'al Keri he does compel [to have immersion][1].", 

            " And shouldest thou say that in fact R. Judah even exempts a mere Ba'al Keri,", 

            " and the point of variance [between him and the Rabbis] is the man with a running issue who experienced emission, to show thee the extreme view taken by the Rabbis[2], I then quote the latter part of the Mishnaic teaching :", 

            " \"A woman who during intercourse experiences the menstrual flow requires immersion.\" ", 

            "For whom does he mention this ?", 

            " If it is supposed for the Rabbis, it is surely obvious ; since if a man with a running issue who experiences emission and originally was not under the necessity of bathing is compelled by the Rabbis to have immersion, how much more so a woman who experiences the menstrual flow during intercourse and originally was under the necessity of bathing ! ", 

            "Must it not be for R. Judah ?  But the statement is intended to apply to this case exclusively, viz. : "

        ], 

        [

            "a woman who experienced the menstrual flow during intercourse does not require immersion ; but a mere Ba'al Keri he does place under the obligation[3]. ", 

            "Do not read He says Grace but He meditates[4]. ", 

            "But does R. Judah hold that meditation [is sufficient] ?", 

            " For lo, there is a teaching :", 

            " A Ba'al Keri who has no water in which to bathe should read the Shema', but without the benediction before and after ; and he eats his meal with Grace after but not before, but he meditates [upon the Grace before meals] in his heart without uttering it with his lips. These are the words of R. Meir ;", 

            " but R. Judah says :", 

            " He should utter them both[5]!", 

            " Rab Nahman b. Isaac said : ", 

            "R. Judah treats the Grace before and after meals like the Halakot of Derek Eres[6]; ", 

            "for there is a teaching: ", 

            "\"Thou shalt make them known unto thy children and thy children's children\" (Deut. iv. 9) and it continues, \"The day that thou stoodest before the Lord thy God in Horeb\" (Deut. iv. 10) — as [the Israelites stood at Horeb] with dread and fear aod trembling and shaking, so here [when teaching Torah] must it be with dread and fear and trembling and shaking.", 

            " Hence [the Rabbis] said :", 

            " Men with a running issue, lepers and those who have had intercourse with menstruous women are permitted to read the Pentateuch, the Prophets and the Hagiographa[1], to study Mishnah, Midrash[2], Talmud, Halakot and Aggadot ; but those who are Ba'al Keri are forbidden[3].", 

            " R. Jose says : ", 

            "The Ba'al Keri may study what is familiar to him[4], but he must not expound the Mishnah.", 

            " R. Jonathan b. Joseph says :", 

            " He may expound the Mishnah but not the Talmud. ", 

            "R. Nathan b. Abishalom says : ", 

            "Also the Talmud may he expound, but he must not pronounce the name of God when it occurs[5]. ", 

            "R. Johanan the Sandal-maker, disciple of R.'Akiba, said in the name of R.'Akiba : ", 

            "Such a man should not enter upon study at all. Another version of this statement is : ", 

            "Such a man should not enter a House of Study at all. ", 

            "R. Judah says : ", 

            "He may study the Halakot of Derek Eres. ", 

            "It once happened that R. Judah, who had experienced emission, was walking by the river, ", 

            "and his disciples said to him,", 

            " \"Master, teach us a chapter of the Halakot of Derek Eres[6].\"", 

            " He descended into the water, bathed, and then taught them.", 

            " They said to him, ", 

            "\"Hast thou not taught us. Master, ", 

            "that such an one may study the Halakot of Derek Eres?\" ", 

            "He replied,", 

            " \"Although I am lenient by permitting others, I take a stricter view with myself.\" ", 

            "There is a teaching : R. Judah b. Batyra used to say :", 

            " The words of Torah do not contract defilement[7].", 

            " It happened that a disciple was speaking indistinctly over against R. Judah b. Batyra[8]. ", 

            "He said to him :", 

            " My son, open thy mouth and let thy words issue forth clearly, ", 

            "because words of Torah cannot contract defilement; as it is said, \"Is not My word like a fire? saith the Lord\" (Jer. xxiii 29) — as fire does not contract defilement, so also words of Torah do not contract defilement. ", 

            "The teacher stated above :", 

            " \"He may expound the Mishnah but not the Talmud.\" ", 

            "This supports the statement of R. El'ai,", 

            " for R. El'ai declared that Rab Aha b. Jacob[1] said in the name of our master[2] : ", 

            "The Halakah is that he may expound the Mishnah but not the Talmud.", 

            " This is as the Tannaim [taught] :", 

            " He may expound the Mishnah but not the Talmud ; these are the words of R. Meir.", 

            " R. Judah b. Gamaliel says in the name of R. Hannina b. Gamaliel : ", 

            "Both of them are forbidden ;", 

            " but [the Rabbis] said to him : Both of them are permitted.", 

            " He who says both are forbidden agrees with R. Johanan the Sandal-maker; and he who says both are permitted agrees with R. Judah b. Batyra. ", 

            "Rab Nahman b. Isaac said : The world acts in conformity with the following three Elders[3]: ", 

            "according to R. El'ai in the matter of the first-shorn wool[4]; according to R. Josiah in the matter of diverse seeds ; according to R. Judah b. Batyra in the matter of words of Torah. According to R. El'ai in the matter of the firstshorn wool — for there is a teaching :", 

            " R. El'ai says : ", 

            "The law of the first-shorn wool applies only in the [Holy] Land. ", 

            "According to R. Josiah in the matter of diverse seeds — for there is a teaching[5]: ", 

            "[not translated] R. Josiah says : ", 

            "A man is not guilty [of the infraction of this law] until he sows wheat, barley and kernels with one throw of the hand. ", 

            "According to R. Judah b. Batyra in the matter of words of Torah — for there is a teaching : R. Judah b. Batyra says : ", 

            "Words of Torah cannot contract defilement. ", 

            "When Ze'iri came [from Palestine] he said : ", 

            "The Rabbis have abolished immersion[6]. Another version is : [he said :] ", 

            "The Rabbis have abolished the washing of the hands.", 

            " He who says, \"The Rabbis have abolished immersion\" agrees with the view of R. Judah b. Batyra.", 

            " He who says, \"The Rabbis have abolished the washing of the hands\" is in accord with Rab Hisda who cursed the man who went looking for water at the time of prayer[7]. ", 

            "Our Rabbis have taught : ", 

            "A Ba'al Keri upon whom nine Kabs of water have been poured becomes clean.", 

            " Nahum, the man of  Gam Zu[1], whispered this to R. 'Akiba, who whispered it to Ben 'Azzai. Ben 'Azzai went out and taught it to his disciples publicly. ", 

            "Two Palestinian Amoraim, R. Jose b. Abin and R. Jose b. Zebida, differ on this matter ; ", 

            "one stating that Ben 'Azzai taught it, the other that he whispered it.", 

            " He who states that he taught it, because of the nullifying of Torah and procreation[2] ; ", 

            "he who states that he whispered it, so that disciples of the wise should not be constantly found in the company of their wives like cocks [with the hens][3]. ", 

            "R. Jannai said :", 

            " I have heard that some take a lenient view[4] and others a stricter view ; but whoever applies the stricter rule to himself, his days and years will be prolonged for him. ", 

            "R. Joshua b. Levi said : ", 

            "What is the purpose of those [who are Ba'al Keri] who bathe in the morning ?", 

            " What is their purpose !", 

            " And it was he who said that", 

            " a Ba'al Keri is forbidden to be engaged with words of Torah[5] !", 

            " Nay, this is what he means to say : ", 

            "What is their purpose in using forty Saot of water, ", 

            "when it is possible [to become clean] with nine Kabs? What is their purpose in undergoing complete immersion when ", 

            "it is possible [to become clean] with water poured over one ? ", 

            "R. Hannina replied :", 

            " They have erected a great fence[6] thereby; for there is a teaching : ", 

            "Once a man solicited a woman for an immoral purpose, ", 

            "and she said to him,", 

            " \"Thou good-for-nothing[7]! ", 

            "Hast thou forty Saot of water in which to immerse?\" ", 

            "He immediately left her. ", 

            "Rab Huna said to the Rabbis,", 

            " \"My masters, why do you make light of this immersion[8]? ", 

            "Is it because of the cold ? It is possible [to fulfil the requirements] in the baths[9]!\"", 

            " Rab Hisda asked him, ", 

            "\"Is it then right to have immersion in warm water ?\" ", 

            "He replied, ", 

            "\"Rab Adda b. Ahabah is of the same opinion as thou[1].\" ", 

            "R. Zera was sitting in a tub in a bath-house. ", 

            "He said to his attendant,", 

            " \"Go, bring me nine Kabs of water and dash them over me.\" ", 

            "R. Hiyya b. Abba[2] said to him,", 

            " \"Why does the master require all that when he is sitting in the midst of water ?\"", 

            " He replied,", 

            " \"It is like the regulation of forty Saot. ", 

            "Just as forty Saot", 

            " are necessary for immersion but not pouring, so are nine Kabs necessary for pouring but not immersion.\" ", 

            "Rab Nahman ordered a pitcher of the capacity of nine Kabs[3]. ", 

            "When Rab Dimai came [from Palestine], he said : R. 'Akiba and R. Judah the locksmith[4] declared :", 

            " The teaching [that nine Kabs may be poured over a Ba'al Keri to cleanse him] is meant to apply only to a delicate person who experienced the emission involuntarily ; but for a delicate person who caused it to happen, forty Saot are necessary. ", 

            "Rab Joseph said : ", 

            "Rab Nahman's pitcher is broken[5].", 

            " When Rabin came he said : ", 

            "Such a case happened in Usha[6] "

        ], 

        [

            " in the ante-room of R. Osha'ya, and they came and consulted  Rab Assi[7]. He said to them : ", 

            "The teaching [about the nine Kabs] was meant to apply only to a delicate person who caused it to happen ; but the delicate person who experienced it involuntarily was exempt therefrom altogether. ", 

            "Rab Joseph said ; ", 

            "Rab Nahman's pitcher is repaired[8]. ", 

            "Note that all the Amoraim and Tannaim are at variance over the ordinance of Ezra, so let us see how Ezra ordained it. ", 

            "Abbai said :", 

            " Ezra ordained forty Saot for a healthy person whose emission was voluntary and nine Kabs for a healthy person when it was involuntary.", 

            " Then came the Amoraim and differed as to a person indelicate health[1]. ", 

            "Some were of the opinion that", 

            " the delicate person whose emission was voluntary is like the healthy man whose emission was voluntary [and requires forty Saot], and the delicate person when it was involuntary like the healthy man when it was involuntary [and requires nine Kabs].", 

            " Others, however, were of opinion that", 

            " the delicate person whose emission was voluntary is like a healthy man whose emission was involuntary [and requires nine Kabs], and the delicate person when it was involuntary is exempt therefrom altogether. ", 

            "Raba said :", 

            " Granted that Ezra instituted immersion ; did he, then, institute the pouring of water?", 

            " For lo, the teacher said,", 

            " \"Ezra instituted immersion for those who are Ba'al Keri[2]\" !", 

            " But, said Raba,", 

            " Ezra instituted immersion in forty Saot for a healthy person whose emission was voluntary,", 

            " and then the Rabbis came and instituted [the pouring of] nine Kabs for a healthy man when it was involuntary.", 

            " After that the Amoraim[3] came and differed as to what was to be done to a person in delicate health. ", 

            "Some were of opinion that ", 

            "the delicate person whose emission was voluntary was like a healthy man when it was voluntary [and required immersion], and a delicate person when it was involuntary like a healthy person when it was involuntary [and required pouring]. ", 

            "Others, however, were of opinion that", 

            " the healthy person when it was voluntary required forty Saot ; and the delicate person when it was voluntary, like the healthy man when it was involuntary, required nine Kabs; but a delicate person whose emission was involuntary was exempt therefrom altogether.", 

            " Raba said :", 

            " The Halakah is — Both the healthy man and the delicate person when it is voluntary require forty Saot ; the healthy man when it is involuntary requires nine Kabs; but the delicate person when it is involuntary is exempt therefrom altogether. ", 

            "Our Rabbis have taught: ", 

            "A Ba'al Keri upon whom nine Kabs of water have been poured becomes clean. ", 

            "Of what does this speak ? [If he wishes to study Torah] for himself; but [if he wishes to teach it] to others, forty Saot are necessary. ", 

            "R. Judah says that", 

            " in every case forty Saot [are required]. ", 

            "R. Johanan and R. Joshua b. Levi, and R. Eleazar[1] and R. Jose b. R. Hannina—one of the first pair is at variance with one of the second pair on the interpretation of the first part of this teaching. ", 

            "One says :", 

            " The statement, \"Of what does this speak? [If he wishes to study Torah] for himself; but [if he wishes to teach it] to others, forty Saot are necessary\" is intended to apply only to a delicate person whose emission was voluntary, but nine Kabs suffice him when it was involuntary. ", 

            "The other says : ", 

            "Whoever [wishes to teach Torah] to others, even if he be a delicate person whose emission was involuntary, [cannot be regarded as clean] until there have been forty Saot. ", 

            "And one of the first pair is at variance with one of the second pair on the latter part of the teaching. ", 

            "One says :", 

            "The statement, \"R. Judah says that in every case forty Saot are required\"", 

            " is intended to apply only [to water found] in the ground[2], but not [to water] in vessels[3].", 

            " The other says :", 

            " It applies even [to water] in vessels.", 

            " It is quite right for him who says, \"It applies even [to water] in vessels,\" for that is what has been stated, ", 

            "viz. : \"R. Judah says that in every case forty Saot are required\" ; ", 

            "but for him who says, \"In the ground, yes, but in vessels, no,\" what does the phrase \"in every case\" include?", 

            " It is to include drawn water[4]. ", 

            "Rab Pappa and Rab Huna b. R. Joshua and Raba b. Samuel dined together. ", 

            "Rab Pappa said to them, ", 

            "\"Permit me to say Grace[5], because nine Kabs have been poured over me.\" ", 

            "Raba b. R. Samuel said to them, \"We have learnt:", 

            " 'Of what does this speak? [If he wishes to study Torah] for himself [nine Kabs are sufficient] ; but [if he wishes to teach it] to others, forty Saot are necessary[6].' ", 

            "So permit me to say Grace, because forty Saot have been poured over me\" [by means of immersion]. ", 

            "Rab Huna said to them, ", 

            "\"Permit me to say Grace, since I have had need neither of the one nor the other.\" ", 

            "Rab Hamma used to bathe on the day preceding Passover[7] in order to exempt others from their obligation. ", 

            "But the Halakah is not in accord with their view[8]. ", 

            "MISHNAH If he was standing in the Tefillah and recollects that he is a Ba'al Keri, he should not interrupt [his prayer] but shorten it.", 

            " If he had gone down to bathe, should he have time to ascend, clothe himself and read [the Shema'] before sunrise, he must ascend, clothe himself and read ; but if not, he should immerse his body in the water and read. ", 

            "He may not immerse himself in evil-smelling water, nor water of soaking[1], until he has poured [fresh] water therein. ", 

            "To what distance must he remoce himself from it[2] and excrement [if he wishes to read the Shema'] ? Four cubits. ", 

            "GEMARA Our Rabbis have taught :", 

            " If a man was standing in the Tefillah and recollects that he is a Ba'al Keri, he should not interrupt [his prayer] but shorten it.", 

            " If he was reading in the Torah[3] and recollects that he is a Ba'al Keri, he should not interrupt and go away, but should continue reading with hurried pronunciation of the words.", 

            " R. Meir says : ", 

            "A Ba'al Keri is not permitted to read more than three verses in the Torah. ", 

            "There is another teaching : ", 

            "If a man was standing in the Tefillah and saw some excrement opposite him, he should step forward until he has left it behind him a distance of four cubits. ", 

            "There is, however, a teaching", 

            " [that in these circumstances he should step] sideways!", 

            " There is no contradiction; ", 

            "[he should step forward] when that is possible, and [sideways] when he cannot do the other.", 

            " If a man was reciting the Tefillah and found excrement where he was standing, Rabbah said : ", 

            "Even if he himself was responsible for it, his Tefillah is valid. ", 

            "Raba retorted : ", 

            "But lo [it is written], \"The sacrifice of the wicked is an abomination\" (Prov. xxi. 27)!", 

            " Therefore, said Raba, ", 

            "since he is responsible [for the excrement], although he has uttered the prayer, his Tefillah is an abomination[4]. ", 

            "Our Rabbis have taught :", 

            " If he was standing in the Tefillah and the urine began to drip upon his knees, ", 

            "he should interrupt [his prayer] until it ceases and then repeat the Tefillah. ", 

            "To what point does he return?", 

            " Rab Hisda and Rab Hamnuna [differ]. One says that ", 

            "he recommences from the beginning;", 

            " the other says that ", 

            "he goes back only to the place where he stopped.", 

            " One may suppose that the following is the point of divergence : "

        ], 

        [

            " One is of opinion ", 

            "that if the man has waited sufficient time to finish the remainder of the Tefillah, he should recommence from the beginning. ", 

            "The other is of opinion that ", 

            "[in any event] he should go back only to the point where he stopped. ", 

            "Rab Ashe said : The phrase \"If the man has waited\"", 

            " must be altered to \"If the man has not waited\"; ", 

            "because everybody agrees that if he waited sufficient time to finish the remainder of the Tefillah, he recommences from the beginning; but the point of divergence there [between Rab Hisda and Rab Hamnuna] is the case where the man did not wait. ", 

            "One is of the opinion that ", 

            "the man was in an uncomfortable state and unfit [to pray], and therefore his Tefillah is invalid; ", 

            "while the other is of opinion that", 

            " the man was fit [to pray] and his Tefillah is valid. ", 

            "Our Rabbis have taught :", 

            " If a man feels the need to relieve himself, he should not say the Tefillah; and if he does, his prayer is an abomination. ", 

            "Rab Zebid (another version : Rab Judah) said : ", 

            "This teaching is meant to apply only to one who is unable to contain himself; but if he is able to contain himself, his Tefillah is valid. ", 

            "But for how long [must one be able to contain himself before venturing to say the Tefillah]? ", 

            "Rab Sheshet said : ", 

            "[Sufficient time to enable one to walk] a Parsah. ", 

            "There are some who make [this statement of Rab Zebid] a part of the Baraita [quoted above ; thus :] ", 

            "Of what does this speak[1]? Of a case where a man is unable to contain himself; but if he is able to contain himself, his Tefillah is valid.", 

            "But for how long [must one be able to contain himself before venturing to say the Tefillah]?", 

            " Rab Zebid said : ", 

            "[Sufficient time to enable one to walk] a Parsah. ", 

            "R. Samuel b. Nahmani said in the name of R. Jonathan :", 

            " If a man feels the need to relieve himself, he should not say the Tefillah; because it is said, ", 

            "\"Prepare to meet thy God, O Israel\" (Amos iv. 12). ", 

            "R. Samuel b. Nahmani also said in the name of R. Jonathan : ", 

            "What means that which is written, \"Guard thy foot when thou goest to the house of God\" (Eccles. iv. 17)? Guard thyself so that thou sinnest not; but if thou sinnest, bring an offering into My presence. ", 

            "\"And be ready to hearken \" (Eccles. iv. 1 7) — ", 

            "Raba said : ", 

            "Be ready to hearken to the words of the Sages ; for if they sin, they bring an offering and repent.", 

            " \"It is better than when fools give sacrifices\" (ibid.) — be not like the fools who sin and bring an offering without repenting. ", 

            "\"For they know not to do evil \" (ibid.)[1] — if so, they are righteous ! Nay, [the meaning is :] ", 

            "Be not like the fools who sin and bring an offering and know not whether they bring it for the good [they have done]", 

            " or for the evil [they have committed]. ", 

            "The Holy One, blessed be He, says, ", 

            "\"They are unable to discern between good and evil, and they bring an offering into My presence!\"", 

            " Rab Assi[2] (another version: Rab Hannina b. Pappa)[3] said: ", 

            "Take heed to thy orifices[4] at the time when thou standest in prayer before Me[5]. ", 

            "Our Rabbis have taught: When one is about to enter a privy, he should divest himself of the Tefillin at a [minimum] distance of four cubits and then enter, ", 

            "Rab Aha b. Rab Huna said in the name of Rab Sheshet: ", 

            "This teaching applies only to a regular privy[6], but with an occasional one, he may divest himself [of the Tefillin] and at once proceed to relieve himself;", 

            " and when he comes out, he walks a distance of four cubits and relays them, because he has [by his use thereof] made it a regular privy. ", 

            "The question was raised :", 

            " May a man, wearing his Tefillin, enter a regular privy for the purpose of urinating? ", 

            "Rabina permitted it; Rab Adda b. Mattena prohibited it. ", 

            "The question was put to Raba, and he replied :", 

            " It is forbidden, because we are afraid that he may relieve himself otherwise while wearing them. ", 

            "Another version is : ", 

            "[We are afraid] that he may break wind while wearing them. ", 

            "There is a further teaching : ", 

            "When one is about to enter a regular privy, he divests himself of the Tefillin at a [minimum] distance of four cubits, leaves them on the window-sill which is near the public road, and then enters. When he comes out, he walks a distance of four cubits and relays them. These are the words of Bet Shammai. ", 

            "Bet Hillel declare that", 

            " he may hold them in his hand and enter. ", 

            "R. 'Akiba says : ", 

            "He holds them in his garment and enters.", 

            " In his garment, dost thou imagine? ", 

            "He may sometimes forget them and they will fall !", 

            " But say that", 

            " he holds them in his garment with his hand and enters, leaving them in a hole near the privy,", 

            " but not in a hole near the public road, lest some passer-by take them and it lead him into suspicion. ", 

            "For it once happened that a disciple left his Tefillin in a hole near the public road. A harlot came and took them, and then went to the House of Study and said, ", 

            "\"Look what so-and-so gave me as my hire.\"", 

            " When the disciple heard that, he went to the top of the roof, threw himself therefrom and died. ", 

            "On that occasion it was ordained that a man should hold the Tefillin in his garment with his hand and enter. ", 

            "Our Rabbis have taught :", 

            " At first people used to leave the Tefillin in holes near the privy, but mice came and carried them away ;", 

            " therefore it was ordained that they should be left on window-sills near the public road ; but because passers-by used to take them,", 

            " it was ordained that they should hold them in their hand and enter. ", 

            "R. Meyasha, the grandson[1] of R. Joshua b. Levi, said : ", 

            "The Halakah is — One should roll them up like a book[2] and hold them in his right hand opposite his heart. ", 

            "Rab Joseph b. Minyomi said in the name of Rab Nahman :", 

            " This is so, provided that the strap does not protrude from beneath his hand a handbreadth.", 

            " R. Jacob b. Aha said in the name of R. Zera : ", 

            "This teaching only applies when there is still sufficient time left in the day to relay them; but if not, ", 

            "he should make for them a kind of bag, a handbreadth in size, and place them therein[3]. ", 

            "Rabbah b. Bar Hannah said in the name of R. Johanan : ", 

            "During the day he rolls them up like a kind of book and places them in his hand opposite his heart, but at night he makes for them a kind of bag, a handbreadth in size, and places them therein. ", 

            "Abbai said : ", 

            "This teaching only applies when the bag is reserved for that purpose ; but if it is not reserved for that purpose, it may be even less than a handbreadth in size. ", 

            "Mar Zotra (another version: Rab Ashe) said : ", 

            "Thou mayest infer that this is so from the fact that small vessels[4] protect [the contents from contracting defilement] in the tent of the dead. ", 

            "Rabbah b. Bar Hannah also said : ", 

            "At the time that we were following R. Johanan[1], on desiring to enter a privy, if he carried a book of Aggadta, he handed it to us; but if he carried Tefillin, he did not hand them to us. He said,", 

            " \"Since the Rabbis permit it, "

        ], 

        [

            " I will retain them[2].\" ", 

            "Raba said : ", 

            "At the time that we were following Rab Nahman, if he carried a book of Aggadta, he handed it to us before entering a privy; if he carried Tefillin, he did not hand them to us. He said,", 

            " \"Since the Rabbis permit it, I will retain them.\" ", 

            "Our Rabbis have taught : ", 

            "A man should not hold the Tefillin in his hand, or a scroll of the Torah on his arm and say his prayers[3]. He may not urinate while holding them, or sleep with them, neither a regular sleep nor a chance sleep. ", 

            "Samuel said: ", 

            "A knife, money, a dish and a loaf come under the same rule. ", 

            "Raba said in the name of Rab Sheshet : ", 

            "The Halakah is not in accord with the above Baraita[4] because it emanates from Bet Shammai[5];", 

            " for if it emanated from Bet Hillel, since one is allowed to enter a regular privy [holding the Tefillin][6], how much more so a chance one[7]! ", 

            "It is quoted in objection: ", 

            "\"What I have permitted thee in one place I have forbidden thee in another, [and this is an argument a fortiori which cannot be refuted\"][8] — does this not refer to the Tefillin? ", 

            "It is quite right if thou sayest that the above Baraita emanates from Bet Hillel; for then I have permitted thee elsewhere[6] [to enter] a regular privy [with Tefillin], but here I forbid thee [to enter] a chance privy ! ", 

            "On the other hand, if thou sayest that it emanates from Bet Shammai, they do not permit it in either case[9] ! ", 

            "To what, then, does the quoted statement refer? To the question of one handbreadth or two. ", 

            "For one teacher states :", 

            " When a man relieves himself, he should uncover himself one hand-breadth behind[1] and two in front[2]; ", 

            "and there is another teaching: ", 

            "He should uncover himself one handbreadth behind and not at all in front. ", 

            "It may be taken that both these teachings apply to a male[3], ", 

            "and there is no contradiction : ", 

            "the former referring to the major function of nature, the other to the minor. ", 

            "But how canst thou understand it in this way? ", 

            "For if the second teaching refers to the minor function, why uncover a handbreadth behind ? ", 

            "Nay ; they should both be referred to the major function, and there is no contradiction : ", 

            "the first teaching applying to a male, the other to a female[4].", 

            " If this be so, that which is mentioned in the sequel, ", 

            "viz. \"This is an argument a fortiori which cannot be refuted\" — what means it cannot be refuted?", 

            " It is a natural proceeding[5]! ", 

            "Quite so; [therefore the quoted statement must refer to] the Tefillin, and the refutation of Raba in the name of Rab Sheshet remains unanswered. ", 

            "Nevertheless there is a difficulty:", 

            " Since it is permitted to enter a regular priyy [with Tefillin], should it not be all the more permissible to enter a chance privy[6]! ", 

            "But this is what he means to say: ", 

            "They permit a regular privy[7] where there is no splashing [of urine likely to defile the hand which holds the Tefillin], but they prohibit a chance privy where there is this likelihood[8].", 

            " If so, why does it mention \"[This is an argument a fortiori] which cannot be refuted \"?", 

            " [What has just been said] is an excellent refutation ! ", 

            "But this is what he means to say :", 

            " This question [of carrying Tefillin in a regular privy but not a chance one] thou mayest argue with a reason[9]; but thou must not argue it by means of a fortiori deduction[1], for if thou usest this method of argument, it is an argument which cannot be refuted. ", 

            "Our Rabbis have taught : ", 

            "Who wishes to partake of a regular meal[2] should walk a distance of four cubits ten times, or a distance of ten cubits four times[3], and relieve himself ; after that he should enter [the dining-room]. ", 

            "R. Isaac said : ", 

            "Who is about to partake of a regular meal should first divest himself of his Tefillin and after that enter[4]. This is at variance with the opinion of R. Hiyya, who says: ", 

            "He leaves them upon his table, and thus it is becoming of him to do. ", 

            "How long [should he leave them there] ?", 

            " Rab Nahman b. Isaac said :", 

            " Until the time of saying Grace. ", 

            "One teacher stated : ", 

            "A man may tie up his Tefillin with liis money[5] in his underwear[6]. But there is another teaching :", 

            " A man may not do so !", 

            " There is no contradiction. The latter refers to one who has assigned [a place in his underwear in which to deposit his Tefillin]; the other refers to a man who has not assigned such a place. ", 

            "For Rab Hisda said :", 

            " In the cloth in which one assigns to tie up his Tefillin one must not tie up coins, if he has already placed the Tefillin therein. If he assigned to tie up his Tefillin in it but has not bound them therein, or if he has bound up his Tefillin in the cloth without such assignment, he may tie up money therein. ", 

            "But according to Abbai who said that the assignment is the criterion, if he assigned to deposit his Tefillin in the cloth, although he has not actually done so — ", 

            "or having bound them therein, if he thereupon assign it for the purpose — then it is forbidden [to tie up money therein] ; but if he has not made that assignment, it is not [forbidden]. ", 

            "Rab Joseph b. Rab Nehunyah[7] asked Rab Judah: ", 

            "May a man place his Tefillin beneath his pillow [at night] ? ", 

            "About placing them at the foot of the bed is no question, since that would involve disrespectful treatment; but I ask about placing them beneath his pillow — how is it ? ", 

            "He replied : Thus said Samuel :", 

            " It is allowed, even if his wife be with him. ", 

            "Against this teaching is quoted : ", 

            "A man may not place his Tefillin at the foot of the bed because it would be disrespectful, but he may place them beneath his pillow. ", 

            "Should, however, his wife be with him, it is forbidden ; ", 

            "but if there is a place three handbreadths above or below[1], he may place them beneath his pillow ! ", 

            "The refutation of Samuel remains unanswered. ", 

            "Raba said : ", 

            "Although it is stated that the refutation of Samuel remained unanswered, nevertheless the Halakah is in accord with his view.", 

            "What is the reason?  "

        ], 

        [

            "The more one guards them [against  contemptuous treatment] the better[2]. ", 

            "Where, then, should one place them? ", 

            "R. Jeremiah said : ", 

            "Between the mattress and the bolster, where he does not lay his head. ", 

            "But R. Hiyya has taught : ", 

            "He should place them in a bag under his pillow !", 

            " Yes, if he leaves the top of the bag protruding outside [the pillow]. ", 

            "Bar Kappara used to tie them in the bed-curtain, leaving the cases of the Tefillin outside[3].", 

            " Rab Shesha b. Rab Iddi used to place them upon a stool and spread a cloth over them. ", 

            "Rab Hamnuna[4] b. Rab Joseph said : ", 

            "On one occasion I was standing before Raba, and he said to me, ", 

            "\"Go, bring me my Tefillin\";", 

            "and I found them between the mattress and the bolster, where he did not lay his head ; and I knew that it was the day of bathing[5] and he had done this for the purpose of teaching us the Halakah for practice[6]. ", 

            "Rab Joseph b. Rab Nehunyah[7] asked Rab Judah : ", 

            "How is it when two sleep in one bed — does one turn his face away and read the Shema' and the other act likewise[8]? ", 

            "He answered : Thus said Samuel :", 

            " [That is so] even if his wife is with him. ", 

            "Rab Joseph retorted : ", 

            "[Samuel mentions] his wife, but is it not the more necessary to mention [the case when he is with] somebody else? ", 

            "For on the contrary, ", 

            "his wife is like part of himself, whereas another is not like part of himself[1]!", 

            " It is quoted in objection:", 

            " If two sleep in one bed, one turns his face away and reads [the Shema'] and the other acts likewise. ", 

            "But there is another teaching:", 

            " One who sleeps in a bed with his children or members of his household by his side should not read the Shema' unless a sheet separates between them ; ", 

            "but if his children or the members of his household are minors, then he is permitted [to read the Shema' without such separation]!", 

            " This is quite right according to Rab Joseph and there is no contradiction [between the two teachings], ", 

            "the first referring to his wife, the second to somebody else[2]. ", 

            "But with Samuel's view there is a contradiction[3]. ", 

            "Samuel could reply to thee: ", 

            "Is it right according to Rab Joseph's opinion?", 

            " For lo, there is a teaching :", 

            " If a man sleeps in a bed with his children or the members of his household[4], he may not read the Shema' unless a sheet separates between them !", 

            " What, then, is there for thee to say ? There are Tannaim [who are at variance] on Rab Joseph's view of the question of the wife, and there are also Tannaim [who are at variance] on my view[5].", 

            " The master said, ", 

            "\"He turns his face away and reads the Shema'\" — ", 

            "but their buttocks will be in contact !", 

            " This supports the opinion of Rab Huna who said that ", 

            "with buttocks there is no concern on the score of nakedness. ", 

            "It is possible to say that the following teaching is a support of Rab Huna's opinion, viz. : ", 

            "A woman may sit and cut off the Hallah while she is naked, ", 

            "because she is able to cover her nakedness with the ground[6]; but it is not so with a man. ", 

            "Rab Nahman b. Isaac explained this [as applying only to a case where] for instance, her nakedness is sunk in the ground[1]. ", 

            "The master said above,", 

            " \"If his children or members of his household are minors, it is permitted.\" Up to what age? ", 

            "Rab Hisda said[2]: ", 

            "With females, three years and one day; ", 

            "with a male, nine years and one day. ", 

            "Others declare : ", 

            "With females, eleven years and one day ; with a male, twelve years and one day — i.e. with both of them until the age when \"the breasts were fashioned and the hair grown\" (Ezek. xvi. 7). ", 

            "Rab Kahana asked Rab Ashe : ", 

            "Raba said above, \"Although the refutation of Samuel's view remained unanswered, the Halakah is in accord with him\" ; how is it here[3]? ", 

            "He replied : ", 

            "Wilt thou weave all these things in one web[4]? ", 

            "Nay, ", 

            "where it is said[5], it is said ; and where it is not said, it is not said. ", 

            "Rab Mari asked Rab Pappa : ", 

            "How is it if a hair protruded from his garment[6] ? ", 

            "The latter exclaimed : Hair is hair[7]. ", 

            "R. Isaac said : ", 

            "A handbreadth of a woman [if exposed] is nakedness. ", 

            "For what purpose?", 

            " Is it a question of gazing upon her? Behold Rab Sheshet said : ", 

            "Why do the Scriptures enumerate the female ornaments worn outside together with those worn under the garments[8] ? This is to tell thee that ", 

            "whoever gazes upon the little finger of a woman is as though he had gazed at her nakedness ! ", 

            "Nay, ", 

            "[the statement of R. Isaac refers] to his wife and for the purpose of reading the Shema'[9]. ", 

            "Rab Hisda said : ", 

            "The calf of a woman's leg is to be regarded as nakedness; as it is said, \"Uncover the leg, pass through the rivers\" (Is. xlvii. 2) and it continues, \"Thy nakedness shall be uncovered, yea, thy shame shall be seen\" (Is. xlvii. 3). ", 

            "Samuel said : ", 

            "A woman's voice is to be regarded as nakedness ; as it is said, \"For sweet is thy voice, and thy countenance is comely\" (Cant. ii. 14). ", 

            "ab Sheshet said: ", 

            "A woman's hair is to be regarded as nakedness; as it is said, \"Thy hair is as a flock of goats\" (ibid. iv. 1). ", 

            "R. Hannina said :", 

            " I have seen Rabbi hang up his Tefillin. ", 

            "Against this is quoted : ", 

            "He who hangs up his Tefillin will himself be hanged ! ", 

            "The Doreshe Hamurot[1] said,", 

            " \"And thy life shall hang in doubt before thee\" (Deut. xxviii. 66) — this refers to one who hangs up his Tefillin ! ", 

            "There is no contradiction ; for this means one who hangs them up by the thongs, whereas Rabbi hung them up by the case. ", 

            "or if thou wilt I can say that", 

            " whether to hang them by the thong or case is forbidden ; and when Rabbi hung them up it was in a bag. ", 

            "If this be so, what need was there to mention it ?", 

            "[not translated]", 

            " Thou mightest have said that the Tefillin require laying down like a scroll of the Torah ; therefore he informs us[2]. ", 

            "R. Hannina also said :", 

            " I have seen Rabbi belch, yawn, sneeze, expectorate,  "

        ], 

        [

            "and put his garment in order[3] [during his prayer], but he would not rewrap himself[4]; and when he yawned, he would place his hand upon his chin. ", 

            "Against this is quoted : ", 

            "He who makes his voice heard during prayer is of the small of faith[5]; ", 

            "he who raises his voice when praying is of the prophets of falsehood[6]; he who belches and yawns [during prayer] is of the proud of spirit; ", 

            "he who sneezes during prayer should regard it as a bad omen, ", 

            "and some say that ", 

            "it is an indication that he is contemptible; ", 

            "he who expectorates during prayer is as though he expectorated in the presence of the King !", 

            " It is quite right that there is no difficulty in the matter of belching or yawning,", 

            " for here[1] it was an involuntary act and [the denunciation just quoted] refers to one who does it deliberately ; but there is a difficulty", 

            " in the matter of sneezing[2]! No; there is no difficulty; ", 

            "for here[1] it was from above, but the latter refers to one who does so from below[3]. ", 

            "For R. Zera said : ", 

            "This thing was taught me in the school of Rab Hamnuna, and is equal in worth to me to all my studies[4]. ", 

            "He who sneezes during prayer may regard it as a good omen ; for just as it brings him gratification below [on earth], so will it bring him gratification above[5]. ", 

            "But there is a difficulty in the matter of expectoration! ", 

            "No, there is no difficulty;", 

            " for it may be [that Rabbi acted] according to the teaching of Rab Judah", 

            " who said :", 

            " If one is standing in prayer and his spittle collected in his mouth, he may empty it into his Tallit, and if his Tallit is costly, he may empty it into his underwear[6].", 

            " Rabina was once standing before Rab Ashe [during prayer], and the spittle collected in the latter's mouth, and he expectorated behind him. ", 

            "Rabina said to him, ", 

            "\"Does not the master hold the opinion of Rab Judah that one should empty his spittle into his underwear?\"", 

            " He replied,", 

            " \"I am fastidious [in this matter].\" ", 

            "[The teacher stated above[7]:] \"He who makes his voice heard during prayer is of the small of faith.\" ", 

            "Rab Huna said :", 

            " This teaching applies only to one who is able to direct his heart when whispering [the words of prayer] ; but if he is unable to do so, he is permitted [to pray aloud]. ", 

            "And this holds good only of one praying alone ; but with a congregation it would cause disturbance to others. ", 

            "R. Abba was avoiding ", 

            "Rab Judah because he wished to go up to the land of Israel ; for Rab Judah declared :", 

            " Whoever goes up from Babylon to the land of Israel commits a transgression because of [the injunction] which is stated, ", 

            "\"They shall be carried to Babylon, and there shall they be, until the day that I remember them, saith the Lord\" ( Jer. xxvii. 22).", 

            " R. Abba said :", 

            " I will go and hear some teaching from him at the seminary and then I will depart. ", 

            "He went and found a Tanna teaching the following in the presence of Rab Judah :", 

            " If one was standing in the Tefillah and broke wind, he should wait until the odour passes off and then resume the prayer [from where he interrupted it] ; ", 

            "another version is : ", 

            "If he was standing in the Tefillah and felt the need to break wind, he should step back four cubits and having relieved himself, wait until the odour passes off and then resume his prayer, ", 

            "saying,", 

            " \"Lord of the universe ! Thou hast created us with many orifices and vessels. Revealed and known to Thee is our shame and confusion in our lifetime, and in our end we are but worm and vermin\"; ", 

            "he then resumes at the place where he interrupted. ", 

            "R. Abba said to him: ", 

            "Had I only come to hear this, it would suffice me. ", 

            "Our Rabbis have taught :", 

            " If one is sleeping in his cloak and is unable to put forth his head because of the cold, he makes a sort of partition with his cloak around his neck and reads the Shema'.", 

            "Others declare ", 

            "[that he makes the partition] by his heart. ", 

            "But according to the first Tanna, the heart sees the nakedness [during prayer] !", 

            " He holds that", 

            " when the heart sees the nakedness, it is permitted [to read the Shema'].", 

            " Rab Huna said in the name of R. Johanan:", 

            " If one is walking in filthy courtways [and the time for reading the Shema' arrives], he should place his hand over his mouth and read the Shema'. ", 

            "Rab Hisda said to him,", 

            " \"By God !", 

            " if R. Johanan had told me that himself, I would not have listened to him !\" ", 

            "Another version is : Rabbah b. Bar Hannah said in the name of R. Joshua b. Levi : ", 

            "If one is walking in filthy courtways, he should place his hand over his mouth and read the Shema'. ", 

            "Rab Hisda said to him,", 

            " \"By God ! if R. Joshua b. Levi had told me that himself, I would not have listened to him !\"", 

            " But did Rab Huna really say that?", 

            " For Rab Huna has said : ", 

            "A disciple of the wise is forbidden to stand in a filthy place, because it is impossible for him to stand anywhere without meditating upon Torah!", 

            " There is no contradiction ; the latter refers to standing still, the former to walking. ", 

            "And did R. Johanan really say what is attributed to him? ", 

            "For lo, Rabbah b. Bar Hannah has said in the name of R. Johanan :", 

            " One is permitted to meditate anywhere upon words of Torah except the bath-house and privy ! ", 

            "And shouldest thou urge that here also one refers to standing and the other to walking, ", 

            "it cannot be so ; ", 

            "because R. Abbahu once followed R. Johanan and he was reading the Shema', but when he reached the filthy courtways he lapsed into silence. ", 

            "He said to R. Johanan, ", 

            "\"Where should I resume [my prayer] ?\"", 

            " He replied,", 

            " \"If thou hast waited sufficient time to finish the whole, return to the commencement\" ! ", 

            "This is what R. Johanan meant to say to him,", 

            " \"As for me, I do not hold [that the reading of the Shema' should be interrupted] ; but as for thee, since thou dost hold that view, if thou hast waited sufficient time to finish the whole, return to the commencement.\" ", 

            "There is a teaching in agreement with Rab Huna and a teaching in agreement with Rab Hisda.", 

            " There is a teaching in agreement with Rab Huna : ", 

            "If he was walking in filthy courtways, he should place his hand over his mouth and read the Shema'. ", 

            "There is a teaching in agreement with Rab Hisda :", 

            " If he was walking in filthy courtways, he should not read the Shema' ; ", 

            "and not only so, but if he was reading it and entered [such a place], he should stop. ", 

            "If he did not stop, what then? ", 

            "R. Meyasha, the grandson of R. Joshua b. Levi, said :", 

            " Of him the Scriptures state, \"Wherefore I gave them also statutes that were not good, and ordinances whereby they should not live\" (Ezek. xx. 25). ", 

            "R. Assi said :", 

            " [Of him the Scriptures state], \"Woe unto them that draw iniquity with cords of vanity\" (Is. v. 18). ", 

            "Rab Adda b. Ahabah said : From the following,", 

            " \"Because he hath despised the word of the Lord\" (Num. xv. 31). ", 

            "But if he does stop, what is his reward? ", 

            "R. Abbahu said : Of him the Scriptures state,", 

            " \"Through this thing ye shall prolong your days\" (Deut. xxxii. 47). ", 

            "Rab Huna said :", 

            " If his cloak was girded about his loins[1], he is permitted to read the Shema'.", 

            " There is a teaching to the same effect :", 

            " If his cloak of stuff, or skin, or sackcloth was girded about his loins, he is permitted to read the Shema' ; "

        ], 

        [

            " but for the Tefillah [it is not permitted] until he covers his heart.", 

            "Rab Huna also said :", 

            " If a man forgot and entered a privy wearing his Tefillin, he should place his hand over them until he finishes. Until he finishes,", 

            " dost imagine? ", 

            "Nay, it is as Rab Nahman b. Isaac[2] has said : ", 

            "Until he finishes the first discharge[3]. ", 

            "Let him, then, stop at once and stand up!", 

            " [No,] because of [the saying of] Rabban Simeon b. Gamaliel ; ", 

            "for there is a teaching : Rabban Simeon b. Gamaliel says :", 

            " If the fecal discharge is kept back", 

            " it causes dropsy, and if the fluid in the urinary duct is kept back it causes jaundice[4]. ", 

            "It has been reported :", 

            " If there be filth upon his body, or his hand is placed within a privy[1], ", 

            "Rab Huna said :", 

            " It is permitted to read the Shema' ;", 

            " Rab Hisda said :", 

            " It is forbidden to read it.", 

            " Raba asked :  ", 

            "What is Rab Huna's reason ? Because it is written, \"Let everything that hath breath[2] praise the Lord\" (Ps. el. 6). ", 

            "And Rab Hisda said :", 

            " It is forbidden to read the Shema' [in such circumstances] — ", 

            "what is the reason ? Because it is written, \"All my bones[3] shall say, Lord who is like unto Thee\" (ibid. xxxv. 10). ", 

            "It has been reported :", 

            " If there is a foul odour for which there is a cause [present][4], Rab Huna said : ", 

            "A man should remove himself a distance of four cubits[5] and read the Shema'. ", 

            "Rab Hisda said: ", 

            "He should remove himself a distance of four cubits from the place where the odour ceases and read the Shema'. ", 

            "There is a teaching in agreement with Rab Hisda :", 

            " A man should not read the Shema' opposite the excrement of a human being, or of dogs, or pigs, or poultry ; nor opposite the filth of a dunghill which gives forth a bad odour. ", 

            "If there be a place ten cubits higher or lower[6], he sits down[7] at the side and reads the Shema'; but if not, he removes himself as far as he can see it.", 

            " The same rule applies to the Tefillah.", 

            " \"If there is a foul odour for which there is a cause [present], he removes himself a distance of four cubits from the place of the odour and reads the Shema'.\"", 

            " Raba said : The Halakah is not in agreement with this teaching in all these cases, but according to the following teaching :", 

            " A man should not read the Shema' opposite the excrement of human beings[8], nor opposite that of pigs or dogs when he has placed skins therein[9].", 

            "Rab Sheshet was asked : ", 

            "How is it with a foul odour which has no [material] cause[10]? ", 

            "He replied :", 

            " Come and behold the mats in the school of Rab, on which some are sleeping while others are studying[1]. ", 

            "But this refers only to words of Torah, not to the reading of the Shema'[2]. ", 

            "And even of words of Torah this is not said except [when the bad odour is caused] by another ; but if he himself is the cause, he must not [even study until the odour has passed off]. ", 

            "It has been reported : If manure is being carried past a person,", 

            " Abbai said :", 

            " It is permitted to read the Shema' ;", 

            " Raba said :", 

            " It is prohibited to read it. ", 

            "Abbai said : Whence do I derive my opinion ? For there is a Mishnaic teaching :", 

            " If a ritually unclean person[3] is standing under a tree and a person who is ritually clean passes by him, the latter also becomes defiled. If, however, a person ritually clean is standing under a tree and an unclean person passes by, the former remains in his state of purity[4]; but should [the unclean person] remain standing there, then the former becomes unclean. ", 

            "The same law holds good with a stone which has become infected[5].", 

            " And Raba[6]? He can tell thee :", 

            " In this latter circumstance the criterion is a fixed place ; for it is written,", 

            " \"He shall dwell alone ; without the camp shall his dwelling be\" (Lev. xiii. 46)[7]. But here[8] the All-merciful declared,", 

            " \"Therefore shall the camp[9] be holy\" (Deut. xxiii. 15), and behold that is not so. ", 

            "Rab Pappa said :", 

            " A pig's snout is to be regarded as passing manure [for the purpose of reading the Shema']. ", 

            "That is obvious[10]!", 

            " No; it is necessary [to mention it], because even if it just came up out of the river [it is to be so considered]. ", 

            "Rab Judah said :", 

            " If one is uncertain whether excrement is present, it is forbidden [to read the Shema']. ", 

            "If one is uncertain whether urine is present, it is permitted. ", 

            "Another version is : Rab Judah said :", 

            " If one is uncertain whether excrement is in the room, it is permitted [to read it], but by an ash-heap it is forbidden[1].", 

            " If one is uncertain whether urine is present, even by an ash-heap it is permitted. ", 

            "His opinion agrees with that of Rab Hamnuna who said : ", 

            "The Torah only forbids [the Shema' to be read] by fecal matter. He is also in agreement with ", 

            "R. Jonathan[2] who asked :", 

            " It is written \"Thou shalt have a place also without the camp, whither thou shalt go forth abroad\" (Deut. xxiii. 13) and it continues,", 

            " \"And thou shalt have a paddle among thy weapons ; and it shall be when thou sittest down abroad, thou shalt dig therewith, and shalt turn back and cover that which cometh from thee\" (ibid. V. 14) — ", 

            "how is this[3]? The latter verse refers to the major natural function, the former to the minor.", 

            " Infer, then, that the Torah forbids [the Shema' to be read] near to urine only when it is by fecal matter ; ", 

            "but if it has fallen upon the ground, it is permitted [by the Torah], but the Rabbis have decreed against it. Have the Rabbis decreed against it ? When it is certain [that urine is there] ; but if there is a doubt, they do not decree against it. ", 

            "Where it is certain [that urine is present], how long [must one wait before it is allowed to read the Shema' there] ?", 

            " Rab Judah said in the name of Samuel : ", 

            "As long as the ground is sufficiently wet to moisten. ", 

            "The same reply is given by Rabbah b. Bar Hannah in the name of R. Johanan ", 

            "[As long as the ground is sufficiently wet to moisten]", 

            "and by 'Ulla. ", 

            "[As long as the ground is sufficiently wet to moisten]", 

            "Geniba said in the name of Rab :", 

            "As long as the trace thereof can be recognised. ", 

            "Rab Judah [Rab Josef] said : ", 

            "May his teacher forgive Geniba[4]; ", 

            "since in the case of excrement Rab Judah said in the name of Rab : ", 

            "When the surface has hardened it is permitted [to read the Shema' thereby], how much more so with urine[5] ! ", 

            "Abbai said to him : ", 

            "What seest thou that thou reliest upon this; rely upon that ", 

            "which Rabbah b. Rab Huna said in the name of Rab[6] :", 

            " It is forbidden [to read the Shema' near] excrement even when it is like earthenware. ", 

            "What means excrement like earthenware? ", 

            "Rabbah b. Bar Hannah said in the name of R. Johanan; ", 

            "When one can throw it to the ground without its crumbling to pieces. ", 

            "Others say : ", 

            "When one can roll it without its crumbling to pieces. ", 

            "Rabina said : ", 

            "I was once standing before Rab Jeremiah[1] of Difti ; he noticed some excrement, and he said to me,", 

            " \"See whether its surface has hardened or not[2].\" ", 

            "Another version is : He said to him, ", 

            "\"See whether it has become cracked.\" ", 

            "How, then, is it with reference to this matter ?", 

            " It has been reported: ", 

            "When the excrement is like earthenware,", 

            " Amemar said :", 

            " It is forbidden ; ", 

            "Mar Zotra said :", 

            " It is permitted. ", 

            "Raba said : The Halakah is — ", 

            "when the excrement is like earthenware it is forbidden ; and similarly with urine, so long as the ground is sufficiently wet to moisten.", 

            " It is quoted in objection : ", 

            "With urine, so long as the ground is wet enough to moisten it is forbidden ; but if it has been absorbed [in the soil] or dried up[3], it is permitted.", 

            " But is not soaking into the soil like drying up by the sun? [No ;] for as when it dries up, no trace can be recognised, so when it has penetrated into the soil, there must be no trace visible; but if there be such a trace, it is forbidden [to read the Shema' thereby] even though the ground be not sufficiently wet to moisten[4] !", 

            " But against thine own argument, I quote the first clause [of the Baraita brought in objection, viz. :]", 

            " \"With urine, so long as the ground is wet enough to moisten it is prohibited\" ; hence if the trace of it be recognisable, it is permitted[5]! ", 

            "No such deduction can be drawn. ", 

            "It is possible to say that [the question under consideration]", 

            " is like [the following discussion of] the Tannaim :", 

            " It is forbidden to read the Shema' by a vessel from which urine has been poured; ", 

            "but with urine which has been poured out, if it has been absorbed it is permitted, if it has not been absorbed it is forbidden. ", 

            "R. Jose says :", 

            " So long as the earth is sufficiently wet to moisten [it is forbidden]. ", 

            "What does the first Tanna understand by \"absorbed\" and \"not absorbed\" ?", 

            " If it is supposed that \"absorbed\" means that the earth is not sufficiently wet to moisten, and \"not absorbed\" means that it can moisten, and R. Jose comes to declare, ", 

            "\"So long as the earth is sufficiently wet to moisten\" it is forbidden, but if the trace thereof can be recognised it is permitted — ", 

            "then he is in agreement with the first Tanna[1]! ", 

            "Nay, ", 

            "by \"absorbed\" he must mean that no trace can be recognised and by \"not absorbed\" that the trace is recognisable, and then R. Jose comes to declare, ", 

            "\"So long as the earth is sufficiently wet to moisten\" it is forbidden, but if the trace can be recognised it is permitted.", 

            " No[2]; everybody agrees that so long as the earth can moisten it is forbidden, and  if the trace can be recognised it is permitted ;  "

        ], 

        [

            "but here the point at issue is that the earth must be so wet as to moisten something which can moisten something else. ", 

            "If he had gone down to bathe, should he have time to ascend, clothe himself and read [the Shema'] before sunrise, he must ascend, clothe himself and read. ", 

            "It is possible to say that the Mishnah states the law anonymously in agreement with R. Eliezer who declares: ", 

            "He may finish it any time until sunrise[3]. Thou mayest even say that it is in agreement with R. Joshua[4] and perhaps it is here like the Wetikin[5] ; ", 

            "for R. Johanan said: ", 

            "The Wetikin finish it with the sunrise. ", 

            "But if not, he should immerse his body in the water and read. ", 

            "But his heart sees his nakedness !", 

            " R. Eleazar (another version : R.Aha b. Abba b. Aha in the name of our master[6]) said :", 

            " The teaching here refers to turbid water which is to be considered like the solid earth, so that his heart does not see his nakedness. ", 

            "Our Rabbis have taught : ", 

            "With clear water, he must sit immersed up to his neck and read [the Shema'], ", 

            "while others declare", 

            " he should stir up the water with his foot. But according to the first Tanna his heart sees his nakedness[7]! ", 

            "He holds that ", 

            "when his heart sees his nakedness, it is permitted [to read].", 

            " But lo, his heel sees his nakedness[8] !", 

            " He holds that ", 

            "when his heel sees his nakedness, it is permitted. ", 

            "It has been reported : ", 

            "If his heel sees his nakedness, it is permitted [to read the Shema']. ", 

            "If the heel touches, Abbai says :", 

            " It is forbidden [to read] ; Raba says :", 

            " It is permitted. ", 

            "So Rab Zebid taught this subject. ", 

            "Rab Hinnana b. Rab Ika, however, taught it thus :", 

            " If the heel touches, all agree that it is forbidden [to read] ; ", 

            "but if the heel sees [the nakedness], Abbai says :", 

            " It is forbidden ; Raba says :", 

            " It is permitted, because the Torah was not given to the ministering angels[1]. ", 

            "The Halakah is :", 

            " If the heel touches, it is forbidden ; if it sees, it is permitted. ", 

            "Raba said :", 

            " If there be excrement in a transparent vessel, it is permitted to read the Shema' thereby ; if nakedness be in a transparent vessel[2], it is forbidden to read the Shema' thereby.", 

            " \"If there be excrement in a transparent vessel, it is permitted to read the Shema' thereby\" ; because with excrement the criterion is whether it is covered : and behold it is covered.", 

            " \"If nakedness be in a transparent vessel, it is forbidden to read the Shema' thereby\" ; because the All-merciful declared, \"That He see no unseemly thing[3] in thee\" (Deut. xxiii. 15), and behold it is visible. ", 

            "Abbai[4] said :", 

            " Should the excrement be but a minute quantity, one can nullify it [by covering it] with spittle. ", 

            "Raba said :", 

            " It must be with thick spittle. ", 

            "Raba said :", 

            " If excrement be in a hole, he may place his sandal over it and read the Shema'. Mar b. Rabina asked : ", 

            "How is it if excrement adheres to his sandal ?", 

            " The question remained unanswered. ", 

            "Rab Judah[5] said :", 

            " It is forbidden to read the Shema' in the presence of a naked gentile. ", 

            "Why is a gentile specified ? Even by a naked Israelite it is likewise [forbidden] ! ", 

            "[That it is forbidden with an Israelite is obvious][6] ; but it was necessary to specify the case of a gentile.", 

            " For thou mightest have said :", 

            " Since it is written with reference to the gentiles, \"Whose flesh is as the flesh of asses\" (Ezek. xxiii. 20), argue that [in this matter the naked gentile is to be considered] only like an ass[7] ; therefore he informs us that", 

            " to them also [when exposed] is \"nakedness\" attributed ; for it is written, \"And they saw not their father's nakedness\" (Gen. ix. 23)[8]. ", 

            "He may not immerse himself in evil-smelling water, nor water of soaking, until he has poured [fresh] water therein. ", 

            "How much water must he proceed to add[1]?", 

            " Nay, the Mishnah must be read thus: ", 

            "He may not immerse himself at all in evil-smelling water, nor in water of soaking ; ", 

            "nor [may he read the Shema' by a vessel containing] urine, until he has poured [fresh] water therein, and then he may read it.", 

            " Our Rabbis have taught : ", 

            "How much water must be poured therein ? Any small quantity. ", 

            "R. Zakkai says : ", 

            "A fourth [of a Log]. ", 

            "Rab Nahman said : ", 

            "The difference of opinion applies only to [where the vessel contained urine and into which water has been poured] afterwards ; but if originally [the vessel contained water, and urine was then poured into it, then all agree] that any small quantity of water will suffice.", 

            " But Rab Joseph said :", 

            " The difference of opinion applies only to [where there was water] originally [and urine had afterwards been added] ; but where [water has to be added] afterwards, all agree that a fourth [of a Log] is necessary.", 

            " Rab Joseph said to his attendant,", 

            " \"Bring me a fourth [of a Log] in accordance with the opinion of R. Zakkai.\" ", 

            "Our Rabbis have taught :", 

            " It is forbidden to read the Shema' by a bed-pan for excrement or urine, although empty[2]; also by urine[3] until he has poured water therein. ", 

            "How much water should he pour therein ?", 

            " Any small quantity. ", 

            "R. Zakkai says : ", 

            "A fourth [of a Log],", 

            " whether it be before or behind the bed. ", 

            "Rabban Simeon b. Gamaliel says :", 

            " If it be behind the bed, he may read it[4] ; if it be before the bed he may not, but he removes himself a distance of four cubits and reads. ", 

            "R. Simeon b. Eleazar says : ", 

            "Even if the room be the size of a hundred[5] cubits, he may not read until he has removed it or placed it under the bed. ", 

            "The question was asked : ", 

            "How did [Rabban Simeon b. Gamaliel] mean, \"If [the urine] be behind the bed, he may read forthwith ; if it be before the bed, he removes himself a distance of four cubits and reads\" ?", 

            " Or perhaps he meant this :", 

            " If it be behind the bed, he removes himself a distance of four cubits and reads ; if it be in front of the bed, he may not read at all ! ", 

            "Come and hear : For there is a teaching : R. Simeon b. Eleazar says :", 

            " If it be behind the bed, he may read forthwith ; if it be in front of the bed, he removes himself a distance of four cubits. ", 

            "Rabban Simeon b. Gamaliel says : ", 

            "Even if the room be the size of a hundred[1] cubits, he may not read until he has removed it or placed it under the bed. ", 

            "Our question is solved for us[2] ; but the two teachings are contradictory[3] ! ", 

            "Reverse [the names of the teachers] in the latter clause[4]. ", 

            "What seest thou to reverse [the names of the teachers] in the latter clause ?", 

            " Reverse them in the former ! ", 

            "Whom hast thou heard say that ", 

            "a whole room is to be considered as four cubits[5]? It was R. Simeon b. Eleazar. ", 

            "Rab Joseph said : I asked Rab Huna, ", 

            "\"If a bed is less than three [hand breadths] high, it is evident to me that it is to be regarded as solid [with the ground][6]; but how is it with", 

            " three, four, five, six, seven, eight or nine?\" ", 

            "He replied,", 

            " \"I do not know.\" ", 

            "There was certainly no need for me to ask about ten. ", 

            "Abbai said [to Rab Joseph],", 

            " \"Thou hast done well not to ask [about ten hand breadths] ; for every ten constitute a separate stratum.\" ", 

            "Raba said : The Halakah is that ", 

            "less than three is regarded as solid [with the ground], and ten constitute a separate stratum ; but it is about the height from three to ten that Rab Joseph questioned Rab Huna, and he was unable to explain it. ", 

            "Rab[7] said :", 

            " The Halakah is in accord with R. Simeon b. Eleazar;", 

            " and so declared Bali in the name of Rab Jacob, the son of Samuel's daughter[8] : ", 

            "The Halakah is in accord with R. Simeon b. Eleazar. ", 

            "But Raba maintained", 

            " the Halakah was not in accord with him. ", 

            "Rab Ahai[9] contracted a marriage between his son and the house of Rab Isaac b. Samuel b. Marta. He led him under the wedding-canopy, but the marriage was not successfully consummated.", 

            " Rab Ahai went to investigate the cause, and he noticed a scroll of the Torah lying in the bedroom.", 

            " He said to them[10], ", 

            "\"If I had not come now, you would have endangered my son's life ; ", 

            "for there is a teaching :", 

            " It is forbidden to have connubial intercourse in a room where a scroll of the Torah or Tefillin are lying, until they are taken out or placed in a receptacle within a receptacle.\" ", 

            "Abbai said :", 

            " This teaching applies only to a receptacle which is not used expressly for that purpose ; but if it is used for that purpose, even ten receptacles are only to be considered as one. ", 

            "Raba said :  ", 

            "A cloth  "

        ], 

        [

            "spread over a chest [containing sacred books] is regarded as a receptacle within a receptacle. ", 

            "R. Joshua b. Levi said : ", 

            "For a scroll of the Torah it is necessary to make a partition of ten [hand breadths][1]. ", 

            "Mar Zotra paid a visit to Rab Ashe's house, and saw the sleeping accommodation of Mar b. Rab Ashe, whereby a scroll of the Torah was lying and for which he had made a partition of ten handbreadths. ", 

            "He asked him, ", 

            "\"According to whose opinion [hast thou done this]?\" \"According to R. Joshua b. Levi.\"", 

            " \"Under which circumstances did R. Joshua b. Levi say that ? When there is no other room ; but the master has another room !\"", 

            " He said to him, ", 

            "\"I did not think of that.\" ", 

            "To what distance must he remove himself from it and excrement [if he wishes to read the Shema'] ? Four cubits. ", 

            "Raba said in the name of Rab Sahorah in the name of Rab Huna[2] : ", 

            "This teaching applies only to [excrement which is behind him ; but if it is in front of him, he must remove himself as far as the eye can see it. Similarly is it with the Tefillah. ", 

            "But it is not so ! ", 

            "For Rafram b. Pappa said in the name of Rab Hisda : ", 

            "A man may stand opposite a privy and say the Tefillah ! ", 

            "With what are we here dealing ? With a privy which does not contain excrement[3].", 

            " But that is not so ! ", 

            "For Rab Joseph b. Hannina said : ", 

            "When they speak of a \"privy\" they mean even one in which there is no excrement, and when they speak of a \"bath-house\" they mean even one in which there is no person. ", 

            "But with what are we here dealing? ", 

            "With a new one[4]. ", 

            "And lo, Rabina raised the question : ", 

            "How is it with a place which had been designated to be used as a privy? Do we take account of the designation or not[5] ?", 

            " How is this question of Rabina to be understood ? Whether one may stand in such a place to pray therein, not to pray over against it.", 

            " Raba said : ", 

            "The privies of the Persians, although they may contain excrement, are to be regarded as closed in[1]. ", 

            "MISHNAH A man with a running issue who experienced emission, a menstruous woman from whom the semen has escaped, and a woman who during intercourse experiences the flow require immersion; but R. Judah exempts them therefrom. ", 

            "GEMARA  The question was asked :", 

            " If a Ba'al Keri sees a flow, how is it according to R. Judah's view ? ", 

            "For although R. Judah there [in the Mishnah] exempts the man with a running issue who experienced emission — and such a man originally did not require immersion[2] — but a Ba'al Keri who experiences a flow — and such a man originally did require immersion — does he compel to have immersion ? Or perhaps there is no difference ? ", 

            "Come and hear :", 

            " A woman who during intercourse experiences the flow requires immersion ; but R. Judah exempts her therefrom. ", 

            "Behold, a woman in these circumstances is identical with a Ba'al Keri who experienced a flow ; and since R. Judah exempts her, conclude [that he exempts him also]. ", 

            "R. Hiyya taught explicitly : ", 

            "A Ba'al Keri who experienced a flow requires immersion ; but R. Judah exempts him therefrom. ", 

            "May we return to thee : He whose dead !", 

            "MISHNAH The morning Tefillah [may be said] until midday. R. Judah says: ", 

            "Until the fourth hour.", 

            " The afternoon Tefillah [may be said] until the evening. ", 

            "R. Judah says : Until the middle of the afternoon. ", 

            "As far the Tefillah of the evening,  it has no fixed time. ", 

            "The additional Tefillah [may be said] at any time in the day. ", 

            "R. Judah says : Until the seventh hour. ", 

            "GEMARA I quote against the Mishnah : ", 

            "The obligation [of the Shema'] is at sunrise, so as to unite the Ge'ullah and the Tefillah[1], and consequently one says the Tefillah in the day-time[2]! ", 

            "For whom is this teaching intended? For the Wetikin[3]; for R. Johanan said:", 

            " The Wetikin used to finish it with the sunrise.", 

            " As for the rest of the world, [they may say it] until midday.", 

            " And not beyond that? For Rab Mari b. Rab Huna, the son of R. Jeremiah b. Abba, has said in the name of R. Johanan: ", 

            "If a man erred and omitted to say the Tefillah in the evening, he should say it twice in the morning; [if he omitted it] in the morning, he should say it twice in the afternoon. ", 

            "One can therefore say the prayer all day long ! Up to midday one receives the reward of having said the Tefillah in its due time; but beyond that, one receives the reward of having said the Tefillah, but not the reward of having said it in its due time. ", 

            "The question was asked : ", 

            "How is it if one erred and omitted the afternoon Tefillah — shall he say it twice in the evening ?", 

            " If thou thinkest thou canst answer [by quoting] \"If one erred and omitted the evening Tefillah, he should say it twice in the morning,\" [that is different] because it is one day ; as it is written, \"And there was evening and there was morning one day \" (Gen. i. 5)[4]. But here the Tefillah is the substitute for the sacrifice[1], and the day having passed, the sacrifice becomes void[2]. ", 

            "Or is it perhaps because Tefillah is supplication, and one may pray whenever he wishes? ", 

            "Come and hear:", 

            " For Rab Huna b. Judah said in the name of R. Isaac, in the name of R. Johanan[3]: ", 

            "If one erred and omitted the afternoon Tefillah, he should say it twice in the evening, and the principle \"The day having passed, the sacrifice becomes void\" does not apply.", 

            " It is quoted in objection, ", 

            "\"That which is crooked cannot be made straight, and that which is wanting cannot be numbered\" (Eccles. i. 15) —", 

            " \"that which is crooked cannot be made straight,\" i.e. one who has omitted the Shema' of the evening or morning, or the Tefillah of the evening or morning[4];", 

            " \"and that which is wanting cannot be numbered,\" i.e. his companions were numbered for the purpose of a religious duty[5], and he was not numbered among them! ", 

            "R. Isaac said in the name of R. Johanan:", 

            " With whom are we here dealing[6]? With one who intentionally omitted [the Shema' or Tefillah]. ", 

            "Rab Ashe said :", 

            " There is confirmation in the fact that he used the term \"omitted\" and not \"erred.\" Draw that conclusion[7].  "

        ], 

        [

            "Our Rabbis have taught :", 

            " If one erred and omitted the afternoon Tefillah on the Sabbath-eve, he says the Tefillah twice on the night of the Sabbath. If one erred and omitted the afternoon Tefillah on the Sabbath, he says the week-day Tefillah twice at the conclusion of the Sabbath. In the first he adds the paragraph of \"Division[8],\" but not in the second[9]. If he added this paragraph in the second and not in the first, then the reading of the first Tefillah counts for him but not the second[10].", 

            " One might deduce from this teaching that since he did not add the paragraph of \"Division\" in the first Tefillah, he is as though he had not prayed at all and we make him repeat it.", 

            " But against this I quote : ", 

            "If one erred and did not mention the reference to rain[1] in the benediction \"Thou sustainest the living[2]\" or the request for rain in the benediction of \"the Years[3],\" we make him repeat it ; but if he omitted the paragraph of \"Division\" in the benediction \"Thou favourest man with knowledge,\" we do not make him repeat it, because he is able to say it over the cup [of wine][4]!", 

            " The contradiction [remains unsolved]. ", 

            "It has been reported : R. Jose b. R. Hannina said : ", 

            "The Patriarchs instituted the Tefillot. ", 

            "R. Joshua b. Levi said:", 

            " The Tefillot were instituted to correspond with the continual sacrifices. ", 

            "There is a teaching in agreement with both of them. ", 

            "There is a teaching in agreement with R. Jose b. R. Hannina:", 

            " Abraham instituted the morning Tefillah; as it is said, \"And Abraham got up early in the morning to the place where he had stood\" (Gen. xix. 27) — \"standing\" means prayer; as it is said, \"Then stood up Phineas and prayed\" (Ps. cvi. 30)[5].", 

            " Isaac instituted the afternoon Tefillah; as it is said, \"And Isaac went out to meditate in the field at eventide\" (Gen. xxiv. 63) — \"meditation\" [sihah] means prayer; as it is said, \"A prayer of the afflicted when he fainteth, and poureth out his complaint [sihah] before the Lord\" (Ps, cii. 1). ", 

            "Jacob instituted the evening Tefillah ; as it is said, \"And he lighted [paga'] upon the place, and tarried there all night\" (Gen. xxviii. 11) —  \"alighting\" means prayer; as it is said, \"Therefore pray not thou for this people, neither lift up cry nor prayer for them, neither make intercession [paga'] to Me\" (Jer. vii. 16). ", 

            "There is also a teaching in agreement with R. Joshua b. Levi :", 

            " Why is it declaimed: The morning Tefillah [may be said] until midday ? Because the morning continual offering could be brought until midday. ", 

            "R. Judah says : ", 

            "Until the fourth hour, because the morning continual offering could be brought until the fourth hour. ", 

            "And why is it declared : The afternoon Tefillah [may be said] until the evening? Because the twilight continual offering could be brought until the evening. ", 

            "B. Judah says :", 

            " Until the middle of the afternoon, because the twilight continual offering could be brought until the middle of the afternoon.", 

            " And why is it declared : As for the Tefillah of the evening, it has no fixed time? Because the limbs[6] and the fat[1] which had not been consumed by the evening may be offered at any time during the night. ", 

            "And why is it declared : The additional Tefillah [may be said] at any time in the day? Because the additional offering could be brought at any time during the day. ", 

            "R. Judah says : ", 

            "Until the seventh hour, because the additional offering could be brought until the seventh hour[2]. ", 

            "Which is \"the greater afternoon\"? The time from six and a half hours and onwards[3] ", 

            "And which is \"the lesser afternoon\"? The time from nine and a half hours and onwards[4]. ", 

            "The question was asked : ", 

            "Does R. Judah mean[5] the middle of the first afteraoon-tide or the middle of the latter afternoon-tide? ", 

            "Come and hear : ", 

            "For there is a teaching : R. Judah says : ", 

            "[The Sages] mean the middle of the latter afternoon-tide, and that is eleven hours less a quarter[6].", 

            " We might suppose that this is a refutation of R. Jose b. R. Hannina[7]! ", 

            "But he could reply :", 

            " I certainly maintain that the Patriarchs instituted the Tefillot, but the Rabbis subsequently found a basis for them in the sacrifices. ", 

            "For if thou sayest not so[8], who instituted the additional Tefillah, according to R. Jose b. R. Hannina? ", 

            "But", 

            " the Patriarchs instituted the Tefillot, and the Rabbis subsequently found a basis for them in the sacrifices. ", 

            "R. Judah says: Until the fourth hour. ", 

            "The question was asked:", 

            " Is \"until\" inclusive, or is it perhaps exclusive[9]? ", 

            "Come and hear:", 

            " R. Judah says: Until the middle of the afternoon. ", 

            "That is quite right if thou maintainest that this means \"until\" but not including — for that is the point of variance between R. Judah and the Rabbis[10]; but if thou maintainest that [[fol. 27 a.]] it means \"until\" and including, then R. Judah would be in agreement "

        ], 

        [

            " with the Rabbis !", 

            " What, then, does it signify? ", 

            "Until but not including. Let me, then, quote the sequel of the teaching:", 

            " The additional Tefillah [may he said] at any time in the day. R. Judah says: ", 

            "Until the seventh hour. ", 

            "But there is a teaching:", 

            " If there be before a man two Tefillot, one the additional and the other of the afternoon, he should say that of the afternoon and afterwards the additional ; because the former is constant, the latter not constant[1]. ", 

            "R. Judah says: ", 

            "He should first recite the additional Tefillah and afterwards that of the afternoon, because [the time of the former] lapses, but the other does not. ", 

            "That is quite right if thou maintainest that \"until\" means including, and thus the two Tefillot are found together; ", 

            "but if thou maintainest that \"until\" means excluding, how is it these two Tefillot are found together?", 

            " For when the time of the afternoon Tefillah has arrived, the time of the additional Tefillah has passed[2]! ", 

            "What, then, does it signify? \"Until\" and including[3]. ", 

            "Then the difficulty in the first clause remains, viz. : ", 

            "What is the point of variance between R. Judah and the Rabbis[4]? ", 

            "Dost thou hold the opinion that when R. Judah mentioned ", 

            "\"The middle of the afternoon\" he meant the second half?", 

            " He meant the first half, and he must be understood to say : When does the first half conclude and the latter half commence?", 

            " At the expiration of the eleventh hour less a quarter[5].", 

            "Rab Nahman[6] said : ", 

            "We have also learnt so[7]. R. Judah b. Baba testified to five matters, viz. : ", 

            "We permit a woman to repudiate a marriage which has been contracted for her while she was a minor[8]; we permit a woman to remarry although there is only one witness[1] ; and concerning a cock which was stoned in Jerusalem for having killed a child[2]; and that wine forty days old was poured over the altar[3]; and concerning the morning continual offering that it was brought in the first four hours[4]. ", 

            "Conclude from this that", 

            " \"until\" is inclusive ; yes, draw that conclusion. ", 

            "Rab Kahana said : ", 

            "The Halakah is in accord with R. Judah, since there is such a teaching in the Behirta[5]. ", 

            "\"And concerning the morning continual offering that it was brought in the first four hours.\" ", 

            "Who is the authority for the following teaching :", 

            " \"And as the sun waxed hot, it melted\" (Exod. xvi. 21) — this refers to the fourth hour of the day?", 

            " Thou sayest \"the fourth hour\"; but perhaps it means the sixth hour ! ", 

            "When the Bible states", 

            " \"In the heat of the day\" (Gen. xviii. 1) it means the sixth hour. How, then, am I to understand \"As the sun waxed hot, it melted\" ? That refers to the fourth hour[6].", 

            " In accordance with whose opinion is this?", 

            " It can be neither R. Judah's nor the Rabbis'.", 

            " If it were R. Judah's, up to [and including] the fourth hour is still morning[7] ; and if it were the Rabbis', up to midday is still morning !", 

            " If thou wilt I can say", 

            " it is R. Judah's view or", 

            "the Rabbis'.", 

            " If thou wilt I can say it is the view of the Rabbis — because the Scriptures state, ", 

            "\"Morning by morning\" (Exod. l.c.), thus dividing the morning into two parts[8].", 

            " If thou wilt I can say it is R. Judah's view — because one word for \"morning\" is superfluous, the intention being to anticipate [the time for gathering] by one hour[1] ", 

            "Everybody agrees \"As the sun waxed hot, it melted\" means in the fourth hour. How is this proved? ", 

            "Rab Aha b. Jacob said: The Scriptures state,", 

            " \"As the sun waxed hot, it melted\" — which is the hour when the sun is hot and the shade cool?", 

            " Say it is the fourth hour. ", 

            "The afternoon Tefillah [may he said] until the evening. R. Judah says: Until the middle of the afternoon. ", 

            "Rab Hisda asked Rab Isaac[2]: ", 

            "Rab Kahana stated above[3] that the Halakah is in accordance with R. Judah since there is such a teaching in the Behirta. How is it here[4]? ", 

            "He was silent and answered him not a word. ", 

            "Rab Hisda said :", 

            " \"We see from the fact that Rab recited the Sabbath-Tefillah on the Sabbath-eve while it was yet day, it is to be concluded that the Halakah is in agreement with R, Judah[5] !", 

            " On the contrary, from the fact that Rab Huna and the Rabbis did not say the [Sabbath]- Tefillah until it was night, conclude that the Halakah is not in agreement with R. Judah. ", 

            "Since it has not been reported whether the Halakah accords with either, he who acted in agreement with the one did rightly, and he who acted in agreement with the other did rightly. ", 

            "Rab went on a visit to the house of Geniba and said the Sabbath-Tefillah on the Sabbath-eve. R. Jeremiah b. Abba was praying behind Rab, and when the latter finished his Tefillah he did not interrupt the devotions of R. Jeremiah[6]. ", 

            "Draw three deductions from this : ", 

            "A man may say the Sabbath- Tefillah ", 

            "on the Sabbath-eve[7] ; a disciple may pray behind his master ; and it is forbidden to pass in front of those who are saying the Tefillah. ", 

            "[This last-mentioned] supports the teaching of R. Joshua b. Levi :", 

            " It is forbidden to pass in front of those who are saying the Tefillah. ", 

            "But it is not so, ", 

            "seeing that R. Assi and R. Ammi did so pass !", 

            " It was beyond a distance of four cubits that R. Ammi and R. Assi passed.", 

            " But how could R. Jeremiah act thus[8]? ", 

            "For lo, Rab Judah said in the name of Rab:", 

            " A man should never pray "

        ], 

        [

            " in front of or  behind his master ! ", 

            "And there is a teaching: R. Eliezer[1] says:", 

            " He who prays behind his master[2], or greets his master or returns his salutation[3], or opposes [the opinions taught by] his master's school, or reports a teaching [in his master's name] which he had not heard from his master's lips, causes the Shekinah to depart from Israel ! ", 

            "It was different with R. Jeremiah b. Abba, because he was a disciple-colleague, ", 

            "and thus he asked Rab,", 

            " \"Hast thou made the 'division'[4]?\"", 

            " to which he replied,", 

            "\"Yes, I have done so\"; and R. Jeremiah did not say, \"Did the master make the 'division'?\" ", 

            "But had he made the 'division'? ", 

            "For lo, R. Abin[5] said : ", 

            "On one occasion Rabbi said the Sabbath-Tefillah on the Sabbath-eve, and then entered the bath and came out and taught us our chapter ; and it was not yet dark ! ", 

            "Rab said : ", 

            "He must have gone into the bath-house only to perspire, and that happened before the decree was issued against it. ", 

            "That cannot be correct, ", 

            "because Abbai permitted Rab Dimai b. Liwai[6] to fumigate baskets[7]! ", 

            "That was a mistake. ", 

            "Can a mistake [of this nature] be rectified?", 

            " For Abidan[8] said : ", 

            "On one occasion the heavens became thick with clouds, so that the people were led to believe that it was dusk. They entered the Synagogue and said the Tefillah for the conclusion of the Sabbath on the Sabbath. Afterwards the clouds dispersed and the sun shone forth ; so they came and put the question to Rabbi. His reply was that ", 

            "since they had said the Tefillah, it must stand.", 

            " It is different with a Congregation, because we do not put them to trouble[9]. ", 

            "R. Hiyya b. Ashe[10] said: ", 

            "Rab said the Sabbath-Tefillah on the Sabbath-eve[11] ; R. Josiah said the Tefillah for the conclusion of the Sabbath on the Sabbath. ", 

            "\"Rab said the Sabbath-Tefillah on the Sabbath-eve\" —", 

            " did he recite the \"Sanctification[12]\" over the cup of wine, or did he omit it? ", 

            "Come and hear : ", 

            "For Rab Nahman[13] said in the name of Samuel : ", 

            "A man may say the Sabbath-Tefillah on the Sabbath-eve and recite the \"Sanctification\" over the cup of wine;", 

            " and the Halakah is in accord with his view.", 

            " \"R. Josiah said the Tefillah for the conclusion of the Sabbath on the Sabbath\" ", 

            "did he recite the Habdalah over the cup of wine or did he omit it? ", 

            "Come and hear : ", 

            "For Rab Judah said in the name of Samuel :", 

            " A man may say the Tefillah for the conclusion of the Sabbath on the Sabbath and recite the Habdalah over the cup of wine.", 

            " R. Zera said in the name of R. Assi[1], in the name of R. Eleazar, in the name of R. Hannina, in the name of Rab[2] : ", 

            "At the side of this pillar, R. Ishmael b. R. Jose said the Sabbath-Tefillah on the Sabbath-eve.", 

            " When 'Ulla came he said :", 

            " It was at the side of this palm-tree, not pillar ; it was not R. Ishmael b. R. Jose, but R. Eleazar b. R. Jose ; and it was not the Sabbath-Tefillah on the Sabbath-eve, but the Tefillah for the conclusion of the Sabbath on the Sabbath. ", 

            "As for the Tefillah of the evening, it has no fixed time. ", 

            "What means it has no fixed time?", 

            " If we are to suppose that should a man so desire, he can say the Tefillah at any time during the night, then let the Mishnah teach explicitly, \"The evening Tefillah [may be said] at any time during the night\"!", 

            " What, then, means it has no fixed time?", 

            " It is in accord with him who declared that ", 

            "the evening-Tefillah is voluntary;", 

            " for Rab Judah said in the name of Samuel:", 

            " As for the evemng-Tefillah, Rabban Gamaliel declares it to be ", 

            "obligatory, but R. Joshua declares it to be", 

            " voluntary. ", 

            "Abbai said[3] :", 

            " The Halakah is in agreement with him who declares it to be obligatory ; ", 

            "but Raba[4] said :", 

            " The Halakah is in agreement with him who declares it to be voluntary. ", 

            "Our Rabbis have taught :", 

            " It happened that a disciple came before R. Joshua and asked him,", 

            " \"Is the evening-Tefillah voluntary or obligatory?\"", 

            " He replied,", 

            " \"It is voluntary.\" ", 

            "Then he came before Rabban Gamaliel and asked him", 

            " the same question. ", 

            "He replied, ", 

            "\"It is obligatory.\" ", 

            "He thereupon said to him,", 

            " \"But has not R. Joshua told me it was voluntary!\"", 

            " Rabban Gamaliel said to him,", 

            " \"Wait until the shield-bearers[5] enter the House of Study.\" ", 

            "When the shield-bearers had assembled, the questioner stood up and asked,", 

            " \"Is the evening-Tefillah voluntary or obligatory ?\" ", 

            "Rabban Gamaliel replied,", 

            " \"It is obligatory.\" ", 

            "Rabban Gamaliel said to the Sages, ", 

            "\"Is there anyone who has a different opinion on this matter?\" ", 

            "R. Joshua said to him,", 

            " \"No[1]\"", 

            " Then Rabban Gamaliel said to him,", 

            " \"But has it not been reported to me in thy name that it is voluntary ?\" ", 

            "And he added,", 

            " \"Joshua, stand up that it may be testified against thee.\" ", 

            "R. Joshua stood up and said,", 

            " \"If I were living and he[2] dead, the living would be able to deny the statement of the dead ; but seeing that I am alive and he also is alive, how can the living deny the statement of the living ! \" ", 

            "Then Rabban Gamaliel sat and commenced his discourse while R. Joshua remained standing[3], until all those present began to murmur and cried to Huspit the interpreter[4], ", 

            "\"Stop !\"", 

            " and he stopped.", 

            " They said,", 

            " \"How long is [Rabban Gamaliel] going to continue heaping indignities upon [R. Joshua]?", 

            " Last year he slighted him on the question of the New Year[5] ; he slighted him on the question of the firstborn in the incident of R. Sadok[6]; and here again he has slighted him. Come, let us depose him[7]! ", 

            "Whom shall we appoint in his stead ? ", 

            "Shall we appoint R. Joshua ?", 

            " [No ;] he is a party in the incident.", 

            " Shall we appoint R. 'Akiba ?", 

            " [No ;] perhaps Rabban Gamaliel will plague him because of his lack of ancestral merit[8]. ", 

            "Let us, then, appoint R. Eleazar b. 'Azariah, for he is wise, rich, and he is of the tenth generation from Ezra. ", 

            "He is wise, so if anyone[9] puts difficult questions to him, he will be able to reply to him ; and he is rich, so if it be necessary for someone to attend at the palace of the Emperor[10], he will be qualified to do so ; and he is of the tenth generation from Ezra, so he possesses ancestral merit and Rabban Gamaliel will not be able to worry him on that score.\" ", 

            "They attended upon R. Eleazar b. 'Azariah and asked him, ", 

            "\"Would the master consent to become the head of the College?\" ", 

            "He replied,", 

            " \"I will first go and take counsel with the members of my household.\"", 

            " He went and consulted his wife,", 

            " and she said to him, "

        ], 

        [

            " \"Perhaps they will soon depose thee!\" ", 

            "He answered[1]", 

            " \"[Let a man] use the cup of honour[2] for one day, and to-morrow let it be broken.\" ", 

            "She said to him,", 

            " \"Thou hast no grey hair[3]!\" ", 

            "That day he was eighteen[4] years of age; but a miracle was wrought for him, and eighteen rows of hair[5] turned grey. ", 

            "That is what R. Eleazar b. 'Azariah meant when he said,", 

            " \"Behold I am like one seventy years old,\" and not \"I am seventy years old[6].\" ", 

            "It has been taught : ", 

            "That same day, they removed the doorkeeper [of the College] and permission was granted to the disciples to enter ;", 

            " for Rabban Gamaliel had issued a proclamation:", 

            " \"A disciple, who is not inwardly the same as outwardly[7], will not be allowed to enter the House of Study.\" ", 

            "That day many forms had to be added[8]. ", 

            "R. Johanan said : ", 

            "Abba Jose[9] b. Dostai and the Rabbis differ as to the number; one declaring", 

            " four hundred forms were added,", 

            " the other declaring it was seven hundred. ", 

            "This [vast addition] depressed Rabban Gamaliel who said, ", 

            "\"Perhaps, God forbid, I have withheld Torah from Israel !\"", 

            " He was shown in a dream white pitchers full of ashes\". ", 

            "It was not really so[11] ; but he was shown this to relieve his mind. ", 

            "It has been taught :", 

            " That same day 'Eduyyot[1] was learnt, and wherever we find the phrase \"on that day\" it refers to that occasion.", 

            " There was not a Halakah which had been left in a state of uncertainty in the House of Study which was not then made clear. ", 

            "Even Rabban Gamaliel did not absent himself from the House of Study[2]. For there is a Mishnaic teaching: ", 

            "On that day an Ammonite proselyte, named Judah, came before them in the House of Study and said to them,", 

            " \"May I enter the Community [of Israel]?\" ", 

            "Rabban Gamaliel replied to him,", 

            " \"Thou art forbidden to enter the Community.\"", 

            " R. Joshua said to him, ", 

            "\"Thou art permitted to enter the Community.\" ", 

            "Rabban Gamaliel asked R. Joshua, ", 

            "\"But has it not been said,", 

            " 'An Ammonite or a Moabite shall not enter into the assembly of the Lord '?\" (Deut. xxiii. 4).", 

            " R. Joshua answered him,", 

            " \"Do, then, the Ammonites and Moabites still inherit their lands? ", 

            "Did not Sennacherib, king of Assyria, long ago come up and confuse all the nationalities ? As it is said,", 

            " 'I have removed the bounds of the peoples, and have robbed their treasures, and have brought down as one mighty the inhabitants' (Is. X. 13) ; and whoever issues [from a mixed body] issues from the majority[3].\" ", 

            "Rabban Gamaliel said to him, ", 

            "\"But has it not been said,", 

            "'Afterward I will bring back the captivity of the children of Ammon, saith the Lord' (Jer. xlix. 6) ? and therefore they have returned !\" ", 

            "R. Joshua retorted, ", 

            "\"And has it not been said,", 

            " 'I will turn the captivity of My people Israel' (Amos ix. 14)? but they have not yet returned !\" ", 

            "They immediately permitted him to enter the Community. ", 

            "Rabban Gamaliel thereupon said,", 

            " \"Since it is so, I will go and conciliate R. Joshua[4].\"", 

            " When he arrived at the latter's house, he noticed that the walls of his house were blackened, ", 

            "and said to him, ", 

            "\"From the walls of thy house it can be recognised that thou art a charcoal-burner[5].\" ", 

            "R. Joshua replied,", 

            " \"Woe to the generation whose leader thou art, for thou knowest not the struggle of the disciples to support and feed themselves!\" ", 

            "He said to him, ", 

            "\"I beg thy pardon[1]; forgive me.\"", 

            " He took no notice of him. ", 

            "\"Do it out of regard for my father!\" ", 

            "He made peace with him. ", 

            "They said, ", 

            "\"Who will go and tell the Rabbis [that we are reconciled]? \" ", 

            "A fuller[2] said to them,", 

            " \"I will go,\" ", 

            "R. Joshua sent [the following message] to the House of Study,", 

            " \"Let him who has been accustomed to wear the mantle [of honour] still wear it ; and shall he who has not been accustomed to wear the mantle say to him who has been accustomed to wear it, 'Take off thy mantle and I shall put it on'[3]?\"", 

            " R. 'Akiba said to the Rabbis, ", 

            "\"Bolt the doors, so that the slaves of Rabban Gamaliel may not enter and injure the Rabbis[4].\" ", 

            "R. Joshua said,", 

            " \"It is better that I should rise and go myself to him[5].\" ", 

            "He went and knocked at his door, ", 

            "and said to him, ", 

            "\"Let the sprinkler[6] who is the son of a sprinkler sprinkle; for shall one who is not a sprinkler nor the son of a sprinkler say to a sprinkler who is the son of a sprinkler,", 

            " 'Thy water is cave water and thy ashes the ashes of a stove'[7]?\" ", 

            "R. 'Akiba said to him,", 

            " \"R. Joshua, thou hast become reconciled ! ", 

            "Have we not done this only out of regard for thine honour? ", 

            "To-morrow thou and I will go early to the door of [Rabban Gamaliel's] house[8].\" ", 

            "They asked,", 

            " \"What shall we do? ", 

            "Shall we depose [R. Eleazar b. 'Azariah] ? We have the tradition,", 

            " 'We may raise to a higher degree of sanctity but not degrade to a lower degree! ' ", 

            "If we ask one of them to give the discourse on one Sabbath and the other on the next Sabbath, it will lead to jealousy.", 

            " Let, then, ", 

            "Rabban Gamaliel give the discourse three Sabbaths [in the month] and R. Eleazar b. 'Azariah one Sabbath,\"", 

            " That is what the teacher meant who asked,", 

            " \"Whose Sabbath was it? It was R. Eleazar b. 'Azariah's[1]\" ]", 

            "And the disciple was R. Simeon b. Johai[2]. ", 

            "The additional Tefillah [may he said] at any time in the day. [R. Judah says: Until the seventh hour.] ", 

            "R. Johanan said :", 

            " If one reads it after the seventh hour, he is called a transgressor. ", 

            "Our Rabbis have taught[3]: ", 

            "If there be before a man two Tefillot, one of the afternoon and the other the additional, he should say that of the afternoon and afterwards the additional, because the former is constant, the latter not constant[4]. ", 

            "R. Judah says : ", 

            "He should first recite the additional Tefillah and afterwards that of the afternoon, because the former is a duty that lapses, but the other is not. ", 

            "R. Johanan said :", 

            " The Halakah is — one first says the afternoon Tefillah and then the additional. ", 

            "When R. Zera[5] was weary of study, he used to go and sit at the entrance of the school of R. Nathan b. Tobi saying, ", 

            "\"When the Rabbis pass by, I will stand up before them and receive the reward[6]\" ", 

            "He once went out ; and when R. Nathan b. Tobi came he asked him[7], ", 

            "\"Who is stating the Halakah in the House of Study?\" ", 

            "He replied, \"Thus spake R. Johanan : ", 

            "The Halakah is not according to R. Judah who said", 

            ", 'He should first recite the additional Tefillah and afterwards that of the afternoon'.\"", 

            " R. Zera asked him, ", 

            "\"Did R. Johanan say that?\"", 

            " He replied,", 

            " \"Yes,", 

            " it was taught us by him forty times.\"", 

            " He asked him,", 

            " \"Is this the only one [he expounded] to thee, or was it new to thee[8]?\"", 

            " He replied,", 

            " \"It was new to me, because I was in doubt [whether it was not a teaching] of R. Joshua b. Levi.\" ", 

            "R. Joshua b. Levi said : ", 

            "Whoever prays the additional Tefillah after the seventh hour, as taught by R. Judah, of him the Scriptures state, ", 

            "\"Those who are smitten [nuge][9] because of the advocated appointed seasons will I gather, who are of thee\" (Zeph. iii. 18).", 

            " How is it known that nuge is a term of \"breaking\" ? ", 

            "As Rab Joseph translated : ", 

            "\"A breach has come upon the enemies of the house of Israel[1] because they delayed the times of the festivals in Jerusalem.\" ", 

            "R. Eleazar said : ", 

            "Whoever says the morning Tefillah after the fourth hour, of him the Scriptures declare, ", 

            "\"Those who are troubled [nuge] because of the appointed seasons will I gather, who are of thee.\"", 

            " How is it known that nuge is a term for \"trouble\" ?", 

            " For it is written, ", 

            "\"My soul melteth away from heaviness [tugah]\" (Ps. cxix. 28).", 

            " Rab Nahman b. Isaac said : From the following :", 

            " \"Her virgins are afflicted [nugot], and she herself is in bitterness\" (Lam. i. 4).  "

        ], 

        [

            "Rab Iwya was ill and did not attend Rab Joseph's discourse[2]. ", 

            "The next day when he arrived, Abbai wished to set Rab Joseph's mind at rest[3] ; ", 

            "so he said to him,", 

            " \"For what reason did not the master attend the discourse?\" ", 

            "He replied, ", 

            "\"My heart was faint and I could not.\" ", 

            "He asked him, ", 

            "\"Why didst thou not eat something and come?\"", 

            " He answered, ", 

            "\"Does not the master agree with the opinion of Rab Huna", 

            " who said :", 

            " It is forbidden a man to eat anything before praying the additional Tefillah?\"", 

            " He replied, ", 

            "\"Then the master should have said the additional Tefillah by himself and eaten something and attended.\"", 

            " He said to him, ", 

            "\"Does not the master agree with the opinion of R. Johanan who declared :", 

            " A man is forbidden to anticipate the congregational Tefillah by praying alone?\"", 

            " He replied, ", 

            "\"But has it not been reported in this connection :", 

            " R. Abba[4] said : ", 

            "This teaching applies only when he is with the Congregation[5]?\" ", 

            "The Halakah is in accord", 

            "neither with Rab Huna nor R. Joshua b. Levi.", 

            " [It is not] in accord with Rab Huna, as is here mentioned. [Nor is it] in accord with R. Joshua b. Levi who said : ", 

            "When the time of the afternoon Tefillah has arrived, it is forbidden to eat anything before praying the afternoon Tefillah. ", 

            "MISHNAH R. Nehunya h. Hakkanah, on entering and leaving the House of Study, used to offer a short prayer. ", 

            "They said to him : ", 

            "What is the nature of this prayer ?", 

            " He replied : ", 

            "On entering I pray that no offence should occur through me; and when I leave I offer thanks-giving for my portion [1]. ", 

            "GEMARA Our Rabbis have taught : ", 

            "What used he to say on entering ?", 

            " \"May it be Thy will, O Lord my God, that no offence occur through me ;", 

            " that I stumble not in the matter of Halakah ; that my colleagues have occasion to rejoice in me ; that I pronounce not anything clean that is unclean, or unclean that is clean; that my colleagues stumble not through me in the matter of Halakah ; and that I may have occasion to rejoice in them.\" ", 

            "What used he to say on leaving? ", 

            "\"I give thanks before Thee, O Lord my God, that Thou hast set my portion with those who sit in the House of Study and not with those who sit at street-corners[2]; for I and they rise early — I to words of Torah, but they to vain matters ; I and they labour, but I labour and receive a reward whereas they labour and receive no reward ; I and they hasten — I to the life of the world to come, but they to the pit of destruction.\" ", 

            "Our Rabbis have taught : ", 

            "When R. Eliezer was ill, his disciples went in to visit him.", 

            " They said to him, ", 

            "\"Master, teach us the ways of life whereby we may be worthy of the life of the world to come.\" ", 

            "He said to them, ", 

            "\"Be careful of the honour of your colleagues ; restrain your children from recitation[3], and seat them between the knees of the disciples of the wise ; and when you pray, know before Whom ye stand ; and on that account will you be worthy of the life of the world to come.\" ", 

            "When Rabban Johanan b. Zakkai was ill, his disciples went in to visit him. ", 

            "On beholding them, he began to weep.", 

            "His disciples said to him, ", 

            "\"O lamp of Israel, right-hand pillar[1], mighty hammer! Wherefore dost thou weep ?\"", 

            " He replied to them,", 

            " \"If I was being led into the presence of a human king who to-day is here and tomorrow in the grave, who if he were wrathful against me his anger would not be eternal, who if he imprisoned me the imprisonment would not be everlasting, who if he condemned me to death the death would not be for ever, and whom I can appease with words and bribe with money — even then I would weep ; ", 

            "but now, when I am being led into the presence of the King of kings, the Holy One, blessed be He, Who lives and endures for all eternity, Who if He be wrathful against me His anger is eternal. Who if He imprisoned me the imprisonment would be everlasting. Who if He condemned me to death the death would be for ever, and Whom I cannot appease with words nor bribe with money — ", 

            "nay more, when", 

            " before me lie two ways, one of the Garden of Eden and the other of Gehinnom, and I know not in which I am to be led — shall I not weep ?\"", 

            " They said to him,", 

            " \"Our master, bless us !\" ", 

            "He said to them,", 

            " \"May it be His will that the fear of Heaven be upon you [as great] as the fear of flesh and blood,\" ", 

            "His disciples exclaimed,", 

            " \"Only as great !\" ", 

            "He replied,", 

            " \"Would that it be [as great] ;", 

            " for know ye, when a man intends to commit a transgression, he says,", 

            " 'I hope nobody will see me'[2].\" ", 

            "At the time of his departure [from the world] he said to them, ", 

            "\"Remove all the utensils because of the defilement[3] and prepare a seat for Hezekiah, king of Judah, who is coming[4].\" ", 

            "MISHNAH  Rabban Gamaliel says: ", 

            "Every day one should pray the eighteen [benedictions][5].", 

            " R. Joshua says : ", 

            "The abstract of the eighteen [benedictions][6]. ", 

            "R. 'Akiba says:", 

            " If his prayer is fluent in his mouth, he should pray the eighteen ; but if not, an abstract of the eighteen. ", 

            "R. Eliezer says :", 

            " If one makes his prayer a fixed task, his prayer is not a supplication.", 

            " R. Joshua says :", 

            " If one is journeying in a place of danger, he should offer a short prayer, saying :", 

            " \"Save, O Lord, Thy people, the remnant of Israel ; in all times of crisis may their needs be before Thee. Blessed art Thou, O Lord, Who hearkenest to prayer.\" ", 

            "If he is riding upon an ass, he should alight and say the Tefillah ;", 

            " but if he is unable to alight, he should turn his face [in the direction of Jerusalem] If he is unable to turn his face, he should direct his heart towards the Holy of Holies. ", 

            "If he is journeying in a ship or on a raft, he should direct his heart towards the Holy of Holies. ", 

            "GEMARA To what do these eighteen benedictions correspond ? ", 

            "R. Hillel, the son of R. Samuel b. Nahmani, said : ", 

            "They correspond to the eighteen times the Divine Name [JHWH] is mentioned by David  in the Psalm \"Ascribe unto the Lord, O ye sons of might\" (Ps.xxix).", 

            " Rab Joseph said :", 

            " They correspond to the eighteen times the Divine Name[1] is mentioned in the Shema'. ", 

            "R. Tanhum said in the name of R. Joshua b. Levi :", 

            " They correspond to the eighteen vertebrae in the spinal column. ", 

            "R. Tanhum also said in the name of R. Joshua b. Levi : ", 

            "When one says the Tefillah, he must bow[2] until all the vertebrae in the spine are loosened.", 

            " 'Ulla said : ", 

            "[He must bow] until he sees a ring [of flesh formed] opposite his heart. ", 

            "R. Hannina said : ", 

            "If he lowered his head, more than that is unnecessary. ", 

            "Raba said :", 

            " That is so, if it gives him pain [to bow low] and he appears like one making obeisance. ", 

            "As to those eighteen benedictions — there are nineteen !", 

            " R. Levi said : ", 

            "The benediction relating to the Minim[3] was subsequently instituted at Jabneh[4]. ", 

            "Corresponding to what was it instituted? ", 

            "R. Levi said : ", 

            "According to R. Hillel, the son of R. Samuel b. Nahmani[1], it corresponds to \"The God [el]", 

            " of glory thundereth\" (Ps. xxix. 3) ; according to Rab Joseph, it corresponds to \"One\" in the Shema' ;", 

            "according to R. Tanhum in the name of R. Joshua b. Levi, it corresponds to the small vertebra in the spinal column. ", 

            "Our Rabbis have taught :", 

            " Simeon the Cotton-dealer[3] arranged the eighteen benedictions in order in the presence of Rabban Gamaliel at Jabneh. ", 

            "Rabban Gamaliel asked the Sages,", 

            " \"Is there anyone who knows how to word the benediction relating to the Minim?\" ", 

            "Samuel the Small stood up and worded it.  In the  following year he had forgotten it[4], "

        ], 

        [

            "and reflected for two or three hours[5] ; but they did not discharge him[6]. ", 

            "Why did they not discharge him ?", 

            " For lo, Rab Judah said in the name of Rab :", 

            " If [the Precentor] errs in all the [eighteen] benedictions we do not discharge him ; but [if he errs] in the benediction relating to the Minim we do discharge him, for fear that he is a Min !", 

            " It was different with Samuel the Small, because he had himself worded it. ", 

            "But there may be a fear that perhaps he had apostatized ! ", 

            "Abbai said : We have a tradition that ", 

            "a good man does not become bad. ", 

            "He does not ? ", 

            "Behold it is written, \"But when the righteous turneth away from his righteousness and committeth iniquity\" (Ezek. xviii. 24)! ", 

            "That refers to a man who was originally wicked[7]; but the man who is originally righteous does not. ", 

            "He does not ? ", 

            "Behold there is a Mishnaic teaching : ", 

            "\"Trust not in thyself until the day of thy death[8]\" ; and Johanan the High Priest held the Office of High Priest for eighty years and eventually became a Sadducee ! ", 

            "Abbai said :", 

            " Johanan is the same person as Januaeus[9]. ", 

            "Raba said : ", 

            "They are different persons ; and Jannaeus was originally wicked, but Johanan originally righteous.", 

            " That is quite right according to Abbai[1] ; but it is in contradiction with Raba's view[2]. ", 

            "Raba can reply that even with one who was ", 

            "originally righteous there is the possibility of his apostatizing. ", 

            "If so, why did they not discharge [Samuel the Small]?", 

            " It was different with him, because he had already commenced it[3]. ", 

            "For Rab Judah in the name of Rab (another version : R. Joshua b. Levi) said : ", 

            "This teaching[4] applies only to one who has not commenced it ; but if he had commenced it, he may finish it. ", 

            "To what do the seven Sabbath-benedictions[5] correspond ? ", 

            "R. Halafta b. Saul said:", 

            " To the seven \"voices\" which David mentioned concerning the waters (Ps. xxix.).", 

            " To what do the nine benedictions in the New Year Tefillah[6] correspond ? ", 

            "R. Isaac[7] of Kartignin[8] said :", 

            " To the nine references to the Divine Name which Hannah made in her prayer (I Sam. ii. 1-10) ; for the teacher said :", 

            " On the New Year's day ", 

            "Sarah, Rachel and Hannah were \"visited.\" ", 

            "To what do the twenty-four benedictions of the fast day[9] correspond ? ", 

            "R. Helbo said: ", 

            "To the twenty-four \"cries[10]\" Solomon mentioned when he brought the Ark into the house of the Holy of Holies (I Kings viii.).", 

            " In that case, one should say them every day[11]! ", 

            "[No ;] when did Solomon say them ? On a day of supplication ; and so we likewise say them on a day of supplication. ", 

            "R. Joshua says : The abstract of the eighteen [benedictions]. ", 

            "What is the abstract of the eighteen ?", 

            " Rab said :", 

            " An abstract of each benediction. ", 

            "Samuel said [1] : ", 

            "\"Give us understanding, O Lord, our God, to know Thy ways ; circumcise our hearts to fear Thee, and forgive us so that we may be redeemed. Keep us far from our pains ; satiate us on the pastures of Thy land and gather our scattered ones from the four [corners of the earth]. Let them that go astray be judged according to Thy will, and wave Thy hand over the wicked. Let the righteous rejoice in the rebuilding of Thy city and in the establishment of Thy Temple, and in the flourishing of the horn of David Thy servant, and in the clear-shining light of the son of Jesse, Thine anointed. Even before we call, do Thou answer. Blessed art Thou, O Lord, Who hearkenest unto prayer.\" ", 

            "Abbai cursed him who says the prayer \"Give us understanding[2].\" ", 

            "Rab Nahman said in the name of Samuel : ", 

            "During the whole of the year, one may say the prayer \"Give us understanding\" except at the conclusion of the Sabbath and Festivals, because then it is necessary to say the \"Division\" in the benediction \"Thou favourest man with knowledge[3].\"", 

            " Rabbah b. Samuel[4] objected :", 

            " Let him, then, say the fourth benediction separately[5] !", 

            " Have we not the Mishnaic teaching : R. 'Akiba says : ", 

            "One may say the fourth benediction by itself ; ", 

            "R. Eliezer says :", 

            " [One can say the \"Division\"] in the benediction of thanksgiving[6]?", 

            " But do we act the whole of the year in accordance with R. 'Akiba's view that we should do so now [at the conclusion of the Sabbath and Festivals] ? ", 

            "On what ground do we not follow R. 'Akiba's view during the whole year ? Because eighteen benedictions were instituted, not nineteen ;", 

            " and so here also, seven were instituted, not eight[7]. ", 

            "Mar Zotra objected :", 

            " Let it be included in brief in the [shortened] Tefillah, thus: \"Give us understanding, Thou Who dividest between holy and profane\" ! ", 

            "The question [remained unanswered]. ", 

            "Rab Bebai b. Abbai said :", 

            " The whole of the year one may say the prayer \"Give us understanding\" except during the rainy season[1], because it is necessary to add the request [for rain] in the benediction of \"the Years.\" ", 

            "Mar Zotra objected :", 

            " Let it be included in brief in the [shortened] prayer thus : \"Satiate us on the pastures of Thy land, and give dew and rain\" !", 

            " It would lead to confusion.", 

            " If so, the inclusion of the \"Division\" in the benediction \"Thou favourest man with knowledge\" should likewise lead to confusion ! ", 

            "They answered :", 

            " In this latter case, since it comes at the beginning of the prayer, it would not cause confusion ; but in the former, since it occurs in the middle of the prayer, it would. ", 

            "Rab Ashe objected :", 

            " Let him say it in the benediction \"Who hearkenest unto prayer[2]\" ; ", 

            "for R. Tanhum declared in the name of R. Assi :", 

            " If a man erred and omitted the reference to rain in the benediction of \"the Revival of the Dead[3],\" we make him repeat it ; [if he omitted] the request [for rain] in the benediction of \"the Years,\" we do not make him repeat it, because he can include it in \"Who hearkenest unto prayer\" ; but [if he omitted] the \"Division\" in \"Thou favourest man with knowledge,\" we do not make him repeat it, because he is able to say it over the cup of wine[4] !", 

            " It is different with one who erred. ", 

            "It was mentioned above : \"R. Tanhum declared in the name of R. Assi :", 

            " If a man erred and omitted the reference to rain in the benediction of 'the Revival of the Dead,' we make him repeat it; [if he omitted] the request [for rain] in the benediction of 'the Years,' we do not make him repeat it, because he can include it in 'Who hearkenest unto prayer' ; but [if he omitted] the 'Division' in 'Thou favourest man with knowledge,' we do not make him repeat it, because he is able to say it over the cup of wine!\" ", 

            "Against this is quoted :", 

            " If one erred and omitted the reference to rain in the benediction of \"the Revival of the Dead,\" we make him repeat it ; [if he omitted] the request [for rain] in the benediction of \"the Years,\" we make him repeat it; but [if he omitted] the \"Division\" in \"Thou favourest man with knowledge,\" we do not make him repeat it, because he is able to say it over the cup of wine ! ", 

            "There is no contradiction, ", 

            "the latter referring to one praying alone, the former to one praying with a Congregation. ", 

            "Why should he not repeat it if praying with a Congregation? Because he can hear it from the Precentor[5]. If so [the reason stated above] \"because he can include it in 'Who hearkenest unto prayer'\" should rather be, because he can hear it from the Precentor ! ", 

            "Nay, both the teachings refer to one praying alone and there is no contradiction ;", 

            " the statement [of R. Tanhum] refers to one who reminds himself [that he had omitted the prayer for rain] before reaching the benediction \"Who hearkenest unto  prayer[1],\"  "

        ], 

        [

            "whereas the statement [of the Baraita] refers to one who reminds himself [of the omission] after having said the benediction \"Who hearkenest unto prayer.\" ", 

            "R. Tanhum said in the name of R. Assi[2], in the name of R. Joshua b. Levi :", 

            " If a man erred and omitted the reference to the New Moon in the sixteenth benediction[3], he must repeat it. If he reminded himself thereof in the seventeenth benediction, he goes back to the sixteenth ; if in the eighteenth, he goes back to the sixteenth. If he had concluded the Tefillah, he must recommence it. ", 

            "Rab Pappa the son of Rab Aha b. Adda said :", 

            " The statement \"If he had concluded the Tefillah, he must recommence it\" only applies should he have moved his feet[4] ; but if he has not done so, he returns to the sixteenth benediction. ", 

            "He was asked : ", 

            "Whence hast thou obtained this teaching? ", 

            "He replied:", 

            " From my father my teacher have I heard it, and he from Rab[5]. ", 

            "Rab Nahman b. Isaac said : ", 

            "The statement that if he had moved his feet he must recommence the Tefillah applies only to one who is not accustomed to offer personal supplications at its conclusion[6] ; but if that be his practice, he returns to the sixteenth benediction. ", 

            "Another version is : Rab Nahman b. Isaac said : ", 

            "The statement that if he had not moved his feet, he returns to the sixteenth benediction applies only to one who is accustomed to offer personal supplication at the conclusion of the Tefillah ; but if that be not his practice, he goes back to its commencement. ", 

            "R. Eliezer says :", 

            " If one makes his prayer a fixed task [keba'], his prayer is not supplication. ", 

            "What means keba'?", 

            " R. Jacob b. Iddi said in the name of R. Osha'ya : ", 

            "Anyone whose prayer seems to him a burden. ", 

            "The Rabbis say : ", 

            "Anyone who does not recite it in language of supplication[7]. ", 

            "Rabbah and Rab Joseph both said : ", 

            "Anyone who is not able to add something new thereto[1]. ", 

            "R. Zera said :", 

            " I am able to add something new, but I am afraid that I may become confused. ", 

            "Abbai b. Abin and R. Hannina b. Abin both said :", 

            " [His prayer is keba'] who does not pray at dawn and sunset[2] ;  for R. Hiyya b. Abba said in the name of R. Johanan :", 

            " It is a religious duty to pray at dawn and sunset. ", 

            "R. Zera said : ", 

            "What Scriptural authority is there for this? \"They shall fear Thee with the sun and before the moon[3] throughout all generations\" (Ps. Ixxii. 5).", 

            " In the West[4], they cursed anyone who prayed at those times. Why? ", 

            "Perhaps the time will be unsuitable for him[5]. ", 

            "R. Joshua says : If one is journeying in a place of danger, he should offer a short prayer, saying : \"Save, O Lord, Thy people, the remnant of Israel ; in all times of crisis may their needs be before Thee.\" ", 

            "What means \"times of crisis ['ibbur]\"? ", 

            "Rab Hisda said in the name of Mar 'Ukba : ", 

            "Even at the time when Thou art full of wrath ['ebrah] against them like a woman big with child ['ubberet], may all their needs be before Thee.", 

            " Another version is : Rab Hisda said in the name of Mar 'Ukba :", 

            " Even at the time when they transgress ['oberim] the words of Torah, may all their needs be before Thee. ", 

            "Our Rabbis have taught : ", 

            "He who journeys in a place of herds of wild beasts or bands of robbers should offer a short prayer.", 

            " Which is the short prayer ?", 

            " R. Eliezer said :", 

            " \"Do Thy will in Heaven above ; grant tranquility of spirit to those who fear Thee below, and do that which is good in Thy sight. Blessed art Thou, O Lord, Who hearkenest unto prayer.\"", 

            " R. Joshua said : ", 

            "\"Hear the lament of Thy people Israel, and speedily fulfil their request. Blessed art Thou, O Lord, Who hearkenest unto prayer.\"", 

            "R. Eleazar b. Sadok said :", 

            " \"Hear the cry of Thy people Israel, and speedily fulfil their request. Blessed art Thou, O Lord, Who hearkenest unto prayer.\"", 

            " Others say :", 

            " \"The needs of Thy people Israel are many but their mind short[6]. May it be Thy will, O Lord our God, to grant each one sufficient for his maintenance, and to every person enough for his want. Blessed art Thou, O Lord, Who hearkenest unto prayer.\" ", 

            "Rab Huna said : ", 

            "The Halakah is in accord with the \"others.\" ", 

            "Elijah[1] said to Rab Judah, the brother of Rab Sala Hasida :", 

            " \"Be not wrathful and thou wilt not sin. Be not intoxicated and thou wilt not sin. When thou settest out on a journey, take counsel with thy Creator and go forth.\" ", 

            "What means, \"Take counsel with thy Creator and go forth\" ?", 

            " R. Jacob said in the name of Rab Hisda : ", 

            "This refers to the prayer to be offered on undertaking a journey. ", 

            "R. Jacob also said in the name of Rab Hisda : ", 

            "Whoever sets out on a journey should offer the prayer ordained for a journey. ", 

            "What is this prayer?", 

            " \"May it be Thy will, O Lord my God, to conduct me in peace, to direct my steps in peace, to uphold me in peace, and to deliver me from every enemy and ambush by the way. Send a blessing upon the work of my hands, and let me obtain grace, lovingkindness and mercy in Thine eyes and in the eyes of all who behold me. Blessed art Thou, O Lord, Who hearkenest unto prayer[2].\" ", 

            "Abbai said : ", 

            "Always  "

        ], 

        [

            "should a man associate himself with the Community[3].", 

            " How should he pray ?", 

            " \"May it be Thy will, O Lord our God, to conduct us in peace\" etc. ", 

            "When should he ofter this prayer ? ", 

            "R. Jacob said in the name of Rab Hisda : ", 

            "From the time he sets forth on his journey. ", 

            "And how long[4]? ", 

            "R. Jacob said in the name of Rab Hisda: ", 

            "The distance of a Parsah. ", 

            "And how should he offer it ?", 

            "Rab Hisda said : ", 

            "Standing ;", 

            " Rab Sheshet said : ", 

            "Even while journeying. ", 

            "Rab Hisda and Rab Sheshet were once on a journey together. Rab Hisda stood up and offered the prayer. ", 

            "Rab Sheshet[5] said to his attendant, ", 

            "\"What is Rab Hisda doing?\" ", 

            "He replied, ", 

            "\"He is standing and praying.\"", 

            " He said to him,", 

            " \"Raise also me up and I too will pray ; for if thou canst be good, do not allow thyself to be called evil[6].\" ", 

            "\"What is the difference between \"Give us understanding[1]\" and the short prayer[2]? ", 

            "\"Give us understanding\" requires three benedictions before and three after it[3], and when he reaches his house, he need not again say the Tefillah ; ", 

            "whereas with the short prayer there is no necessity to utter the three benedictions before and after, but when he reaches his house, he must say the Tefillah. ", 

            "The Halakah is also that", 

            " \"Give us understanding\" must be said standing, but the short prayer can be said either standing or journeying. ", 

            "If he is riding upon an ass, he should alight and say the Tefillah.", 

            "Our Rabbis have taught :", 

            " If a man is riding upon an ass and the time of the Tefillah arrives, should he have somebody to hold his ass, he must alight and pray ; but if not, he sits in his place and prays. ", 

            "Rabbi says : ", 

            "In either case, he should sit in his place and pray, because his mind is unsettled. ", 

            "Raba[4] (another version : R. Joshua b. Levi) said : ", 

            "The Halakah is in agreement with Rabbi.  ", 

            "Our Rabbis have taught : A blind man or one who is unable to locate the directions should direct his heart to his Father in Heaven ; as it is said, \"And they pray unto the Lord\" (I Kings viii. 44).", 

            " If he is standing outside the [Holy] Land, he must direct his heart towards the land of Israel ; as it is said, ", 

            "\"And pray unto Thee toward their land\" (ibid. v. 48).", 

            " If he is standing in the land of Israel, he must direct his heart towards Jerusalem ; as it is said,", 

            " \"And they pray unto the Lord toward the city which Thou hast chosen\" (ibid. v. 44).", 

            " If he is standing in Jerusalem, he must direct his heart towards the Temple ; as it is said, ", 

            "\"And pray toward this house\" (II Chron. vi. 32).", 

            " If he is standing in the Temple, he must direct his heart towards the Holy of Holies; as it is said,", 

            " \"And they pray toward this place\" (I Kings viii. 35). ", 

            "If he is standing in the Holy of Holies, he must direct his heart towards the mercy-seat[5].", 

            " If he is standing behind the mercy-seat, he must imagine himself to be in front of it. ", 

            "Consequently", 

            " if he is standing in the East, he must turn West ; if in the West, he must turn East ; if in the South, he must turn North ; if in the North, he must turn South.", 

            " As a result, all Israel will be directing their heart to one spot. ", 

            "R. Abin (another version : R. Abina) said : ", 

            "What Scriptural authority is there for this ? \"Thy neck is like the tower of David, builded with turrets [talpiyyot] (Cant, iv. 4), i.e. a heap [tel] for all mouths [piyyot][1]. ", 

            "Samuel's father and Levi, when they wished to set out on a journey, used to rise up early[2] and say the Tefillah; and when the time arrived for reading the Shema' ", 

            "they read it then[3].", 

            " In accord with whose opinion is this ? ", 

            "That of the Tanna of the teaching : If one rises early to set out on a journey, they may bring him a Shofar[4] which he blows, a Lulab which he shakes, a Megillah in which he reads ; and when the time arrives for reading the Shema' he reads it. ", 

            "If he rose early to sit in a travelling coach or ship, he may say the Tefillah, and when the time arrives for reading the Shema' he reads it. ", 

            "R. Simeon b. Eleazar says :", 

            " In all circumstances, he reads the Shema' and then says the Tefillah in order to unite it with the Ge'ullah.", 

            " In what do they differ ?", 

            " The former holds that ", 

            "to say the Tefillah standing is of greater importance[5]; the latter holds that ", 

            "to unite the Ge'ullah with the Tefillah is of greater importance. ", 

            "Maremar and Mar Zotra used to gather in their house ten men[6] on the Sabbath preceding a Festival[7], say the prayers and then go to the study-session. ", 

            "Rab Ashe used to say the prayers in the presence of the assembly alone and sitting[8], and when he returned to his house, he again said the Tefillah standing.", 

            " The Rabbis said to him,", 

            " \"The master should act like Maremar and Mar Zotra[9].\" ", 

            "He replied,", 

            " \"It is too much trouble for me.\"", 

            " \"Then let the master act like Samuel's father and Levi[10].\" ", 

            "He replied, ", 

            "\"We have not seen the Rabbis who are older than we acting in this manner.\" ", 

            "MISHNAH  R. Eleazar b. 'Azariah says : ", 

            "The additional Tefillah is only to be said with the local Congregation. The Sages say:", 

            " Whether with or without the local Congregation. ", 

            "R. Judah says in his name[1]: ", 

            "In any place where there is a local Congregation, the individual is exempt from the additional Tefillah[2]. ", 

            "GEMARA R. Judah is identical with the first Tanna's view ! ", 

            "There is a difference between them, viz. : ", 

            "an individual who lives in a place where there is no local Congregation[3]. ", 

            "The first Tanna holds that ", 

            "he is exempt [from the additional Tefillah], but R. Judah holds that ", 

            "he is under the obligation. ", 

            "Rab Huna b. Hinnana[4] said in the name of Rab Hiyya b. Rab[5] : ", 

            "The Halakah is in agreement with R. Judah as stated in the name of R. Eleazar b. 'Azariah.", 

            " Rab Hiyya b. Abin said to him : ", 

            "Thou hast said well ; for Samuel has declared : ", 

            "Never have I said the additional Tefillah alone "

        ], 

        [

            " in  Nehardea[6] except on the day when the king's army came to the town[7], and the Rabbis were so troubled that they did not say the Tefillah, and I said it alone, because I was like an individual without a local Congregation. ", 

            "R. Hannina the Bible-teacher sat before R. Jannai ; as he sat he said,", 

            " \"The Halakah is in agreement with R. Judah as stated in the name of R. Eleazar b. 'Azariah.\" ", 

            "He said to him,", 

            " \"Go out and read thy Bible verses in the street[8], ", 

            "for the Halakah is not in agreement with R. Judah as stated in the name of R. Eleazar b. 'Azariah.\"", 

            " R. Johanan said, ", 

            "\"I noticed that R. Jannai said the Tefillah and then said another Tefillah[9].\" ", 

            "R. Jeremiah said to R. Zera, ", 

            "\"Perhaps he did not at first direct his heart [to his prayer] and finally did so[1]!\"", 

            " He replied, ", 

            "\"See how great a man testifies concerning him[2].\" ", 

            "Although there were thirteen Synagogues in Tiberias[3], R. Ammi and R. Assi never said the Tefillah except between the pillars where they studied[4]. ", 

            "It has been reported : Rab Isaac b. Abdemi said in the name of our teacher[5] : ", 

            "The Halakah is in agreement with R. Judah as stated in the name of R. Eleazar b. 'Azariah. ", 

            "R. Hiyya b. Abba said the Tefillah[6] and then said another. ", 

            "R. Zera asked him, ", 

            "\"Why did the master act so?", 

            " Is it because the master did not direct his heart [with the first] ? But R. Eleazar has said :", 

            " A man should always examine himself; if he can direct his heart, then let him pray, but if not, he should not pray !", 

            " Or is it because the master did not include the reference to the New Moon [in the first Tefillah][7]? But there is a teaching:", 

            " If a man erred and omitted the reference to the New Moon in the evening Tefillah, we do not require him to repeat it, because he can say it in the morning Tefillah; [if he omitted it] in the morning, we do not require him to repeat it, because he can say it in the additional Tefillah ; [if he omitted it] in the additional Tefillah, we do not require him to repeat it, because he can say it in the afternoon ! \" ", 

            "He replied,", 

            " \"Has it not been reported in this connection : R. Johanan declared that this teaching applies only to a Congregation[8]?\" ", 

            "How long must one wait between Tefillah and Tefillah[9]?", 

            " Rab Huna and Rab Hisda [differ]. One said : ", 

            "Until his mind can offer supplication ;", 

            " the other said : ", 

            "Until his mind can offer beseeching prayer. ", 

            "He who says : Until his mind can offer supplication [tithonen], it is because it is said, ", 

            "\"And I supplicated [waethannan] the Lord\" (Deut. iii. 23) ;", 

            " and he who says : Until his mind can offer beseeching prayer [titholel], it is because it is written, \"And Moses besought [wayyehal] the Lord\" (Exod. xxxii. 11). ", 

            "Rab 'Anan said in the name of Rab :", 

            " If a man erred and omitted the reference to the New Moon in the evening Tefillah, we do not require him to repeat it, because the Bet Din only consecrate the new month in the day-time. ", 

            "Amemar said :", 

            "It is probable that Rab's statement applies to a full month[1] ; but in the case of a detective month, we require him to repeat it. ", 

            "Rab Ashe said to Amemar : ", 

            "Since Rab has stated a reason[2], what has it to do whether the month is full or defective ! ", 

            "Certainly there is no difference. ", 

            "May we return unto thee : The morning Tefillah ! ", 

            "MISHNAH One must not stand up to say the Tefillah except in a serious frame of mind[1].", 

            " The pious men of old[2] used to wait an hour[3] and then say the Tefillah, in order to direct their heart to their Father in Heaven. ", 

            "Even when a king ", 

            "greets him, he must not respond ; and though a serpent be wound round his heel, he must not interrupt. ", 

            "GEMARA Whence is this teaching derived[4]? ", 

            "R. Eleazar said :", 

            " For the Scriptures state, ", 

            "\"She was in bitterness of soul and prayed unto the Lord\" (I Sam. i. 10). ", 

            "How is it derived from this verse? ", 

            "Perhaps it was different with Hannah since she was very sore of heart ! ", 

            "But said R. Jose b. R. Hannina : [Derive it] from the following : ", 

            "\"But as for me, in the abundance of Thy lovingkindness will I come into Thy house ; I will bow down toward Thy holy Temple in the fear of Thee\" (Ps. v. 8). ", 

            "How is it derived from this verse ? Perhaps it was different with David, since he afflicted his soul exceedingly in prayer ! ", 

            "But said R, Joshua b. Levi : [Derive it] from the following : ", 

            "\"Worship", 

            " the Lord in the beauty of holiness\" (ibid. xxix. 2) — read not \"beauty\" [hadrat] but \"trembling\" [herdat]. ", 

            "How is it derived from this verse ?", 

            " Perhaps I may indeed tell thee that \"in the beauty of holiness\" is to be understood literally, as with Rab Judah who used to adorn himself[5] and then pray ! ", 

            "But said Rab Nahman b. Isaac : [Derive it] from the following :", 

            " \"Serve the Lord with fear, and rejoice with trembling\" (ibid. ii. 11). ", 

            "What means \"rejoice with trembling\"?", 

            " Rab Adda b. Mattena said in the name of Rabbah[6]: ", 

            "Where there is rejoicing[7] let there be trembling. ", 

            "Abbai was sitting in the presence of Rabbah, and noticed that he was very merry.", 

            " He said to him,", 

            " \"It is written, 'Rejoice with trembling'!\" ", 

            "He replied, ", 

            "\"I have laid the Tefillin[1].\" ", 

            "R. Jeremiah was sitting in the presence of R. Zera, and noticed that he was very merry. He said to him, \"It is written, 'In all pain[2] there is profit'!\" (Prov. xiv. 23). ", 

            "He replied, ", 

            "\"I have laid the Tefillin.\" ", 

            "Mar b. Rabina made a wedding-feast for his son, and noticed that the Rabbis were very merry. "

        ], 

        [

            "He seized a costly goblet[3] worth four hundred Zuz and broke it before them, and", 

            "they became more serious. ", 

            "Rab Ashe made a wedding-feast for his son, and noticed that the Rabbis were very merry. He seized a goblet of white crystal and broke it before them, and they became more serious. ", 

            "The Rabbis said to Rab Hamnuna the Small[4] at the wedding-feast of Mar b. Rabina, ", 

            "\"Let the master sing for us.\"", 

            " He replied to them,", 

            " \"Woe to us for we are destined to die! Woe to us for we are destined to die!\" ", 

            "They said to him, ", 

            "\"What can we answer after thee ?\" ", 

            "He said to them,", 

            " \"Where is the Torah and where the religious precept which will protect us[5]?\" ", 

            "R. Johanan said in the name of R. Simeon b. Johai :", 

            " It is forbidden that a man's mouth be filled with laughter in this world ; because it is written,", 

            " \"Then will our mouth be filled with laughter, and our tongue with singing\" (Ps. cxxvi. 2). When ? At the time when \"They will say among the nations. The Lord hath done great things with these\" (ibid.).", 

            " It was said of R. Simeon b. Lakish that never again was his mouth full of laughter in this world after hearing this teaching from his master R. Johanan[6]. ", 

            "Our Rabbis have taught : ", 

            "One must not stand up to say the Tefillah immediately after being engaged in a lawsuit or the discussion of a Halakah[7] ; but he may do so after the discussion of a Halakah which has been decided. ", 

            "What is meant by a Halakah which has been decided ?", 

            " Abbai said : ", 

            "Like that of R. Zera who stated :", 

            " The daughters of Israel are very strict with themselves ; for if they see even a drop of menstrual flow as small as a mustard seed, they wait seven clear days after it. ", 

            "Raba said :", 

            " Like that of Rab Hosha'ya who stated : ", 

            "A man should act cunningly with his produce, and store it together with the chaff, so that his cattle may eat of it and it become exempt from the tithe[1].", 

            " If thou wilt I can say ", 

            "like that of Rab Huna who stated in the name of R. Ze'ira[2] : ", 

            "He who draws blood from an animal destined for a sacritice is forbidden to make use of it, and [should he use it] he must bring a transgression-offering[3]. ", 

            "The Rabbis act according to our Miahnah[4] ; Rab Ashe acted according to the Baraita[5]. ", 

            "Our Rabbis have taught :", 

            " One must not stand up to say the Tefillah from the midst of sorrow, idleness, jocularity, [frivolous] conversation, levity, or idle chatter, but only from the midst of the joy of a religious duty.", 

            " Similarly a man should not take leave of another from the midst of [frivolous] conversation, jocularity, levity, or idle chatter ; but from the midst of a discussion of Halakah. For so we find that the former prophets used to conclude their addresses with words of praise and consolation.", 

            " So also Mari the son of[6] Rab Huna the son of R. Jeremiah b. Abba taught : ", 

            "A man should not take leave of another except from the midst of a discussion of Halakah, so that he may remember him thereby. ", 

            "Thus, Rab Kahana[7] accompanied Rab Shimi b. Ashe from Pom-Nahara[8] to Be-Sinyata[9] in Babylon.", 

            "When he arrived there, he said to him,", 

            " \"Is it true what people say that", 

            " these Babylonian palms are from the time of Adam till now ?\"", 

            " He answered, ", 

            "\"Thou hast reminded me of something which R. Jose b. R. Hannina said, viz. : ", 

            "What means that which is written, 'Through a land that no man passed through, and where no man dwelt' (Jer. ii. 6) ? Since no man passed through it, how could anyone dwell there !", 

            " But it intends to tell us that", 

            " every land concerning which Adam decreed that it should be inhabited has become inhabited, and every land concerning which Adam did not so decree has not been inhabited[1].\" ", 

            "Rab Mordecai accompanied Rab Ashe[2] from Hagronya[3] to Be-Kipe[4] ; another version :", 

            " to Be-Dura[5]. ", 

            "Our Rabbis have taught : ", 

            "He who prays must direct his heart to Heaven. ", 

            "Abba Saul said: A [Biblical] indication for this matter is :", 

            " \"Thou wilt direct their heart, Thou wilt cause Thine ear to attend\" (Ps. x. 17). ", 

            "There is a teaching: R. Judah said:", 

            " It was the practice of R. 'Akiba, when he said the Tefillah with the Congregation, to shorten [the time in which he said it] and step back[6], so as to avoid troubling the Congregation[7]; but when he said the Tefillah alone, a man might leave him in one corner and find him in another corner. And why so? Because of his bowings and genuflections. ", 

            "R. Hiyya b. Abba said : ", 

            "A man should always pray in a room which has windows ; as it is said, ", 

            "\"Now his windows were open in his upper chamber towards Jerusalem\" (Dan. vi. 11).", 

            " It is possible to imagine that a man can pray all the day long ; but it has already been clearly stated by Daniel, ", 

            "\"And he kneeled upon his knees three times a day and prayed, and gave thanks before his God \" (ibid.). ", 

            "It is possible to imagine that only when he was taken into captivity, he commenced to pray thus ;", 

            " but it has been said,", 

            " \"As he did aforetime\" (ibid.).", 

            " It is possible to imagine that one can pray in any direction he wishes; ", 

            "therefore there is a teaching to state, \"Towards Jerusalem\" (ibid.).", 

            " It is possible to imagine that a man can include all his prayers in one act of devotion ; but it has already been clearly stated by David,", 

            " \"Evening and morning and at noonday\" (Ps. Iv. 18).", 

            " It is possible to imagine that one should utter his prayers aloud ;", 

            " but it has already been clearly stated by Hannah, viz.", 

            " \"Her voice could not be heard\" (I Sam. i. 13).", 

            " It is possible to imagine that a man could pray for his own needs and afterwards say the statutory prayers ; ", 

            "but it has already been clearly stated by Solomon, viz.", 

            " \"To hearken unto the cry and to the prayer\" (I Kings viii. 28) — \"cry\" means statutory prayer, and \"prayer\" means personal supplication. ", 

            "One may not offer anything [of personal supplication] after \"True and firm[1]\": but after the Tefillah, he can say something even like the order of confession for the Day of Atonement[2], ", 

            "It has been likewise reported : R. Hiyya b. Ashe declared in the name of Rab :", 

            " Although it has been said that one may pray for his personal needs in the benediction \"Who hearkenest unto prayer[3],\" if he desires to add after the Tefillah even something like the order of [confession for] the Day of Atonement, he may do so. ", 

            "Rab Hamnuna said :", 

            " How many weighty Halakot there are to be learnt from the passage relating to Hannah !", 

            " \"Now Hannah, she spake in her heart\" (I Sam. i. 13) — hence it is deduced that one who prays must direct his heart. ", 

            "\"Only her lips moved\" — hence, one who prays must pronounce [the words] with his lips. ", 

            "\"But her voice was not heard\" — hence, it is forbidden to raise the voice when praying.", 

            " \"Therefore Eli thought she had been drunken\" — hence, it is forbidden to pray when intoxicated. \"And Eli said to her. How long wilt thou be drunken?\" (ibid. v. 14) — [[fol. 31 b.]] R. Eleazar said: ", 

            "Hence, if one sees in his neighbour  "

        ], 

        [

            "anything that is unseemly, he must rebuke him.", 

            "\"And Hannah answered and said, No, my lord\" (ibid. v. 15) — 'Ulla (another version: R. Jose b. R. Hannina) declared : ", 

            "She said to Eli, \"Thou art not 'a lord' in this affair, nor does the Holy Spirit rest upon thee, seeing thou hast suspected me of this thing.\" ", 

            "Some declare that she spoke to him thus :", 

            " \"Thou art not a lord ; neither the Shekinah nor the Holy Spirit is with thee, for thou hast judged me in the scale of guilt and not in the scale of merit[4]. Dost thou not know 'I am a woman of sorrowful spirit'?\"", 

            " \"I have drunk neither wine nor strong drink\" — R. Eleazar said : ", 

            "Hence it is deduced that one who is wrongly suspected must clear himself. ", 

            "\"Count not thy handmaid for a wicked woman\" (I Sam. i. 16) — R. Eleazar said : ", 

            "Hence it is inferred that if a drunken person prays, it is as though he practised idolatry; for it is written here \"a wicked woman[1],\" and elsewhere it is written, \"Certain base fellows[2] are gone out from the midst of thee\" (Deut. xiii. 14) — as the reference in this latter passage is to idolatry, so also in the other passage idolatry is intended.", 

            " \"Then Eli answered and said, Go in peace\" (I Sam. i. 17) — R. Eleazar said : ", 

            "Hence, if one wrongly suspected another, he must conciliate him ;", 

            " nay more, he must bless him ; as it is said, ", 

            "\"And the God of Israel grant thy petition\" (ibid.). ", 

            "\"And she vowed a vow and said, O Lord of hosts\" (ibid. v. 11) — R. Eleazar said :", 

            " From the day that the Holy One, blessed be He, created His universe, there was nobody who called Him \"[Lord of] hosts\" until Hannah came and gave Him that designation. ", 

            "Hannah said before the Holy One, blessed be He, ", 

            "\"Lord of the universe ! From all the multitudes of hosts which Thou hast created in Thy universe, is it hard in Thine eyes to grant me even one son?\" ", 

            "A parable : To what is the matter like ? To a human king who made a feast for his servants. A poor man came and stood at the entrance and said to them,", 

            " \"Give me a morsel of bread\" ;", 

            " but they took no notice of him.", 

            " He pushed his way through and entered the presence of the king, ", 

            "exclaiming,", 

            " \"My lord, the king ! From all the feast which thou hast made, is it hard in thine eyes to spare me a morsel of bread ?\" ", 

            "\"If thou wilt indeed look[3]\" (ibid.) — R. Eleazar said: ", 

            "Thus spake Hannah before the Holy One, blessed be He, ", 

            "\"Lord of the universe ! If Thou wilt look, well and good ; but if Thou wilt not look, I will go and seclude myself [with another man][4] before Elkanah my husband ; and having done so, they will administer to me the waters of the woman suspected of adultery, and Thou wilt surely not make Thy Torah a fraud ; for it is said,", 

            " 'Then she shall be cleared, and shall conceive seed'\" (Num. v. 28).", 

            " This is quite right for him who maintains that if [the woman wrongly suspected] was barren, then she will conceive ; but according to him who maintains [that as the result of her proved innocence], if she usually gave birth in pain she now gives birth with ease, [if she usually brought forth] daughters she now brings forth sons[1], [if she usually brought forth] dark[2] children she now brings forth fair children, [if she usually brought forth] short children she now brings forth tall children — what is there to say[3]?", 

            " For there is a teaching :", 

            " \"Then she shall be cleared, and shall conceive seed\" — this teaches that if she had been barren she now conceives; these are the words of R. Ishmael. ", 

            "R. 'Akiba said to him :", 

            " In that case, all barren women will go and lay themselves under suspicion, and she who has not done wrong [after receiving the waters] will conceive ! ", 

            "Nay,", 

            " it teaches, that if she usually gave birth in pain, she now gives birth with ease ; that she will have tall children instead of short, fair instead of dark, two instead of one. ", 

            "But how is \"If Thou wilt indeed look\" to be explained[4]? The Torah speaks according to the language of the sons of man[5]. ", 

            "\"[If Thou wilt indeed look] on the affliction of Thy handmaid, and remember me, and not forget Thy handmaid, but wilt give unto Thy handmaid\" (I Sam. i. 11). ", 

            "R. Jose b. R. Hannina said : ", 

            "Why is \"Thy handmaid\" repeated thrice ? Hannah spake before the Holy One, blessed be He, ", 

            "\"Lord of the universe ! Three breaches [bidke] through which death comes[6] hast Thou created in a woman ; ", 

            "(another version : Three causes [dibke] of death), viz, : ", 

            "neglect of the laws concerning menstruation, Hallah and kindling the Sabbath-lights[7]. Have I transgressed any of them?\" ", 

            "\"But wilt give Thy handmaid seed of men\" (ibid.). What means \"seed of men\"?", 

            " Rab said : ", 

            "A man among men[8]. ", 

            "Samuel said : ", 

            "Seed which will anoint two men ; and who are they ? Saul and David. ", 

            "R. Johanan said : ", 

            "Seed equal to two men ; and who are they? Moses and Aaron ; as it is said,", 

            " \"Moses and Aaron among His priests, and Samuel among them that call upon His name\" (Ps. xcix. 6). ", 

            "The Rabbis say : ", 

            "\"Seed of men\" means seed which will be swallowed up among men[9]. ", 

            "When Rab Dimai came [from Palestine] he explained [the words of the Rabbis to mean] : ", 

            "neither tall nor dwarfish nor short, neither dark[1] nor ruddy nor pale, neither too wise nor too foolish. ", 

            "\"I am the woman that stood by thee here\" (I Sam. i. 26). R. Joshua b. Levi said : ", 

            "Hence it is deduced that it is forbidden to sit within four cubits of [one engaged in] prayer[2]. ", 

            "\"For this child I prayed\" (ibid. v. 27). R. Eleazar said : ", 

            "Samuel was one who decided a Halakah in the presence of his master[3] ;", 

            " as it is said, ", 

            "\"And when the bullock was slain, the child was brought to Eli\" (ibid. v. 25). Because \"the bullock was slain,\" therefore \"the child was brought to Eli[4]\"! ", 

            "Nay; but Eli said to them,", 

            " \"Call a priest that he may come and slay [the bullock].\" ", 

            "Samuel saw them going for a priest to slay it? so he said to them,", 

            " \"Why go searching for a priest to slay it? I", 

            "f the act of slaying is performed by a non-priest it is valid.\"", 

            " They brought him before Eli, who asked him,", 

            " \"Whence hast thou this teaching?\" ", 

            "He replied,", 

            " \"Is it written, 'The priest shall slay'?", 

            " It is written, 'The priests shall present the blood' (Lev. i, 5). ", 

            "From the receiving of the blood onwards is the function of the priesthood ; ", 

            "hence, the act of slaying is valid if performed by a non-priest.\"", 

            " Eli said to him,", 

            " \"An excellent teaching hast thou expounded ; still thou art one who decided a Halakah in the presence of thy master[5], and whoever does that incurs the penalty of death.\" ", 

            "Then Hannah came and cried before him, ", 

            "\"I am the woman that stood by thee here.\"", 

            " He said to her, ", 

            "\"Leave me alone that I may punish him, and I will pray that [a son] greater than he be granted thee.\"", 

            " She answered him, ", 

            "\"For this child I prayed.\" ", 

            "\"Now Hannah she spake in[6] her heart\" (I Sam. i. 13) — Eleazar said in the name of R. Jose b. Zimra : ", 

            "[She spoke] about the concerns of her heart. ", 

            "She spake before Him,", 

            " \"Lord of the universe ! In all that Thou hast created in a woman Thou hast created nothing in vain — eyes to see, ears to hear, a nose to smell, a mouth to speak, hands wherewith to do work, feet to walk with, breasts to suckle with. ", 

            "But these breasts which Thou hast placed upon my ", 

            "Give me a son, that I may suckle with them.\" ", 

            "R. Eleazar also said in the name of R. Jose b. Zimra :", 

            " Whoever imposes a fast upon himself on the Sabbath[1], ", 

            "the decree of seventy years is annulled for him[2] ; but for all that the penalty for [denying himself] the delight of the Sabbath will be exacted from him. ", 

            "How can he make amends? ", 

            "Rab Nahman b. Isaac said :", 

            " Let him observe a fast [in expiation] of his fast. ", 

            "R. Eleazar also said : ", 

            "Hannah spoke rebelliously to the Most High; as it is said, ", 

            "\"She prayed against[3] the Lord\" (I Sam. i. 10), which teaches that she spoke rebelliously to the Most High. ", 

            "R. Eleazar also said :", 

            " Elijah spoke rebelliously to the Most High ; as it is said, ", 

            "heart, why have I not occasion to suckle with them? \"For Thou didst turn their heart backward\" (I Kings xviii. 37). ", 

            "R. Samuel b. Rab Isaac said : ", 

            "Whence [do we find] that the Holy One, blessed be He, replied and admitted [the plea of] Elijah ? "

        ], 

        [

            "For it is written, ", 

            "\"[In that day, saith the Lord, will I assemble...] her that I have afflicted\" (Micah iv. 6). ", 

            "Rab Hamma b. R. Hannina said : ", 

            "Were it not for the following three verses, the feet of the enemies of Israel would give way under them[4];", 

            " first, that which is written, ", 

            "\"Her that I have afflicted\" (ibid.); second, that which is written, ", 

            "\"Behold as the clay in the potter's hand, so are ye in My hand, O house of Israel\" (Jer. xviii. 6) ; third,", 

            " that which is written, ", 

            "\"I will take away the stony heart out of your flesh, and I will give you a heart of flesh\" (Ezek. xxxvi. 26). ", 

            "Rab Pappa said : [It may also be learnt] from this passage:", 

            " \"And I will put My spirit within you, and cause you to walk in My statutes\" (ibid. v. 27). ", 

            "R. Eleazar also said : ", 

            "Moses spoke rebelliously to the Most High; as it is said, ", 

            "\"And Moses prayed unto the Lord\" (Num. xi. 2) — ", 

            "read not \"unto [el] the Lord\" but \"against ['al] the Lord\"; for so the school of R. Eliezer b. Jacob interchange the letters aleph and 'ayin. ", 

            "The school of R. Jannai say : [It may be learnt] from the passage", 

            " \"And Di-Zahab\" (Deut. i. 1). What means \"And Di-Zahab\"?", 

            " The school of R. Jannai declare : Thus spake Moses before the Holy One, blessed be He,", 

            " \"Lord of the universe ! It was because of the silver and gold [zahab] which Thou didst bounteously give to Israel until they cried, 'It is sufficient' [dai], that they were induced to make the calf.\"", 

            " The school of R. Jannai said, ", 

            "\"A lion growls not in a den full of straw but in a den full of meat[1].\"", 

            " R. Osha'ya said :", 

            " A parable: [It may be likened] to a man who had a lean cow but of large build. He fed it on horse-beans, and it kicked him. ", 

            "He said to it, ", 

            "\"What caused thee to kick me but the horse-beans on which I fed thee!\"", 

            "R. Hiyya b. Abba said in the name of R. Johanan : ", 

            "A parable : [It may be likened] to a man who had a son. He washed him, anointed him, gave him to eat and drink, tied a purse about his neck, and set him at the entrance of a brothel. How can that son help sinning ? ", 

            "Rab Aha b. Rab Huna said in the name of Rab Sheshet :", 

            " That is what people say : \"He whose stomach is full increaseth deeds of evil\" ; as it is said, ", 

            "\"When they were fed, they became full, they were filled, and their heart was exalted ; therefore have they forgotten Me\" (Hosea xiii. 6). ", 

            "Rab Nahman[2] said : [It may be learnt] from this passage : ", 

            "\"Then thy heart be lifted up, and thou forget the Lord thy God\" (Deut. viii. 14) ; ", 

            "and the Rabbis said from the following:", 

            " \"And they shall have eaten their fill, and waxen fat, and turned unto other gods \" (ibid. xxxi. 20) ; ", 

            "or if thou wilt, from the following :", 

            "\"But Jeshurun waxed fat and kicked \" (ibid, xxxii. 15). ", 

            "R. Samuel b. Nahmani said in the name of R. Jonathan :", 

            " Whence is it that the Holy One, blessed be He, afterwards admitted [the plea of] Moses ? As it is said,", 

            " \"I multiplied unto her silver and gold, which they used for Baal\" (Hosea ii. 10). ", 

            "\"And the Lord spake unto Moses, Go, get thee down\" (Exod. xxxii. 7). What means \"Go, get thee down\" ? ", 

            "R, Eleazar said : The Holy One, blessed be He, spake to Moses, ", 

            "\"Moses, get thee down from thy greatness. ", 

            "Have I given thee greatness but for the sake of Israel? And now that Israel has sinned, what art thou to Me?\"", 

            " Immediately the strength of Moses was weakened, and he had not the power to speak[1].", 

            " But when He said, ", 

            "\"Let Me alone, that I may destroy them\" (Deut. ix. 14), Moses said [to himself],", 

            " \"This matter depends upon me.\" He at once stood up and strengthened himself with prayer and besought mercy [for Israel]. ", 

            "A parable : [It may be likened] to a king who was enraged against his son, and he struck him a violent blow. His friend was sitting in his presence but was afraid to say anything to him.", 

            " The king exclaimed, ", 

            "\"Were it not that my friend were sitting in my presence, I would kill thee.\"", 

            " [The friend] said [to himself], ", 

            "\"This matter depends upon me.\" He at once stood up and rescued him. ", 

            "\"Now therefore let Me alone, that My wrath may wax hot against them and that I may consume them ; and I will make of thee a great nation\" etc. (Exod. xxxii. 10). ", 

            "R. Abbahu[2] said : ", 

            "Were it not explicitly written, it would be impossible to say it ;", 

            " for this teaches that Moses caught hold of the Holy One, blessed be He, like a man who takes hold of his neighbour by his garment, and said before Him,", 

            " \"Lord of the universe ! I will not let Thee alone until Thou forgivest and pardonest them.\" ", 

            "\"I will make of thee a great nation\" etc. R. Eleazar said : Moses spake before the Holy One, blessed be He,", 

            " \"Lord of the universe ! If a stool with three legs[3] cannot stand before Thee in the time of Thy wrath, how much less a stool with but one leg[4] !", 

            " Nay more, I have reason to feel abashed before my ancestors. ", 

            "For now will they say, ", 

            "'Behold the leader whom He appointed over them ! He sought greatness for himself and begged not mercy on their behalf!\" ", 

            "\"And Moses besought [wayyehal] the Lord his God\" (ibid. v. 11). R. Eleazar said : ", 

            "This teaches that Moses stood in prayer before the Holy One, blessed be He, until he wore Him out [hehelehu][5]. ", 

            "Raba said :", 

            " [Moses besought Him] until He annulled His vow for him ; for it is written here wayyehal \"and he besought,\" and elsewhere it is written, \"he shall not break [yahel] his word\" (Num. XXX. 3) ; and a teacher has said :", 

            " [He who makes a vow] cannot break it himself, but others can break it on his behalf[6]. Samuel[1] said: It teaches that Moses jeopardised himself unto death on their behalf[2] ; as it is said, \"And if not, blot me, I pray Thee, out of Thy book which Thou hast written\" (Exod. xxxii. 32). ", 

            "Raba said in the name of Rab Isaac :", 

            " It teaches that he called into play [hal] the attribute of mercy upon them[3]. ", 

            "The Rabbis say :", 

            " It teaches that Moses spake before the Holy One, blessed be He,", 

            " \"Lord of the universe ! It would be profanation [hullin] for Thee to do such a thing.\"", 

            " \"And Moses besought the Lord.\"", 

            " There is a teaching : R. Eliezer the Elder[4] said :", 

            " This teaches that Moses stood in prayer before the Holy One, blessed be He, until ahilu seized him. ", 

            "What means ahilu? ", 

            "R. Eleazar said : ", 

            "The fire of the bones. ", 

            "What means \"fire of the bones\"?", 

            " Abbai said:", 

            " Eshshata degarme[5]. ", 

            "\"Remember Abraham, Isaac and Israel, Thy servants, to whom Thou didst swear by Thine own self\" (ibid. v. 13).", 

            " What means \"By Thine own self\" ? ", 

            "R. Eleazar said : ", 

            "Moses spake before the Holy One, blessed be He,", 

            " \"Lord of the universe ! If Thou hadst sworn", 

            " to them by heaven and earth, I might have said that as heaven and earth will be annulled, so will Thine oath be annulled ;", 

            "but now that Thou hast sworn to them by Thy great name, as Thy great name lives and endures for all eternity, so must Thine oath endure for all eternity.\" ", 

            "\"And Thou saidst unto them, I will multiply your seed as the stars of heaven, and all this land that I have spoken of will I give unto your seed\" (ibid.).", 

            " The phrase \"that I have spoken of\" ", 

            "should rather be \"that Thou hast spoken of\"[6] ! ", 

            "R. Eleazar said :", 

            " Up to here we have the words of the disciple, but from here onwards the words of the Master[7]. ", 

            "R. Samuel b. Nahmani said : ", 

            "All of them are the words of the disciple ; but thus spake Moses before the Holy One, blessed be He, ", 

            "\"Lord of the universe ! The word which Thou saidst unto me, 'Go, speak to Israel,' I went and spoke in Thy name. And now what can I say to them?\" ", 

            "\"Because the Lord was not able [yekolet]\" (Num. xiv. 16). It should have been yakol[1]! ", 

            "R. Eleazar said : Moses spake before the Holy One, blessed be He, ", 

            "\"Lord of the universe ! Now will the nations of the world say, 'His strength has become weak like that of a woman and He is unable to deliver [His people]'!\" ", 

            "The Holy One, blessed be He, said to Moses, ", 

            "\"But have they not already seen the miracles and mighty acts which I wrought for Israel by the Red Sea?\"", 

            " He said before Him, ", 

            "\"Lord of the universe ! They will still be able to say, ", 

            "'Against one king[2] He was able to stand, but not against thirty-one[3]'!\" ", 

            "R. Johanan said : ", 

            "Whence is it that the Holy One, blessed be He, afterwards yielded to Moses? As it is said, \"And the Lord said, I have forgiven according to thy word\" (ibid. v. 20).", 

            " The school of R. Ishmael taught :", 

            " \"According to thy word\" — the nations of the world will say thus,", 

            " \"Happy the disciple to whom his Master yielded.\" ", 

            "\"But in very deed, as I live\" (ibid. v. 21) — ", 

            "Raba said in the name of Rab Isaac : ", 

            "This teaches that the Holy One, blessed be He, said to Moses, ", 

            "\"Moses, thou hast made Me to survive [in the estimation of the peoples] with thy word.\" ", 

            "R. Simlai expounded : ", 

            "A man should always recount the praise of the Holy One, blessed be He, and thereafter pray [for his needs]. ", 

            "Whence have we this? From Moses; for it is written, \"And I besought the Lord at that time, saying\" (Deut. iii. 23). ", 

            "Then it is written, \"O Lord God, Thou hast begun to show Thy servant Thy greatness, and Thy strong hand ; for what god is there in heaven or on earth, that can do according to Thy works, and according to Thy mighty acts ?\" (ibid. v. 24). And after that it is written, \"Let me go over, I pray Thee, and see the good land\" etc. (ibid. v. 25). ", 

            "(Mnemonic: Deeds, Charity, Offering, Priest, Fast, Lock, Iron[4].)  "

        ], 

        [

            "R. Eleazar said : ", 

            "Greater is prayer than good deeds ; ", 

            "for thou hast no one greater in good deeds than Moses, our teacher, nevertheless he was only answered through prayer ; as it is said, ", 

            "\"Speak no more unto Me of this matter\" (ibid. v. 26), which is followed by, \"Get thee up into the top of Pisgah\" (ibid. v. 27)[5]. ", 

            "R. Eleazar also said :", 

            " Greater is fasting than charity.", 

            " What is the reason ? The former [demands the sacrifice] of the person, the latter of money. ", 

            "R. Eleazar also said : ", 

            "Greater is prayer than sacrifices ; as it is said, \"To what purpose is the multitude of your sacrifices unto Me?\" (Is. i. 11), and it is written, \"And when ye spread forth your hands\" (ibid. v. 15)[1].", 

            " R. Johanan said :", 

            " A Kohen who has committed murder must not lift up his hands[2]; as it is said, \"Your hands are full of blood\" (ibid.). ", 

            "R. Eleazar also said : ", 

            "From the day the Temple was destroyed, the gates of prayer were locked ; as it is said,", 

            " \"Yea, when I cry and call for help, He shutteth out my prayer\" (Lam. iii. 8). But although the gates of prayer are locked, the gates of tears remain unlocked ; as it is said, \"Hear my prayer, O Lord, and give ear unto my cry ; keep not silence at my tears\" (Ps. xxxix. 13).", 

            " Raba never proclaimed a fast ", 

            "on a cloudy day, because it is said, \"Thou hast covered Thyself with a cloud, so that no prayer can pass through\" (Lam. iii. 44). ", 

            "R. Eleazar also said : ", 

            "From the day the Temple was destroyed, a wall of iron divides between Israel and their Father in Heaven ; as it is said, \"And take thou unto thee an iron griddle, and set it for a wall of iron between thee and the city\" (Ezek. iv. 3). ", 

            "R. Hannin said in the name of R. Hannina : ", 

            "Whoever prolongs his prayer, his prayer will not return empty. ", 

            "Whence have we this ? From Moses our teacher ; as it is said, ", 

            "\"And I prayed unto the Lord\" (Deut. ix. 26), and it is afterwards written, \"[Now I stayed in the mount... forty days and forty nights ;] and the Lord hearkened unto me that time also\" (ibid. x. 10). ", 

            "But it is not so !", 

            " For R. Hiyya b. Abba has said in the name of R. Johanan : ", 

            "Whoever prolongs his prayer and calculates on it[3] will eventually come to pain of heart ; as it is said,", 

            " \"Hope[4] deferred maketh the heart sick\" (Prov. xiii. 12). What is his remedy? Let him occupy himself with Torah; as it is said, \"But desire fulfilled is a tree of life\" (ibid.), and \"tree of life\" is nothing else than Torah, as it is said, \"It is a tree of life to them that lay hold upon it\" (Prov. iii. 18)! ", 

            "There is no contradiction; the latter teaching refers to one who prolongs his prayer and calculates on it, the former to one who prolongs his prayer without calculating on it. ", 

            "R. Hamma b. Hannina said :", 

            " If a man sees that he prays and is not answered he should repeat his prayer ; as it is said, \"Wait for the Lord ; be strong and let thy heart take courage ; yea, wait thou for the Lord\" (Ps. xxvii. 14). ", 

            "Our Rabbis have taught: Four things require effort, viz. :", 

            " Torah, good deeds, prayer and worldly occupation. ", 

            "Whence is it that Torah and good deeds [require effort] ? As it is said, \"Only be strong and very courageous to observe to do according to all the law\" (Josh. i. 7) —", 

            " \"be strong\" in Torah, and \"very courageous\" in good deeds. ", 

            "Whence is it that prayer [requires effort] ? As it is said, \"Wait for the Lord ; he strong, and let thy heart take courage; yea, wait thou for the Lord\" (Ps. I.c.). ", 

            "Whence is it that worldly occupation [requires effort]? As it is said, \"Be of good courage, and let us prove strong for our people\" etc. (II Sam. X. 12). ", 

            "\"But Zion said. The Lord hath forsaken me, and the Lord hath forgotten me\" (Is. xlix. 14). ", 

            "But a woman forsaken is the same as a woman forgotten ! ", 

            "R. Simeon b. Lakish said : The community of Israel spake before the Holy One, blessed be He, ", 

            "\"Lord of the universe ! Should a man marry a woman after his first wife, he remembers the deeds of the first ; but Thou hast forsaken me and forgotten me!\" ", 

            "The Holy One, blessed be He, replied,", 

            " \"My daughter, twelve constellations have I created in the firmament[1], and for each constellation I have created thirty[2] hosts, and for each host I have created thirty legions, and for each legion I have created thirty files, and for each file I have created thirty cohorts, and for each cohort I have created thirty camps[3], and in each camp I have suspended three hundred and sixty-five thousand myriads of stars, in accordance with the days of the solar year, and all of them have I only created for thy sake ; and yet thou sayest, 'Thou hast forsaken me, Thou hast forgotten me'!\" ", 

            "\"Can a woman forget her sucking child ['ulah]?\" (Is. xlix. 15). The Holy One, blessed be He, said, ", 

            "\"Can I forget the burnt-offerings ['olot] of rams and the firstborn of animals which Thou didst offer to Me in the wilderness?\" ", 

            "[The community of Israel] spake before Him, ", 

            "\"Lord of the universe ! Since there is no forgetfulness before the throne of Thy glory, perhaps Thou wilt not forget against me the incident of the Golden Calf!\"", 

            " He replied, ", 

            "\"Yea, 'these' will be forgotten\" (ibid.)[1]. ", 

            "Israel spake before Him, ", 

            "\"Lord of the universe! Since there is forgetfulness before the throne of Thy glory, perhaps Thou wilt forget for me the incident at Sinai!\"", 

            " He replied,", 

            " \"Yet 'the I' will I not forget thee\" (ibid.)[2]. ", 

            "That is the meaning of R. Eleazar's statement in the name of R. Osha'ya :", 

            " What is that which is written, \"Yea, 'these' will be forgotten\"? That refers to the incident of the Golden Calf; \"Yet 'the I' will I not forget thee\"? That refers to the incident at Sinai. ", 

            "The pious men of old used to wait an hour. ", 

            "Whence is this?", 

            " R. Joshua b. Levi said : ", 

            "The Scriptures state, \"Happy are they that dwell in Thy house\" (Ps. Ixxxiv, 5). ", 

            "R. Joshua b. Levi also said : ", 

            "He who prays should wait an hour after his prayer[3] ; as it is said, \"Surely the righteous shall give thanks unto Thy name, the upright shall dwell in Thy presence\" (ibid. cxl. 14)[4].", 

            " There is a teaching to the same effect : ", 

            "He who prays should wait an hour before and an hour after his prayer. ", 

            "Whence is it [that he should wait an hour] before his prayer? As it is said, \"Happy are they that dwell in Thy house.\" ", 

            "Whence is it [that he should wait an hour] after his prayer? As it is said, \"Surely the righteous shall give thanks unto Thy name; the upright shall dwell in Thy presence.\" ", 

            "Our Rabbis have taught : ", 

            "The pious men of old used to wait an hour, pray for an hour, and again wait an hour. ", 

            "Since they spent nine hours in the day in connection with prayer[5], how was their Torah kept up, and how was their work done ?", 

            " But since they were pious, their Torah was preserved[1] and their work was blessed[2]. ", 

            "Even when a king greets him, he must not respond. ", 

            "Rab Joseph said : This teaching applies only to the Israelite kings ; but for the kings of other peoples he must stop. ", 

            "Against this is quoted : ", 

            "He who prays [the Tefillah] and sees a highway robber[3] or waggon coming towards him should not interrupt but shorten it and step back ! ", 

            "There is no contradiction ;", 

            " for this means where it is possible to shorten, he should shorten, but if not, he should interrupt. ", 

            "Our Rabbis have taught : ", 

            "It happened that a pious man was saying the Tefillah by the roadside. A nobleman passed and greeted him ; but he did not respond. The nobleman waited until he had concluded his prayer ; ", 

            "and after he had concluded it, he said to him, ", 

            "\"Good for nothing[4]! Is it not written in your Torah, 'Only take heed to thyself, and keep thy soul diligently' (Deut iv. 9) and 'Take ye therefore good heed unto yourselves' (ibid. V. 15)? When I greeted thee, why didst thou not return my salutation?", 

            " If I had cut off thy head with a sword, who would have demanded thy blood at my hand?\"", 

            " He replied,", 

            " \"Wait until I shall have conciliated thee with words.\"", 

            " And he continued, ", 

            "\"If thou hadst been standing before a human king,  and thy friend had greeted thee, wouldst thou have  "

        ], 

        [

            "responded to him?\"", 

            "he replied", 

            " \"No,\" ", 

            "\"And if thou hadst responded to him, what would they have done to thee?\" ", 

            "He answered,", 

            " \"They would have cut off my head with the sword.\" ", 

            "He said to him, ", 

            "\"May we not use the a fortiori argument : ", 

            "If thou standing before a human king, who is here to-day and to-morrow in the grave, actest thus, how much more so I who was standing before the supreme King of kings, the Holy One, blessed be He, Who lives and endures for all eternity?\"", 

            " The nobleman was at once conciliated, and the pious man departed for his house in peace. ", 

            "And though a serpent is wound round his heel, he must not interrupt. ", 

            "Rab Sheshet said : ", 

            "This teaching applies only to a serpent, but if it be a scorpion he may interrupt[1]. ", 

            "Against this is quoted :", 

            " If a man fell into a den of lions, we cannot testify concerning him that he is dead[2] ; but if he fell into a pit of serpents or scorpions, we can so testify[3] !", 

            " It is different in this case, because through the pressure[4] they will injure him.", 

            " R. Isaac[5] said:", 

            " If he saw oxen[6], he may interrupt ; for Rab Osha'ya taught : ", 

            "One should remove himself fifty cubits from an ox which has never injured anybody and as far as he can see it from an ox whose owner has been warned of its tendency to gore.", 

            " It has been taught in the name of R. Meir : ", 

            "Even when the ox has its head in the [fodder-] basket, go up to the roof, and remove the ladder from under thee[7]. ", 

            "Samuel said: ", 

            "This applies only to a black ox in the days of Nisan, because Satan then dances between its horns[8]. ", 

            "Our Rabbis have taught :", 

            " It happened in a certain place that there was a lizard which injured people. They came and informed R. Hannina b. Dosa[9].", 

            " He said to them, ", 

            "\"Show me its hole.\"", 

            " They pointed it out to him, ", 

            "and he placed his heel over the mouth of the hole. The lizard came out and bit him, and it died[10]. ", 

            "He put it on his shoulder and brought it to the House of Study. ", 

            "He said to them,", 

            " \"See, my sons, it is not the lizard that kills but sin that kills.\" ", 

            "At that time the saying originated :", 

            " \"Woe to the man who meets a lizard ; but woe to the lizard which R. Hannina b. Dosa meets.\" ", 

            "MISHNAH We refer to rain in the benediction of \"the Revival of the Dead[1]\" and the request [for rain] in the benediction of \"the Years[2],\" and the \"Division\" in \"Thou favourest man with knowledge[3].\" ", 

            "R. 'Akiba says : ", 

            "One should say the last mentioned as a fourth benediction by itself. ", 

            "R. Eliezer says : ", 

            "[It is to be included] in the \"Thanksgiving[4].\" ", 

            "GEMARA We refer to rain in the benediction of \"the Revival of the Dead.\" ", 

            "Why ?", 

            " Rab Joseph said :", 

            " Because it is equal to the revival of the dead[5], therefore they fixed it in the benediction of \"the Revival of the Dead.\" ", 

            "And the request [for rain] in the benediction of \"the Years.\"", 

            " Why ?", 

            " Rab Joseph said :", 

            " Because it is sustenance, therefore they fixed it in the benediction relating to sustenance. ", 

            "And the \"Division\" in \"Thou favourest man with knowledge.\" ", 

            "Why? ", 

            "Rab Joseph said : ", 

            "Because it is wisdom[6], they fixed it in the benediction relating to wisdom. ", 

            "The Rabbis say :", 

            " Because it refers to the non-holy, therefore they fixed it in the [first] benediction [of the Tefillah] for the week-day. ", 

            "R. Ammi said : ", 

            "Great is knowledge, which is placed at the beginning of the benediction said in the week-day [Tefillah]. ", 

            "R. Ammi also said[7] : ", 

            "Great is knowledge which is placed between two references to the Divine Name[8] ; as it is said, ", 

            "\"For a God of knowledge is the Lord\" (I Sam. ii. 3).", 

            " It is forbidden to have mercy upon one who does not possess knowledge ; as it is said, ", 

            "\"For it is a people of no understanding, therefore He that made them will not have compassion upon them\" (Is. xxvii. 11)[9]. ", 

            "R. Eleazar said : ", 

            "Great is the Sanctuary which is placed between two references to the Divine Name; as it is said, ", 

            "\"...Thou hast made, O Lord, the sanctuary, O Lord...\" (Exod. xv. 17).", 

            " R. Eleazar also said : ", 

            "Every one who possesses knowledge is as though the Sanctuary was built in his days ;", 

            " for \"knowledge\" is placed between two references to the Divine Name and \"Sanctuary\" is similarly placed. ", 

            "Rab Aha Karhinaah[1] retorted : ", 

            "In that case, great is vengeance which is placed between two references to the Divine Name; as it is said,", 

            " \"A God of vengeance, the Lord\" (Ps. xciv. 1)[2]!", 

            " He replied : ", 

            "Quite so, in certain circumstances it is great ; ", 

            "and that is what 'Ulla said : ", 

            "Why is \"vengeance\" mentioned twice in the verse[3]? ", 

            "One for good, the other for evil — for good, as it is written,", 

            " \"He shone forth from Mount Paran\" (Deut. xxxiii. 2) ; for evil, as it is written,", 

            " \"O Lord, Thou God, to Whom vengeance belongeth, Thou God, to Whom vengeance belongeth, shine forth\" (Ps. xciv. 1). ", 

            "R. 'Akiba says : One should say the last-mentioned as a fourth benediction by itself. ", 

            "Rab Shamman b. Abba said to R. Johanan,", 

            " \"It is a fact that the men of the Great Assembly[4] instituted for Israel benedictions and prayers, Sanctifications and Divisions ; let us see where it was arranged [for the Habdalah to be said].\" ", 

            "He replied to him,", 

            " \"At first they fixed it in the Tefillah ; when the people became prosperous[5], they arranged for it to be said over the cup of wine[6]; when the people became poor, they again fixed it in the Tefillah ; and they said :", 

            " He who pronounces the 'Division' in the Tefillah must do it again over the cup of wine.\"", 

            " It has been similarly reported : R. Hiyya. b. Abba said in the name of R. Johanan : ", 

            "The men of the Great Assembly instituted for Israel benedictions and prayers, Sanctifications and Divisions.", 

            " At first they fixed [the Habdalah] in the Tefillah; when the people became prosperous, they arranged for it to be said over the cup of wine ; when they again became poor, they fixed it in the Tefillah ; and they said :", 

            " He who pronounces the \"Division\" in the Tefillah must do it again over the cup of wine.", 

            " It has been likewise reported : Rabbah and Rab Joseph both declare : ", 

            "He who pronounces the \"Division\" in the Tefillah must do it again over the cup of wine. ", 

            "Raba said : We quote against this teaching :", 

            " If one erred and omitted the reference to rain in the benediction of \"the Revival of the Dead\" or the request [for rain] in the benediction of \"the Years,\" we make him repeat it ; but [if he omitted] the \"Division\" in \"Thou favourest man with knowledge\" we do not make him repeat it, because he is able to say it over the cup of wine ! ", 

            "Do not say \"because he is able to say it over the cup of wine\" but \"because he says it over the cup of wine.\"", 

            " It has been similarly reported : R. Benjamin b. Jephet said : ", 

            "R. Assi[1] asked R. Johanan in Zidon (another version : R. Simeon b. Jacob of Tyre asked R. Johanan), \"But I have heard that ", 

            "one who says the 'Division' in the Tefillah must say it again over the cup of wine ; or is it not so?\"", 

            " He replied, ", 

            "\"Yes, he must say the Habdalah over the cup of wine.\" ", 

            "The question was raised :", 

            " How is it with one who says the Habdalah over the cup of wine, does he say it in the Tefillah? ", 

            "Rab Nahman b. Isaac replied : We draw an a fortiori conclusion from the Tefillah :", 

            " If of the Tefillah where [the Habdalah] was originally instituted they say : ", 

            "He who pronounced the \"Division\" in the Tefillah must do so again over the cup of wine, ", 

            "how much more so must one who says the Habdalah over the cup of wine, where it was not originally instituted, [say it in the Tefillah] ! ", 

            "R. Aha[2] the Tall taught in the presence of Rab Huna[3] : ", 

            "He who pronounces the \"Division\" in the Tefillah is more praiseworthy than he who says it over the cup of wine ; but if he says it in both, may blessings alight upon his head. ", 

            "But this is self-contradictory ! ", 

            "Thou declarest, \"He who pronounces the 'Division' in the Tefillah is more praiseworthy than he who says it over the cup of wine\"; hence it is sufficient to say it ", 

            "in the Tefillah alone ! And then he teaches,", 

            " \"But if he says it in both, may blessings alight upon his head\"; but since he has fulfilled his obligation with the former, he is exempt and [the latter] will be a superfluous benediction, ", 

            "and Rab has declared (another version : R. Simeon b. Lakish ; or R. Johanan and R. Simeon b. Lakish both declare) :", 

            " Whoever utters a superfluous benediction commits a transgression because of [the injunction],", 

            " \"Thou shalt not take the name of the Lord thy God in vain\" (Exod. xx. 7) ! ", 

            "Understand him therefore to mean :", 

            " If he pronounced the \"Division\" in the Tefillah and not over the cup of wine, may blessings alight upon his head. ", 

            "Rab Hisda[1] asked Rab Sheshet : ", 

            "If a man erred [and omitted the Habdalah] in both, how is it ?", 

            " He replied :", 

            " If he erred in both, he must start again. "

        ], 

        [

            " Rabina asked Raba : ", 

            "What is the Halakah [if one pronounced the \"Division\" in the Tefillah, must he say it over the cup of wine] ? ", 

            "He replied : ", 

            "It is like the Sanctification ; although one sanctifies [the Sabbath] in the Tefillah, he must do so over the cup of wine; so also with the Habdalah, although he said it in the Tefillah, he must do so over the cup of wine. ", 

            "R. Eliezer said :", 

            " [It is to he included] in the \"Thanksgiving\" ", 

            "R. Zera was riding on an ass, and R. Hiyya b. Abin was following him. ", 

            "He said to him, \"Is it really so as thou didst state in the name of R. Johanan :", 

            " The Halakah is in agreement with R. Eliezer on a Festival which occurs on the conclusion of the Sabbath ?\"", 

            " He replied,", 

            " \"Yes.\" ", 

            "\"The Halakah being so, is it to be inferred that there are some who differ from him[2]?", 

            " Are there not, indeed, some who differ?\"", 

            " \"The Rabbis differ from him.\" ", 

            "\"On which point do the Rabbis differ?\" \"On the other days of the year[3].\" \"Do they differ on the question of a Festival which occurs at the conclusion of the Sabbath?", 

            " Behold R. 'Akiba differs[4]!\"", 

            " \"Do we, then, act in accordance with R. 'Akiba the whole year, that we should now agree and act in accord with his view? ", 

            "Why do we not act in agreement with R. 'Akiba the whole year?", 

            " Because eighteen benedictions were instituted, not nineteen; and so here also, seven benedictions were instituted, not eight[1].\"", 

            " [R. Zera] said to him:", 

            " It has not been reported that the Halakah [is in accord with R. Eliezer], but it has been reported that we incline [towards his view][2].", 

            " For it has been reported : Rab Isaac b. Abdemi said in the name of our teacher[3] : ", 

            "The Halakah [is in accord with R. Eliezer] ; but some say : ", 

            "We incline [towards his view].", 

            " R. Johanan said :", 

            " [The Rabbis] acknowledge [that the Halakah is in agreement with him]. ", 

            "R. Hiyya b. Abba said : ", 

            "[R. Eliezer's opinion] is probable.", 

            " R. Zera said :", 

            " Take the statement of R. Hiyya. b. Abba in thine hand[4], because he is most careful to report a teaching exactly as it issued from the mouth of his teacher ; like Rahba of Pombedita[5]. ", 

            "For Rahba said in the name of R. Judah : ", 

            "The Temple mount was a double colonnade, and it was a colonnade within a colonnade[6]. ", 

            "Rab Joseph said :", 

            " I know neither the one nor the other[7] ; but from Rab and Samuel I know that they instituted a \"pearl\"[8] for us in Babylon : ", 

            "\"Thou, O Lord our God, hast made known unto us the judgments of Thy righteousness ; Thou hast taught us to perform the statutes of Thy will. Thou hast caused us to inherit seasons of joy and feasts of free will gifts, and hast given us as an heritage the holiness of the Sabbath, the glory of the appointed time, and the celebration of the festival. Thou hast made a distinction between the holiness of the Sabbath and that of the festival, and hast hallowed the seventh day above the six working days ; Thou hast distinguished and sanctified Thy people Israel by Thy holiness. And Thou hast given us,\" etc. ", 

            "MISHNAH Whoever says [in his Tefillah] \"To a bird's nest do Thy mercies extend[1]\" or \"For the good be Thy name remembered[2]\" or \"We give thanks, we give thanks[3],\" him do we silence.", 

            "GEMARA It is right that ", 

            "we silence him who says, \"We give thanks, we give thanks,\" because he makes it appear as though there were two Powers[4]; and likewise him who says, \"For the good be Thy name remembered,\" the inference being that for the good [may it be remembered] but not for the bad ; and we have a Mishnaic teaching : ", 

            "A man is in duty bound to utter a benediction for the bad even as he utters one for the good[5]. ", 

            "But why [do we silence him who says], \"To a bird's nest do Thy mercies extend\"?", 

            " Two Amoraim in the West[6] differ, viz. : R Jose b. Abin and R. Jose b. Zebida : ", 

            "one said : ", 

            "Because he causes jealousy between God's creatures[7] ; the other said : ", 

            "Because he makes the ordinances of the Holy One, blessed be He, to be simply acts of mercy, whereas they are injunctions[8]. ", 

            "A certain man went down [to the Ark][9] in the presence of Rabbah and said, ", 

            "\"Thou hast compassion on a bird's nest ; do Thou have compassion and mercy upon us.\" ", 

            "Rabbah exclaimed, ", 

            "\"How this Rabbinical scholar knows how to find favour with his Lord[10]!\" ", 

            "Abbai said to him, ", 

            "\"Lo, we have learnt in the Mishnah: We silence him!\" ", 

            "But Rabbah merely wished to test Abbai[11]. ", 

            "A certain man went down [to the Ark] in the presence of R. Hannina. He said[1],", 

            " \"O God, the great, the mighty, the revered, the glorious, the powerful, the feared, the strong, the courageous, the certain, the honoured.\" ", 

            "R. Hannina waited until he had finished. ", 

            "When he had finished, he said to him, ", 

            "\"Hast thou exhausted all the praises of thy Lord? ", 

            "What is the use of all those [adjectives]? The three which we do say[2], if Moses our teacher had not used them in the Torah[3] and the men of the Great Assembly[4] come and instituted them in the Tefillah, we should not have been able to say ; and thou dost go on saying all those!\" ", 

            "A parable : [It may be likened] to a human king who possessed a million golden denarii[5], and people kept praising him as the possessor of [a million denarii of][6] silver; is it not an insult to him ? ", 

            "R. Hannina also said :", 

            " Everything is in the hand of Heaven except the fear of Heaven[7]; as it is said, ", 

            "\"And now, O Israel, what doth the Lord thy God require of thee but to fear\" (Deut. x. 12).", 

            " Is, then, the fear of Heaven a small thing[8]? ", 

            "Lo, R. Hannina has said in the name of R. Simeon b. Johai[9] : ", 

            "The Holy One, blessed be He, has in His treasury nothing but the store of heavenly fear; as it is said, ", 

            "\"And the fear of the Lord which is His treasure\" (Is. xxxiii. 6) !", 

            " Yes, in the estimation of Moses it was a small thing ;", 

            " for R. Hannina said : ", 

            "A parable : [It may be likened] to a man from whom a large vessel is required ; possessing it, it seems to him small ; but if he does not possess it, though it be small, it seems to him large. ", 

            "[ Who says], \"We give thanks,\" him do we silence. ", 

            "R. Zera said : Whoever says Shema', Shema'[10] is like him who says \"We give thanks, we give thanks\" [and is to be silenced]. ", 

            "Against this is quoted : ", 

            "He who reads the Shema' and repeats the words is to be reprimanded. ", 

            "He is to be reprimanded, but not silenced !", 

            " There is no contradiction. ", 

            "This refers to one who repeats it word by word ; but the former refers to him who repeats it verse by verse[1]. ", 

            "Rab Pappa asked Abbai : ", 

            "But perhaps he at first did not direct his mind and finally did so[2]! ", 

            "He replied : "

        ], 

        [

            "Has anyone intimacy with Heaven[3] ?", 

            " If he did not at first direct his mind [to his prayer], we smite him with a smith's hammer until he does direct his mind[4]. ", 

            "MISHNAH He who says in his Tefillah ", 

            "\"The good bless Thee\" behold this is the way of error[5].", 

            " If a man step before the Ark[6] and make a mistake [in the Tefillah], another replaces him ; and at such a time, one may not decline[7].", 

            " From where does the latter begin? ", 

            "From the commencement of the benediction where the other erred. ", 

            "He who steps before the Ark should not respond \"Amen\" after [the benedictions of] the Kohanim[8] because it might cause him confusion. If there be no other Kohen there but himself he does not raise his hands [for the priestly benediction] ; ", 

            "but if he is confident that he can raise his hands and return to the Tefillah[9], he is permitted. ", 

            "GEMARA Our Rabbis have taught :", 

            " [If one is invited] to step before the Ark, he should first decline[10]; should he not do so, he is like cooking without salt. But if he decline unduly, he is like cooking spoilt by over-salting. ", 

            "How should he act ? The first time [of asking] he declines ; the second time he wavers ; the third time he stretches his legs and descends [before the Ark]. ", 

            "Our Rabbis have taught :", 

            "There are three things where excess is bad and a small quantity pleasant :", 

            " leaven, salt and declining an office. ", 

            "Rab Huna said :", 

            " If he erred in the first three benedictions [of Tefillah], he commences again at the beginning; if in the middle benedictions, he returns to \"Thou favourest man with knowledge[1]\" ; if in the last [three], he returns to the \"Service[2].\" ", 

            "Rab Assi said : ", 

            "The middle benedictions have no order[3]. ", 

            "Rab Sheshet quoted in objection :", 

            " From where does the latter begin ? From the commencement of the benediction where the other erred ! This is a refutation of Rab Huna ; ", 

            "but Rab Huna can reply : ", 

            "The middle benedictions are all one benediction[4]. ", 

            "Rab Judah said[5]:", 

            " A man should never pray for his personal needs in the first three or last three benedictions, but in the middle ones.", 

            " For R. Hannina[6] said : ", 

            "[When saying] the first three benedictions, he is like a slave recounting praise before his master ; [when saying] the middle benedictions, he is like a slave begging a reward from his master ; [when saying] the last three benedictions, he is like a slave who, receiving a reward from his master, takes his departure and goes away. ", 

            "Our Rabbis have taught : ", 

            "It happened that a disciple who descended before the Ark in the presence of R. Eliezer unduly prolonged [the prayers]. ", 

            "His disciples said to him, ", 

            "\"Our master, what a prolonger he is!\" ", 

            "He replied, ", 

            "\"Did he prolong more than Moses, our teacher, ", 

            "of whom it is written, ", 

            "'The forty days and forty nights that I fell down'\" (Deut. ix. 25)?", 

            " It again happened that a disciple who descended before the Ark in the presence of R. Eliezer unduly shortened [the prayers].", 

            " His disciples said to him, ", 

            "\"What a shortener he is!\"", 

            " He replied,", 

            " \"Did he shorten more than Moses, our teacher ; ", 

            "for it is written,", 

            " 'Heal her now, O God, I beseech Thee'\" (Num. xii. 13)[7]?", 

            " R. Jacob said in the name of Rab Hisda :", 

            " Whoever prays on behalf of another need not mention his name ; as it is said, ", 

            "\"Heal her now, O God, I beseech Thee,\" without mentioning Miriam's name. ", 

            "Our Rabbis have taught : ", 

            "These are the benedictions at which a man bends low ; ", 

            "at the beginning and end of the \"Patriarchs[1]\" and at the beginning and end of the \"Thanksgiving[2].\" ", 

            "Should anyone come to bend low at the end and beginning of every benediction, we tell him not to do so. ", 

            "R. Simeon b. Pazzi said in the name of R. Joshua b. Levi in the name of Bar Kappara : ", 

            "The ordinary man [acts] as we have stated ;\n"

        ], 

        [

            " a high priest [bends] at  the end of each benediction ; a king at the beginning and end of each benediction. ", 

            "R. Isaac b. Nahmani said : It was explained to me by R. Joshua b. Levi : ", 

            "The ordinary man [acts] as we have stated ; a high priest [bends] at the beginning of each benediction ; a king, when once he bends, should not straighten himself [until the end of the Tefillah] ; as it is said,", 

            " \"And it was so, that when Solomon had made an end of praying all this prayer and supplication unto the Lord, he arose from before the altar of the Lord from kneeling on his knees\" (I Kings viii. 54). ", 

            "Our Rabbis have taught :", 

            " \"Bowing\" means upon the face ; as it is said, ", 

            "\"Then Bath Sheba bowed with her face to the earth\" (ibid. i. 31).\"Bending\" means upon the knees[3]; as it is said,", 

            " \"From kneeling on his knees\" (ibid. viii. 54). \"Prostrating\" means spreading out the hands and legs ; as it is said,", 

            " \"Shall I and thy mother and thy brethren indeed come to prostrate ourselves to thee to the earth?\" (Gen. xxxvii. 10). ", 

            "Rab Hiyya b. Rab Huna said :", 

            " I saw Abbai and Raba just recline on their side[4].", 

            " One taught: ", 

            "He who bends the knee in the \"Thanksgiving\" is praiseworthy ; ", 

            "but there is another teaching :", 

            " Such an one is to be reprimanded ! ", 

            "There is no contradiction ;", 

            " one referring to the beginning, the other to the end [of the benediction]. ", 

            "Raba bent the knee at the beginning and end of the \"Thanksgiving,\"", 

            " The Rabbis asked him,", 

            " \"Why has the master acted so?\"", 

            " He replied, ", 

            "\"I saw Rab Nahman bend the knee, and I saw Rab Sheshet do it. ", 

            "Moreover, the teaching : ", 

            "He who bends the knee in the 'Thanksgiving' is to be reprimanded — ", 

            "refers to the 'Thanksgiving' in the Hallel[1].\"", 

            " And the teaching : ", 

            "He who bends the knee in the \"Thanksgiving\" of the Tefillah and in the \"Thanksgiving\" of the Hallel is to be reprimanded — ", 

            "to what does this refer? To the \"Thanksgiving\" in the Grace after meals[2]. ", 

            "MISHNAH If one errs while saving the Tefillah, it is a bad omen for him ; and should he be the messenger of the congregation[3], it is a bad omen for those who deputed him, since a man's deputy is similar to himself. ", 

            "They declared concerning R. Hannina b. Dosa[4] that when praying on behalf of the sick, he would say, \"This one will live, that one will die.\" ", 

            "They asked him, ", 

            "\"How knowest thou?\"", 

            " He replied, ", 

            "\"If my prayer is fluent in my mouth, I know that he is accepted; but if not, I know that he is rejected.\" ", 

            "GEMARA To which[5]? ", 

            "R. Hiyya[6] stated that Rab Safra said in the name of one attached to the school of Rabbi[7]:", 

            " To the \"Patriarchs[8].\"", 

            " Others refer this [statement of Rab Safra] to the following Baraita: ", 

            "One who says the Tefillah must direct his heart to each benediction ; but if unable to do so to each one, he must at least direct his heart to one. To which? ", 

            "R. Hiyya stated that Rab Safra said in the name of one attached to the school of Rabbi :", 

            " To the \"Patriarchs.\" ", 

            "They declared concerning R. Hannina b. Dosa, etc. ", 

            "Whence is this? ", 

            "R. Joshua b. Levi[9] said :For the Scriptures state, ", 

            "\"Peace, peace to him that is far off and to him that is near, saith the Lord that createth[10] the fruit of the lips; and I will heal him\" (Is.lvii. 19). ", 

            "R. Hiyya b. Abba said in the name of R. Johanan : ", 

            "Every prophet prophesied only to marry his daughter to a disciple of the wise, and for him who transacts the affairs of a disciple of the wise and allows him to enjoy his possessions ; but as for the disciples of the wise themselves, \"No eye hath seen what God, and nobody but Thee[1], will work for him that waiteth for Him\" (Is. Ixiv. 3)[2]. ", 

            "R. Hiyya b. Abba also said in the name of R. Johanan :", 

            " Every prophet only prophesied for the days of the Messiah ; but as for the world to come, \"No eye hath seen what God, and nobody but Thee, will work for him that waiteth for Him.\" ", 

            "This is at variance with the opinion of Samuel who said : ", 

            "There is no difference between this world and the days of the Messiah, except the servitude of the heathen kingdoms alone ; as it is said,", 

            " \"For the poor shall never cease out of the land\" (Deut. xv. 11)[3]. ", 

            "R. Hiyya b. Abba also said in the name of R. Johanan : ", 

            "Every prophet only prophesied for the penitent ; but as for the perfectly righteous, \"No eye hath seen what God, and nobody but Thee, will work for him that waiteth for Him.\" ", 

            "This is at variance with the opinion of R. Abbahu who said :", 

            " The place which the penitent occupy, the perfectly righteous are unable to occupy ; as it is said, ", 

            "\"Peace, peace to him that is far off and to him that is near\" —", 

            " \"to him that is far off [from God]\" first, and then \"to him that is near.\" But R. Johanan can reply :", 

            " What means \"To him that is far off\"? To him who was far off from transgression from the first ; and what means \"To him that is near\"? To him that was near transgression and has now removed himself therefrom. ", 

            "What is the significance of \"No eye hath seen\" etc.? ", 

            "R. Joshua b. Levi said :", 

            " It refers to the wine preserved in the grape from the six days of creation. ", 

            "R. Samuel b. Nahmani[4] said :", 

            " It refers to Eden[5], upon which the eye of no creature has gazed. ", 

            "Perhaps thou wilt ask : Where, then, was Adam ?", 

            " In the Garden. ", 

            "But perhaps thou wilt say that", 

            " the Garden is the same as Eden ! Therefore there is a teaching to tell thee, ", 

            "\"And a river went out of Eden to water the Garden\" (Gen. ii. 10). Hence the Garden and Eden are distinct. ", 

            "Our Rabbis have taught :", 

            " It once happened that the son of Rabban Gamaliel was ill. He sent two disciples of the wise to R. Hannina b. Dosa to pray on his behalf. ", 

            "When he saw them, he ascended to an upper chamber and prayed on his behalf.", 

            " On descending he said to them, ", 

            "\"Go, the fever has left him.\" ", 

            "They said to him,", 

            " \"Art thou a prophet?\"", 

            " He replied,", 

            " \"'I am no prophet nor a prophet's son' (Amos vii. 14) ; but so is my tradition :", 

            " If my prayer is fluent in my mouth, I know that he is accepted ; but if not, I know that he is rejected.\" ", 

            "They sat down and wrote and noted the time.", 

            " When they came to Rabban Gamaliel, he said to them, ", 

            "\"By the Temple-service! ", 

            "You have neither understated nor overstated [the time]. But thus it happened ; at that very hour the fever left him, and he asked us for water to drink.\" ", 

            "It also happened with R. Hannina b. Dosa that he went to Torah with Rabban Johanan b. Zakkai. The son of Rabban Johanan b. Zakkai fell ill, ", 

            "and he said to him,", 

            " \"Hannina, my son ! Pray on his behalf that he may live\" ", 

            "R. Hannina laid his head between his knees, and prayed on his behalf, and he recovered.", 

            " Rabban Johanan b. Zakkai said, ", 

            "\"Were Ben Zakkai to press his head between his knees all the day long, no notice would be taken of him.\"", 

            " His wife said to him,", 

            " \"Is, then, Hannina greater than thou?\" ", 

            "He replied, ", 

            "\"No; he is like a slave before the King[1], and I like a nobleman before the King.\" ", 

            "R. Hiyya b. Abba also said in the name of R Johanan : ", 

            "A man should not pray except in a room which has windows ; as it is said, ", 

            "\"Now his windows were open in his upper chamber towards Jerusalem\" (Dan. vi. 11)[2]. Rab Kahana said : ", 

            "I consider him impertinent who prays in a valley[4].", 

            " Rab Kahana also said : ", 

            "I consider him impertinent who recounts his sins[5] ; as it is said,", 

            " \"Happy is he whose transgression is forgiven, whose sin is pardoned[6]\" (Ps. xxxii. 1). ", 

            "May we return unto thee : One must not stand."

        ], 

        [

            "MISHNAH ", 

            "What benediction do we say over fruit ? ", 

            "Over the fruit of trees, one says, ", 

            "\"[Blessed art Thou, O Lord our God, King of the universe] Who Createst the fruit of the tree,\" except over wine ; for over wine ons says, ", 

            "\"...Who createst the fruit of the vine.\" ", 

            "Over the fruits of the earth one says :", 

            " \"... Who createst the fruit of the ground,\" except over bread; for over bread one says, ", 

            "\"...Who bringest forth bread from the earth.\" ", 

            "Over vegetables one says, ", 

            "\"... Who createst the fruit of the ground\" ; but R. Judah declares :", 

            " \"... Who createst divers kinds of herbs.\" ", 

            "GEMARA  Whence is this derived [1]?", 

            " For our Rabbis have taught:", 

            " \"The fruit thereof shall be holy, for giving praise [hillulim][2] unto the Lord\" (Lev. xix. 24) — this teaches that they require a benediction before and after partaking of them. Hence said R. 'Akiba : ", 

            "A man is forbidden to taste anything without previously saying a benediction. But is the phrase \"holy for giving praise\" intended to teach that ?", 

            " Surely it is required [to teach as follows :] First,", 

            " that the All-merciful declares [the owner] must redeem it[3] and then eat it ;", 

            "and second,", 

            " only those things which require \"a song of praise\" require redemption, but if they do not require \"a song of praise,\" redemption is unnecessary[4] ! This is according to the statement of R. Samuel b. Nahmani in the name of R. Jonathan who said : ", 

            "[not translated]", 

            "Whence is it that we say \"a song of praise\" only over wine ? As it is said, \"And the vine said unto them, Should I leave my wine which cheereth God and man?\" (Judges ix. 13). If it cheereth man, how does it cheer God ? ", 

            "Hence it is to be inferred that we have \"a song of praise\" only over wine'. ", 

            "It is quite right[2] according to him who teaches \"the planting of the fourth year[3]\"; but according to him who teaches \"the vineyard of the fourth year\" what is there to say[4]? ", 

            "For it has been reported : ", 

            "R. Hiyya and R. Simeon b. Rabbi [differ] ; one teaches", 

            " \"The vineyard of the fourth year,\" the other teaches ", 

            "\"The planting of the fourth year.\" ", 

            "According to him who teaches \"the vineyard of the fourth year\" it is quite right[5] if he argues by analogy of expression[6] ; for there is a teaching : ", 

            "Rabbi says : It is stated here, ", 

            "\"That it may yield unto you more richly the increase thereof\" (Lev. xix. 25), and it is stated elsewhere, ", 

            "\"the increase of the vineyard\" (Deut. xxii. 9) — as in the latter passage \"increase\" refers to the vineyard, so also in the former passage it refers to the vineyard ; and there thus remains over one hillul to be interpreted as meaning that a benediction is required [when partaking of fruits]. ", 

            "But if he does not resort to this argument from analogy, whence does he derive the necessity for a benediction ?", 

            " And even if he resort to this method of reasoning, we find that a benediction is required after eating[7] ; but whence is it that a benediction is necessary before eating ? ", 

            "This is no difficulty ; for we can use a fortiori reasoning —", 

            " if he is to bless God when he is satisfied, how much more so when he is hungry[8] ! We find this in connection with ", 

            "[the produce of] the vineyard[9]; whence is it [that a benediction is required with] other species ?", 

            " It can be derived from the instance of the vineyard — as the vineyard, a thing that is enjoyed, requires a benediction, so also everything which is enjoyed requires a benediction. ", 

            "But it is possible to object : ", 

            "Why [is a benediction required with the fruit of] the vineyard ? Because there is the obligation of the gleanings[1].", 

            " Let, then, the instance of corn show [whether this point is material][2] ! ", 

            "But why [is a benediction required when partaking of food made from] corn ? Because there is the obligation of Hallah.", 

            " Then let the instance of the vineyard show [whether this point is material][3]! ", 

            "The argument has therefore to be reinstated[4], ", 

            "because the feature of the first case is not like that of the second and vice versa[5] ; but the factor common to both is that each is something which is enjoyed and consequently requires a benediction. Hence everything which is enjoyed requires a benediction. ", 

            "How is this[6] the factor common to them both? [That they are both brought upon] the altar is likewise a common factor[7] !", 

            " Then the olive must also be included because it likewise has this factor of [being brought to] the altar !", 

            " Does, then, the olive need inclusion because of the factor of the altar ? ", 

            "Behold, the expression kerem \"vineyard\" is explicitly written in connection therewith ; for it is stated, ", 

            "\"And he burnt up the shocks and the standing corn, and also the olive-yards[8]\" (Judges xv. 5) ! ", 

            "Rab Pappa answered :", 

            " It is called \"a kerem of olives\" but not kerem without qualification.", 

            " Nevertheless the difficulty remains,", 

            " \"How is this the factor common to them both ? [That they are both brought upon] the altar is likewise a common factor.\" ", 

            "One can, however, derive [the necessity for a benediction] from \"the seven species[9]\" — as \"the seven species\" are things enjoyed and require a benediction, so everything that is enjoyed requires a benediction. ", 

            "But why do \"the seven species\" [require a benediction]? Because they are under the obligation of first-fruits[1]. ", 

            "And further,", 

            " it is right [that a benediction is necessary] after partaking of them, but whence is it [that a benediction is necessary] before partaking of them ?", 

            " That is no difficulty ; because it can be derived by a fortiori reasoning —", 

            " if he says a benediction when satisfied, how much more so when hungry ! According to him", 

            " who teaches \"the planting of the fourth year\" it is quite right [that a benediction is required] for everything that is planted;", 

            " but whence [does he derive the necessity for a benediction] for things not planted, like meat, eggs, fish?", 

            "It is, however, a generally held opinion that ", 

            "a man is forbidden to enjoy anything of this world without a benediction[2]. ", 

            "Our Rabbis have taught :", 

            " A man is forbidden to enjoy anything of this world without a benediction, and whoever does so commits sacrilege[3]. ", 

            "What is the remedy ? Let him go to a Sage. ", 

            "Let him go to a Sage ! What can he do for him, ", 

            "seeing that he has done what is forbidden ?", 

            " But, said Raba : ", 

            "[The meaning is,] let him from the first go to a Sage who will teach him the benedictions, so that he should not come to commit sacrilege. ", 

            "Rab Judah said in the name of Samuel : ", 

            "Whoever enjoys anything of this world without a benediction is as though he had partaken of the holy things of Heaven ; as it is said,", 

            " \"The earth is the Lord's, and the fulness thereof\" (Ps. xxiv. 1). ", 

            "R. Levi asked : ", 

            "t is written, \"The earth is the Lord's and the fulness thereof,\" and it is written, \"The heavens are the heavens of the Lord, but the earth hath He given to the children of men\" (ibid. cxv. 16) !", 

            " There is no contradiction ; the former passage referring [[fol. 35 b.]] to before the benediction [has been uttered], "

        ], 

        [

            " the latter to after the benediction. ", 

            "R. Hannina b. Pappa said :", 

            " Whoever enjoys anything of this world without a benediction is as though he robbed the Holy One, blessed be He, and the Community of Israel[1] ; as it is said, ", 

            "\"Whoso robbeth his father or his mother and saith, It is no transgression, the same is the companion of a destroyer\" (Prov. xxviii, 24) — ", 

            "\"father\" is none other than the Holy One, blessed be He ; as it is said, \"Is not He thy father that hath gotten thee?\" (Deut. xxxii. 6) ;", 

            " and \"mother\" is none other than the Community of Israel ; as it is said, ", 

            "\"Hear, my son, the instruction of thy father, and forsake not the teaching of thy mother\" (Prov. i. 8).", 

            " What means \"the companion of a destroyer\" ?", 

            " R. Hannina b, Pappa said : ", 

            "He is the companion of Jeroboam, the son of Nebat, who corrupted Israel against their Father in Heaven. ", 

            "R. Hannina b. Pappa asked :", 

            " It is written, \"Therefore will I take back My corn in the time thereof\" etc. (Hosea ii. 11), and it is written, ", 

            "\"And thou shalt gather in thy corn\" etc. (Deut. xi. 14) !", 

            " There is no contradiction;", 

            " the latter referring to the time when Israel perform the will of the All-present, the former to when Israel neglect His will. ", 

            "Our Rabbis have taught :", 

            " \"And thou shalt gather in thy corn\" — what has this teaching to tell us ? Since it is written,", 

            " \"This book of the law shall not depart out of thy mouth [but thou shalt meditate therein day and night]\" (Josh. i. 8), it is possible to think that these words [are to be understood] as they are written[2]; ", 

            "therefore there is a teaching to say, ", 

            "\"And thou shalt gather in thy corn,\" ie. conduct at the same time a worldly occupation. These are the words of R. Ishmael. ", 

            "R. Simeon b. Johai says :", 

            " Is it possible for a man to plough at the time of ploughing, sow at seed-time, reap at harvest-time, thresh at the time of threshing, and winnow at the time of wind[3] — what is to become of Torah? ", 

            "But ", 

            "when Israel perform the will of the All-present, their work is done by others; as it is said, ", 

            "\"And strangers shall stand and feed your flocks,\" etc. (Is. Ixi. 5) ; ", 

            "and at the time when Israel perform not the will of the All-present, their work has to be done by themselves ; as it is said,", 

            " \"And thou shalt gather in thy corn.\"", 

            " Not that alone, but the work of others will be done by them ; as it is said, ", 

            "\"And thou shalt serve thine enemy\" etc. (Deut. xxviii. 48). ", 

            "Abbai said :", 

            " Many acted in accord with the teaching of R. Ishmael[1] and it proved efficacious ; but he who acted in accord with R. Simeon b. Johai did not find it so. ", 

            "Raba said to the Rabbis :", 

            " I beg of you not to appear before me during the days of Nisan and Tishri[2], so that you may not be concerned about your maintenance the whole year. ", 

            "Rabbah b. Bar Hannah stated that R. Johanan said in the name of R. Judah b. R. El'ai[3] : ", 

            "Come and see that the later generations are not like the former generations. The former generations made their Torah their principal concern and their work only occasional, and both flourished in their hand ; whereas the later generations made their work their principal concern and their Torah only occasional and neither flourished in their hand. ", 

            "Rabbah b. Bar Hannah also stated that R. Johanan said in the name of R. Judah b. R. El'ai :", 

            " Come and see that the later generations are not like the former generations. ", 

            "The former generations used to bring their fruits home by way of the kitchen-garden[4] in order to make them liable to the tithe ; whereas the later generations bring their fruits home by way of the roof, or courts, or enclosures in order to exempt them from the tithe. ", 

            "For R. Jannai has said : ", 

            "Produce is not subject to the tithe until it sees the face of the house ; as it is said,", 

            " \"I have put away the hallowed things out of my house\" (Deut. xxvi. 13). ", 

            "R. Johanan said : Even [if it see] a fixed court [it is subject to the tithe] ; as it is said, ", 

            "\"That they may eat within thy gates and be satisfied\" (ibid. v. 12). ", 

            "Except over wine, etc. Why is wine different ? ", 

            "Should one say because it is changed [from the grape] into something higher [in value], therefore there is a change in the benediction, ", 

            "but lo, oil which is changed [from the olive] into something higher [in value] has no alteration in the benediction ;", 

            " for Rab Judah said in the name of Samuel, and similarly said R. Isaac in the name of R. Johanan :", 

            " Over olive-oil we pronounce the benediction \"...Who createst the fruit of the tree\" ! ", 

            "The answer is :", 

            " In this case [of oil, the benediction is unaltered] because none other is possible. What other benediction could he say? ", 

            "Should he use the formula \"...Who createst the fruit of the olive,\" the olive itself is called \"fruit[1]\"! ", 

            "Then let him say \"...Who createst the fruit of the olive-tree[2].\"", 

            " But said Mar Zotra : ", 

            "Wine nourishes, oil does not. ", 

            "Oil does not nourish ?", 

            " Lo, there is a Mishnaic teaching : ", 

            "He who vows [to abstain] from food may partake of water and salt ! And we argue that ", 

            "water and salt are not called \"food,\" but everything else is so called ; and we further say that this is a refutation of Rab and Samuel who maintain that ", 

            "we pronounce the benediction \"...Who createst various kinds of food\" only over the five species[3]. ", 

            "Moreover Rab Huna said : ", 

            "[The quoted Mishnah means,] Whoever declares \"Everything that nourishes [I forbid] myself\" —", 

            " hence conclude that oil does nourish[4] ! ", 

            "But ", 

            "wine satisfies and oil does not. ", 

            "Does wine satisfy? ", 

            "Lo, Raba used to drink wine the whole of the day preceding Passover to whet his appetite in order to eat the unleavened bread with greater zest !", 

            " A large quantity whets the appetite, but a little satisfies [hunger]. ", 

            "But does it satisfy at all? ", 

            "For lo, it is written,", 

            " \"And wine that maketh glad the heart of man, making the face brighter than oil, and bread that stayeth man's heart\" (Ps. civ. 15) — it is bread, not wine, that is a stay! ", 

            "Nay, ", 

            "wine does both, it satisfies and makes glad, whereas bread is only a stay, but does not cheer.", 

            " If so, let him utter three benedictions[5] ! ", 

            "But men do not fix their meals for its sake[6]. ", 

            "Rab Nahman b. Isaac[7] asked Raba : ", 

            "How is it if a man did fix his meal on its account[8]? ", 

            "He replied : ", 

            "When Elijah[9] comes, let him say whether such can be fixed for a meal ; at present, at least, such a thought does not exist amongst men[10]. ", 

            "It was stated above : ", 

            "\"Rab Judah said in the name of Samuel, and similarly said R. Isaac in the name of R. Johanan :", 

            " Over olive-oil we pronounce the benediction '...Who createst the fruit of the tree'.\" ", 

            "How is this meant[1]?", 

            " Should I say that he drinks it as a beverage, it does him harm[2];", 

            " for there is a teaching : ", 

            "He who drinks the oil of an offering repays its value but not a fifth in addition ; but he who anoints himself with the oil of an offering repays its value plus a fifth[3]! ", 

            "But [perhaps it is here meant that] he eats it together with bread.", 

            " If so, the bread is the principal food and the oil is only accessory ; ", 

            "and we have the Mishnaic teaching : This is the general rule :", 

            " In the case of a food which is the principal thing and together with it something accessory, the benediction is to be uttered over the former, and there is no necessity for a benediction over the latter ! ", 

            "But ", 

            "[perhaps what is meant is] he drinks it with elaiogaron[4].", 

            " (Rabbah b, Samuel said[5] :", 

            "Elaiogaron is the juice of beets ; oxygaron is the juice "

        ], 

        [

            " of all other kinds of boiled vegetables.)", 

            " If so, the elaiogaron is the principal thing and the oil an accessory ;", 

            " and we have the Mishnaic teaching : This is the general rule :", 

            " In the case of a food which is the principal thing and together with it is something accessory, the benediction is to be uttered over the former, and there is no necessity for a benediction over the latter ! ", 

            "With what are we here dealing [6]? With the case of one who has a sore throat[7]; ", 

            "for there is a teaching : ", 

            "One suffering from a sore throat may not directly mollify it with oil on the Sabbath, but he should put a large quantity of oil into an elaiogaron and swallow it.", 

            " This is evident[8]!", 

            " But shouldest thou imagine that", 

            "because he intends it as a cure no benediction at all is necessary, therefore it informs us that ", 

            "since he derives enjoyment from it, he is required to pronounce a benediction[9]. ", 

            "Over wheaten-flour, Rab Judah says : ", 

            "[The benediction is] \"...Who createst the fruit of the ground.\"", 

            " Rab Nahman said :", 

            " It is \"...By Whose word all things exists[1].\" ", 

            "Raba said to Rab Nahman : ", 

            "Thou shouldest not differ from Rab Judah, because R. Johanan and Samuel agree with him ; ", 

            "for Rab Judah said in the name of Samuel, and similarly said R. Isaac in the name of R. Johanan : ", 

            "We pronounce over olive-oil the benediction \"... Who createst the fruit of the tree\" — ", 

            "hence infer  that ", 

            "although it has undergone change[2], it still remains essentially the same[3];", 

            " and like-wise here [with wheaten-flour] although it has undergone change, it still remains essentially the same[4].", 

            " Are, however, the two cases analogous ?", 

            " There [with oil], it has not another and higher value ; but here it has by being made into bread !", 

            " But if [the wheaten-flour] have another and higher value, should we no longer use the benediction \"...Who createst the fruit of the ground,\" but say instead \"...By Whose word all things exist\"? ", 

            "And lo, R. Zera said in the name of Rab Mattena in the name of Samuel : ", 

            "Over raw cabbage and barley-flour we use the benediction \"...By Whose word all things exist\"; is it not then to be supposed that wheaten-flour requires the benediction \"...Who createst the fruit of the ground[5]\"?", 

            " No; wheaten-flour also requires \"...By Whose word all things exist.\" ", 

            "Then he should have specified wheaten-flour, and [we could have argued for ourselves] how much more so barley-flour[6]!", 

            " If he had specified wheaten-flour, I might have thought that", 

            " it applies only to wheat, but barley requires no benediction at all ; therefore he mentioned it for us. ", 

            "Is, then, [barley-flour] of less value than salt and brine[7]? ", 

            "For there is a teaching[8]: ", 

            "Over salt and brine one says \"...By Whose word all things exist.\"", 

            " It was necessary[9] ; for otherwise it might have entered thy mind to item, the rest being accessory; consequently it is established that there is a circumstance where oil requires a benediction. say that", 

            " salt or brine a man is accustomed to convey to his mouth [with his food, and therefore a benediction is required], but since barley-flour is injurious by creating tape-worms no benediction should be uttered at all ;", 

            " therefore he teaches us that ", 

            "since there is some enjoyment therefrom, it is necessary to pronounce a benediction. ", 

            "Over the palm-heart[1], Rab Judah said:", 

            " [The benediction is] \"...Who createst the fruit of the ground\" ; ", 

            "but Samuel said :", 

            " It is \"...By Whose word all things exist.\" ", 

            "Rab Judah said : It is \"...Who Greatest the fruit of the ground\" because it is fruit. Samuel said : It is \"...By Whose word all things exist\" because in the end it hardens[2]. ", 

            "Samuel said to Rab Judah : ", 

            "Thou keen-witted one[3]! ", 

            "Thy opinion is correct: because over the radish, though it in the end grows hard, we say \"...Who createst the fruit of the ground.\"", 

            " But it is not so[4] ! For people plant radishes for the sake of the tuber, but people do not plant palms for the sake of the heart[5] ! Is it, then, [to be assumed] that", 

            " in every case where men do not plant specifically to obtain that article of food, we do not pronounce the benediction[6] over it?", 

            " Lo, the caper-bush men plant for the purpose of the caper-blossom ; and we have a Mishnaic teaching : ", 

            "In the case of the various kinds of capers, over the leaves and young shoots one says", 

            " \"...Who createst the fruit of the ground,\" but over the berries and buds[7]", 

            " \"...Who createst the fruit of the tree[8]\" !", 

            " Rab Nahman b. Isaac said : ", 

            "Men do plant caper-bushes for the sake of the shoots, but not the palm for the sake of the heart ; ", 

            "and although Samuel praised Rab Judah[9], the Halakah is in agreement with Samuel. ", 

            "Rab Judah said in the name of Rab : ", 

            "As for the caper-bush which is still in a state of 'Orlah outside the [Holy] Land, one throws away the berries but eats the buds ;", 

            " that is to say, the berries are fruit[1] but not the buds. ", 

            "Against this [deduction] I quote :", 

            " ln the case of the various kinds of capers, over the leaves and their young shoots one says \"...Who createst the fruit of the ground,\" but over the berries and buds \"...Who createst the fruit of the tree[2]!\" ", 

            "He[3] speaks according to the view of R. 'Akiba ;", 

            " for there is a Mishnaic teaching : R. Eliezer[4] says :", 

            " In the case of the caper-bush, we give tithe of the young shoots and the berries and buds ; R. 'Akiba says : ", 

            "We only give tithe of the berries because they are fruit[5]. ", 

            "Then let him say that the Halakah is in agreement with R. 'Akiba[6]! ", 

            "If he had said that the Halakah is in agreement with R. 'Akiba, I might have thought that [that is so] even in the Land of Israel ; therefore he informs us : ", 

            "Whoever takes a lenient view within the Land, the Halakah is in accord with him outside the Land, but not within. ", 

            "Then let him say : ", 

            "The Halakah is in agreement with R. 'Akiba outside the Land; for everyone who takes the lenient view within the Land[7], the Halakah is in accord with him outside the Land !", 

            " If he had stated that, I might have said : ", 

            "This applies to the tithe of trees which within the Land is a Rabbinical ordinance ; but with regard to 'Orlah, which within the Land is ordained by the Torah, I must suppose that likewise outside the Land we must apply it ! Therefore he informs us[8]. ", 

            "Rabina found Mar b. Rab Ashe throwing away the berries and eating the caper-buds[9].", 

            " He said to him :", 

            " What is thy opinion — like R. 'Akiba's who takes the lenient view[10]? Then let the master act in accord with Bet Shammai who take a still more lenient view[11].", 

            " For there is a Mishnaic teaching :", 

            " In the case of the caper-bush. Bet Shammai say :", 

            " It constitutes Kila'im in a vineyard ; but Bet Hillel say : ", 

            "It does not. Both, however, admit that it is subject to", 

            " 'Orlah. ", 

            "This is self-contradictory ! ", 

            "Thou declarest, \"In the case of the caper-bush, Bet Shammai say :", 

            " It constitutes Kila'im in a vineyard\" — hence it is a kind of vegetable[1] ! It then goes on to state,", 

            " \"Both, however, admit that it is subject to 'Orlah\" — hence it is a kind of tree[2]! ", 

            "There is no contradiction; ", 

            "for Bet Shammai, being in doubt[3], take the stricter view in both cases[4]. ", 

            "Nevertheless[5] Bet Shammai have a doubt whether it is subject to 'Orlah; and we have a Mishnaic teaching:", 

            " Where there is a doubt [whether a thing is subject to] 'Orlah — in the Land of Israel it is prohibited [to be used][6], in Syria it is permitted, and outside the Land one may go down and buy it, "

        ], 

        [

            "but he must not see the man gathering it [from the bushes][7]. ", 

            "When R. 'Akiba is in opposition to R. Eliezer, we act according to his view[8]; but when Bet Shammai are in opposition to Bet Hillel, [the opinion of the former] is not Mishnah[9]. ", 

            "Thou mayest, however, derive [a conclusion][10] from the fact that [the bud] constitutes a protection of the fruit, and the All-merciful declared, ", 

            "\"Ye shall deem it an uncircumcision with its fruit[11]\" (Lev. xix. 23) — the word \"with\" meaning to include what is attached to the fruit ; and what is that ? The protection of the fruit[12]. ", 

            "Raba replied : ", 

            "When do we declare a thing to be the protection of the fruit ? When it is so either plucked or attached [to the tree] ; but here [the bud is only a protection] when attached, but not when plucked[13].", 

            " Abbai quoted in objection:", 

            " The top-piece of a pomegranate is reckoned in[14] but not the blossom[1];", 

            " and since it is stated that the blossom is not reckoned in, conclude that it is not food. And we have a Mishnaic teaching with reference to 'Orlah : ", 

            "The skins of the pomegranate and its blossom, and the shells of nuts and the kernels are subject to 'Orlah[2] !", 

            " But, said Raba : ", 

            "When do we declare that a thing constitutes the protection of the fruit ? When it is there at the time the fruit has ripened ; but the caper-bud is not there at the time the fruit has ripened[3]. ", 

            "But it is not so[4] ! ", 

            "For Rab Nahman has said in the name of Rabbah b. Abbuha : ", 

            "The calyces surrounding dates are forbidden because of 'Orlah, since they are the protection of the fruit ; ", 

            "and when are they the protection of the fruit? In the early stages [of the fruit's growth], then are they called the protection of the fruit !", 

            " Rab Nahman holds the same view as R. Jose ;", 

            " for there is a Mishnaic teaching : R. Jose said : ", 

            "The grape-bud is forbidden[5] because it is fruit ; but the Rabbis differ from him[6]. ", 

            "Rab Shimi[7] of Nehardea[8] asked :", 

            " But do the Rabbis differ from him in the case of other trees[9]? ", 

            "For lo, there is a Mishnaic teaching : ", 

            "From what time must we cease cutting down the trees in the seventh year[10]?", 

            " Bet Shammai say : ", 

            "All trees, as soon as they produce fruit. ", 

            "Bet Hillel say : ", 

            "Carob trees when they begin to form chains, vines when they form globules, olive-trees when they bloom, and all other trees when they produce fruit. ", 

            "And Rab Assi[11] said : ", 

            "Boser and Garua' and the white bean are the same[12].", 

            " [The same as] the white bean, dost thou imagine ? ", 

            "Nay, the meaning is : ", 

            "The size [of Boser and Garua'] is like that of the white bean. ", 

            "Whom hast thou heard declaring that", 

            " the Boser is [to be considered fruit] but not the grape-bud? The Rabbis[13]. It states : ", 

            "\"All other trees when they produce fruit.\" ", 

            "But, said Raba: ", 

            "When do we say a thing is the protection of the fruit? When, if the protection is removed, the fruit perishes ;", 

            " but here [in the case of the caper] the fruit does not perish if the protecting [bud] is removed. The experiment was made ; they removed the blossom of the pomegranate and the fruit withered ; they removed the flower of the caper but the caper survived[1]. ", 

            "The Halakah is according to Mar b. Rab Ashe who threw away the berries and ate the buds ;", 

            " and since these are not regarded as fruit for the purpose of 'Orlah, they are likewise not so regarded for the purpose of the benediction. We accordingly utter over them not \"...Who createst the fruit of the tree\" but \"...Who createst the fruit of the ground.\" ", 

            "Over pepper, Rab Sheshet said:", 

            " [The benediction is] \"...By Whose word all things exist\" ;", 

            " Raba said :", 

            " None at all [is required][2]. ", 

            "Raba is consistent with his opinion [expressed elsewhere] ; for he has said : ", 

            "If one chews pepper-corns on the Day of Atonement he is free [from guilt][3]; if he chews ginger on the Day of Atonement he is likewise free.", 

            " It is quoted in objection :", 

            " R. Meir has declared : From the statement of Scripture, ", 

            "\"Ye shall deem it an uncircumcision with its fruit\" (Lev. xix. 23), do I not know that a food-bearing tree is intended ?", 

            " Why, then, is there a teaching to tell us \"trees for food\" (ibid.)? To include a tree whose wood and fruit taste alike. And which is that? Pepper ; to teach thee that pepper is subject to 'Orlah[4], and to teach thee that the Land of Israel lacks nothing ; as it is said, ", 

            "\"A land wherein thou shalt eat bread without scarceness, thou shalt not lack any thing in it\" (Deut. viii. 9)!", 

            " There is no contradiction[5] ; ", 

            "the latter refers to moist [pepper][6], the other to dried. ", 

            "The Rabbis[7] said to Maremar : ", 

            "He who chews ginger on the Day of Atonement is free [from guilt]. ", 

            "But lo, Raba declared :", 

            " The preserved ginger which comes from India is permitted[8], and we pronounce the benediction \"...Who createst the fruit of the ground\" over it[9]! ", 

            "There is no contradiction;", 

            " the latter referring to moist [ginger], the other to dried. ", 

            "Over Habis[1] boiled in a pot and also pounded grain,", 

            " Rab Judah said :", 

            " [The benediction is] \"...By Whose word all things exist\" ; ", 

            "Rab Kahana said : It is", 

            " \"...Who createst various kinds of food.\"", 

            " With plain pounded grain[2] all agree that \"...Who createst all kinds of foods\" is the correct benediction, the disagreement arising in connection with pounded grain made like a boiled Habis. Rab Judah maintained [that the benediction should be]", 

            " \"...By Whose word all things exist,\" being of the opinion that the honey is the principal ingredient ; ", 

            "whereas Rab Kahana maintained it is \"...Who createst various kinds of foods,\" holding that the flour is the principal ingredient. ", 

            "Rab Joseph said :", 

            " The view of Rab Kahana seems more probable, because Rab and Samuel both say that ", 

            "a dish which contains one of the five species[2] requires the benediction \"...Who createst various kinds of foods.\" ", 

            "It has just been mentioned : \"Rab and Samuel both say : ", 

            "A dish which contains one of the five species requires the benediction '...Who createst various kinds of foods'.\"", 

            " It has likewise been reported : Rab and Samuel both say:", 

            " A dish which is of the five species requires the benediction \"...Who createst various kinds of foods.\"", 

            " It was necessary [to give both these statements].", 

            " If we had been taught only the second, I might have said that [that benediction is required] because the dish has the appearance [of one of the five species], but not if mixed with other ingredients ;  "

        ], 

        [

            "therefore we are informed that a dish which  contains it [requires that benediction].  ", 

            "If, on the other hand, we had been taught only the first, I might have said a dish containing any of the five species does [require that benediction], but not rice or millet because these are mixed with other ingredients. ", 

            "Should, however, it have the appearance [of one of the five species], we might say that even with rice or millet we pronounce the benediction \"...Who createst various kinds of foods\"; therefore we are informed, ", 

            "\"A dish which is of the five species requires the benediction '...Who createst various kinds of foods',\"", 

            " to the exclusion of rice and millet ; for even if it retain its appearance we do not say that benediction. ", 

            "And over rice and millet do we not bless \"...Who createst various kinds of foods\"?", 

            " Lo, there is a teaching :", 

            " If they brought before a man bread of rice or of millet, he pronounces a benediction before and after as with any other cooked dish. ", 

            "And with reference to a cooked dish there is a teaching : ", 

            "Before partaking thereof one should bless \"...Who createst various kinds of foods\" and after it one benediction which is an abstract of three[1]!", 

            " [Bread of rice or of millet] is like a cooked dish [in one respect] but unlike a cooked dish [in another]. ", 

            "It is like a cooked dish in so far as there is a benediction before and after partaking thereof.", 

            " But it is unlike a cooked dish; for over a cooked dish one says at first \"...Who createst various kinds of foods,\" and in the end one benediction which is an abstract of three. [With rice and millet], however, one first says \"...By Whose word all things exist\" and in the end \"...Who createst many living beings with their wants,\" etc.[2] ", 

            "Is not rice a cooked dish[3]? ", 

            "And lo, there is a teaching ; The following are cooked dishes[3] :", 

            " grist, groats, fine flour, split grain, barley-meal and rice! ", 

            "Who said this? R. Johanan b. Nuri ; ", 

            "for there is a teaching : R. Johanan b. Nuri says :", 

            " Rice is a species of corn[3], and through its fermentation [during Passover] one incurs the penalty of excision[4]; but a man can comply with the requirements of the law therewith during Passover[5]. ", 

            "The Rabbis, however, do not agree with him. ", 

            "Do they not?", 

            "Lo, there is a teaching : ", 

            "He who chews wheat should say the benediction \"...Who createst the fruit of the ground\";", 

            " if he ground it, baked and then boiled it, should the pieces of bread be still whole, before partaking thereof he says \"...Who bringest forth bread from the earth[6]\" and afterwards he says the three benedictions[7]; but if the pieces are no longer whole[8], he first says \"...Who createst various kinds of foods\" and afterwards one benediction which is an abstract of three. ", 

            "He who chews rice says the benediction \"...Who createst the fruit of the ground\";", 

            " if he ground it, baked and then boiled it, although the pieces are still whole, he first says \"...Who createst various kinds of foods\" and afterwards one benediction which is an abstract of three.", 

            " According to whom [is this teaching]? ", 

            "If I say it is R. Johanan b. Nuri who declared \"Rice is a kind of corn,\" then one should say \"...Who bringest forth bread from the earth\" and the three benedictions[1]! ", 

            "Must it not be the Rabbis[2]? This is a refutation of Rab and Samuel[3], ", 

            "and it remains unanswered. ", 

            "The teacher stated :", 

            " \"He who chews wheat should say the benediction '...Who createst the fruit of the ground'.\" ", 

            "But there is a teaching: ", 

            "[He should say] \"...Who createst divers kinds of seeds\"![4]", 

            " There is no contradiction;", 

            " the latter being the opinion of R. Judah[5], the other of the Rabbis. ", 

            "For our Mishnah teaches : Over vegetables one says :", 

            " \"...Who createst the fruit of the ground\" ;", 

            " but R. Judah declares:", 

            " \"...Who createst divers kinds of herbs.\" ", 

            "The teacher stated : ", 

            "\"He who chews rice says the benediction '...Who createst the fruit of the ground'; if he ground it, baked and then boiled it, although the pieces are still whole, he first says '...Who createst various kinds of foods' and afterwards one benediction which is an abstract of three.\"", 

            " But there is a teaching:", 

            " After partaking thereof no benediction is required ! ", 

            "Rab Sheshet said : ", 

            "There is no contradiction : ", 

            "one being the opinion of Rabban Gamaliel, the other of the Rabbis. ", 

            "For there is a teaching : This is the general rule — ", 

            "Any food which belongs to the seven species[6], Rabban Gamaliel says :", 

            " Three benedictions [are required after partaking thereof], whereas the Rabbis say :", 

            " One benediction which is an abstract of three. ", 

            "It once happened that Rabban Gamaliel[7] and the Elders were reclining in an upper chamber in Jericho ; dates were set before them and they ate. Rabban Gamaliel gave permission to R. 'Akiba to say Grace[8].", 

            " R. 'Akiba sat up and said one benediction which is an abstract of three. ", 

            "Rabban Gamaliel said to him,", 

            " \"'Akiba, how long wilt thou put thy head between strife!\" ", 

            "He replied,", 

            " \"Our master ! Although thou sayest thus and thy colleagues say otherwise, thou hast taught us, our master, ", 

            "that where the individual and the many differ, the Halakah is in accord with the view of the many ! \" ", 

            "R. Judah said in his name[1] : ", 

            "Any food which belongs to the seven species "

        ], 

        [

            " and is not a kind of corn, or if a kind of corn it has not been made into bread, Rabban Gamaliel declares ", 

            "three benedictions [are required after partaking thereof], but the Sages declare: ", 

            "Only one benediction[2].", 

            " And any food which does not belong to the seven species and is not a kind of corn, for instance, bread of rice or millet, Rabban Gamaliel declares:", 

            " One benediction which is an abstract of three, but the Sages declare : ", 

            "None at all. ", 

            "According to whom, then, dost thou confirm [the teaching: After partaking of rice one benediction which is an abstract of three is necessary] ? According to Rabban Gamaliel. I will quote the latter part of the first teaching, viz. :", 

            " \"If the pieces are no longer whole, he first says '...Who createst various kinds of foods' and afterwards one benediction which is an abstract of three.\" Whose teaching is this ?", 

            " If Rabban Gamaliel's, since he has just declared that for dates and pounded grain [3] three benedictions are necessary, how much more necessary should they be if the pieces are no longer whole[4]! ", 

            "Nay, it is evident that it must be the Rabbis'[5]. If so, the Rabbis contradict themselves[6]! ", 

            "But it is certainly the view of the Rabbis ; and with reference to rice the teaching is: ", 

            "After partaking thereof ", 

            "no benediction is required[7]. ", 

            "Raba said : ", 

            "Over the Rihata[8] of the field labourers which contains a large admixture of flour, the benediction is \"...Who createst various kinds of food.\"", 

            " Why? Because the flour is the principal ingredient. ", 

            "[Over the Rihata] of townspeople which does not contain so much flour, the benediction is \"...By Whose word all things exist.\"", 

            " Why? Because honey is the principal ingredient.", 

            "Raba afterwards said :", 

            " Over both kinds the benediction is \"...Who createst various kinds of foods\";", 

            " because Rab and Samuel both declare : ", 

            "Over any food which contains one of the five species, the benediction is \"...Who createst various kinds of foods.\" ", 

            "Rab Joseph said : Over the Habis which contains pieces of bread the size of an olive, before partaking thereof the benediction is \"...Who bringest forth bread from the earth,\" and afterwards three benedictions. ", 

            "If it does not contain pieces of bread the size of an olive, before partaking thereof the benediction is \"...Who createst various kinds of foods\" and afterwards one benediction which is an abstract of three. ", 

            "Rab Joseph said : ", 

            "Whence have I this' ? There is a teaching: ", 

            "If one[2] were standing and bringing meal-offerings in Jerusalem, he says", 

            " \"Blessed [art Thou, O Lord our Grod, King of the universe], Who has kept us in life, and hast preserved us, and enabled us to reach this season.\"", 

            " If he[3] takes them to eat, he says the benediction \"...Who bringest forth bread from the earth\"; and it is taught in this connection : ", 

            "They must all be broken into pieces[4] about the size of an olive. ", 

            "Abbai said to him : ", 

            "But according to the Tanna of the school of R. Ishmael who declared, \"He must crumble [the meal-offerings] until they return to the condition of flour [before eating thereof],\" it would then be unnecessary to pronounce the benediction \"...Who bringest forth bread from the earth[5].\" ", 

            "And if thou sayest that is so[6], lo there is a teaching :", 

            " If he gathered together from all of them[7] about the size of an olive and ate them, should it be leaven he incurs the penalty of excision[8], and if unleaven, a man can therewith comply with the requirements of the law during Passover[9]! ", 

            "With what are we here dealing? When he rekneaded the crumbs into a compact mass[1]. ", 

            "In that case, I shall quote the latter part of the Baraita:", 

            " That is, only if he eats them the time it takes to eat half [a roll][2]. But if he rekneaded them, it should have stated \"he eats it\" ", 

            "not \"he eats them\"! ", 

            "With what are we here dealing ? When [the crumbs] are from a whole[3] loaf.", 

            "How is it then in this matter? ", 

            "Rab Sheshet said : ", 

            "Over Habis, although it does not contain pieces of bread the size of an olive, he blesses \"...Who bringest forth bread from the earth.\"", 

            " Raba said :", 

            " This is only so if it has the semblance of bread. ", 

            "Troknin[4] is subject to Hallah. ", 

            "When Rabin came, R. Johanan said:", 

            " It is exempt from Hallah. ", 

            "What is Troknin ?", 

            "Abbai[5] said :", 

            " Dough baked in a cavity made in the ground. ", 

            "Abbai also said :", 

            " Tarita is exempt from [6] Hallah. ", 

            "What is Tarita? ", 

            "Some say : ", 

            "A scalded puff-pastry. Others declare it to be", 

            " Indian bread[7]. ", 

            "Yet others declare it to be ", 

            "bread made into Kuttah[8]. ", 

            "R. Hiyya taught : ", 

            "Bread made into Kuttah is exempt from Hallah. ", 

            "But there is a teaching ;", 

            " It is subject to Hallah !", 

            " Yes, but there it mentions the reason, viz. : R. Judah says : ", 

            "The way they are made decides[9]. "

        ], 

        [

            " If he made them into cakes[10], they are subject [to Hallah]; but if he made them into \"shingles[11],\" they are exempt. ", 

            "Abbai asked Rab Joseph : ", 

            "Which benediction is to be said over dough baked in a cavity made in the ground ?", 

            " He said to him : ", 

            "Dost thou consider it to be bread ?", 

            " It is only a thick mass, and the benediction is \"...Who createst various kinds of foods.\" ", 

            "Mar Zotra made a meal of it and said the benediction \"...Who bringest forth bread from the earth\" and [afterwards] the three benedictions[1].", 

            " Mar b. Rab Ashe said :", 

            " A man can comply with the requirements of the law therewith on the Passover. On what ground ? We may apply to it the term \"bread of affliction\" (Deut. xvi. 3). ", 

            "Mar b. Rab Ashe also said : ", 

            "Over the honey of the date-palm we use the benediction \"...By Whose word all things exist[2].\" ", 

            "What is the reason ?", 

            " Because it is only the moisture [of the tree]. ", 

            "According to whom is this ?", 

            " According to the Tanna of the following Mishnaic teaching :", 

            " In the case of the honey of the date-palm, cider, the vinegar of winter-grapes[3] and other fruit-juices which are brought as an offering, [if a non-priest in error partake thereof] R. Eliezer condemns him to pay the value plus a fifth[4]; but R. Joshua exempts him[5]. ", 

            "One of the Rabbis asked Raba : ", 

            "How is it with Trimma[6] ? ", 

            "Raba was not sure what he had asked him. ", 

            "Rabina was sitting in the presence of Raba and said [to the questioner] :", 

            " Dost thou mean a brew of sesame seeds, or of saffron, or of grape-kernels ?", 

            " In the meantime Raba recalled it[7] and he said to him : ", 

            "Thou must surely mean a brew of ground dates ; and thou remindest me of something that R. Assi said, ", 

            "viz. : It is permissible to make Trimma from dates brought as an offering, but one must not make strong drink of them. ", 

            "And the Halakah is : ", 

            "Over dates made into Trimma we say the benediction \"...Who createst the fruit of the tree.\"", 

            " On what ground ? Because [the dates are considered] as remaining in their original condition [as fruit]. ", 

            "Over Shattit[8] Rab said :", 

            " [The benediction is] \"...By Whose word all things exist\"; Samuel said: It is ", 

            "\"...Who createst various kinds of foods.\" ", 

            "Rab Hisda said : ", 

            "There is no difference of opinion between them ;", 

            " the latter referring to a thick mass, the other to a thin mass. The thick mass is used as food, the thin as a remedy. ", 

            "Rab Joseph[1] quoted in objection : ", 

            "\"[R. Judah and R. Jose] both hold that we may stir up a Shattit on the Sabbath and drink Egyptian beer[2]\" !", 

            " If, then, thou thinkest that [the Shattit] is intended as a remedy, is it permitted to compound a remedy on the Sabbath ? ", 

            "Abbai said to him :", 

            " Art thou not of the opinion [that it is permitted to compound a remedy on the Sabbath] ?", 

            " Lo, there is a Mishnaic teaching :", 

            " All foods may be eaten as a remedy, and likewise all liquids may be drunk !", 

            " What is there for thee to say[3]?", 

            " The man intended it as a food [and therefore it may be prepared on the Sabbath] ; so here also [in the case of the Shattit] the man intended it as a food. ", 

            "(Another version is : ", 

            "What is there for thee to say? The man intended it as a food, and it became a remedy of itself ; so here also [the Shattit] was intended as a food, and it became a remedy of itself[4].) ", 

            "It was necessary to have the statements of Rab and Samuel[5]. ", 

            "For from that [quotation from the Mishnah] I might have said that [only when the Shattit] is intended as a food and becomes a remedy of itself [is a benediction required] ;", 

            " but here, since it was from the outset intended as a remedy, no benediction is at all required[6]. Therefore [from Rab and Samuel's statement] we are informed that ", 

            "since one derives enjoyment therefrom, it is necessary to say a benediction. ", 

            "For over bread one says : \"... Who bringest forth bread from the earth.\" ", 

            "Our Rabbis have taught : ", 

            "What does he say ? ", 

            "\"...Who bringest forth [hammosi'] bread from the earth.\" R. Nehemiah stated : ", 

            "It is \"...Who brought forth [mosi'][7] bread from the earth.\" ", 

            "Raba said : ", 

            "Nobody disagrees about mosi that it has the meaning \"brought forth\" ; as it is said, ", 

            "\"God Who brought them forth [mosiam][8] out of Egypt\" (Num. xxiii. 22). In what do they differ? In the word hammosi'.", 

            " The Rabbis hold that ", 

            "hammosi' means \"Who brought forth,\" for it is written", 

            " \"Who brought thee forth [hammosi'] water out of the rock of flint\" (Deut. viii. 15) ;", 

            " and R. Nehemiah holds it means ", 

            "\"Who bringeth forth,\" as it is said, ", 

            "\"Who bringeth you out [hammosi'] from under the burden of the Egyptians\" (Exod. vi. 7).", 

            " The Rabbis explain this verse as follows :", 

            " Thus spake the Holy One, blessed be He, to Israel,", 

            " \"When I bring you forth, I will do that for you whereby you may know that I am He that brought you forth[1] from Egypt; for it is written", 

            " 'And ye shall know that I am the Lord your God Who brought you out [hammosi']'\" (ibid.). ", 

            "The Rabbis praised Rab Zebid the father of R. Simeon b. Rab Zebid to R. Zera[2] as being a great man and expert in the benedictions.", 

            " R. Zera said to them, ", 

            "\"Should he come to you bring him to me.\" ", 

            "On one occasion Rab Zebid paid him a visit. He was handed some bread, and began the benediction [using the word] mosi'. ", 

            "R. Zera exclaimed,", 

            " \"Is this he of whom they declare he is a great man and expert in the benedictions !", 

            " It would have been right if he had said hammosi';\n"

        ], 

        [

            " then he would have informed us of the explanation[3] and also intimated that the Halakah is in accord with the Rabbis.", 

            " But since he said mosi', what does he wish us to infer?\" ", 

            "But Rab Zebid acted thus to exclude himself from the divergence of opinion, ", 

            "the Halakah being in agreement with the Rabbis, viz. : ", 

            "hammosi', for it is established in accord with the Rabbis who declare", 

            " the word to mean \"Who brought forth[4].\" ", 

            "Over vegetables one says : ", 

            "He teaches that vegetables resemble bread [in this respect] : as bread is changed by the fire [in appearance, but the benediction remains unaltered], so also are vegetables changed by the fire [but the benediction is the same].", 

            " Rabbanai[5] said in the name of Abbai : This means that", 

            " the benediction over boiled vegetables is \"...Who createst the fruit of the ground.\" (From whence is this derived ? Since he taught that vegetables resemble bread[1].) ", 

            "Rab Hisda expounded in the name of our teacher — and who is he? Rab:", 

            " Over boiled vegetables we pronounce the benediction \"...Who createst the fruit of the ground\" ; ", 

            "but our teachers who came down from the land of Israel [to Babylon] — and who are they ? 'Ulla in the name of R. Johanan — said : ", 

            "Over boiled vegetables we pronounce the benediction \"...By Whose word all things exist.\"", 

            " I[2] say that ", 

            "any article of food which in its original state[3] requires \"...Who createst the fruit of the ground,\" if cooked requires \"...By Whose word all things exist\" ; ", 

            "and whatever in its original state[4] requires \"...By Whose word all things exist,\" if cooked requires \"...Who createst the fruit of the ground.\" ", 

            "It is quite right that food which in its original state requires \"...By Whose word all things exist,\" if cooked requires \"...Who createst the fruit of the ground\" ; for it is found thus in the instances of cabbage, beet and the pumpkin. ", 

            "But something which in its original state requires \"...Who createst the fruit of the ground,\" if cooked requires \"...By Whose word all things exist\" — where is such to be found ? ", 

            "Rab Nahman b. Isaac said :", 

            " There are the instances of garlic and leek. ", 

            "Rab Nahman expounded in the name of our teacher — and who is he? Samuel : ", 

            "Over boiled vegetables we pronounce the benediction \"...Who createst the fruit of the ground\"; ", 

            "but our colleagues who came down from the land of Israel — and who are they ? 'Ulla in the name of R. Johanan — said : ", 

            "Over boiled vegetables the benediction is \"... By Whose word all things exist.\"", 

            " I say that", 

            " [their difference of opinion] is taught in the following controversy; ", 

            "for there is a teaching : ", 

            "One complies with the requirements of the law[5] with a wafer which has been soaked or cooked, provided it has not dissolved. These are the words of R. Meir[6] ; but R. Jose says : ", 

            "One complies with the requirements of the law with a wafer which has been soaked, but not with one which has been cooked even if it has not dissolved[7]. ", 

            "It is not so ; for it is agreed by all that over boiled vegetables the benediction is \"...Who createst the fruit of the ground[1]\" ; and only in this case[2] does R. Jose say so because we require the taste of the unleavened bread, and it is not there [if the wafer is cooked]. Hence, however, even R. Jose admits it[3]. ", 

            "R. Hiyya b. Abba said in the name of R. Johanan : ", 

            "Over boiled vegetables we pronounce the benediction \"...Who createst the fruit of the ground.\" But R. Benjamin b. Jephet said in the name of R. Johanan: ", 

            "Over boiled vegetables the benediction is \"...By Whose word all things exist.\" ", 

            "Rab Nahman b. Isaac said :", 

            " 'Ulla confirmed this error according to R. Benjamin b. Jephet[4]. ", 

            "R. Zera asked in astonishment : ", 

            "What has the statement of R. Benjamin b. Jephet to do by the side of that of R. Hiyya b. Abba[5] !", 

            " R. Hiyya b. Abba paid careful attention and learnt the teaching from R. Johanan his master, but R. Benjamin b. Jephet was not so attentive. ", 

            "Also, R. Hiyya b.Abba used to revise his study in the presence of R. Johanan his master every thirty days, but R. Benjamin b. Jephet did not do so.", 

            " Besides, apart from these two reasons[6], there is the incident when lupines were cooked seven times in a pot and eaten as a dessert ; they came and questioned R. Johanan[7], and he replied,", 

            " \"...Who createst the fruit of the ground[8].\"", 

            " And R. Hiyya b. Abba likewise said :", 

            " I saw R. Johanan eat a salted[9] olive, and he pronounced a benediction before and after. ", 

            "This is quite right if thou maintainest that food when cooked is to be regarded as remaining the same ; then, before partaking [of the salted olive] the benediction is \"...Who createst the fruit of the tree,\" and afterwards he says one benediction which is an abstract of three. Shouldest thou, however, maintain that cooked food is not to be regarded as remaining the same, it is right that before partaking thereof one should say \"...By Whose word all things exist\" ; but what benediction is to be said afterwards ? ", 

            "Perhaps", 

            " \"...Who createst many living beings with their wants\" etc.[1] ", 

            "Rab Isaac b. Samuel[2] quoted in objection :", 

            " In the case of herbs wherewith one complies with the requirements of the law on Passover, they or their stalk are legitimate, but not if they have been pickled or cooked or sodden !", 

            " If thou thinkest they are to be regarded as remaining the same, why not when [these herbs are cooked] ? There it is different ; ", 

            "because we require the taste of the bitter herbs[3] and it is not there [if they are cooked]. ", 

            "R. Jeremiah asked R. Zera,", 

            " \"How could R. Johanan pronounce a benediction over a salted olive", 

            " since, if the stone had been removed,  "

        ], 

        [

            "the minimum quantity is wanting[4]?\"", 

            " He replied, ", 

            "\"Dost thou think that the quantity equivalent to a large olive is necessary [to constitute the minimum] ? ", 

            "About the size of an average olive is sufficient ; and there was that quantity, because the olive which they brought to R. Johanan was of a large size, so that although the stone was removed, the minimum still remained.\"", 

            " For there is a Mishnaic teaching :", 

            " The olive which they mention [as constituting the minimum] is neither small nor large but an average size, viz. : the kind called Egori[5].", 

            " R. Abbahu said :", 

            " Its name is not Egori but Ibroti[6]; and some say ", 

            "Simrosi[7]. Why is it called Egori ? Because its oil is stored up [agur] within it. ", 

            "We can say that this is like [the discussion of] the Tannaim. For two disciples were sitting in the presence of Bar Kappara, When there were set before him cabbage, Damascene plums and poultry. Bar Kappara gave one of the disciples permission to say the benediction. He sat up and said the benediction over the poultry. His companion laughed at him, ", 

            "and Bar Kappara became angry, saying,", 

            "\"Not with him who uttered the benediction, but with him who laughed, am I angry.", 

            " If thy companion is like one who has never tasted meat[1], wherefore dost thou laugh at him?\" ", 

            "Then he said, ", 

            "\"Not with him who laughed am I angry, but with him who uttered the benediction\" ;", 

            " and he continued,", 

            " \"If there is no wisdom here, is there no old age here[2]?\"", 

            " It has been taught that", 

            " both of them did not survive that year[3].", 

            " Is it not that they differed in the following point :", 

            " He who said the benediction thought that", 

            " for cooked vegetables and poultry it is \"...By Whose word all things exist,\" and therefore what is best liked is to be preferred [for the benediction][4] ; ", 

            "but he who laughed thought that for cooked vegetables it is \"...Who createst the fruit of the ground\" and for poultry \"...By Whose word all things exist,\" and therefore the fruit should be given precedence ? ", 

            "No ; they both agreed that for cooked vegetables and poultry it is \"...By Whose word all things exist\" ; and here they differed on the following point : ", 

            "One thought that ", 

            "what is best liked is to be preferred [for the benediction], whereas the other thought that ", 

            "the cabbage should receive precedence", 

            " because it is nourishing[5]. ", 

            "R. Zera said : When we were at the school of Rab Huna he said to us :", 

            " For the tops of turnips, if he cut them into large pieces, the benediction is \"...Who createst the fruit of the ground\"; if into small pieces, it is \"...By Whose word all things exist[6].\" ", 

            "But when we came to the school of Rab Judah he said :", 

            " In either case it is ", 

            "\"...Who createst the fruit of the ground,\" because one cuts them up a great deal to sweeten the taste. ", 

            "Rab Ashe said : When we were at the school of Rab Kahana he said to us : ", 

            "For a broth of beet, into which one does not put much flour, the benediction is \"...Who createst the fruit of the ground \" ; for a broth of turnip, into which much flour is put, it is \"...Who createst various kinds of foods.\" ", 

            "Afterwards he said :", 

            " In either case it is \"...Who createst the fruit of the ground,\" and that they put much flour into it is only done to make it adhere. ", 

            "Rab Hisda said : ", 

            "The broth of beet is pleasant to the heart and good for the eyes, how much more so for the bowels. ", 

            "Abbai said :", 

            " That is only so when it remains on the stove and makes the sound Tuk, Tuk[1]. ", 

            "Rab Pappa said :", 

            " It is evident to me that the water of the beet is like the beet[2], the water of the turnip like the turnip, and the water of all vegetables like the vegetables themselves. ", 

            "Rab Pappa asked : ", 

            "How is it with dill-water ? Is it used to sweeten the taste[3] or to remove the bad smell? ", 

            "Come and hear:", 

            " Dill, when it gives a taste to the dish, does not come under the law of Terumah[4] and does not contract the impurity of foods. ", 

            "Conclude from this that", 

            "it is used to sweeten the taste! Draw that conclusion. ", 

            "Rab Hiyya b. Ashe said : ", 

            "Over stale bread [which has been placed] in a pot [to soak], the benediction is \"...Who bringest forth bread from the earth.\" This is at variance with R. Hiyya[5] who said :", 

            " This benediction must conclude with [the cutting or breaking of] the bread[6].", 

            " Raba retorted :", 

            "Why is stale bread different, that no [benediction should be pronounced before partaking thereof] ? Is it because when the benediction is concluded, it is concluded over a divided loaf ?  ", 

            "But in the case of [fresh] bread also, when the benediction is concluded, it is likewise concluded over a divided loaf !"

        ], 

        [

            "But, declared Raba :", 

            " One says the benediction and afterwards breaks [the bread]. ", 

            "The people of Nehardea[7] acted according to R. Hiyya, but the Rabbis acted according to Raba. ", 

            "Rabina said : My mother told me,", 

            " \"Thy father acted according to R. Hiyya, for R. Hiyya maintained that ", 

            "the benediction must conclude with [the breaking of] the bread ; but the Rabbis acted according to Raba.\" ", 

            "The Halakah is in agreement with Raba who maintained that ", 

            "one should say the benediction and afterwards break the bread. ", 

            "It has been reported : If pieces of bread and whole loaves were set before them, ", 

            "Rab Huna declares that ", 

            "the benediction is to be pronounced over the pieces and it is not necessary over the loave[8]. R. Johanan declared :", 

            " [To say the benediction over] the whole loaf is the best way to perform the religious duty ; but should there be a piece of wheaten-bread and a loaf of barley-bread, all agree that the benediction should be pronounced over the former[1] and is unnecessary over the latter.", 

            " R. Jeremiah b. Abba said :", 

            " It is like [the discussion of] the Tannaim, viz.: ", 

            "We take Terumah with a whole onion, though small in size, but not with half of a large onion. ", 

            "R. Judah says : ", 

            "Not so, but we take it with the half of a large onion. ", 

            "Do they not differ on the following point : One[2] maintains", 

            " that which is of greater value is to be preferred, ", 

            "while the other maintains that which is whole is to be preferred ? ", 

            "Where there is a priest present[3], there is no difference of opinion that what is of greater value is to be preferred, the disagreement arising where there is no priest[4]. ", 

            "For there is a Mishnaic teaching :", 

            " Wherever there is a priest present, the Terumah is to be taken from the best, but where there is no priest, it is to be taken from that which is most durable ; R. Judah says :", 

            " It is only to be taken from the best. ", 

            "Rab Nahman b. Isaac said : ", 

            "He who fears Heaven complies with the regulation of the law according to the teaching of both[5] ; and who is it [that acts thus]?", 

            " Mar b. Rabina, ", 

            "for he used to place the piece of bread with the whole loaf and break both. ", 

            "A Tanna taught in the presence of Rab Nahman b. Isaac[6] : ", 

            "One should place the piece of bread with the whole loaf and break them both and then say the benediction. ", 

            "Rab Nahman said to him,", 

            " \"What is thy name?\"", 

            " He replied,", 

            " \"Shalman[7].\"", 

            " He said to him,", 

            " \"Peaceful art thou and peaceful thy teaching, for thou hast restored peace between the disciples.\" ", 

            "Rab Pappa said : ", 

            "All agree that on Passover one should place the piece together with the whole and break them both.", 

            " What is the reason ? \"Bread of affliction\" (Deut. xvi. 3) it is written[8]. ", 

            "R. Abba[9] said : ", 

            "On the Sabbath one should break bread over two loaves. ", 

            "What is the reason ? \"Twice as much bread\" (Exod. xvi 22) it is written[1]. ", 

            "Rab Aahe said : ", 

            "I saw Rab Kahana take two loaves but only break one[2].", 

            " R. Zera used to break off [on the Sabbath a piece of bread to suffice] for the whole of the meal. ", 

            "Rabina said to Rab Ashe : ", 

            "But this must have looked like voracity !", 

            " He replied :", 

            " Since he did not act so every day but only now [on the Sabbath] it would not have that appearance. ", 

            "When R. Ammi and R. Assi had occasion to use the bread of 'Erub, they would pronounce over it the benediction \"...Who bringest forth bread from the earth,\" saying,", 

            " \"Since one religious duty[3] is being fulfilled therewith, let us perform still another[4].\" \n"

        ], 

        [

            "Rab[5] declared:", 

            " [If one broke the bread and pronounced the benediction, and before eating handed a piece to another saying,] \"Take it, the benediction has been made; take it, the benediction has been made ! \" it is unnecessary for him to pronounce it again [before partaking of the bread][6]. [But if before eating he says,] \"Bring salt, bring the relish,\" he must repeat the benediction. ", 

            "R. Johanan declared that", 

            " even if he said, \"Bring salt, bring the relish,\" he likewise need not repeat the benediction[7]. ", 

            "[Should he, however, say,] \"Mix food for the oxen ! Mix food for the oxen !\" the benediction must be repeated. ", 

            "Rab Sheshet declared that ", 

            "even if he said \"Mix food for the oxen,\" he also need not repeat the benediction. For Rab Judah said in the name of Rab: ", 

            "A man must not eat his meal before giving food to his cattle ; as it is said,", 

            " \"And I will give grass in thy fields for thy cattle\" and then \"thou shalt eat and be satisfied\" (Deut. xi. 15). ", 

            "Raba b. Samuel said in the name of R. Hiyya[8] : ", 

            "The one who is about to break bread is not permitted to do so until they place salt or relish before each person.", 

            "Raba b. Samuel visited the house of", 

            " the Exilarch[9]. They set bread before him and he broke it forthwith[1]. ", 

            "They said to him,", 

            " \"Has the master retracted his teaching?\" ", 

            "He replied, ", 

            "\"This bread[2] requires no condiment[3].\" ", 

            "Raba b. Samuel also said in the name of R. Hiyya : ", 

            "Urine is only completely evacuated in a sitting posture[4]. ", 

            "Rab Kahana said[5] : ", 

            "Where there is loose earth, this is so even when standing[6]; ", 

            "and should there be no loose earth, let him stand on an elevated place and urinate on to a declivity. ", 

            "Raba b. Samuel also Said in the name of R. Hiyya : ", 

            "After every food eat salt, and after every beverage drink water, and thou wilt not come to harm[7]. ", 

            "There is a teaching to the same effect : ", 

            "After every food eat salt, and after every beverage drink water, and thou wilt not come to harm. ", 

            "There is another teaching : ", 

            "Who has partaken of any food without eating salt or drunk any beverage without drinking water will be troubled during the day with a bad odour in his mouth and at night with croup. ", 

            "Our Rabbis have taught: ", 

            "He who makes his food float in water[8] will not suffer with indigestion. ", 

            "How much [should he drink] ? ", 

            "Rab Hisda said : ", 

            "A cupful to a loaf. ", 

            "Rab Mari said in the name of R. Johanan :", 

            " He who makes it a habit to eat lentils once in thirty days keeps croup away from his house ; ", 

            "but not every day. ", 

            "What is the reason[9] ? Because it is bad for the breath of the mouth. ", 

            "R. Mari also said in the name of R. Johanan : ", 

            "He who makes it a habit to eat mustard once in thirty days keeps illnesses away from his house ; but not every day. ", 

            "What is the reason ? Because it is bad for heartweakness. ", 

            "Rab Hiyya b. Ashe said in the name of Rab :", 

            " He who makes it a habit to eat small fish will not suffer with indigestion ; ", 

            "more than that, small fish make a man's whole body fruitful[10] and strong. ", 

            "Rab Hamma b. R. Hannina said: ", 

            "He who makes it a habit to use black cumin will not suffer with pain of the heart.", 

            " It is quoted in objection : Rabban Simeon b. Gamaliel says : ", 

            "Black cumin is one of the sixty deadly poisons, and he who sleeps to the east of his store [of cumin], his blood is on his own head[1] !", 

            " There is no contradiction ; ", 

            "the latter referring to its odour, the other to its taste. ", 

            "The mother of R. Jeremiah used to bake bread for him and sprinkle [black cumin] upon it, and then scrape it off[2]. ", 

            "But R. Judah declares :", 

            " \"...Who createst divers kinds of herbs.\" ", 

            "R. Zera (another version : R. Hinnana b. Pappa) said :", 

            " The Halakah is not in accord with R. Judah[3]. ", 

            "R. Zera (another version: R. Hinnana b. Pappa) also said: ", 

            "What is R. Judah's reason[4]? The Scriptures state,", 

            " \"Blessed be the Lord day by day\" (Ps. Ixviii. 20) — are we to bless Him by day and not by night ! ", 

            "Nay, it means to tell thee : ", 

            "Day by day give Him the appropriate blessing[5] ; ", 

            "so here also, for every species of food give Him an appropriate benediction. ", 

            "R. Zera (another version : R. Hinnana b. Pappa) also said : ", 

            "Come and see that the attribute of the Holy One, blessed be He, is not like that of the human being.", 

            " The attribute of the human being is to support the empty vessel[6] but not the full ; ", 

            "but the Holy One, blessed be He, is not so — He supports the full vessel, not the empty[7]. As it is said, ", 

            "\"And He said. If hearing, thou wilt hear\" (sic ! Exod. xv. 26) — i.e. if thou wilt hear [once], thou wilt hear again[8]; but if not, thou wilt not hear.", 

            " Another explanation is :", 

            " If thou wilt hear the old, thou wilt also hear the new[9]; but should thine heart turn aside [from the Torah], thou wilt never again hear. ", 

            "MISHNAH If one said the benediction \"... Who createst the fruit of the ground\" over fruits of the tree, he has complied with the requirements of the law. If, over fruits of the earth, he said \"...Who createst the fruit of the tree,\" he has not so complied.", 

            " If over all of them he said \"...By Whose word all things exist,\" he has complied with the requirements of the law. ", 

            "GEMARA Who is it that teaches that the main feature about the tree is the earth[1]? ", 

            "Rab Nahman b. Isaac said:", 

            " It is R. Judah ; for there is a Mishnaic teaching:", 

            " If the water-supply dried up[2] or the tree was cut down, one brings [the first-fruits to Jerusalem] but does not make the declaration[3]. ", 

            "R. Judah says: ", 

            "He both brings [the first-fruits] and makes the declaration[4]. ", 

            "If, over fruits of the earth, etc.  ", 

            "This is evident !", 

            "Rab Nahman b. Isaac said :", 

            " It is only necessary for R. Judah who declares that wheat is a kind of tree ;", 

            " for there is a teaching :", 

            " The tree from which Adam ate was — so says R. Meir —", 

            " the vine, because thou hast nothing which brings lamentation upon man as does wine; as it is said, ", 

            "\"And he drank of the wine, and was drunken\" (Gen. ix. 21). ", 

            "R. Nehemiah says:", 

            " It was the fig-tree, for by the very thing that they were disgraced were they restored ; as it is said, \"And they sewed fig-leaves together\" (ibid. iii. 7). ", 

            "R. Judah said :", 

            " It was wheat, because a child does not know to call \"Father, mother\" before it has tasted wheat[5].", 

            " It may enter thy mind to say that since R. Judah maintains that wheat is a kind of tree, the benediction over it should be \"...Who createst the fruit of the tree\"! Therefore we are informed that", 

            " we say the benediction \"...Who createst the fruit of the tree\" only where, if thou takest away the fruit, a stem remains which again produces ;  "

        ], 

        [

            "but where, if thou takest away the fruit, there is no stem to produce again fruit[1], we do not say the benediction \"...Who createst the fruit of the tree\" but \"...Who createst the fruit of the ground.\" ", 

            "If over all of them he said \"...By Whose word all things exist,\" etc. ", 

            "It has been reported : Rab Huna said : ", 

            "Except bread and wine[2] ; ", 

            "but R. Johanan said : ", 

            "Even bread and wine. ", 

            "Let us say that this is like [the following controversy of] the Tannaim :", 

            " If one sees bread and exclaims, \"How fine is this bread ; blessed be the All-present Who created it,\" he has complied with the requirements of the law[3].", 

            " If he sees a fig and exclaims,", 

            " \"How fine is this fig, blessed be the All-present Who created it,\" he has likewise complied. These are the words of R. Meir ;", 

            "but R. Jose says :", 

            " Whoever changes the form which the Sages assigned to the benedictions has not fulfilled his obligation. ", 

            "Let us say that Rab Huna is in agreement with R. Jose[4] and R. Johanan with R. Meir[5]!", 

            " Rab Huna could tell thee:", 

            " I am even in agreement with R. Meir ;", 

            " for R. Meir only speaks above of a case where one mentions the name of bread, but where he does not mention the name of bread, even R. Meir admits [that the man's words do not constitute a valid benediction][6].", 

            " R. Johanan, on the other hand, could tell thee :", 

            " I am in agreement even with R. Jose ; for R. Jose only disagrees above because the man used a form of benediction which the Rabbis had not ordained, but if he had said \"...By Whose word all things exist\" which the Rabbis had ordained, even R. Jose admits [that it would be valid]. ", 

            "Benjamin the shepherd used to double the bread[7] and say", 

            " \"Blessed be the Lord of this bread[8].\" ", 

            "Rab said:", 

            " He thereby complied with the requirements of the law. ", 

            "But Rab has declared :", 

            " A benediction which contains no mention of the Divine Name is no benediction[1]! ", 

            "What Benjamin did say was", 

            " \"Blessed be the All-merciful, the Lord of this bread.\"", 

            " But lo, we require three benedictions! ", 

            "What means, then, \"he has complied with the requirements of the law\" as stated by Rab? He has complied so far as the first benediction is concerned[2]. ", 

            "What does he intend to teach us? That [it is valid] although he said it in a non-holy tongue[3]! We have already learnt : The following may be said in any language : ", 

            "The portion of the Sotah[4], the declaration concerning the tithe[5], the Shema', Tefillah and the Grace after meals[6]!", 

            " [Nevertheless Rab's statement] was necessary ; ", 

            "for it might have entered thy mind to say that this[7] only applies when one utters the benediction in a non-holy language exactly as the Rabbis ordained it in the holy tongue ; but should he not say it in the non-holy language exactly as the Rabbis ordained it in the holy tongue, I am to declare that he has not [complied]. Therefore he informs us [that the benediction is valid even when the wording does not exactly conform to the Hebrew original]. ", 

            "It was stated above : \"Rab said : ", 

            "A benediction which contains no mention of the Divine Name is no benediction.\" ", 

            "But R. Johanan has said :", 

            " A benediction which contains no reference to the Divine Kingship[8] is no benediction! ", 

            "Abbai said: Rab's opinion seems more probable ; for there is a teaching[9] :", 

            " [It is written] \"I have not transgressed any of Thy commandments, neither have I forgotten\" (Deut. xxvi. 13) —", 

            " \"I have not transgressed,\" i.e. by omitting the benediction, \"neither have I forgotten,\" i.e. to mention Thy Name thereby ; but he does not teach here [that it is necessary to refer to] the Kingship.", 

            " (R. Johanan, however, explains : \"Neither have I forgotten,\" i.e. to mention Thy Name and Kingship thereby[10].) ", 

            "MISHNAH  Over anything whose growth is not from the earth, one says", 

            " \"...By Whose word all things exist.\" ", 

            "Over vinegar, fruit which falls unripe from the tree and locusts, one says", 

            " \"...By Whose word all things exist.\"", 

            " R. Judah declares:", 

            " No benediction is to be pronounced over anything which comes under the category of a curse[1]. ", 

            "If there were several kinds of food before him, R. Judah says: ", 

            "Should there be among them one of the seven species[2], he pronounces the benediction over that. ", 

            "The Sages declare: ", 

            "He may say it over whichever of them he pleases. ", 

            "GEMARA Our Rabbis have taught : ", 

            "Over anything whose growth is not food the earth, e.g.", 

            " the flesh of cattle, beasts, birds and fish, one says \"...By Whose word all things exist.\" ", 

            "Over milk, eggs and cheese, one says \"...By Whose word.\"", 

            " Over bread which has become mouldy, wine over which a film has formed, and cooked food which has gone bad[3], one says \"...By Whose word.\"", 

            " Over salt, brine, morils and truffles, one says \"...By Whose word.\" ", 

            "That is to say that morils and truffles are not grown from the soil. ", 

            "There is, however, a teaching : ", 

            "He who vows not to eat fruits grown from the earth is forbidden to eat the fruits of the earth but is allowed morils and truffles; if he declares, \"All that is grown from the earth shall be forbidden me,\" he is also prohibited from eating morils and truffles ! ", 

            "Abbai replied: ", 

            "These grow from the earth but do not derive their nutriment therefrom. ", 

            "But lo, the Mishnah reads : Anything whose growth is not from the earth! ", 

            "Read,", 

            " \"Anything which does not derive nutriment from the earth,\" ", 

            "Over fruit which falls unripe from the tree [nobelot]. ", 

            "What are nobelot?", 

            " R. Zera and R. El'a [differ in their explanation]. One says: ", 

            "They are the fruit scorched by the sun;", 

            " the other says : ", 

            "They are dates blown from the tree by the wind. ", 

            "Our Mishnah states : R. Judah declares :", 

            " No benediction is to be pronounced over anything which comes under the category of a curse. ", 

            "That is quite right according to him who says nobelot means \"Fruit scorched by the sun,\" for that may be called a kind of curse ; but according to him who says it means \"Dates blown from the tree by the wind,\" how is this a kind of curse? ", 

            "[R. Judah's statement refers] to the remainder[1]. ", 

            "Another version :", 

            " It is quite right according to him who says nobelot means \"Fruit scorched by the sun\" that over it we pronounce the benediction \"...By Whose word\"; ", 

            "but according to him who says [it means] \"Dates blown from the tree by the wind\" the benediction \"...By Whose word\" ", 

            "should rather be \"...Who createst the fruit of the tree[2]\" !", 

            " Nay,", 

            " everybody agrees that nobelot without further qualification means \"Fruit scorched by the sun\"; where they differ is with reference to nobelot temarah. ", 

            "For there is a Mishnaic teaching: ", 

            "Those fruits with which, in case of doubt as to the tithe[3], the law deals leniently are:", 

            " Shitin, Rimin, 'Uzradin[4], Benot Shuah, Benot Shikmah, Gofnin, Nispah and Nobelot Temarah. ", 

            "Shitin, Rabbah b. Bar Hannah said in the name of R. Johanan,", 

            " are a species of figs. Rimin are lote[5].", 

            " 'Uzradin are crab-apples.", 

            " Benot Shuah, Rabbah b. Bar Hannah said in the name of R. Johanan,", 

            " are white figs. ", 

            "Benot Shikmah, Rabbah b. Bar Hannah said in the name of R. Johanan,", 

            " are sycamore-figs.", 

            " Gofnin are late grapes.", 

            " Nispah is the caper-bush.", 

            " Nobelot Temarah — R. El'a and R. Zera [differ in their explanation] — One says", 

            " \"Fruit scorched by the sun\" ; the other says ", 

            "\"Dates blown from the tree by the wind.\" ", 

            "It is quite right according to him who says [it means] \"Fruit scorched by the sun,\" that is what he teaches, viz.", 

            " \"Those fruits with which, in case of doubt as to the tithe, the law deals leniently\" — it is the doubt that exempts them [from the tithe], but if there is certainty[6], then they are subject. ", 

            "But according to him who says it means \"Dates blown from the tree by the wind,\" how can they be subject [to the tithe] in the case of certainty, since they are public property[7]? ", 

            "With what are we here dealing? ", 

            "With a case where he has arranged them for storage; ", 

            "for R. Isaac[1] stated that R. Johanan said in the name of R. Eliezer b. Jacob : ", 

            "Gleanings, forgotten sheaves, and the produce of the corner of the field[2], if he[3] arranged them for storage, they become subject to the tithe.  ", 

            "Others say:"

        ], 

        [

            "It is quite right according to him who maintains it[4] means \"Dates blown from the tree by the wind\" — then that is why he mentions here [in our Mishnah] nobelot without further specification[5] and there [in the Mishnaic quotation] he calls it [nobelot] temarah. But according to him who says [nobelot temarah] means \"Fruit scorched by the sun,\" let him teach in both passages[6] either nobelot temarah or nobelot without further specification !", 

            " The question [remains unanswered]. ", 

            "If there were several kinds of food before him, etc. ", 

            "'Ulla said : ", 

            "The difference of opinion arises when the benediction is the same for them ; for R. Judah holds that", 

            " one of the seven species is to be given preference, whereas the Rabbis hold that", 

            " the kind which is best liked should be given preference. ", 

            "Where, however, the benediction is not the same, all agree that he should first say it over that which he likes best and then say it over the others. ", 

            "Against this is quoted :", 

            " If radishes and olives were before him, he pronounces the benediction over the radishes and he is exempt from saying it over the olives[7] ! ", 

            "With what are we here dealing? With the case where the radishes are the principal item[8].", 

            " If so, I will quote the continuation : ", 

            "R. Judah says : ", 

            "He pronounces the benediction over the olive, because it belongs to the seven species !", 

            " Does not R. Judah agree with the Mishnaic teaching :", 

            " In the case of a food which is the principal thing and together with it is something accessory, the benediction is to be uttered over the former and there is no necessity for a benediction over the latter[9]? ", 

            "Shouldest thou declare that here also R. Judah is not in agreement, lo there is a teaching : ", 

            "R. Judah says : If the olive is only there on account of the radish, he pronounces the benediction over the radish and it is unnecessary over the olive ! ", 

            "We certainly deal here with the case where the radish is the principal item ; and where R. Judah and the Rabbis differ is in another matter. The text is defective and should read thus :", 

            "[There were before him]", 

            " If radishes and olives were before him, he says the benediction over the former and it is unnecessary over the latter. ", 

            "Of what does it speak here? When the radish is the principal item ; but should that not be so, all agree that he says the benediction over one and then over the other. ", 

            "Where there are two species, the benediction for which is the same, he says the benediction over any one he pleases ", 

            "R. Judah says : ", 

            "He utters it over the olive, because it is one of the seven species. ", 

            "R. Ammi and R. Isaac Nappaha[1] are at variance over this matter[2].", 

            " One declares that the difference of opinion arises ", 

            "when the benediction is the same, for R. Judah holds that one of", 

            " the seven species is to be given preference, whereas the Rabbis hold that ", 

            "the kind which is best liked is to be given preference. Where, however, the benediction is not the same, all agree that he says the benediction over one and then over the other. ", 

            "The second [Rabbi] declares that", 

            " there is difference of opinion even where the benediction is not the same. ", 

            "It is quite right according to him who declares that there is difference of opinion where the benediction is the same; that is clear. But according to him who declares that they disagree where the benediction is not the same, in what do they differ? ", 

            "R. Jeremiah said :", 

            " In which is to come first ;", 

            " for Rab Joseph (another version : R. Isaac) said : ", 

            "Whatever is given precedence in the Scriptural verse must take precedence for the benediction ; as it is said, ", 

            "\"A land of wheat and barley, and vines and fig-trees and pomegranates, a land of olive trees and honey\" (Deut. viii. 8)[3]. ", 

            "This teaching, however, conflicts with the statement of R. Hanan[4] ", 

            "who said: This whole verse only speaks of \"standards[5].\"", 

            " \"Wheat\" — for there is a Mishnaic teaching :", 

            " Whoever enters a plague-infected house with his garments upon his shoulders, his sandals and rings in his hand, he and they immediately become unclean[1].", 

            " If he was clothed in his garments, his sandals upon his feet and his rings upon his finger, he immediately becomes un-clean, but they remain undefiled until he tarries there a sufficient time to eat a peras[2] of wheaten-bread[3], but not barley-bread, reclining and eating it with a relish. ", 

            "\"Barley\" — for there is a Mishnaic teaching : ", 

            "The bone [of a dead person or animal] the size of barley defiles by touch and carrying, but does not defile in a tent[4]. ", 

            "\"Vine\" — it requires a fourth [of a Log] of wine for a Nazirite[5]. ", 

            "\"Fig-tree\" — to carry as much as a dried fig [from a private to a public court or vice versa] constitutes a breach of the Sabbath.", 

            " \"Pomegranate\" — as we have the Mishnaic teaching : ", 

            "The vessels of house-owners[6] "

        ], 

        [

            "have the standard size of a pomegranate[7].", 

            " \"A land of Olive-trees\" — R. Jose b. R. Hannina said: ", 

            "[This means], a land where the standard for everything is the size of the olive. ", 

            "The standard for everything, dost imagine? ", 

            "Lo, there are the others just mentioned[8] ! ", 

            "Nay,", 

            " [the meaning is], a land where the standard for most things is the size of the olive.", 

            " \"Honey\" — one must have eaten as much as a large date on the Day of Atonement [to have incurred the penalty for breaking the fast].", 

            " But the other [Rabbi][9]? [He asks] : ", 

            "Are these standards explicitly stated in this verse ? ", 

            "No, they are ordained by the Rabbis, and this verse serves only as a support. ", 

            "Rab Hisda and Rab Hamnuna were sitting at a meal, when dates and pomegranates were set before them. Rab Hamnuna took and pronounced the benediction over the dates first. ", 

            "Rab Hisda said to him, ", 

            "\"Does not the master agree with the statement of Rab Joseph (another version : R. Isaac), viz. : ", 

            "That which is given precedence in the verse (Deut. viii. 8) must precede for the benediction?\" ", 

            "He replied, \"", 

            "'Dates[10]' is the second word after 'land,' 'pomegranate' the fifth word after 'land[1]'.\" ", 

            "Rab Hisda said to him, ", 

            "\"Would that we had iron feet so that we could always [follow and] listen to thee!\" ", 

            "It has been reported :", 

            " If they set before them figs and grapes in the middle of a meal, ", 

            "Rab Huna declared that", 

            " they require a benediction before partaking thereof but not after.", 

            " Similarly said Rab Nahman :", 

            " They require a benediction before partaking thereof but not after.", 

            " But Rab Sheshet said : ", 

            "They require a benediction both before and after, because there is nothing which requires a benediction before partaking thereof which does not require one after it, bread offered as a dessert[2] being alone excepted.", 

            " This is at variance with the statement of R. Hiyya who said :", 

            " [The benediction over] bread exempts all other articles of food, and that over wine exempts all other kinds of beverage [from the necessity of another benediction].", 

            " Rab Pappa said : The Halakah is — ", 

            "Articles of food which are brought in connection with the meal[3], in the course of the meal, require a benediction neither before nor after; if they are not brought in connection with the meal[4], in the course of the meal, they require a benediction before but not after ;", 

            " if brought after the meal, they require a benediction before and after. ", 

            "They asked Ben Zoma : Why is it said, ", 

            "\"Articles of food brought in connection with the meal, in the course of the meal, require a benediction neither before nor after\"?", 

            "He replied : ", 

            "Because [the benediction over] the bread makes it unnecessary.", 

            " If so, let the bread make [a benediction] unnecessary also for the wine !", 

            " It is different with wine,  "

        ], 

        [

            "because it necessitates a benediction for itself[5]. ", 

            "Rab Huna ate thirteen rolls[6], three to a Kab in size, and said no Grace. ", 

            "Rab Nahman said to him, ", 

            "\"Is there still hunger!\" ", 

            "But everything which others fix as a meal requires Grace. ", 

            "Rab Judah was holding the wedding-feast for his son in the house of Rab Judah b. Habiba[1]. They set before him bread as dessert ; ", 

            "and when it came, he heard them say hammosi. ", 

            "He said to them, ", 

            "\"What is the sisi I hear?", 

            " Perhaps it is the benediction hammosi' that you have said ?\" ", 

            "They replied, ", 

            "\"It is ;", 

            " for there is a teaching : R. Mona said in the name of R. Judah :", 

            " We do pronounce hammosi over bread-dessert, and Samuel declared that ", 

            "the Halakah is in agreement with R. Mona.\" ", 

            "He said to them, ", 

            "\"The Halakah is not in agreement with him.\" It is reported that", 

            " they said to him,", 

            " \"But lo, the master has himself declared in the name of Samuel : The bread-wafers used as dessert may be utilised as an 'Erub and we say the benediction hammosi' over them!\" ", 

            "[He replied,] \"It is different there [with the 'Erub)] because one makes a meal of them ; but here where one does not make a meal of them, no [benediction is necessary].\" ", 

            "Rab Pappa went on a visit to the house of Rab Huna b. Rab Nathan. After they had finished their meal, they set before them several things to eat. Rab Pappa took of them and ate. ", 

            "They said to him, ", 

            "\"Does not the master hold that if one has finished [his meal], he must not eat anything further[3]?\"", 

            " He replied, ", 

            "\"This has only been said when the table has been cleared.\" ", 

            "Raba[4] and R. Zera went on a visit to the house of the Exilarch. ", 

            "After the tray had been taken away from before them, there was sent to them from the Exilarch's house a gift [of fruit][5]. Raba ate it, but R. Zera did not. ", 

            "The latter said to him,", 

            " \"Does not the master hold that if the table has been cleared, it is forbidden to eat?\" ", 

            "He replied, ", 

            "\"We depend upon the Exilarch's tray[6].\" ", 

            "Rab said : ", 

            "He who is accustomed [to anoint his hands] with oil [after finishing a meal], the oil impedes him[7] ", 

            "Rab Ashe said : When we were at the school of Rab Kahana, he said to us,", 

            " \"For instance we are accustomed to the use of oil, and the oil impedes us.\" ", 

            "But the Halakah is in agreement with none of these teachings, but with that which Rab Hiyya b. Ashe said in the name of Rab, viz.: There are three actions which have to be performed with dispatch : ", 

            "the putting on of hands[1] must be followed immediately by the act of slaughtering ; the Tefillah must follow immediately on the Ge'ullah[2] ; and the Grace after meals must follow immediately on the washing of the hands[3]. ", 

            "Abbai[4] declared : We also add[5] :", 

            " A benediction [immediately alights upon him who entertains] disciples of the wise[6] ; as it is said,", 

            " \"The Lord hath blessed me for thy sake\" (Gen. xxx. 27); ", 

            "or, if thou wilt, from this passage, as it is said,", 

            " \"The Lord blessed the Egyptian's house for Joseph's sake \" (ibid. xxxix. 5). ", 

            "MISHNAH  If a man said the benediction over wine before the meal, he is exempt from saying it over the wine after the meal. If he said it over the dainty[7] served before the meal, he is exempt from saying it over the dainty served after the meal. If he said it over the bread, he is exempt from saying it over the dainty; over the dainty, he is not exempt from saying it over the bread. ", 

            "Bet Shammai declare : ", 

            "Nor from saying it over a cooked dish. ", 

            "If men were sitting [at the meal], each one says Grace for himself. If they were reclining[8], one may say it for all.  "

        ], 

        [

            "If wine  is set for them in the course of the meal, each one says the benediction for himself; ", 

            "after the meal, one may say it for all. The same one says the benediction over the perfume, although they do not bring the perfume until after the meal. ", 

            "GEMARA Rabbah b. Bar Hannah said in the name of R. Johanan :", 

            " The teaching[9] applies only to Sabbaths and Festivals, for then a man arranges his meal with wine[10]; but on other days of the year, a benediction is to be said over each cup of wine.", 

            " It has been similarly reported : Rabbah b. Mari[1] said in the name of R. Joshua b. Levi : ", 

            "The teaching applies only to Sabbaths and Festivals and the time when one comes from the bath-house and the meal after blood-letting, for then a man arranges his meal with wine; but on the other days of the year, a benediction is to be said over each cup of wine. ", 

            "Rabbah b. Mari visited the house of Raba on a week-day, and noticed him pronounce the benediction [over the wine] before the meal and again after it ; and he said to him, ", 

            "\"That is correct, and so also said R. Joshua b. Levi.\"", 

            " Rab Isaac b. Joseph visited the house of Abbai on a Festival and noticed that he pronounced the benediction over each cup.", 

            " He said to him,", 

            " \"Does not the master agree with the opinion of R. Joshua b. Levi ?\"", 

            " He replied,", 

            " \"It only just occurred to me[2].\" ", 

            "The question was asked : ", 

            "How is it if wine is brought in the course of the meal[3] — does it make the benediction over the wine after the meal unnecessary? ", 

            "Shouldest thou wish to quote our Mishnah : If a man said the benediction over wine before the meal, he is exempt from saying it over the wine after the meal — this is because both of them are for drinking ; but here, since one[4] is for steeping and the other for drinking, it is not so ; ", 

            "or perhaps that makes no difference ?", 

            " Rab said : ", 

            "He is exempt [from repeating the benediction] ; but Rab Kahana said : ", 

            "He is not. ", 

            "Rab Nahman said:", 

            " He is exempt; but Rab Sheshet said :", 

            " He is not. ", 

            "Rab Huna, Rab Judah and all the pupils of Rab say :", 

            " He is not[5]. ", 

            "Raba quoted against Rab Nahman :", 

            " If wine is set for them in the course of the meal, each one says the benediction for himself ; after the meal, one may say it for all[6]! ", 

            "He replied : This is what he means to say[7], ", 

            "If no wine was set for them in the course of the meal, only after it, then one may say the benediction for all. ", 

            "If he said it over the bread, he is exempt from saying it over the dainty ; over the dainty, he is not exempt from saying it over the bread. ", 

            "Bet Shammai declare : ", 

            "Nor from saying it over a cooked dish. ", 

            "The question was asked :", 

            " Are Bet Shammai in disagreement with the first clause of this teaching, or is it perhaps with the second clause? ", 

            "They are in disagreement with the first clause[1]; for the first Tanna declares :", 

            " If he said it over the bread, he is exempt from saying it over the dainty, so how much more [is it unnecessary for him to say a benediction] over a cooked dish ; then Bet Shammai come to declare that ", 

            "not only does [the benediction over] the bread not exempt that over the dainty, but it does not even exempt that over a cooked dish ! ", 

            "Or is it perhaps with the second clause that Bet Shammai disagree? For it teaches :", 

            " [Having said the benediction] over the dainty, he is not exempt from saying it over the bread ; it is [the benediction over] the bread from which he is not exempt, but he is exempt from that over the cooked dish ;", 

            " and then Bet Shammai come to say : ", 

            "He is not even exempt from that over the cooked dish ! The question [remains unanswered]. ", 

            "If men were sitting [at the meal], each one says Grace for himself. ", 

            "If they were reclining, then yes[2]; but if they were not reclining. no !", 

            " Against this I quote the following :", 

            " If ten were journeying by the way, although they all partake of one loaf, each of them says Grace for himself ; ", 

            "should they sit down to eat, although each eats of his own loaf, one may say Grace for all. ", 

            "Note that he here states \"they sit,\" i.e. although they are not reclining !", 

            " Rab Nahman b. Isaac said : [This Baraita refers to the case where] for instance men say,", 

            " \"Let us go and eat our meal in a certain place[3].\" ", 

            "When Rab died, his disciples followed his cortege.", 

            " On their return they said, ", 

            "\"Let us go and have our meal by the River Danak[4].\" ", 

            "After they had eaten, they sat on and the question was asked : ", 

            "Does our Mishnah intend that only when they recline [does one say the benediction for all] and not if they sit ; or is it perhaps that where people say, \"Let us go and eat our meal in a certain place\" this is to be regarded the same as reclining?", 

            " They were unable [to answer the question]. ", 

            "Rab Adda b. Ahabah stood up,\n"

        ], 

        [

            " turned the torn part of his garment[1] to the rear and made a fresh tear,", 

            " exclaiming,", 

            " \"Rab has died and we have not learnt [the regulations of] the Grace after meals!\"", 

            " In the meanwhile an Elder came and pointed out the disagreement between our Mishnah and the Baraita[2], and taught them : ", 

            "When men say, \"Let us go and eat our meal in a certain place,\" it is the same as if they had reclined. ", 

            "If they were reclining, one may say Grace for all. ", 

            "Rab said :", 

            " This teaching applies only to bread for which reclining is necessary, but for wine reclining is not necessary.", 

            " R. Johanan, however, said :", 

            " Even for wine likewise reclining is needed.", 

            " (Another version : Rab said :", 

            " This teaching applies only to bread where it is beneficial to recline, but with wine it is not beneficial to recline. ", 

            "R. Johanan, however, said : ", 

            "Even with wine it is likewise beneficial to recline.) ", 

            "Against this teaching is quoted : ", 

            "What is the procedure of reclining[3]? ", 

            "The guests enter and seat themselves upon stools and chairs until all are assembled. Then water is brought to them, and each washes one hand[4]. Wine is set for them, and each says the benediction for himself.", 

            " They thereupon ascend [the couch] and recline, and water is brought before them ; and although each one has washed one hand, he again washes both hands[5].", 

            " Wine is brought to them[6], and although each has said the benediction for himself, one may now say it for all ! ", 

            "According to one version of Rab's statement, viz. : ", 

            "\"This teaching applies only to bread for which reclining is necessary, but for wine reclining is not necessary,\" the first part [of this Baraita] is in disagreement[7]!", 

            " It is different with guests, because it is their intention to move their position[8]. ", 

            "And according to the other version of Rab's statement, viz. :", 

            " \"This teaching applies only to bread where it is beneficial to recline, but with wine it is not beneficial to recline,\" the latter part [of the Baraita] is in disagreement[1] !", 

            " It is different there, because while it is beneficial to recline for the bread, it is at the same time beneficial to recline for the wine. ", 

            "If wine is set for them in the course of the meal. ", 

            "Ben Zoma was asked : ", 

            "Why is it stated : If wine is set for them in the course of the meal, each one says the benediction for himself; after the meal, one may say it for all ?", 

            " He replied : ", 

            "Because the gullet is not empty[2]. ", 

            "The same one says the benediction over the perfume, etc. ", 

            "Since he teaches, The same one says the benediction over the perfume, it is to be inferred that there may be somebody more worthy than he ; why, then, [is it his privilege] ? ", 

            "Because he is the first to wash his hands at the conclusion of the meal.", 

            " This supports the statement of Rab ; for Rab Hiyya b. Ashe said in the name of Rab :", 

            " He who is the first to wash his hands at the conclusion of the meal has the privilege of saying Grace. ", 

            "Rab and R. Hiyya were sitting at table in the presence of Rabbi.", 

            " Rabbi said to Rab,", 

            " \"Arise, wash thy hands.\"", 

            " R. Hiyya noticed that Rab was trembling[3], and said to him,", 

            " \"O son of princes[4]! ", 

            "See it is for the privilege of saying Grace after meals that Rabbi tells thee [to wash].\" ", 

            "R. Zera said in the name of Raba b. Jeremiah[5] : ", 

            "From what time may we say the benediction over the smell [of the perfume][6]? From the time its column of smoke ascends.", 

            " R. Zera said to Raba b. Jeremiah", 

            ", \"But one has not yet smelt it!\" ", 

            "He replied,", 

            " \"According to thy reasoning, one says the Grace before meals but has not yet eaten ! ", 

            "His intention is to eat, and so here likewise it is his intention to smell.\" ", 

            "R. Hiyya b. Abba[1] b. Nahmani stated that Rab Hisda said in the name of Rab (another version : Rab Hisda said in the name of Ze'iri) : ", 

            "Overall kinds of perfumes the benediction is \"...Who Greatest fragrant woods,\" excepting musk which comes from a species of animal and its benediction is \"...Who createst various kinds of spices.\" ", 

            "Against this teaching is quoted : ", 

            "We only say \"...Who createst fragrant woods\" over the balsam-trees of the house of Rabbi[2]", 

            " and the balsam-trees of the Emperor's palace and over the myrtle-tree wherever it comes from ! ", 

            "This refutation [remains unanswered]. ", 

            "Rab Hisda asked Rab Isaac[3],", 

            " \"What is the benediction over balsam-oil?\"", 

            " He replied, \"Thus said Rab Judah : ", 

            "It is '...Who createst the oil of our land '.\"", 

            " Rab Hisda said to him,", 

            " \"Leave out Rab Judah, because the land of Israel is very dear to him ; what is the benediction generally?\"", 

            " He replied,", 

            " \"Thus said R. Johanan :", 

            " It is '...Who createst fragrant oil'.\" ", 

            "Rab Adda b. Ahabah said: ", 

            "Over costum the benediction is \"...Who createst fragrant woods,\" but not over the oil in which it is steeped. ", 

            "Rab Kahana said :", 

            " [That is the benediction] even for the oil in which it is steeped, but not the oil with which it is ground. ", 

            "The men of Nehardea[4] said :", 

            " [That is the benediction] even for the oil in which it is ground. \n"

        ], 

        [

            " Rab Giddel said in the name of Rab : ", 

            "Over jasmine[5] the benediction is \"...Who createst fragrant woods.\" ", 

            "Rab Hananel said in the name of Rab:", 

            " Over sea-rush the benediction is \"...Who createst fragrant woods.\" ", 

            "Mar Zotra said : ", 

            "What is the Scriptural authority[6]? \"She had brought them up to the roof, and hid them with the stalks of flax[7]\" (Josh. ii. 6). ", 

            "Rab Mesharsheya said :", 

            " Over the garden-narcissus the benediction is \"...Who createst fragrant woods,\" but over the wild narcissus \"...Who createst fragrant herbs.\" ", 

            "Rab Sheshet said : ", 

            "Over violets the benediction is \"...Who createst fragrant herbs.\" ", 

            "Mar Zotra[8] said : ", 

            "He who smells the citron or quince should say \"Blessed be He Who setteth a beautiful fragrance in fruits.\" ", 

            "Rab Judah said :", 

            " He who goes out during the days of Nisan and sees the trees budding should say", 

            " \"Blessed be He Who has caused nothing to be lacking in His Universe and created therein beautiful creations and beautiful trees where-from men may derive pleasure.\" ", 

            "Rab Zotra b. Tobiah said in the name of Rab : ", 

            "Whence is it learnt that one should pronounce a benediction over a fragrant smell? As it is written, ", 

            "\"Let every soul[1] praise the Lord\" (Ps. cl. 6). From what is it that the soul, but not the body, derives enjoyment? Say it is a fragrant smell. ", 

            "Rab Zotra b. Tobiah also said in the name of Rab : ", 

            "The young men of Israel will in the future give forth a sweet fragrance like Lebanon ; as it is said,", 

            " \"His branches shall spread, and his beauty shall be as the olive-tree, and his fragrance as Lebanon\" (Hosea xiv. 7). ", 

            "Rab Zotra b. Tobiah also said in the name of Rab : What means that which is written, ", 

            "\"He hath made everything beautiful in its time\" (Eccles. iii. 11)? It teaches that the Holy One, blessed be He, makes every occupation agreeable in the eyes of those who follow it. ", 

            "Rab Pappa said : Hence the proverb, ", 

            "\"Hang the heart of a palm-tree around a sow, and it will act as usual[2].\" ", 

            "Rab Zotra b. Tobiah also said in the name of Rab :", 

            "[Walking by the light of] a torch is equal to two[3]; by moonlight is equal to three. ", 

            "The question was asked : ", 

            "Is the light of the torch equal to two, including himself ; or perhaps it is equal to two excluding himself? ", 

            "Come and hear:", 

            " [It is stated,] \"By moonlight is equal to three.\"", 

            " That is quite right if thou sayest it means including himself, well and good ; but if thou sayest it means excluding himself, why are four necessary? ", 

            "For lo, the teacher has said : ", 

            "To a single person an evil spirit appears and injures him ; to two it appears but does not injure them ; to three it does not appear at all ! ", 

            "Certainly it is to be concluded that the expression \"torchlight is equal to two\" means including himself. Draw that conclusion. ", 

            "Rab Zotra b. Tobiah also said in the name of Rab (another version : Rab Hanna b. Bizna in the name of R. Simeon Hasida ; still another version : R. Johanan said in the name of R. Simeon b. Johai) :", 

            " It were better for a man to cast himself into the midst of a fiery furnace rather than cause the face of his fellow-creature to blanche in public[1].", 

            " Whence is this derived ? ", 

            "From Tamar ; as it is said, \"When she was brought forth\" etc. (Gen. xxxviii. 25)[2]. ", 

            "Our Rabbis have taught:", 

            " If they set before him oil and myrtle[3], Bet Shammai declare : ", 

            "He first says the benediction over the oil and then over the myrtle ; ", 

            "Bet Hillel declare : ", 

            "He first says the benediction over the myrtle and then over the oil. ", 

            "Rabban[4] Gamaliel said :", 

            "I will decide —", 

            " Oil we use for its fragrance and for anointing, whereas we use the myrtle only for its fragrance and not for anointing[5]. ", 

            "R. Johanan said : ", 

            "The Halakah is in accord with him who decided. ", 

            "Rab Pappa visited the house of Rab Huna b. Rab Ika[6]; they set before him oil and myrtle. He took and made the benediction first over the myrtle and then over the oil. ", 

            "Rab Huna said to him : ", 

            "Does not the master hold that the Halakah is in accord with the words of him who decided ?", 

            " He replied : Thus said Raba :", 

            " The Halakah is in accord with Bet Hillel. ", 

            "But it was not so, and he only did this to extricate himself. ", 

            "Our Rabbis have taught :", 

            " If oil and wine are set before him, Bet Shammai declare : ", 

            "He should take hold of the oil in his right hand and the wine in his left, say the benediction over the oil and then over the wine ; ", 

            "Bet Hillel declare :", 

            " He should take hold of the wine in his right hand and the oil in his left, say the benediction over the wine and then over the oil.", 

            " And he should rub the oil upon the head of the attendant[7] ; but if the attendant be a disciple of the wise, he should rub it upon the wall, because it is a disgrace for a disciple of the wise to go into the street perfumed. ", 

            "Our Rabbis have taught :", 

            " Six[8] things are a disgrace to a disciple of the wise : ", 

            "He should not go out into the street perfumed ; nor go out alone at night ; nor go out with patched sandals ; nor converse with a woman in the street ; nor recline in the company of 'Amme ha'ares ; nor be the last to enter the House of Study.", 

            " Some declare that ", 

            "he should also not walk with a big stride, nor walk with an erect carriage.", 

            " He should not go out into the street perfumed. R. Abha b. R. Hiyya b. Abba said in the name of R. Johanan[1] :", 

            " This refers to a place where people are suspected of pederasty. ", 

            "Rab Sheshet said : ", 

            "They mean only with his garment [perfumed], but on his body [it is permitted] because it removes [the odour of] perspiration.", 

            " Rab Pappa said :", 

            "[To perfume] his hair is like [perfuming] his garment; ", 

            "but some declare that it is like [perfuming] his body[2]. ", 

            "He should not go out alone at night, because of the suspicion [it may arouse] ; and they mean only where he has no fixed hour [for going out at night], but if he have a fixed hour, it will be well known that he goes out as is his usual custom[3]. ", 

            "He should not go out with patched sandals. This supports the statement of R. Hiyya b. Abba who said : ", 

            "It is a disgrace for a disciple of the wise to go out with patched sandals[4]. ", 

            "But it is not so;", 

            "for R. Hiyya b. Abba went out thus! ", 

            "Mar Zotra b. [5] Rab Nahman said : ", 

            "It means with a patch on top of a patch, ", 

            "and it refers only to the legging ; but as for the sole, we have no objection. ", 

            "And even in the case of the legging, it means only when walking by the way ; but as for wearing such in the house, we have no objection. ", 

            "It further refers to the days of Summer, but in the days of Winter we have no objection[6]. ", 

            "He should not converse with a woman in the street. Rab Hisda said : ", 

            "Even if it be his wife[7].", 

            " There is a teaching to the same effect :", 

            " Even if it be his wife, or his daughter, or his sister, because everybody is not well acquainted with his female relations. ", 

            "He should not recline in the company of 'Amine ha'ares. What is the reason ?", 

            " He may perhaps be induced to be drawn after them. ", 

            "He should not be the last to enter the House of Study; because such an one is called \"a transgressor[8].\" ", 

            "Some declare ", 

            "he should not walk with a big stride. For the teacher has said : ", 

            "A big stride takes away one five hundredth part of the light of a man's eyes.", 

            " What is the remedy for if ? ", 

            "He may restore it [by drinking the wine of] Sanctification on the [Sabbath] night. ", 

            "He should not walk with an erect carriage. For the teacher has said: ", 

            "He who walks with an erect carriage, even a distance of four cubits, is as though he pushed against the feet of the Shekinah[1]; for it is written, ", 

            "The whole earth is full of His glory\" (Is. vi. 3).  "

        ], 

        [

            "MISHNAH If they set before him salted food first and with it bread, he says the benediction over the salted food and this makes it unnecessary over the bread, because the bread is something accessory to it.", 

            " This is the general rule :", 

            " In the case of a food which is the principal thing and together with it is something accessory, the benediction is to be uttered over the former and there is no necessity for a benediction over the latter. ", 

            "GEMARA Is there any salted food which is the principal thing and the bread, accessory ? ", 

            "Rab Aha b. Rab 'Awira said in the name of Rab Ashe[2] : ", 

            "They refer to one who eats the fruits of Gennesareth[3]. ", 

            "Rabbah b. Bar Hannah said : ", 

            "At the time we were following R. Johanan to eat the fruits of Gennesareth, when we were a hundred in number we used each to take ten for him, and when we were ten we used each to take a hundred for him ; and a basket of the capacity of three Saot could not hold a hundred of them. But he ate them all and swore that he had tasted no food. ", 

            "No food, dost imagine? ", 

            "But say,", 

            " [He meant that he had eaten no] satisfying meal. ", 

            "R. Abbahu ate so many of them that a fly would glide down his face[4]. ", 

            "R. Ammi and R. Assi ate so many of them that their hair fell out. ", 

            "R. Simeon b. Lakish ate so many of them that he began to rave. R. Johanan reported this to the household of the Prince, and R. Judah the Prince sent officials after him and brought him to his house. ", 

            "When Rab Dimai came [from Palestine] he said :", 

            " Jannaeus the king[1] had a city on the king's mountain[2] from which they obtained sixty myriad basins of salted fish[3] for the hewers of the fig-trees from one Sabbath-eve to the next[4]. ", 

            "When Rabin came he said :", 

            " Jannaeus the king had a tree on the king's mountain from which they took down forty Saot of young pigeons[5] monthly from three broods. ", 

            "When R. Isaac came he said :", 

            " There was a city in the land of Israel named Gofnit[6] in which were eighty pairs of brothers of a priestly family married to eighty pairs of sisters of a priestly family[7] ; ", 

            "and the Rabbis searched from Sura to Nehardea[8] and could not find [a similar case] with the exception of the daughters of Rab Hisda who were married to Rammi b. Hamma and Mar 'Ukba b. Hamma ; but although the women belonged to a priestly family, the men did not. ", 

            "Rab said : ", 

            "A meal without salt is no meal[9]. ", 

            "R. Hiyya b. Abba said in the name of R. Johanan :", 

            " A meal without some acrid substance[10] is no meal. ", 

            "MISHNAH If one ate grapes, figs or pomegranates, he says after them the three benedictions. These are the words of Rabban Gamaliel ; ", 

            "but the Sages declare : ", 

            "One benediction which is an abstract of three. ", 

            "R. 'Akiba says : ", 

            "Even if one eats [nothing but] boiled vegetables and makes a meal of it, he pronounces thereover the three benedictions.", 

            " If one drinks water to slake his thirst, he says the benediction \"...By Whose word all things exist \"; ", 

            "R. Tarphon says :", 

            " \"...Who createst many living beings and their wants.\" ", 

            "GEMARA What is Rabban Gamaliel's reason[1]?", 

            " Because it is written, ", 

            "\"A land of wheat and barley and vines and fig-trees and pomegranates\" (Deut. viii. 8), and it is written, ", 

            "\"A land wherein thou shalt eat bread without scarceness\" (ibid. v. 9), and it is written", 

            " \"And thou shalt eat and be satisfied, and bless the Lord thy God\" (ibid. v. lO)[2]. ", 

            "And the Rabbis[3]? ", 

            "[The reference to] the \"land\"[4] interrupts the subject-matter[5]. ", 

            "But for Rabban Gamaliel likewise [the reference to] the \"land\" interrupts the subject-matter[6] ! ", 

            "He requires that to exclude the case of one who chews wheat[7].", 

            "R. Jacob b. Iddi said in the name of R. Hannina : ", 

            "Over any food which belongs to the five species[8], before partaking thereof one says the benediction \"...Who createst various kinds of foods,\" and afterwards one benediction which is an abstract of three. ", 

            "Rabbah b. Mari said in the name of R. Joshua b. Levi : ", 

            "Over any food belonging to the seven species[9], before partaking thereof one says the benediction \"...Who createst the fruit of the tree,\" and afterwards one benediction which is an abstract of three. ", 

            "Abbai asked Rab Dimai : ", 

            "What is the one benediction which is an abstract of three?", 

            " He replied :", 

            " For the fruit of the tree it is[10]: \"[Blessed art Thou, O Lord our God, King of the universe,] for the tree and the fruit of the tree and for the produce of the field; for the desirable, good and ample land which Thou didst give as an heritage unto our fathers, that they might eat of its fruits and be satisfied with its goodness. Have mercy, O Lord our God, upon Israel Thy people, upon Jerusalem Thy city, upon Thy Sanctuary and altar. Rebuild Jerusalem, Thy holy city, speedily in our days ; lead us up thither and make us rejoice in its rebuilding[1] ; for Thou art good and beneficent unto all.\" ", 

            "For the five species it is : \"[Blessed... universe] for the sustenance and the nourishment, and for the produce of the field[2],\" etc. And the benediction is concluded : \"[Blessed art Thou, O Lord,] for the land and for the sustenance[3].\" ", 

            "In the case of fruit[4] how should the benediction conclude ? ", 

            "When Rab Dimai came he said : ", 

            "Rab concluded on the New Moon thus, \"Blessed [art Thou, O Lord] Who sanctifiest Israel and the beginnings of the months[5].\" ", 

            "So how should it be concluded in this case of fruit ?", 

            " Rab Hisda said :", 

            " \"[Blessed art Thou, O Lord,] for the land and its fruits.\"", 

            " R. Johanan said:", 

            " \"For the land and for the fruits[6].\"", 

            " R. 'Amram[7] said : ", 

            "There is no contradiction, Rab Hisda's wording being customary with us [in Babylon] and R. Johanan's with them [in Palestine]. ", 

            "Rab Nahman b. Isaac objected : ", 

            "They eat and we make the benediction[8] ! ", 

            "Nay, the wording should be reversed ; ", 

            "Rab Hisda said :", 

            " \"For the land and for the fruits\" ", 

            "and R. Johanan said :", 

            " \"For the land and its fruits.\"  "

        ], 

        [

            "Rab Isaac b. Abdemi said in the name of our teacher[9] : ", 

            "Over  an egg and various kinds of meat, before partaking thereof one says the benediction \"...By Whose word all things exist\" and afterwards \"...Who createst many living beings\" etc. ; ", 

            "but not over vegetables[10]. ", 

            "R. Isaac declared :", 

            " Even over vegetables, but not over water. ", 

            "Rab Pappa said : ", 

            "Even over water. ", 

            "Mar Zotra acted in accord with Rab Isaac b. Abdemi, and Rab Shimi b. Ashe[11] in accord with R. Isaac. (A mnemonic for thee is :", 

            " One in accord with two and two in accord with one[1].)", 

            " Rab Ashe said :", 

            " When I think of it, I act in accord with them all[2]. ", 

            "We have a Mishnaic teaching : ", 

            "Everything that requires a benediction after it requires one before it ; but there are things which require a benediction before but not after.", 

            " This is quite right for Rab Isaac b. Abdemi, since it is to exclude vegetables, and for R.Isaac to exclude water ; but for Rab Pappa what is it to exclude ? ", 

            "It excludes the commandments[3].", 

            " But for the sons of the West[4] who on removing the Tefillin say the benediction, \"[Blessed art Thou, O Lord our God, King of the universe] Who didst sanctify us with Thy commandments and commanded us to observe Thy statutes,\" what is it to exclude ? ", 

            "Fragrant odours. ", 

            "R. Jannai said in the name of Rab[5] :", 

            " Any food [whose minimum standard is the size of] an egg, the egg is superior to it [as nourishment]. ", 

            "When Rabin came he said : ", 

            "Better is a light-roasted[6] egg than six measures of fine flour. ", 

            "When Rab Dimai came he said[7]:", 

            " Better is a light-roasted egg than six [measures of fine flour] and a hard-baked egg than four. Of a boiled egg [it is said], any food [whose minimum is the size of] an egg, the egg is superior to it [as nourishment] with the exception of meat. ", 

            "R. 'Akiba says : Even if one eats boiled vegetables, etc. ", 

            "Is there any boiled vegetable which is to be regarded as nourishment? ", 

            "Rab Ashe said: It refers to cabbage-stalks. ", 

            "Our Rabbis have taught :", 

            " Milt is good for the teeth but bad for the bowels ; horse-beans are bad for the teeth but good for the bowels. ", 

            "All raw vegetables make the complexion pale ; anything not fully grown makes the body shrink ; every living being[8] restores the soul and everything near to the soul[9] restores the soul. ", 

            "Cabbage [is good] as nourishment and beet as a remedy ; but woe to the body[10] through which vegetables keep constantly passing[11]. ", 

            "The master said above,", 

            " \"Milt is good for the teeth but bad for the bowels.\"", 

            " What is the remedy?", 

            " Let him chew it and then throw it away. ", 

            "\"Horse-beans are bad for the teeth but good for the bowels.\"", 

            " What is the remedy? ", 

            "Let him boil them well and swallow them.", 

            " \"All raw herbs make the complexion pale.\" ", 

            "R. Isaac said :", 

            " This refers only to the first meal after blood-letting. ", 

            "R. Isaac also said :", 

            " It is forbidden to converse with him who has eaten [raw] herbs before the fourth hour of the day[1].", 

            " For what reason ? ", 

            "Because of the evil odour.", 

            " R. Isaac also said :", 

            " It is forbidden for a man to eat raw herbs before the fourth hour of the day.", 

            " Amemar, Mar Zotra and Rab Ashe were sitting [at table], and they set before them raw herbs before the fourth hour. Amemar and Rab Ashe ate, but not so Mar Zotra. ", 

            "They said to him,", 

            " \"What is thy opinion ? Is it because R. Isaac declared :", 

            " It is forbidden to converse with him who has eaten [raw] herbs before the fourth hour of the day on account of the evil odour ? Behold we have eaten, and still thou talkest with us!\"", 

            " He replied, ", 

            "\"I agree with the other statement of R. Isaac, viz. :", 

            " It is forbidden for a man to eat raw herbs before the fourth hour of the day.\" ", 

            "\"Anything not fully grown makes the body shrink.\" ", 

            "Rab Hisda said :", 

            " Even a young kid worth a Zuz ; ", 

            "and it only refers to that which is not a fourth [of its full natural size], but if it be a fourth, we have no objection.", 

            " \"Every living being restores the soul.\" ", 

            "Rab Pappa said :", 

            " Even the small fishes from the swamps. ", 

            "\"Everything near to the soul restores the soul.\" ", 

            "Rab Aha b. Jacob said : ", 

            "This is the neck. ", 

            "Raba[2] said to his attendant,", 

            " \"When thou bringest me a piece of meat, take the trouble and obtain it from a place near to where the benediction is pronounced[3].\" ", 

            "\"Cabbage is good as nourishment and beet as a remedy.\"", 

            " Is the cabbage good as food but not as a remedy ? ", 

            "Lo, there is a teaching : ", 

            "Six things cure a man from his sickness and their remedy is [an efficacious] remedy, viz.: ", 

            "Cabbage, beet, a decoction of dry poley[4], the maw, the womb and the large lobe of the liver! ", 

            "But say : ", 

            "Cabbage is good also as nourishment[5].", 

            " \"Woe to the body through which vegetables keep constantly passing.\"", 

            " But it is not so!", 

            " For lo, Raba[6] said to his attendant, ", 

            "\"If thou seest vegetables in the market, never ask me,", 

            " With what wilt thou wrap thy bread?\" ", 

            "Abbai said :", 

            " [It means vegetables] without meat; ", 

            "and Raba said :", 

            " Without wine[1].", 

            " It has been reported: Rab said: ", 

            "[It means vegetables] without meat; ", 

            "Samuel said:", 

            " Without wood[2]; ", 

            "and R. Johanan said : ", 

            "Without wine. ", 

            "Raba asked Rab Pappa ", 

            "the brewer, \"We break [the harmful effects of vegetables] by means of meat and wine ; but you who do not use much wine, how do you break it ?\" ", 

            "He replied,", 

            " \"With chips of wood[2].\" ", 

            "For example, Rab Pappa's[3] wife, when cooking it, broke [its harmful effects] with eighty twigs of Persian trees. ", 

            "Our Rabbis have taught :", 

            " A small salted fish sometimes kills on the seventh, the seventeenth and twenty-seventh, ", 

            "and some say ", 

            "the twenty-third[4] day. ", 

            "This applies only to the case where it has been roasted but not roasted [thoroughly] ; but if it has been well-roasted, there is no objection. ", 

            "And when it has been well-roasted, it only applies to the case where one does not drink beer after it ; but if he drinks beer after it, there is no objection. ", 

            "If one drinks water to slake his thirst, etc. ", 

            "What does this intend to exclude[5] ?", 

            " Rab Iddi b. Abin said :  To exclude him whom\n"

        ], 

        [

            " a piece of food chokes[6]. ", 

            "R. Tarphon says : ", 

            "\"...Who createst many living beings and their wants.\" ", 

            "Raba b. Rab Hanan[7] said to Abbai (another version : to Rab Joseph) : ", 

            "How is the Halakah? ", 

            "He replied : ", 

            "Go and see how the people act[8]. ", 

            "May we return unto thee : What benediction do we say ! ", 

            "MISHNAH  Three who ate together are under the obligation of Zimmun. ", 

            "One who has eaten Demai[1], or the first tithe[2] from which Terumah has been taken[3], or the second tithe[4] or food belonging to the Sanctuary which had been redeemed, and the attendant who has eaten food the size of an olive and the Samaritan may be included for Zimmun. ", 

            "One who has eaten of the untithed, or the first tithe from which Terumah has not been taken, or the second tithe or food belonging to the Sanctuary which had not been redeemed, and the attendant who has eaten Iess than the size of an olive, and the idolator[5] may not be included for Zimmun. ", 

            "Women, slaves and minors may not be included. ", 

            "How much [must one have eaten at the meal] to be included for Zimmun ?", 

            " The size of an olive. ", 

            "R. Judah says : ", 

            "The size of an egg. ", 

            "GEMARA Whence is this derived[6]? ", 

            "Rab Assi said : ", 

            "Because the Scriptures state, \"O magnify ye the Lord with me[7], and let us exalt His name together\" (Ps. xxxiv. 4).", 

            " R. Abbahu said : From the following, ", 

            "\"For I will proclaim the name of the Lord; ascribe ye[8] greatness unto our God\" (Deut. xxxii. 3). ", 

            "Rab Hanan b. Abba[1] said :", 

            " Whence is it that he who responds \"Amen\" must not raise his voice above him who pronounces the benediction? As it is said, ", 

            "\"O magnify ye the Lord with me[2], and let us exalt His name together.\" ", 

            "R. Simeon b. Pazzi said : ", 

            "Whence is it that the translator is not permitted to raise his voice above that of the reader[3]? As it is said, ", 

            "\"Moses spoke, and God answered him by a voice\" (Exod. xix. 19) — there was no need to say \"by a voice\" ; ", 

            "what, therefore, does the teaching \"by a voice\" tell us? By a voice [equal to that] of Moses. ", 

            "There is a similar teaching : ", 

            "The translator is not permitted to raise his voice above that of the reader ; and if the translator is not able to pitch his voice as loud as the reader, then the reader should lower his voice and read. ", 

            "It has been reported :", 

            " If two ate together, ", 

            "Rab and R. Johanan differ in opinion — One declares that", 

            " if they wish to arrange Zimmun they may do so ;", 

            " but the other declares tha", 

            " if they wish to do so, they may not. ", 

            "There is, however, the Mishnaic teaching :", 

            " Three who ate together are under the obligation of Zimmun — ", 

            "three, yes ; two, no[4] ! ", 

            "There [in the case of three] it is obligatory, but here [with two] it is voluntary. ", 

            "Come and hear :", 

            " Three who ate together are under the obligation of Zimmun and are not permitted to divide themselves up[5]. ", 

            "[Hence it is to be inferred that] three can and two cannot make Zimmun ! ", 

            "It is different there, because they originally [being three in number] laid upon themselves the obligation[6]. ", 

            "Come and hear :", 

            " The attendant who was waiting upon two men should eat with them[7], even if they did not give him permission[8]. If he waited upon three, he should only eat with them when they give him permission !", 

            " It is different  there, "

        ], 

        [

            "because it is proper for them to be placed under the obligation of Zimmun from the outset of the meal[9].", 

            " Come and hear:", 

            " Women may arrange Zimmun for themselves and slaves for themselves; but women, slaves and minors may not include each other should they desire Zimmun[1]. ", 

            "And although a hundred women are like two men[2], yet it teaches", 

            " \"Women arrange Zimmun for themselves and slaves for themselves[3]\" !", 

            " It is different there, because there are many persons[4]. ", 

            "If so, I will quote the sequel :", 

            " \"Women and slaves may not include each other, should they desire Zimmun\" — why not ? ", 

            "Are they not many persons !", 

            " It is different there, because [there is the fear] of licentiousness. ", 

            "It is to be concluded that it was Rab who said above, \"If they[5] wish to arrange Zimmun, they may not\" ; ", 

            "for Rab Dimai b. Joseph said in the name of Rab :", 

            " If three ate together, and one of them went out into the street, they call to him [that they desire to include him for Zimmun, and should he consent, even in his absence] they may reckon him in for Zimmun. ", 

            "The reason [why they can have Zimmun without him is] that they called to him ; hence if they did not call to him, they are not [to have Zimmun][6].", 

            " It is different there, because from the outset [by being three] they placed upon themselves the obligation of Zimmun[7]. ", 

            "Nay, it is to be concluded that it was R. Johanan who said above, \"If they[5] wish to have Zimmun, they may not\" ; ", 

            "for Rabbah b. Bar Hannah said in the name of R. Johanan : ", 

            "If two ate together, one of them may comply with the requirements of the law by means of the Grace said by the other ;", 

            " and we ask the question :", 

            " What does he intend to inform us ?", 

            " For we have the teaching :", 

            " If a man heard [Grace said by another], although he does not make the responses, he has complied with the requirements of the law !", 

            " And R. Zera said : ", 

            "He means to tell us that there can be no Grace with Zimmun between the two of them. Thus it is to be concluded [that R. Johanan is the author of the above statement]. ", 

            "Raba b. Rab Huna said to Rab Huna[8] :", 

            " But the Rabbis who come from the West declare : ", 

            "If [two] wish to have Zimmun they may ! Is it not to be supposed that they heard this from R. Johanan[1]? ", 

            "No, they heard it from Rab before he went down to Babylon. ", 

            "It was stated above : \"Rab Dimai b. Joseph said in the name of Rab :", 

            "If three ate together and one of them went into the street, they call to him and include him for Zimmun.\" ", 

            "Abbai said :", 

            " That is only if they called to him and he makes the responses[2]. ", 

            "Mar Zotra said :", 

            " This teaching only applies to three ; but with ten [they cannot include him] unless he comes back[3]. ", 

            "Rab Ashe objected ; ", 

            "On the contrary, the reverse is more probable, because", 

            " nine look like ten, but two do not look like three[4] ! ", 

            "But the Halakah is in agreement with Mar Zotra. ", 

            "What is the reason ? Since it is necessary to mention the Divine Name, which is not customary with less than ten. ", 

            "Abbai said : We have it by tradition that ", 

            "if two ate together, it is a meritorious act on their part to separate[5]. ", 

            "There is a teaching to the same effect : ", 

            "If two ate together, it is a meritorious act on their part to separate. ", 

            "Of what does it speak here ? When both of them are learned[6] ; but if one is learned and the other illiterate, the former says Grace and the other fulfils his obligation [by listening]. ", 

            "Raba stated : The following have I said and it has been similarly reported[7] in the name of R. Zera : ", 

            "If three ate together, one should interrupt his meal for the other two[8] but two need not interrupt their meal for one. ", 

            "They need not ? ", 

            "Lo, Rab Pappa, i.e. he and another, interrupted the meal for Abba Mar, his son !", 

            " Rab Pappa is different, because he acted within the bounds of strict justice[9]. ", 

            "Judah b. Maremar, Mar b. Rab Ashe and Rab Aha of Difti[10] dined together, and there was not one amongst them who was more distinguished than his associates to say Grace for them. ", 

            "They sat on and said[11] : The Mishnah teaches : ", 

            "Three who ate together are under the obligation of Zimmun. That must refer only to where there is an eminent man present[1], but where they are all equal, it is preferable to separate for the purpose of the Grace.", 

            " Thereupon each said Grace for himself; but when they came before Maremar, he said to them :", 

            " The duty of Grace you have fulfilled, but not the duty of Zimmun ; ", 

            "and should you say, \"Let us go back and have Grace with Zimmun,\" there cannot be a Zimmun retrospectively. ", 

            "If one comes in and finds them saying Grace, what response does he make ? ", 

            "Rab Zebid said,", 

            " \"Blessed be His name, yea, contiuually to be blessed for ever and ever[2].\"", 

            " Rab Pappa said : ", 

            "He responds with \"Amen.\" ", 

            "There is no disagreement here ; the former refers to where he finds them saying, \"Let us say Grace,\" the other to where he finds them saying \"Blessed.\"", 

            " If he finds them saying \"Let us say Grace,\" he responds \"Blessed be His name\" etc., and if he finds them saying \"Blessed,\" he responds \"Amen.\" ", 

            "One taught : ", 

            "He who responds \"Amen\" after his own benedictions is praiseworthy ; but another taught : ", 

            "He is to be reprimanded. ", 

            "There is no contradiction;", 

            " the former refers to \"Who...rebuildest Jerusalem[3],\" the latter to the other benedictions. ", 

            "Abbai responded [\"Amen\" to his benediction \"Who...rebuildest Jerusalem\"] with a loud voice for the day-labourers to hear and stand up[4], because \"Who art kind and dealest kindly[5]\" is not ordained by the Torah[6]. ", 

            "Rab Ashe used to make that response softly, so that the day-labourers should not hold \"Who art kind and dealest kindly\" in contempt[7]. \n"

        ], 

        [

            "R. Zera was ill. R. Abbahu went in to visit him, and took [a vow] upon himself,", 

            "\"If the little one with the scorched legs[8] recovers, I will make a joyous day for the Rabbis.\" ", 

            "He did recover, and R. Abbahu made a feast for all the Rabbis. ", 

            "When it was time to commence the meal, he said to R. Zera,", 

            " \"Let the master begin for us[1].\" ", 

            "He replied,", 

            " \"Does not the master hold with R. Johanan's statement, ", 

            "'The master of the house should break the bread'?\"", 

            " He commenced for them. ", 

            "When the time came to say Grace after meals, he said to R. Zera, ", 

            "\"Let the master say Grace for us.\"", 

            " He replied, ", 

            "\"Does not the master hold with the statement of Rab Huna of Babylon,", 

            " 'The one who breaks bread should say Grace after meals'?\"", 

            " With whose opinion was R. Abbahu in agreement?", 

            " With that which R. Johanan said in the name of R. Simeon b. Johai :", 

            " The master of the house breaks bread so that he may do so with a good will[2], and the guest says Grace so that he may bless his host. ", 

            "What benediction does he use?", 

            " \"May it be Thy will that the master of this house may not be put to shame in this world nor confounded in the world to come.\"", 

            " Rabbi added to this : \"And may he prosper in all his possessions[3]; may all his and our possessions be successful and near to the city[4]; may not Satan have power over the works of his hands nor over ours ; and may there not leap before him or us any thought of sin, transgression or iniquity from now and for evermore.\" ", 

            "Up to where is the benediction of Zimmun[5]? ", 

            "Rab Nahman said:", 

            " Until \"We will bless[6]\";", 

            " but Rab Sheshet said: ", 

            "Until \"[Blessed art Thou, O Lord,] Who givest food unto all[7].\"", 

            " Let us say [that their difference is] like that of the Tannaim ; ", 

            "for one taught :", 

            " The Grace after meals [may be said by] two or three ;", 

            " and there is another teaching : ", 

            "Three or four[8]. ", 

            "They hold that everybody admits that \"Who art kind and dealest kindly\" is not ordained by the Torah[1]. ", 

            "Are we, then, not to suppose that they differ on the following point : He who says, \"[The Grace may be said by] two or three\" holds that [the benediction of Zimmun extends] until \"Who givest food unto all\" ; and he who says \"Three or four\" holds that it extends until \"We will bless\"?", 

            " No ; Rab Nahman reconciles [the two conflicting versions] according to his opinion, and so does Rab Sheshet.", 

            " Rab Nahman reconciles them according to his opinion", 

            " — Everybody agrees that [the Zimmun benediction extends] until \"We will bless\" ; that is quite right for him who said", 

            " \"Three or four,\" but as for him who said \"Two or three,\" he could tell thee that ", 

            "we are here dealing with the Grace of the day-labourers ; for the teacher has said: ", 

            "Such an one opens with \"Who feedest\" and includes \"Who ...rebuildest Jerusalem\" in the benediction of \"the land[2].\" ", 

            "Rab Sheshet reconciles them according to his opinion —", 

            " Everybody agrees that [the Zimmun benediction extends] until \"Who givest food unto all\" ; that is quite right for him who said \"Two or three,\" but he who said \"Three or four\" is of the opinion that", 

            " \"Who art kind and dealest kindly\" is ordained by the Torah[3]. ", 

            "Rab Joseph said : ", 

            "Thou mayest know that \"Who art kind and dealest kindly\" is not ordained by the Torah because day-labourers may omit it[4]. ", 

            "Rab Isaac b. Samuel b. Marta said in the name of Rab[1] : ", 

            "Thou mayest know that \"Who art kind and dealest kindly\" is not ordained by the Torah, because it opens with \"Blessed\"[2] and does not conclude with \"Blessed\"; ", 

            "according to the teaching: ", 

            "One commences all benedictions with \"Blessed\" and concludes them with \"Blessed,\" excepting the benediction over fruits, commandments[3], one benediction which follows immediately on another, and the last benediction of the reading of the Shema'.", 

            " In some of these instances one opens with \"Blessed\" but does not conclude with it ;  "

        ], 

        [

            "and in others one concludes with \"Blessed\" but does not commence with it. ", 

            "Since one opens the benediction \"Who art kind and dealest kindly\" with \"Blessed\" but does not conclude with it, the inference is that it is a benediction by itself. ", 

            "Rab Nahman b. Isaac said :", 

            " Thou mayest know that \"Who art kind and dealest kindly\" is not ordained by the Torah, because they omit it in the house of a mourner[4]; ", 

            "according to the teaching : ", 

            "What do they say in the house of a mourner[5] ?", 

            " \"Blessed... Who art kind and dealest kindly[6].\" ", 

            "R. 'Akiba said, ", 

            "\"Blessed be the true Judge.\" ", 

            "Is, then, \"Who art kind and dealest kindly\" to be said but not \"The true Judge\"? ", 

            "Nay, the meaning is,", 

            " \"Who art kind and dealest kindly\" is also to be said. ", 

            "Mar Zotra visited the house of Rab Ashe whom some bereavement had befallen[7]. [In the Grace after meals] he opened with the benediction[8] :", 

            " \"Who art kind and dealest kindly, true God and Judge, Who judgest with righteousness and in judgment takest [the souls of men unto Thyself], Who rulest in Thy world, doing therein according to Thy will, for all Thy ways are judgment and all is Thine. We are Thy people and Thy servants, and in all circumstances it is our duty to give thanks unto Thee and to bless Thee. O Thou Who repairest the breaches in Israel, mayest Thou also repair this breach in Israel, granting us life.\" ", 

            "To where does he return[1]? ", 

            "Rab Zebid said in the name of Abbai : ", 

            "He returns to the commencement[2] ; but the Rabbis say :", 

            " To the place where he made the interruption[3]. ", 

            "The Halakah is — ", 

            "He returns to the place where he made the interruption. ", 

            "The Exilarch said to Rab Sheshet, ", 

            "\"Although", 

            " you are old[4] Rabbis, the Persians are more expert than you in the etiquette of a meal. When there are two couches, the more important guest reclines first and the other above him ; when there are three, the chief guest reclines in the centre, the next important above him and the third below him.\" ", 

            "Rab Sheshet said to him,", 

            " \"But should the chief guest wish to converse with him [who is above him], he would have to straighten himself and sit up to do so!\" ", 

            "The Exilarch replied,", 

            " \"It is otherwise with the Persians, because he would communicate with him by gesture[5].\" ", 

            "[Rab Sheshet asked the Exilarch], \"With whom do [the Persians] commence to wash previous to the meal ?\" ", 

            "He replied, ", 

            "\"With the chief guest.\"", 

            " \"Does, then, the chief guest watch his hands[6] until all the others wash?\" ", 

            "He replied,", 

            " \"They immediately set a tray before him.\"", 

            " \"With whom do they commence to wash at the conclusion of the meal?\"", 

            " He answered, ", 

            "\"With the person of least importance.\" ", 

            "\"Then the chief guest sits with his hands stained until they all wash!\"", 

            " He replied,", 

            " \"They do not remove the tray from before him until they set water before him.\" ", 

            "Rab Sheshet said [to the Exilarch] :", 

            " I know a teaching, viz. : What is the procedure of reclining ? ", 

            "When there are two couches, the more important person reclines first, and the other below him. When there are three couches, the chief person reclines first, the next important above him, and the third below him. ", 

            "They begin the washing previous to the meal with the chief guest. As for the washing at the conclusion of the meal, when there are five, they commence with the chief guest; but when there are a hundred[1] they commence with the person of least importance until they reach the last five, and then they commence with the principal guest. ", 

            "To whom the water after the meal returns[2], [the privilege of saying] Grace likewise returns.", 

            " This supports the statement of Rab ; for Rab Hiyya said in the name of Rab : ", 

            "He who washes his hands first at the end of a meal is delegated to say Grace. ", 

            "Rab and R. Hiyya were sitting at table in the presence of Rabbi. ", 

            "Rabbi said to Rab, ", 

            "\"Arise, wash thy hands.\" ", 

            "R. Hiyya noticed that Rab was trembling[3] and said to him,", 

            " \"O son of princes! ", 

            "See, it is for the privilege of saying Grace after meals that Rabbi tells thee [to wash].\" ", 

            "The Rabbis have taught :", 

            " We do not honour a man on a road or bridge[4],\n"

        ], 

        [

            "or with [washing] the hands stained [in the course of the meal][5]. ", 

            "Rabin and Abbai were journeying along a road ; the ass of Rabin went in front of Abbai's, and he did not say to him, \"Let the master go [first].\"", 

            " Abbai said [to himself],", 

            " \"Since this young Rabbi has come from the West[6], he has grown very conceited.\" ", 

            "When he reached the entrance of the Synagogue, Rabin said to him, ", 

            "\"Let the master enter [first].\" ", 

            "He retorted, ", 

            "\"And up to now have I not been master[7] !\"", 

            " He replied, \"Thus spake R. Johanan ;", 

            " We only honour a man [by making way for him] in the case of a door which has a Mezuzah.\" ", 

            "\"If there is a Mezuzah, one does ; but if there is no Mezuzah, one does not ?", 

            " Then, in the case of a Synagogue or House of Study which has no Mezuzah, there also one should not honour a man [by making way for him]!\"", 

            " \"Nay, [the meaning is,] ", 

            "A door which is liable to have a Mezuzah affixed[8].\" ", 

            "Rab Judah the son of Rab Samuel b. Shelat said in the name of Rab: ", 

            "Those who recline at table are not permitted to eat anything until he who breaks bread partakes thereof.", 

            " Rab Safra sat there and said, ", 

            "\"To taste\" was said [by Rab, riot \"to eat\"]. ", 

            "What is to be deduced therefrom ? That a man is in duty bound to repeat [a statement] in the exact language of his teacher[1]. ", 

            "Our Rabbis have taught :", 

            " Two may wait upon each other with a dish, but three may not. The one who breaks bread puts forth his hand first[2]; but if he wishes to show respect to his teacher or his superior[3], he has the power to do so. ", 

            "Rabbah b. Bar Hannah was marrying his son into the family of Rab Samuel[4] b. Rab Kattina. He sat beforehand and taught his son[5] : ", 

            "He who is to break the bread is not permitted to do so until the response \"Amen\" has been completed by all. ", 

            "Rab Hisda said : ", 

            "By the majority.", 

            " Rammi b. Hamma asked him,", 

            " \"What difference does the majority make since the benediction has not been completed[6], the minority having not yet completed it?\" ", 

            "He replied, ", 

            "\"I declare that whoever makes the response 'Amen' unduly [prolonged] acts in error[7].\" ", 

            "Our Rabbis have taught:", 

            " In responding \"Amen\" one should not make the word hurriedly pronounced[8] or cut short[9] or an \"orphan[10]\" ; nor should he hurl the benediction from his mouth[11]. ", 

            "Ben 'Azzai says: ", 

            "Whoever responds with an \"orphan Amen,\" his sons will be orphaned, with a \"hurried Amen\" his days will be hurried[12],", 

            " with a \"cut short Amen\" his days will be cut short. But whoever prolongs the \"Amen,\" his days and years will be prolonged for him. ", 

            "Rab and Samuel were sitting at a meal. Rab Shimi b. Hiyya came and hurriedly ate his food.", 

            " Rab said to him, ", 

            "\"What is thine intention — to join with us [in saying Grace with Zimmun]? ", 

            "We have concluded the meal[1].", 

            "\" Samuel said to him,", 

            " \"If they brought me mushrooms or Abba[2] pigeons, should we not eat[3]?\" ", 

            "Rab's disciples were sitting at a meal, and Rab[4] entered. ", 

            "They said,", 

            " \"A great man has come who will say Grace for us.\" ", 

            "He said to them, ", 

            "\"Are you of opinion that a great man must say Grace? ", 

            "No, one who was at the main part of the meal should say Grace.\" ", 

            "But the Halakah is —", 

            " The most important person says Grace, although he arrived at the end of the meal. ", 

            "One who has eaten Demai, etc. ", 

            "But he had no right [to eat it][5] !", 

            " If he so choose, he can renounce his possessions and become a poor man, and then he would have the right [to eat it] ; for we have a Mishnaic teaching :", 

            " We may feed the poor and soldiers[6] on Demai. ", 

            "But Rab Huna has said :", 

            " It has been taught : Bet Shammai declare that", 

            " we may not feed the poor and soldiers on Demai[7]. ", 

            "The first tithe from, which Terumah has been taken. ", 

            "This is evident[8] ! ", 

            "No ; it is necessary to state it for the case where [the Levite] anticipated with the ears of corn and separated therefrom the Terumah of the tithe before [the priest] had separated the great Terumah[9]. ", 

            "This is in accord with R. Abbahu who said in the name of R. Simeon b. Lakish :", 

            " The first tithe, which [the Levite] anticipated and separated from the ears, is exempt from the great Terumah ; ", 

            "as it is said,", 

            " \"Ye shall set apart of it a gift for the Lord, even a tithe of the tithe\" (Num. xviii. 26) —", 

            " i.e. \"a tithe of the tithe\" I tell thee [to set apart], but not a great Terumah or a Terumah of a tithe of a tithe. ", 

            "Rab Pappa said to Abbai :", 

            " In that case, even if [the Levite] anticipated [and separated his tithe] from the corn-heap[1], it would likewise [be exempt from the great Terumah] ! ", 

            "He replied : ", 

            "To meet thy objection the Scriptures state,\n"

        ], 

        [

            " \"Out of all your tithes[2] ye shall set apart\" (Num. xviii. 29). ", 

            "What, however, seest thou[3]? ", 

            "The latter is corn but the other is not[4]. ", 

            "The second tithe or food belonging to the Sanctuary which had been redeemed. ", 

            "This is evident[5] ! ", 

            "With what are we here dealing ? For instance, if he paid its value but not the additional fifth[6] ; hence he informs us that ", 

            "[not having paid] the additional fifth does not prevent him [from being included for Zimmun]. ", 

            "The attendant who has eaten food the size of an olive. ", 

            "This is evident[7] ! ", 

            "Perhaps thou mayest argue that the attendant has no fixed place[8]; therefore we are informed [that he is to be included]. ", 

            "The Samaritan may be included for Zimmun. ", 

            "Why should he be? ", 

            "He is nothing better than an 'Am ha'ares, and there is a teaching :", 

            " 'Amme ha'ares are not to be included for Zimmun ! ", 

            "Abbai said :", 

            " It refers to a Samaritan who is a Haber.", 

            " Raba said : ", 

            "Thou mayest even suppose that it refers to a Samaritan who is an 'Am ha'ares, and we are here dealing with the 'Am ha'ares so designated by the Rabbis who disagree in this matter with R. Meir. ", 

            "For there is a teaching :", 

            " Who is an 'Am ha'ares? ", 

            "Whoever does not eat his non-holy food[9] in a condition of ritual purity — these are the words of R. Meir ;", 

            " but the Sages say :", 

            " Whoever does not properly tithe his fruits. These Samaritans, however, do properly apportion the tithe, for they are careful to observe what is written in the Torah[10]. The teacher has said : ", 

            "The commandments to which the Samaritans adhere they observe more scrupulously than the Israelite. ", 

            "Our Rabbis have taught :", 

            " Who is an 'Am ha'ares?", 

            " Whoever does not read the Shema' evening and morning — these are the words of R. Eliezer; but R. Joshua says : ", 

            "Whoever does not lay Tefillin. Ben 'Azzai says :", 

            " Whoever has no Sisit on his garment[1]. R. Nathan says :", 

            " Whoever has no Mezuzah on his door. R. Nathan[2] b. Joseph says : ", 

            "Whoever has sons and does not rear them to the study of Torah. Others declare :", 

            " Even if one has studied Torah and Mishnah but has not ministered to the disciples of the wise[3], he is an 'Am ha'ares. ", 

            "Rab Huna said : ", 

            "The Halakah is in accord with the last mentioned. ", 

            "Rammi b. Hamma refused to include for Zimmun ", 

            "Rab Menashya b.Tahlifa who taught Sifra, Sifre[4] and the Halakah. ", 

            "When Rammi b. Hamma departed this life, Raba said : ", 

            "He only died because he refused to include Rab Menashya b. Tahlifa for Zimmun. ", 

            "But there is a teaching : Others declare ; ", 

            "Even if one has studied Torah and Mishnah but has not ministered to the disciplas of the wise, he is an 'Am ha'ares[5] !", 

            " It is different with Rab Menashya b. Tahlifa because he did minister to the Rabbis, but Rammi b. Hamma failed to make careful inquiry about him. ", 

            "Another version is : ", 

            "Rab Menashya heard the teachings from the mouth of the Rabbis and studied them, and therefore was like a Rabbinical scholar. ", 

            "One who has eaten of the untithed, or the first tithe, etc. ", 

            "[If he has eaten of] the untithed, it is evident [that he should not be included]! ", 

            "No; it was necessary to state it because of the untithed which is so designated by the Rabbis. ", 

            "How is this meant? As referring to that which grows in an unperforated pot[6]. ", 

            "The first tithe from which Terumah has not been taken. ", 

            "That is evident ! ", 

            "No ; it is necessary [to mention it] for the case where [the Levite] anticipated [the priest by taking the tithe] from the corn-heap[1]. ", 

            "Thou mayest argue that it is ", 

            "as Rab Pappa said to Abbai[2]. Therefore we are informed that it is as Abbai answered him[3]. ", 

            "The second tithe or food belonging to the Sanctuary which had not been redeemed. ", 

            "This is evident ! ", 

            "No ; it is necessary [to mention it] for the case where it has been redeemed but not according to the Halakah.", 

            " With \"the second tithe,\" for instance, where he redeemed it with uncoined silver, whereas the All-merciful declared,", 

            " \"Thou shalt bind up the money in thy hand\" (Deut. xiv. 25) — i.e. money which has a stamp upon it[4]. With \"food belonging to the Sanctuary\" for which [for instance] he had given a piece of land in exchange but he had not redeemed with money ; whereas the All-merciful declared,", 

            " \"He shall add the fifth part of the money of thy valuation unto it, and it shall be assured to him\" (Lev. xxvii. 19)[5]. ", 

            "And the attendant who has eaten less than the size of an olive. ", 

            "That is evident[6] ! ", 

            "But since he taught the first clause relating to food the size of an olive, he also teaches the latter clause relating to food less than the size of an olive. ", 

            "And the idolator[7] may not be included for Zimmun. ", 

            "That is evident ! ", 

            "With what are we here dealing ? With a proselyte who has been circumcised but not undergone immersion ; for R. Zera said in the name of R. Johanan[8] : ", 

            "He is certainly not to be regarded as a proselyte until he has been circumcised and undergone immersion, and so long as he has not undergone immersion he is still a non-Jew. ", 

            "Women, slaves and minors may not be included for Zimmun, ", 

            "R. Jose[1] said : ", 

            "An infant lying in the cradle may be included for Zimmun. ", 

            "But lo, there is our Mishnaic teaching :", 

            " Women, slaves and minors may not be included! ", 

            "R. Jose is in agreement with the statement of R. Joshua b. Levi who said : ", 

            "Although they declare that an infant lying in the cradle may not be included for Zimmun, yet we may consider him an addition. to make up a quorum of ten[2]. ", 

            "R. Joshua b. Levi also said :", 

            " Nine [free] men and a slave may be reckoned together for a quorum[3].", 

            " Against this is quoted :", 

            " It happened that R. Eliezer went into a Synagogue and did not find ten there, so he freed his slave and with him completed the requisite number. ", 

            "Since he freed him he was [included], but had he not freed him, he would not !", 

            " Two had been required [to complete the quorum], so he freed one slave and fulfilled the obligation [of having ten] with the other.", 

            " But how could he act thus ?", 

            " For lo, Rab Judah declared : ", 

            "Whoever frees his slave transgresses a command of the Torah ; as it is said, ", 

            "\"Of them shall ye take your bondmen forever\" (Lev. xxv. 46) ! ", 

            "For the purpose of fulfilling a religious duty it is different. ", 

            "But it is fulfilling a religious duty through the means of a transgression[4] ! ", 

            "The fulfilling of a religious duty which affects the many[5] is different. ", 

            "R. Joshua b. Levi also said : ", 

            "A man should always go early to the Synagogue so that he may have the merit of being counted with the tirst ten ; for even if a hundred come after him, he receives upon himself the reward of them all. ", 

            "The reward of them all, dost imagine? ", 

            "Nay, he means to say,", 

            " he is given a reward equal to them all.", 

            "Rab Huna said : ", 

            "Nine and the Ark[6] may be reckoned together for a quorum. ", 

            "Rab Nahman asked him :", 

            " Is the Ark a man ! ", 

            "But, said Rab Huna, ", 

            "since nine look like ten, they may be reckoned together.", 

            " Another version is : ", 

            "When they are gathered together[1]; ", 

            "another version is : ", 

            "When they are scattered. ", 

            "R. Ammi said :", 

            " Two and the Sabbath[2] may be reckoned together for Zimmun. ", 

            "Rab Nahman asked him :", 

            " Is the Sabbath a man! ", 

            "But, said R. Ammi, ", 

            "two disciples of the wise who sharpen [their minds] one against the other with the study of Halakah may be reckoned together [for Zimmun]. ", 

            "Rab Hisda declared :", 

            " For instance, I and Rab Sheshet. ", 

            "Rab Sheshet declared : ", 

            "For instance, I and Rab Hisda. ", 

            "R. Johanan said[3] : ", 

            "A minor who develops puberty prematurely may be included for Zimmun. ", 

            "There is a teaching to the same effect : ", 

            "A minor who shows signs of puberty[4] is to be included, but if he does not show such signs[5] he is not to be included ; we are, however, not to be very particular with a minor[6]. ", 

            "But this is self-contradictory !", 

            " Thou sayest :", 

            " If he shows signs of puberty he is [to be included], but if not, he is not ; and then it continues, ", 

            "\"We are, however, not to be very particular with a minor\" ! What does this mean to include? ", 

            " Surely "

        ], 

        [

            "it is to include the boy who  develops puberty prematurely. ", 

            "But the Halakah is not in agreement with any of these teachings, but with that which Rab Nahman said : ", 

            "A minor who understands to Whom we say Grace is to be included for Zimmun. ", 

            "Abbai and Raba[7] were sitting in the presence of Rabbah. He asked them, ", 

            "\"To Whom do we say Grace[8]?\"", 

            " They replied,", 

            " \"The All-merciful.\" ", 

            "\"And where does the All-merciful dwell?\" ", 

            "Raba pointed upwards to the ceiling ; Abbai went outside and pointed towards the heavens. ", 

            "Rabbah said to them, ", 

            "\"Both of you are Rabbis ; ", 

            "for that is what the proverb says,", 

            " 'Every pumpkin is known by its stem[1]'.\" ", 

            "Rab Judah b. Rab Samuel b. Shelat said in the name of Rab :", 

            " If nine ate corn-food and one ate vegetables, they are to be reckoned together[2]. ", 

            "R. Zera[3] said, \"I asked Rab Judah,", 

            " 'How is it with eight", 

            " or seven[4] ?' ", 

            "He replied, ", 

            "'It makes no difference.' ", 

            "Concerning six there was[5] no need for me to ask.\" ", 

            "R. Jeremiah said to him,", 

            " \"Well hast thou done", 

            " in not asking [about six]. What is the reason there[6]? Because there is a majority [who have eaten cornfood].\" But here also [with six] there is a majority !", 

            " But R. Zera was of opinion that", 

            " we require a clearly recognisable majority[7]. ", 

            "King Jannaeus and his Queen were dining together, and since he had put the Rabbis[8] to death, he had nobody to say Grace for them. ", 

            "He said to his wife,", 

            " \"Would that we had somebody to say Grace for us.\"", 

            " She said to him, ", 

            "\"Swear to me that if I bring thee such a man, thou wilt not harm him.\"", 

            " He swore to her ; ", 

            "and she brought him her brother, Simeon b. Shetah[9]. The king gave him a seat between himself and her, ", 

            "and said to him,", 

            " \"See how much honour I pay thee.\" ", 

            "He replied, ", 

            "\"It is not thou that honourest me, but it is the Torah that brings me honour ; for it is written, 'Extol her, and she will exalt thee ; she will bring thee honour when thou dost embrace her' (Prov. iv. 8)[10].\"", 

            " The king said to him,", 

            " \"Thou seest they[11] do not accept any lordship[12]!\" ", 

            "He was handed a cup of wine to say Grace. ", 

            "He said, \"How shall I word the Grace[1]? ' Blessed be He of Whose bounty Jannaeus and his companions have eaten'?\" ", 

            "He drank the cup of wine. ", 

            "They gave him another cup of wine and then he said Grace. ", 

            "R. Abba b. R. Hiyya b. Abba said[2] :", 

            " Simeon b. Shetah who did this[3] acted so on his own account[4]. For thus said R. Hiyya b. Abba in the name of R. Johanan : ", 

            "Nobody can cause others to have complied with the requirements of the law[5] until he has eaten corn-food of the size of an olive.", 

            " Against this is quoted : Rabban Simeon b. Gamaliel says :", 

            " If one has ascended [the couch] and reclined with them, even though he has not dipped with them except the smallest quantity[6] and has not eaten with them except a single dried fig, he is to be reckoned with them [for Grace] !", 

            " Yes, he may be reckoned with them, but he is unable to cause others to comply with the requirements of the law until he has eaten corn-food of the size of an olive.", 

            " It has been similarly reported : Rab Hanna[7] b. Judah said in the name of Raba :", 

            " Even if he has not  "

        ], 

        [

            "dipped with them except the smallest quantity and  has not eaten with them except a single dried fig, he is to be reckoned with them, but as for causing others to comply with the requirements of the law, that he cannot do until he has eaten cornfood of the size of an olive. ", 

            "Rab Hanna b. Judah said in the name of Raba : The Halakah is —", 

            " If he has eaten a single cabbage-leaf and drunk a cup of wine, he is to be reckoned with them ; but as for causing others to comply with the requirements of the law, that he cannot do until he has eaten corn-food of the size of an olive. ", 

            "Rab Nahman said : ", 

            "Moses instituted for Israel the benediction \"Who feedest[8]\" at the time the manna descended for them. Joshua instituted for them the benediction of \"the land[9]\" when they entered the land [of Canaan]. David and Solomon instituted [what follows] until[10] \"Who... rebuildest Jerusalem[11].\" ", 

            "David instituted \"[Have mercy, O Lord our God] upon Israel Thy people, upon Jerusalem Thy city,\" and Solomon[12] instituted \"and upon the great and holy House.\" The benediction \"Who art kind and dealest kindly[1]\" was instituted in Jabneh[2] in connection with the slain of Bethar[3] ; ", 

            "for Rab Mattena said : ", 

            "On the day the slain of Bethar were allowed burial, there was instituted in Jabneh the benediction \"Who art kind and dealest kindly\" — \"Who art kind,\" because the bodies did not decompose[4] ; \"and dealest kindly,\" because they were allowed burial. ", 

            "Our Rabbis have taught :", 

            " The following is the order of the Grace after meals : ", 

            "The first benediction is \"Who feedest\" ; the second, the benediction of \"the land\"; the third, \"Who...rebuildest Jerusalem\" ; the fourth, \"Who art kind and dealest kindly.\" On the Sabbath, one begins and ends with consolation and refers to the sanctity of the day in the middle[5].", 

            " R. Eliezer says:", 

            " If he wishes to include [the reference to the Sabbath] in the \"consolation,\" he may do so ; in the benediction of \"the land,\" he may do so ; in the benediction instituted by the Sages in Jabneh, he may do so.", 

            " The Sages, however, say : ", 

            "He should only include it in the \"consolation.\"", 

            " Then the Sages agree with the first Tanna[6]! ", 

            "There is a point of difference between them, viz. : the post factum[7]. ", 

            "Our Rabbis have taught : ", 

            "Whence do we derive the Grace after meals from the Torah? ", 

            "As it is said,", 

            " \"And thou shalt eat and be satisfied and bless\" (Deut. viii. 10) — this refers to the benediction \"Who feedest\"; \"the Lord thy God\" (ibid.)— to the benediction of Zimmun; \"for the land\" (ibid.) — to the benediction of \"the land\" ; \"the good\" (ibid.) — to \"Who. . . rebuildest Jerusalem,\" for so it states ", 

            "\"That goodly hill-country and Lebanon\" (ibid. iii. 25); \"which He hath given thee\" (ibid. viii. 10) — to \"Who art kind and dealest kindly.\"", 

            " I have here only the Grace after meals ; whence do we derive the Grace before meals ?", 

            " Thou canst reason by a fortiori argument — if a man should bless God when satisfied, how much more so when he is hungry[1] ! ", 

            "Rabbi says[2] :", 

            " \"And thou shalt eat and be satisfied and bless\" refers to the benediction \"Who feedest,\" but the benediction of Zimmun is derived from \"Magnify the Lord with me\" (Ps. xxxiv. 4)[3] ; \"for the land\" — to the benediction of \"the land\" ; \"the good\"— to \"Who...rebuildest Jerusalem,\" for so it states \"That goodly hill-country and Lebanon\"; the benediction \"Who art kind and dealest kindly\" was instituted in Jabneh.", 

            " I have here only the Grace after meals ; whence do we derive the Grace before meals ?", 

            " There is a teaching to state,", 

            "\"Which He hath given thee\" — ie. as soon as He hath given thee[4]. ", 

            "R. Isaac said :", 

            " [This reasoning] is unnecessary. Behold it states, ", 

            "\"And He will bless thy bread and water\" (Exod. xxiii. 25)— read not \"And He will bless\" [uberak] but \"And bless thou\" [ubarak]. When is it called \"bread[5]\" ? Before one eats it[6]. ", 

            "R. Nathan[7] said :", 

            " [This reasoning] is unnecessary. Behold it states, ", 

            "\"As soon as ye are come into the city, ye shall straightway find him, before he go up to the high place to eat ; for the people will not eat until he come, because he doth bless the sacrifice ; and afterwards they eat that are bidden\" (I Sam. ix. 13)[8].", 

            " Why all this[9]?", 

            " [10]Because women are garrulous. ", 

            "Samuel[11] said: ", 

            "The women did it in order to gaze upon Saul's beauty; for it is written,", 

            " \"From his shoulders and upward he was higher than any of the people\" (ibid. V. 2). ", 

            "R. Johanan said :", 

            " [The women did it] because one reign must not encroach upon another even a hair's breadth[12]. ", 

            "I have here only the benediction for meals ; whence is the benediction over Torah derived? ", 

            "R. Ishmael said : ", 

            "By a fortiori reasoning — for temporal life[1] one says a benediction ; how much more so for the life of the world to come[2]! ", 

            "R. Hiyya b. Nahmani[3], the disciple of R. Ishmael, says in the name of R. Ishmael :", 

            " [This reasoning] is unnecessary ; for it states, ", 

            "\"For the good land which He hath given thee\" (Deut. viii. 10) and elsewhere it is stated, ", 

            "\"And I will give thee the tables of stone, and the law and the commandments,\" etc. (Exod. xxiv, 12)[4]. ", 

            "R. Meir said :", 

            " Whence is it that as one blesses for the good so should he bless for the bad[5]?", 

            " There is a teaching to state, ", 

            "\"Which the Lord thy God hath given unto thee\" (Deut. xxvi. 11) — He is thy judge in every circumstance wherein He judgeth thee, whether it be with the attribute of goodness or the attribute of punishment[6]. ", 

            "R. Judah b. Batyra said :", 

            " [This reasoning] is unnecessary ; for it states,", 

            " \"Good\" (Deut. viii. 7) and \"the good\" (ibid. V. 10)[7] — ", 

            "\"good\" i.e. Torah, as it is said ", 

            "\"For I give you good doctrine\" (Prov. iv. 2); \"the good\" i.e. the rebuilding of Jerusalem, as it is said \"That goodly[8] hill-country and Lebanon\" (Deut. iii. 25)[9].", 

            "There is a teaching : R. Eliezer[10] says : ", 

            "Whoever does not say \"a desirable, good and ample land\" in the benediction of \"the land\" and \"the kingdom of the house of David\" in \"Who...rebuildest Jerusalem\" has not complied with the requirements of the law.", 

            " Nahum the Elder says :", 

            " He must mention the Covenant[11] in the blessing of \"the land.\"", 

            " R. Jose says :", 

            " He must mention the Torah therein[12]. ", 

            "Pelemo says :", 

            " He must refer to the Covenant before the Torah, because the latter was given with a three-fold covenant "

        ], 

        [

            "but the former with a thirteen-fold covenant[1].  ", 

            "R. Abba[2]  says :", 

            " One must mention thanksgiving therein at the commencement and conclusion[3], and he who shortens [the Grace] must not omit more than one of them ; for whoever omits more than one of them is to be reprimanded. ", 

            "Whoever concludes the benediction of \"the land\" with the words \"[Blessed art Thou, O Lord,] Who givest lands as a heritage,\" or the benediction \"Who...rebuildest Jerusalem\" with the words \"Who savest Israel\" is a boor. And whoever does not include a reference to the Covenant and the Torah in the benediction of \"the land\" and a reference to the kingdom of the house of David in the benediction \"Who...rebuildest Jerusalem\" has not complied with the requirements of the law.", 

            " This supports the teaching of R. El'ai who stated that R. Abba b. Aha[4] said in the name of our master : ", 

            "Whoever omits the reference to the Covenant and the Torah in the benediction of \"the land\" and to the kingdom of the house of David in the benediction \"Who...rebuildest Jerusalem\" has not complied with the requirements of the law. ", 

            "Abba Jose b. Dostai[5] and the Rabbis disagree, one declaring that", 

            " \"Who art kind and dealest kindly\" requires a reference to the [Divine] Kingship[6], the other declaring that", 

            " it does not.", 

            " He who contends that it requires a reference to the Kingship is of opinion that this benediction was ordained", 

            " by the Rabbis[7], and he who contends that it does not is of opinion that the benediction is ordained ", 

            "by the Torah[8]. ", 

            "Our Rabbis have taught : ", 

            "How should one conclude", 

            " the benediction of the rebuilding of Jerusalem?", 

            " R. Jose b. R. Judah says[1] : ", 

            "\"Who savest Israel.\"", 

            " Is one to say \"Who savest Israel\" and not \"Who...rebuildest Jerusalem[2]\"? Nay,", 

            " [it means,] one also says", 

            " \"Who savest Israel.\" ", 

            "Rabbah b. Rab Huna visited the house of the Exilarch. [When saying Grace,] the latter opened with one and concluded with two[3]. ", 

            "Rab Hisda asked:", 

            " What advantage is there in concluding with two? ", 

            "Moreover there is a teaching : Rabbi says : ", 

            "We should not conclude with two ! ", 

            "It has just been stated : \"Rabbi says :", 

            " We should not conclude with two.\"", 

            " Levi quoted against Rabbi, ", 

            "\"For the land and for the food[4]\" !", 

            " It means, \"The land which yields food[5].\"", 

            " \"For the land and for the fruits[6]\"!", 

            " It means \"The land which yields fruits.\"", 

            " \"Who hallowest Israel and the seasons[7]\"!", 

            " It means, \"Israel who sanctify the seasons.\"", 

            " \"Who sanctifiest Israel and the beginnings of the months[8]\"!", 

            " It means, \"Israel who hallow the beginnings of the months.\" ", 

            "\"Who hallowest the Sabbath, Israel and the seasons[7]\" ! ", 

            "This is an exception.", 

            " Why is it different[9]?", 

            " Here it is one idea, but there it is two, each distinct from the other. ", 

            "What is the reason that we do not conclude with two ? We must not perform commandments in bundles[10]. ", 

            "How is it, then, in this matter? ", 

            "Rab Sheshet said :", 

            " If one opens with \"Have mercy... upon Israel Thy people,\" he concludes with \"Who savest Israel\" ; if one opens with \"Have mercy... upon Jerusalem Thy city,\" he concludes with \"Who...rebuildest Jerusalem.\" ", 

            "Rab Nahman[11] said: ", 

            "Even if one opens with \"Have mercy... upon Israel Thy people,\" he should conclude with \"Who... rebuildest Jerusalem\"; because it is said,", 

            " \"The Lord doth build up Jerusalem, He gathereth together the dispersed of Israel\" (Ps. cxlvii. 2) — when \"doth the Lord build up Jerusalem\"? At the time that \"He gathereth together the dispersed of Israel[1].\" ", 

            "R. Zera[2] said to Rab Hisda,", 

            " \"Let the master come and teach.\" ", 

            "He replied, ", 

            "\"[The regulations concerning] Grace after meals have I not learnt, so shall I teach !\" ", 

            "R. Zera asked him, ", 

            "\"How is that?\" He replied, \"When I visited the house of the Exilarch and said the Grace after meals, Rab Sheshet stretched his neck over me like a serpent[3].\"", 

            " \"But why ?\"", 

            " \"Because I made no reference to the Covenant, the Torah or the Kingship.\"", 

            " \"And why didst thou not mention them?\"", 

            " \"In accord with the statement of Rab Hananel in the name of Rab, viz. : ", 

            "If one has not referred to the Covenant, the Torah and the Kingship, he has complied with the requirements of the law — ", 

            "'the Covenant' because it does not apply to women ; 'the Tordh and the Kingship' because they apply neither to women nor slaves.\"", 

            " \"And thou didst abandon all these Tannaim and Amoraim[4] and act according to the view of Rab[5]!\" ", 

            "Rabbah b. Bar Hannah said in the name of R. Johanan : ", 

            "The benediction \"Who art kind and dealest kindly\" requires a reference to the Kingship. ", 

            "What does he intend to tell us — ", 

            "that a benediction which contains no reference to the Kingship has not the name of benediction ? But R. Johanan has already told us this once[6] !", 

            " R. Zera[7] said : ", 

            "He means to say that it needs two references to the Kingship, one for its own sake[8] and one for \"Who...rebuildest Jerusalem.\"", 

            " If so, three are required — one for its own sake, one for \"Who...rebuildest Jerusalem\" and one for the benediction of \"the land\"; ", 

            "for, why should not the benediction of \"the land\" have one?", 

            " Because it is a benediction which is connected with the preceding[9]. Then \"Who...rebuildest Jerusalem\" should likewise not require one because it is a benediction which is connected with the preceding! ", 

            "Strictly speaking, even \"Who...rebuildest Jerusalem\" does not require one ; but since it mentions the kingdom of the house of David, it is not proper to omit a reference to the [Divine] Kingship. ", 

            "Rab Pappa said : This is what R. Zera meant to say:", 

            " It requires two references to Kingship besides the one for its own sake[1]. ", 

            "R. Zera sat behind Rab Giddel and Rab Giddel sat before Rab Huna ; he sat and said :", 

            " If one erred and omitted to mention the reference to the Sabbath [in the Grace after meals][2], he says ", 

            "\"Blessed be He Who has given Sabbaths for rest to His People Israel in love for a sign and a covenant. ", 

            "Blessed [art Thou, O Lord,] Who sanctifiest the Sabbath.\"", 

            " Rab Huna asked Rab Giddel :", 

            " Who said that ? ", 

            "Rab. Again he sat and said :", 

            " If one erred and omitted to mention the reference to the Festival[3], he says, \"Blessed be He Who has given Festivals to His people Israel for rejoicing and a memorial. Blessed... Who Sanctifiest Israel and the seasons.\" ", 

            "He asked him:", 

            " Who said that?", 

            " Rab.", 

            " Again he sat and said :", 

            " If one erred and omitted to mention the reference to the New Moon he says, \"Blessed be He Who has given beginnings of the month to His people Israel for a memorial\" ; but I do not know whether he adds the words \"and for rejoicing\" or not, whether he adds a conclusion to the benediction or not, or whether it is his own or his master's[4]. ", 

            "Giddel b. Minjomi was standing[5] before Rab Nahman. Rab Nahman made a mistake [in the Grace]  "

        ], 

        [

            "and returned to the commencement. ", 

            "He asked him, ", 

            "\"Why did the master do so\"?\"", 

            " He replied, \"Because Rab Shela[6] has said in the name of Rab:", 

            " If one erred, he should return to the commencement.\" ", 

            "\"But Rab Huna has declared in the name of Rab : ", 

            "If one erred, he should say", 

            " 'Blessed be He Who has given' [etc.] \" ! ", 

            "He said to him, ", 

            "\"Was it not reported in this connection : Rab Menashya b. Tahlifa said in the name of Rab: ", 

            "This teaching only applies if he has not commenced the benediction 'Who art kind and dealest kindly' ; but if he has commenced it, he must return to the beginning?\" ", 

            "Rab Iddi b. Abin said in the name of Rab 'Amram, in the name of Rab Nahman, in the name of Samuel[1]: ", 

            "If one erred and omitted the reference to the New Moon in the Tefillah[2] we make him repeat it: in the Grace after meals[3] we do not make him repeat it. ", 

            "Rab Abin[4] asked Rab 'Amram, ", 

            "\"Why is the Tefillah different from the Grace after meals in this respect?\"", 

            " He replied, ", 

            "\"To me also that was a difficulty and I put the question to Rab Nahman, who told me, ", 

            "'I have not heard the reason from the master, Samuel' ; but let us see : With regard to the Tefillah which is an obligation, we make him repeat it ; ", 

            "but with regard to the Grace after meals, where one can eat or not eat just as he pleases, we do not make him repeat it.\"", 

            " \"But now, on the Sabbaths and Festivals, when there is no question of his not eating[5], then also, if he erred, he should repeat it !\"", 

            " He replied, ", 

            "\"Quite so ; for Rab Shela said in the name of Rab :", 

            " If he erred, he must recommence at the beginning.\" ", 

            "\"But Rab Huna declared in the name of Rab :", 

            " If one erred, he says 'Blessed be He Who has given'[6]!\" ", 

            "\"Has it not been reported in that connection :", 

            " 'This teaching only applies if he has not commenced the benediction \"Who art kind and dealest kindly\" ; but if he has started it, he recommences at the beginning'?\" ", 

            "How much [must one have eaten at the meal] to he included for Zimmun ?", 

            "That is to say, R. Meir considers it to be the size of an olive and R. Judah the size of an egg. But we have been told the reverse ;", 

            "for there is a Mishnaic teaching : ", 

            "And so, he who went from Jerusalem and recalled that he had with him holy flesh [7], if he has passed Sofim[8], he burns it where he is ; but if not, he turns back and burns it before the Temple with some of the wood piled on the altar. ", 

            "How much [of the holy flesh must one have to make such a return necessary]? ", 

            "R. Meir says :", 

            " In either case[9] the size of an egg ;", 

            " but R. Judah says :", 

            " In either case the size of an olive[1]! ", 

            "R. Johanan said: ", 

            "The statement must be reversed[2].", 

            " Abbai said : ", 

            "There is certainly no necessity to reverse it ; for here[3] they differ in the interpretation of Scripture : R. Meir holds,", 

            " \"And thou shalt eat\" (Deut. viii. 10) — i.e. eating; \"and thou shalt be satisfied\" — i.e. drinking ; and \"eating\" means the minimum quantity of the size of an olive.", 

            " R. Judah, on the other hand, holds,", 

            " \"And thou shalt eat and be satisfied\" — i.e. eating wherein is some satisfaction; and what is that? That is the minimum quantity of the size of an egg. ", 

            "But in the other case[4], they differ in reasoning; R. Meir holds that", 

            " his return must be equal to his defilement — as his defilement[5] is only possible by means of something of the minimum size of an egg, so must his return be necessitated by holy flesh of the minimum size of an egg. ", 

            "R. Judah, however, holds that ", 

            "his return must be equal to his prohibition[6] — as his prohibition is with something of the minimum size of an olive, so must his return be necessitated by holy flesh of the minimum size of an olive. ", 

            "MISHNAH How do we [say Grace] with Zimmun ? ", 

            "With three persons [at table], one says ", 

            "\"We will bless [Him of Whose bounty we have partaken]\" ; with three and himself, he says \"Bless ye [Him of Whose bounty]\" etc. ", 

            "With ten, one says ", 

            "\"We will bless our God [of Whose bounty]\" etc.; with ten and himself , he says", 

            " \"Bless ye...\" ", 

            "and that is the same whether there be ten or ten myriads[7]. ", 

            "With a hundred, one says", 

            " \"We will bless the Lord our God...\"; ", 

            "with a hundred and himself, he says", 

            " \"Bless ye [the Lord our God]\" etc. With a thousand, one says ", 

            "\"We will bless the Lord our God, the God of Israel...\" ; with a thousand and himself, he says \"Bless ye....\" With ten thousand, one says \"We will bless the Lord our God, the God of Israel, the God of hosts, Who is enthroned above the Cherubim, for the food of which we have partaken\" ; with ten thousand and himself, he says ", 

            "\"Bless ye....\" As he blesses, exactly so do they respond after him:", 

            " \"Blessed be the Lord our God, the God of Israel, the God of hosts, Who is enthroned above the Cherubim, for the food of which we have partaken.\" R. Jose of Galilee says:", 

            " According to the numerical size of the assembly do they determine the form of the benediction; as it is said, ", 

            "\"Bless ye God in full assemblies, even the Lord, ye that are from the fountain of Israel\" (Ps. Ixviii. 27). ", 

            "R. 'Akiba said: ", 

            "What do we find in the Synagogue? Whether many or few, one says \"Bless ye the Lord[1].\" ", 

            "R. Ishmael says : \"Bless ye the Lord Who is to be blessed.\" ", 

            "GEMARA Samuel said : ", 

            "A man should never exclude himself from the general body[2]. ", 

            "But there is our Mishnaic teaching : ", 

            "With three and himself, he says \"Bless ye\"! ", 

            "He means to say  "

        ], 

        [

            "\"Bless ye also\"; but in any case \"We will bless\" is preferable.", 

            " But Rab  Adda b. Ahabah declared :", 

            " The school of Rab say : ", 

            "We have the teaching: Six people [who eat together] should divide themselves up[3], and so up to ten[4].", 

            " That is quite right if thou sayest \"We will bless\" is preferable, and therefore they are to be divided up; but if thou sayest \"Bless ye\" is preferable, why should they be divided up[5]? ", 

            "Is it not, then, to be concluded that \"We will bless\" is preferable?", 

            " Draw that conclusion. ", 

            "There is a teaching to the same effect[6]: Whether one says \"Bless ye\" or \"We will bless,\" we should not take him to task on that account[7] ; but punctilious people do[8]. ", 

            "Also, from the form of benediction used by a man it may be recognised whether he is a disciple of the wise or not.", 

            " How is this ? ", 

            "Rabbi declares :", 

            " [If he says] \"And through Whose goodness [we live],\" he is a disciple of the wise ; but if \"And from Whose goodness[1],\" he is a boor. ", 

            "Abbai said to Rab Dimai :", 

            " But it is written, \"And from Thy blessing let the house of Thy servant be blessed for ever\" (II Sam. vii, 29) ! ", 

            "With a petition it is different[2]. ", 

            "With a petition likewise it is written, \"Open thy mouth wide[3], and I will fill it\" (Ps. Ixxxi. 11) ! ", 

            "This is written in connection with words of Torah[4]. ", 

            "There is a teaching : Rabbi declares :", 

            " If one says \"Through Whose goodness we live\" he is a disciple of the wise ; if he says \"[Through Whose goodness] they live\" he is a boor.", 

            " The Rabbis of Neharbel[5] taught the reverse[6]; but the Halakah is not in agreement with them. ", 

            "R. Johanan declared :", 

            " [If he says] \"We will bless Him of Whose bounty we have partaken\" he is a disciple of the wise ; if he says \"[We will bless] the One of Whose bounty we have partaken\" he is a boor[7]. ", 

            "But Aha b. Raba[8] said to Rab Ashe : ", 

            "But we say : \"[We will bless] the One Who has performed for our fathers and for us all these miracles[9]\" !", 

            " He replied :", 

            " Here it is obvious that it is the Holy One, blessed be He, Who performed the miracles. ", 

            "R. Johanan declared :", 

            " [If he says] \"Blessed be He of Whose bounty we have partaken\" he is a disciple of the wise ; but if he says \"[Blessed be He] for the food of which we have partaken,\" he is a boor[10].", 

            " Rab Huna b. Rab Joshua said : ", 

            "This refers only to three, where the Divine Name is not mentioned ; but with ten, where the Name is mentioned, the matter is clear[11]. As our Mishnah teaches : ", 

            "As he blesses, exactly so do they respond after him:", 

            " \"Blessed be the Lord our God, the God of Israel, the God of hosts, Who is enthroned above the Cherubim, for the food of which we have partaken[1].\" ", 

            "Whether ten or ten myriads. ", 

            "This is self-contradictory !", 

            " Thou sayest : ", 

            "Whether ten or ten myriads, implying that they are the same[2]; and then it continues: ", 

            "With a hundred, one says ; With a thousand, one says ; With ten thousand, one says ! ", 

            "Rab Joseph said : There is no contradiction, ", 

            "the latter being the statement of R. Jose of Galilee, the other of R. 'Akiba.", 

            " For the Mishnah declares : R. Jose of Galilee says : ", 

            "According to the numerical size of the assembly do they bless; as it is said,", 

            " \"Bless ye God in full assemblies.\" ", 

            "R. 'Akiba said : What do we find in the Synagogue ? ", 

            "What does R. 'Akiba make of the verse quoted by R. Jose of Galilee ? ", 

            "He requires that for the following teaching :", 

            " R. Meir says : ", 

            "Whence is it derived that even the embryos in their mothers' womb sang the song at the Red Sea? As it is said,", 

            " \"Bless ye God in full assemblies[3], even the Lord, ye that are from the fountain of Israel\" (Ps. Ixviii. 27). ", 

            "And the other[4]? ", 

            "He derives it from the word \"fountain\"[5]. ", 

            "Raba said : ", 

            "The Halakah is in agreement with R. 'Akiba. ", 

            "Rabina and Rab Hamma b. Buzi visited the house of the Exilarch. [When about to say Grace] Rab Hamma stood up and looked about to see whether there were a hundred people present. ", 

            "Rabina said to him : ", 

            "It is unnecessary ; thus said Raba : ", 

            "The Halakah is in agreement with R. 'Akiba[6]. ", 

            "Raba said : ", 

            "When we dine at the house of the Exilarch, we say Grace in threes[7].", 

            " But they should have said Grace in tens[8] !", 

            " If the Exilarch had heard, he would have been angry[9]. ", 

            "But they could have fulfilled their duty by means of the Grace said by the Exilarch ! ", 

            "Since everybody made the responses in a loud voice, it could not be heard. ", 

            "Rabbah Tospaah said :", 

            " If three were dining together, and one finishing before the others says Grace for himself, they fulfil the obligation of Zimmun with him, but not he with them ; because the Zimmun cannot be retrospective[1]. ", 

            "R. Ishmael says:", 

            "Rafram b. Pappa visited the Synagogue of Abi Gibar[2]. He stood up, read in the Scroll and exclaimed, ", 

            "\"Bless ye the Lord\"; he then stopped and did not say \"Who is to be blessed.\"", 

            " They all shouted", 

            " \"Bless ye the Lord Who is to be blessed,\"", 

            " Raba said: ", 

            "Thou black pot[3]! What hast thou to do with this controversy? ", 

            "Moreover, ", 

            "everybody acts in accord with the opinion of R. Ishmael. ", 

            "MISHNAH  Three who have eaten together are not permitted to separate [before Grace], and, similarly with four or five. ", 

            "Six may divide themselves [into two parties for Zimmun] up to ten. ", 

            "But ten may not divide themselves up, [and similarly] up to twenty. ", 

            "If two parties eat in the same room, should some of one party be visible to some of the other party, they may be reckoned together for Zimmun[4]; but if not, each party arranges Zimmun for itself. ", 

            "We may not ", 

            "say the benediction over wine until water has been added to it[5]. These are the words of R. Eliezer ;", 

            " but the Sages say : ", 

            "The benediction may be pronounced [over wine without dilution]. ", 

            "GEMARA What does he wish to tell us[6]? ", 

            "We have already learnt in the Mishnah :", 

            " Three who ate together are under the obligation of Zimmun[7]! ", 

            "He means to inform us the same as that which R. Abba said in the name of Samuel : ", 

            "Three who sat down to eat together, although they have not yet partaken of food, are not permitted to separate [before saying Grace]. ", 

            "Another version : ", 

            "R. Abba[1] said in the name of Samuel : This is what he teaches [in our Mishnah] : ", 

            "Three who sat down to eat together, although each partakes of his own loaf, are not permitted to separate [before saying Grace].", 

            " Or also [he means to inform us] ", 

            "the same as that which Rab Huna said : ", 

            "Three persons who came together from three parties[2] are not permitted to separate [before saying Grace]. ", 

            "Rab Hisda said : ", 

            " This only applies to those who came together from three different parties, each of which consists of three men[3]. ", 

            "Raba said: "

        ], 

        [

            "This only refers to the case where the original parties did not at the outset include these [three men] in their own place for Zimmun[4] ; but if they had done so, then the necessity for Zimmun has passed from these men[5].", 

            " Raba said : ", 

            "Whence do I state this? ", 

            "For we have the Mishnaic teaching : ", 

            "A [defiled] couch, half of which has been stolen or lost or has been divided between brothers or partners, becomes clean[6]; ", 

            "but if it is restored, it can from that time onwards contract defilement.", 

            " From that time onwards it may contract defilement, but not retrospectively[7].", 

            " Infer from this that since it has been divided, the defilement has passed from it. So here also[8], ", 

            "since the parties had included these men for Zimmun, it passes from them. ", 

            "If two parties eat in the same room, etc. ", 

            "It has been taught :", 

            " If there be an attendant between them[9], he unites them [for Zimmun][10]. ", 

            "We may not say the benediction over wine. ", 

            "Our Rabbis have taught :", 

            "[wine]  Until", 

            " water has been added, we do not say the benediction \"...Who createst the fruit of the vine\" over the wine, but \"...Who createst the fruit of the tree\" ; and we may wash the hands therewith[1]. From the time that water has been added, the benediction is \"...Who createst the fruit of the vine,\" and we may not wash the hands therewith. These are the words of R. Eliezer ; ", 

            "but the Sages say :", 

            " In either case the benediction is \"...Who createst the fruit of the vine,\" and we may not wash the hands therewith.", 

            " In agreement with whom is that which Samuel said : ", 

            "A man may fulfil all his needs with bread[2]? With whom? ", 

            "With R. Eliezer[3].", 

            " R. Jose b. R. Hannina said:", 

            " The Sages agree with R. Eliezer that over a cup of wine intended for the Grace we do not say the benediction until water is added. ", 

            "What is the reason ? ", 

            "Rab Osha'ya answered : ", 

            "We require a commandment to be performed with the choicest[4]. ", 

            "But what is the use [of undiluted wine] according to the Rabbis? ", 

            "R. Zera said :", 

            " It may be used for a beverage made of caryota[5]. ", 

            "Our Rabbis have taught : Four things are said concerning bread — ", 

            "we may not place raw meat upon bread ; we may not pass a cup full of wine over bread ; we may not throw bread ; we may not rest a dish upon bread[6]. ", 

            "Amemar, Mar Zotra and Rab Ashe dined together, and dates and pomegranates were placed before them. Mar Zotra took [some of the fruit] and threw it before Rab Ashe as his portion. The latter said to him, ", 

            "\"Does not the master agree with that which has been taught : ", 

            "One may not throw articles of food?\" ", 

            "[He replied], \"That refers to bread.\"", 

            " \"But there is a teaching; ", 

            "Just as one may not throw bread, so one should not throw any article of food!\" ", 

            "He replied, \"But there is a teaching : ", 

            "Although one may not throw bread, other articles of food may be thrown!\"", 

            " There is, however, no contradiction,", 

            " one referring to that which becomes repugnant [by throwing], the other to that which does not become repugnant. ", 

            "Our Rabbis have taught : ", 

            "We may let wine[1] run through pipes before a bride and bridegroom[2], and throw before them roasted ears of corn and nuts in the Summer[3] but not in Winter; but we may not throw cakes[4] before them in Summer or Winter.  ", 

            "Rab Judah said :", 

            " If one forgot and put food into his mouth without a benediction, he should push it on one side [in his mouth] and say the benediction. ", 

            "Another taught:", 

            " He should swallow it;", 

            " there is another teaching : ", 

            "He should spit it out ; ", 

            "there is still another teaching :", 

            " He should push it aside [in his mouth]. ", 

            "There is no contradiction ;", 

            " the teaching that he should swallow it refers to liquids ; that he should spit it out refers to something that will not become repugnant; and that he should push it on one side refers to something which would become repugnant. "

        ], 

        [

            " But also with something which would not become repugnant let him push it on one side and say the benediction!", 

            " Rab Isaac Kaskesaah[5] explained [why that is not so] in the presence of R. Jose b. Abin, in the name of R. Johanan[6] : ", 

            "Because it is said, \"My mouth shall be filled with Thy praise\" (Ps. Ixxi. 8)[7]. ", 

            "Rab Hisda was asked :", 

            " If one has eaten or drunk without having said the benediction[8], may he say it afterwards? ", 

            "He answered : ", 

            "Shall one who has eaten garlic so that the smell is diffused eat more garlic so that its smell be more diffused[9]?", 

            " Rabina said :", 

            " Consequently, even if he has finished the meal, he may go back and say the benediction ! For there is a teaching :", 

            " If one has had immersion and ascended [from the water], as he ascends he should say ", 

            "\"Blessed... Who hast sanctified us with Thy commandments and commanded us concerning immersion.\" ", 

            "But the two cases are not parallel; for there [in the instance of immersion], the man was not at the outset fit [to pronounce a benediction][1] ; but here [in the instance of the benediction] the man was fit at the outset [to say it], and since it was deferred it must remain so. ", 

            "Our Rabbis have taught :", 

            " Asparagus-beverage[2] is beneficial for the heart, good for the eyes and how much more so for the digestive organs ; so if one grows addicted to it, it is beneficial for the whole of his body ; but if he becomes intoxicated therewith, it is harmful to his whole body.", 

            " Since he teaches that it is beneficial for the heart, it is to be inferred that we are here dealing with [a brew] with wine ; and he teaches,", 

            " \"How much more so for the digestive organs.\" But there is a teaching:", 

            " For the heart, eye and milt it is beneficial, but injurious to the head, bowels and piles !", 

            "The teaching above refers to old wine[3] ; according to the Mishnaic teaching :", 

            " [If one says] \"I vow to abstain from wine because it is injurious to the bowels,\" and they tell him ", 

            "\"But is not old wine beneficial for the bowels ?\" and he remains silent, then he is forbidden to drink new wine but is permitted to drink of the old. Draw that inference[4]. ", 

            "Our Rabbis have taught : Six things are said of the asparagus-beverage : ", 

            "One should only drink it undiluted and full[5]; one receives it with the right hand but drinks it [holding it] with the left ; one must not talk after drinking it ; one must not stop in the course of drinking ; one must only return the cup to him who handed it to him ; he should expectorate after drinking it ; and one must not support it except with its own kind[6]. ", 

            "But there is a teaching :", 

            " One should not support it except with bread !", 

            " There is no contradiction, the latter referring to [a brew] with wine, the other to [a brew] with beer. ", 

            "One teacher states :", 

            " For the heart, eyes and milt it is beneficial but injurious to the head, bowels and piles ; whereas there is another teaching :", 

            " It is beneficial for the head, bowels and piles but injurious to the heart, eyes and milt ! ", 

            "There is no contradiction ;", 

            " the latter referring to [a brew] with wine, the other to [a brew] with beer. ", 

            "One teacher states :", 

            " If he expectorates after drinking it he will be smitten [with illness]; and there is another teaching ;", 

            " If he does not expectorate after drinking it he will be smitten ! ", 

            "There is no contradiction ;", 

            " the latter referring to [a brew] with wine, the other to [a brew] with beer.", 

            " Rab Ashe said : ", 

            "Now that thou maintainest that one who does not expectorate after drinking it will be smitten [with illness], the spittle should be emitted even in the presence of a king[1]. ", 

            "R. Ishmael b. Elisha[2] said : Three things Suriel[3], the Prince of the Presence, related to me: ", 

            "Do not take thy shirt in the morning from the hand of the attendant and put it on[4]; ", 

            "do not let thy hands be washed by one who has not washed his own ; ", 

            "and do not return the cup of asparagus-beverage except to him who handed it to thee, because a band of demons", 

            " (another version : a company of angels of destruction) lies in wait for a man, saying, ", 

            "\"When will he commit one of these acts and be trapped ?\" ", 

            "R. Joshua b. Levi said : Three[5] things did the Angel of Death tell me : ", 

            "Do not take thy shirt in the morning from the hand of the attendant and put it on ; ", 

            "do not let thy hands be washed by him who has not washed his own[6]; ", 

            "and do not stand before women when they return from being with a dead person, because I leap and go before them with my sword in my hand[7], and I have permission to destroy. ", 

            "But if one met [such women], what is the remedy?", 

            " Let him move four cubits from his place ; or if there is a river let him cross it; or if there is another road let him proceed along it ; or if there is a wall let him stand behind it[8] ; but if not, let him turn his face away and say, \"And the Lord said unto Satan, The Lord rebuke thee, O Satan\" (Zech. iii. 2) until they have passed him by. ", 

            "R. Zera said in the name of R. Abbahu (another version: it was taught in a Baraita) : Ten things are said with reference to the cup used for the Grace after meals :", 

            " It requires washing and rinsing, undiluted [wine] and must be full, crowning and covering[1] ; he takes it with both hands and places it in the right hand, raises it a handbreadth from the floor[2] and gazes at it. ", 

            "Some also say :", 

            " He sends it as a present to his household[3], ", 

            "R. Johanan said : We only observe four of those rules :", 

            " washing, rinsing, undiluted [wine] and [the cup] must be full.", 

            " It has been taught: ", 

            "Washing refers to the inside [of the cup], rinsing to the outside. ", 

            "R. Johanan said : Whoever says the benediction over a full cup will be granted a boundless inheritance; as it is said, \"And full with the blessing of the Lord ; possess thou the sea and the south\" (Deut. xxxiii. 23).", 

            " R. Jose b. R. Hannina said: ", 

            "He will be worthy to inherit two worlds, this world and the world to come. ", 

            "\"Crowning\" — Rab Judah used to crown it with disciples[4]. Rab Hisda used to crown it with small cups[5]. ", 

            "R. Hanan said :", 

            " And with undiluted [wine][6]. ", 

            "Rab Sheshet said : ", 

            "Until the benediction of \"the land[7].\"", 

            " \"Covering\" [the head] — Rab Pappa used to wrap himself [in his Tallit], sit down [and say the Grace][8]. Rab Assi[9] used to spread a cloth over his head.", 

            " \"He takes it with both hands\" — R. Hinnana b. Pappa said : ", 

            "What is the Scriptural authority? \"Lift up your hands in holiness[10], and bless ye the Lord\" (Ps. cxxxiv. 2). ", 

            "\"And he places it in his right\" — ", 

            "R. Hiyya b. Abba said in the name of R. Johanan : The earlier [Rabbis] asked : ", 

            "May the left hand support the right?", 

            " Rab Ashe said :", 

            " Since the earlier [Rabbis] raised this question without having it decided,  "

        ], 

        [

            "we must act according to the stricter view[1].", 

            " \"He raises it a hand- breadth from the floor\" — R. Aha b. R. Hannina said[2]: ", 

            "What is the Scriptural authority ? \"I will lift up the cup of salvation and call upon the name of the Lord\" (Ps. cxvi. 13). ", 

            "\"He gazes at it\" — so that his thoughts may not wander.", 

            " \"He sends it as a present to his household\" — so that his wife may be blessed. ", 

            "'Ulla visited the house of Rab Nahman; he wrapped the bread[3] and said Grace and gave the cup of benediction to Rab Nahman.", 

            " Rab Nahman said to him, ", 

            "\"Let the master send the cup of benediction to Jalta[4].\"", 

            " He replied, \"Thus spake R. Johanan:", 

            " The fruit of a woman's body is only blessed through the fruit of a man's body[5]; as it is said, 'He will also bless the fruit of thy body' (Deut. vii. 13) — it is not said 'the fruit of her body' but 'the fruit of thy body'.\"", 

            " There is a teaching to the same effect : R. Nathan says : ", 

            "Whence is it that the fruit of a woman's body is only blessed through the fruit of a man's body? As it is said,", 

            " \"He will also bless the fruit of thy body\" — it is not said \"the fruit of her body\" but \"the fruit of thy body.\"", 

            " Meanwhile Jalta heard [that the cup of benediction had not been sent to her]. She arose in anger, went to the wine-cellar and broke four hundred flasks of wine.", 

            " Rab Nahman said to him,", 

            " \"Let the master send her another cup.\" 'Ulla sent it to her [with the message], ", 

            "\"All this measure of wine belongs to the benediction[6].\" ", 

            "She sent back the reply, ", 

            "\"From pedlars comes gossip, from rags come vermin[7].\" ", 

            "Rab Assi[8] said :", 

            " One must not speak over the cup of benediction. ", 

            "Rab Assi[8] also said : We may not say the benediction over a cup of ill-luck[9]. ", 

            "What means \"a cup of ill-luck\"? ", 

            "Rab Nahman b. Isaac said :", 

            " A second cup[1].", 

            " There is a teaching to the same effect :", 

            " He who drinks [cups of wine] of an even number should not say Grace ; because it is said, ", 

            "\"Prepare to meet thy God, O Israel\" (Amos iv. 12)[2]; but such an one is not fitly prepared. ", 

            "R. Abbahu said (another version : it was taught in a Baraita) :", 

            " He who eats while walking should say Grace standing ; but he who eats standing should sit to say Grace ; and when he reclines at the meal, he should sit up to say Grace.", 

            " The Halakah in every case is :", 

            " He sits and says Grace. ", 

            "May we return unto thee : Three who ate ! ", 

            "MISHNAH  The following are the points of variance between Bet Shammai and Bet Hillel in connection with the meal[1]. ", 

            "Bet Shammai say : [On a Sabbath or Festival] one pronunces the benediction over the day and then over the wine ; but Bet Hillel say : ", 

            "He pronounces the benediction over the wine and afterwards over the day. ", 

            "Bet Shammai say : ", 

            "We wash the hands and then fill[2] the cup ; but Bet Hillel say:", 

            " We fill the cup and then wash the hands. ", 

            "Bet Shammai say : ", 

            "One wipes his hands with a napkin which he lays upon the table ; but Bet Hillel say : ", 

            "[He lays it] upon the bolster [of his couch]. ", 

            "Bet Shammai say:", 

            " [After the meal] they clear up[3] and then we wash the hands [prior to Grace] ; ", 

            "but Bet Hillel say :", 

            " We wash the hands and then they clear up. ", 

            "Bet Shammai say :", 

            " [The order of benedictions is[4]] light, food, spices and Habdalah[5]; but Bet Hillel say :", 

            " Light, spices, food and Habdalah. ", 

            "Bet Shammai say : ", 

            "The wording[6] is \"...Who created the light of fire\" ; but Bet Hillel say : It is", 

            " \"...Who createst the lights of the fire.\" ", 

            "We may not say the benediction over the light or spices of gentiles, over the light or spices of the dead[7], nor over the light or spices of idolatry.", 

            " Nor do we say the benediction over the light until one can make use of its illumination. ", 

            "If one ate and forgot to say Grace, Bet Shammai declare ", 

            "he should return to his place and say it ; but Bet Hillel declare he may say it ", 

            "wherever [the omission] is remembered by him.", 

            " And what length of time may elapse in which he can say Grace? ", 

            "A Sufficient time for the food in the stomach to be digested. ", 

            "If wine is brought to them after the food and there is [only sufficient for] one cup, Bet Shammai declare ", 

            "he says the benediction over the wine and then over the food ; but Bet Hillel declare ", 

            "he says the benediction over the food and then over the wine.", 

            " One may make the response \"Amen\" after an Israelite who pronounces a benediction[1], but not after a Samaritan who pronounces a benediction until he has heard the whole of the benediction. ", 

            "GEMARA Our Rabbis have taught : The points of variance between Bet Shammai and Bet Hillel in connection with the meal are :", 

            " Bet Shammai say : [On a Sabbath or Festival] one pronounces the benediction over the day and then over the wine, because the day causes the wine to be brought[2] and because he has already hallowed the day[3] before the wine was brought.", 

            " But Bet Hillel say : ", 

            "One pronounces the benediction over the wine and then over the day, because the wine causes the Sanctification to be said[4].", 

            " Another reason is : ", 

            "The benediction over the wine is constant but that over the day is not constant, ", 

            "and when we have that which is constant and not constant, the former takes precedence[5]. ", 

            "The Halakah is in agreement with Bet Hillel. ", 

            "Why is this other reason necessary ? ", 

            "Shouldest thou say that there [Bet Shammai offer] two reasons but here [Bet Hillel offer] only one, therefore here also we have two reasons. ", 

            "\"The benediction over the wine is constant but that over the day is not constant, and when we have that which is constant and not constant, the former takes precedence. ", 

            "The Halakah is in agreement with Bet Hillel.\" All this is obvious, ", 

            "for a Bat Kol had issued forth[6]!", 

            " If thou wilt I can say [that this controversy]", 

            " preceded the Bat Kol[7] ; or if thou wilt I can say", 

            " it followed after the Bat Kol,  "

        ], 

        [

            "but R. Joshua it was who said : ", 

            "We pay no attention to a Bat Kol[8]. ", 

            "Do Bet Shammai, however, hold that the benediction over the day is of greater importance[1]?", 

            " Lo, there is a teaching: ", 

            "On entering his house at the conclusion of the Sabbath, he says the benediction over the wine, the light and the spices and after that says the Habdalah ; and should he have only one cup [of wine], he leaves it until after the meal and combines all [the benedictions] afterwards[2]. ", 

            "But how is it shown that this teaching emanates from Bet Shammai ; perhaps it is from Bet Hillel ?", 

            " That cannot enter thy mind ; because it states \"light and afterwards spices,\" and from whom hast thou heard that opinion? Bet Shammai;", 

            " for there is a teaching : R. Judah said :", 

            " Bet Shammai and Bet Hillel do not differ that the benediction over food comes first and Habdalah afterwards ; in what do they differ ? ", 

            "About light and spices — Bet Shammai declare :", 

            " Light and afterwards spices, whereas Bet Hillel declare : ", 

            "Spices and afterwards light. ", 

            "But how is it shown that this teaching emanates from Bet Shammai as interpreted by R. Judah ; perhaps it is from Bet Hillel as interpreted by R. Meir[3]?", 

            " That cannot enter thy mind[4]; for it states here in our Mishnah: ", 

            "Bet Shammai say : [The order of benedictions is] light, food, spices and Habdalah ; but Bet Hillel say : ", 

            "Light, spices, food and Habdalah ;", 

            " and there in the Baraita it states :", 

            " \"Should he have only one cup [of wine], he leaves it until after the meal and combines all [the benedictions] afterwards[5].\" Conclude therefore that it emanates from Bet Shammai as interpreted by R. Judah. ", 

            "Nevertheless there is a difficulty[6] ! ", 

            "Bet Shammai hold", 

            " that the advent of a [holy] day is different from its conclusion ; for with its advent the more we anticipate it the better[1] ; but with its conclusion the later we defer it the better[2], so that it may not seem to us a burden. ", 

            "Do Bet Shammai hold that the Grace after meals requires a cup of wine ? ", 

            "For our Mishnah teaches :", 

            " If wine is brought to them after the food and there is only sufficient for one cup, Bet Shammai declare : ", 

            "He says the benediction over the wine and then over the food[3].", 

            " Is it not to be supposed that he says the benediction [over the wine] and then drinks it ?", 

            " No ; he says the benediction and leaves it [undrunk for the Grace].", 

            " But the teacher has said : ", 

            "He who says a benediction must taste !", 

            " He does taste [but leaves the greater part].", 

            " But the teacher has said :", 

            " If he tasted it, he disqualifies it [for another benediction] ! ", 

            "He tastes it with his hand[4]. ", 

            "But the master has said : ", 

            "The cup of benediction requires a measure [of a fourth of a Log] ; and lo, he made it less than that measure ! He originally had more than the required measure. ", 

            "But it states: \"There is only sufficient for one cup\"!", 

            " There was not sufficient for two cups, but more than enough for one.", 

            " But R. Hiyya has taught : Bet Shammai declare : ", 

            "He says the benediction over the wine and drinks it, and after that says Grace ! ", 

            "Nay,", 

            " there are two Tannaim who differ as to the teaching of Bet Shammai[5]. ", 

            "Bet Shammai say : We wash the hands and then fill the cup, etc. ", 

            "Our Rabbis have taught : Bet Shammai say : ", 

            "We wash the hands and then fill the cup ; for if thou sayest that we till the cup first, there is a fear lest the liquid which is on the outside of the cup may contract defilement on account of his hands and in its turn defile the cup[6]. ", 

            "But the hands can defile the cup[7] ! ", 

            "The hands are [only unclean in] the second degree[1], and [anything unclean in] the second degree cannot make a third [unclean grade] with things non-holy except through the medium of a liquid. ", 

            "But Bet Hillel declare :", 

            " We fill the cup and then wash the hands ; for if thou sayest that we wash the hands first, there is a fear lest the moisture on the hands may contract defilement on account of the cup [which might be ritually unclean] and in its turn defile the hands. But the cup can defile the hands[2]! ", 

            "A vessel[3] cannot make a man contract defilement. ", 

            "But it can defile the liquid which it contains !", 

            " We are dealing here with a vessel whose exterior has been defiled by liquid,", 

            " that is to say whose interior is ritually clean but the exterior unclean ; ", 

            "for there is a Mishnaic teaching :", 

            " If a vessel's exterior has been defiled by liquid, the exterior is unclean "

        ], 

        [

            "but the interior, edge, brim and handle are clean. If, however, the interior is defiled, then the whole of it becomes unclean. ", 

            "What is the point of difference between them ? ", 

            "Bet Shammai hold that", 

            " it is forbidden to use a vessel whose exterior has become defiled by liquid for fear of the spillings[4], but there is no need to fear lest the moisture of the hand will contract defilement through the cup. ", 

            "Bet Hillel, on the other hand, hold that ", 

            "it is permitted to use a cup whose exterior has become defiled by a liquid, saying that ", 

            "spillings are not frequent ; but there is reason to fear lest the moisture on the hand contract defilement on account of the cup. ", 

            "Another reason is that ", 

            "the meal follows immediately on the washing of the hands. ", 

            "Why this other reason? ", 

            "Thus said Bet Hillel to Bet Shammai : ", 

            "According to you who maintain that it is forbidden to use a cup whose exterior has been defiled because of the fear of spillings, even so it is better [to wash the hands last] because the meal follows immediately on the washing of the hands[5]. ", 

            "Bet Shammai say : One wipes his hands, etc. ", 

            "Our Rabbis have taught : Bet Shammai say : ", 

            "One wipes his hands with a napkin which he lays upon the table ; for if thou sayest that [he lays it] upon the bolster, there is a fear lest the moisture on the napkin may contract defilement on account of the bolster and this in turn may render the hands ritually unclean[6]. ", 

            "But the bolster can defile the napkin ! ", 

            "One vessel cannot cause another vessel to contract defilement. ", 

            "But the bolster can make the man unclean! ", 

            "A vessel[1] cannot cause a man to contract defilement. ", 

            "But Bet Hillel say : ", 

            "[He lays it] upon the bolster ; for if thou sayest that [he lays it] upon the table, there is a fear lest the moisture on the napkin may contract defilement on account of the table and in its turn defile the food. ", 

            "But the table can defile the food which is upon it ! ", 

            "We deal here with a table [unclean] in the second degree[2], and [anything unclean in] the second degree cannot make a third [unclean grade] with things non-holy except through the medium of a liquid. ", 

            "What is the point of difference between them? ", 

            "Bet Shammai hold that", 

            " it is forbidden to use a table [unclean in] the second degree through fear of those who are eating Terumah[3];", 

            " but Bet Hillel hold that", 

            " it is permitted to use a table unclean in the second degree, because those who eat Terumah are careful[4]. ", 

            "Another reason is :", 

            " The washing of the hands for non-holy food is not ordained by the Torah.", 

            " Why this other reason ? ", 

            "Thus said Bet Hillel to Bet Shammai : ", 

            "Should you ask what difference is there that in the case of food we are concerned [about defilement][5] but in the case of the hands we have no concern ? Even so [our view] is better because the washing of the hands for non-holy food[6] is not ordained by the Torah ; ", 

            "therefore it is preferable that the hands should be defiled, since that has no basis in the Torah, rather than food should be defiled, for which there is a basis in the Torah. ", 

            "Bet Shammai say : [After the meal] they clear up, etc. ", 

            "Our Rabbis have taught : Bet Shammai say : ", 

            "They clear up and then we wash the hands [before Grace] ; for if thou sayest that we wash the hands first, the consequence may be that thou wilt spoil some food[7].", 

            " (Bet Shammai do not hold that the washing of the hands comes first. What is the reason? On account of the pieces of breads[8].)", 

            " But Bet Hillel say :", 

            " If the attendant is a disciple of the wise, he takes those pieces of bread which are of the size of an olive and leaves the pieces which are less than that size[1].", 

            " This supports the statement of R. Johanan who said : ", 

            "Pieces of bread which are less than the size of an olive may be destroyed by the hand. ", 

            "What is the point of difference between them ? ", 

            "Bet Hillel hold that it is forbidden to employ as an attendant one who is an 'Am ha'ares[2], ", 

            "whereas Bet Shammai hold that ", 

            "such may be employed. ", 

            "R. Isaac[3] b. R. Hannina said in the name of Rab Huna:", 

            " Throughout our Chapter, the Halakah is in agreement with Bet Hillel except in this point where it is in agreement with Bet Shammai. ", 

            "R. Osha'ya, however, teaches the reverse, that here also the Halakah is in agreement with Bet Hillel. ", 

            "Bet Shammai say: [The order of benedictions is] light, food, etc. ", 

            "Rab Huna b. Judah[4] visited the house of Raba[5] and noticed that he said the benediction over the spices first. ", 

            "He said to him :", 

            " Note that Bet Shammai and Bet Hillel do not differ on the question of the light ; ", 

            "for our Mishnah teaches : Bet Shammai say : ", 

            "[The order is] light, food, spices and Habdalah ; ", 

            "but Bet Hillel say :", 

            " Light, spices, food and Habdalah[6]! ", 

            "Raba answered after him[7]:", 

            " These are the words of R. Meir; but R. Judah says: ", 

            "Bet Shammai and Bet Hillel do not differ that [the benediction over] food comes first and Habdalah last.", 

            " In what do they differ ? In [the order of] light and spices ; for Bet Shammai say : ", 

            "First [the benediction] over the light and then the spices, but Bet Hillel say : First over the spices and then the light.", 

            " And R. Johanan said :", 

            " People act in agreement with the view of Bet Hillel as interpreted by R. Judah[8]. ", 

            "Bet Shammai say : The wording is \"...Who created [bara'] the light [me'or] of fire\" etc. ", 

            "Raba said : ", 

            "Everybody agrees about bara' that it means \"he created.\" In what do they differ? About the word bore'[1] ; Bet Shammai hold that", 

            " bore' means \"he will create[2],\"", 

            " but Bet Hillel hold that", 

            " bore' has also the same meaning as bara'. ", 

            "Rab Joseph quoted in objection[3] :", 

            " \"I form the light and create [bore'] darkness\" (Is. xlv. 7); \"He formeth the mountains and createth [bore'] the wind\" (Amos iv. 13); \"He that created [bore'] the heavens and stretched them forth\" (Is. xlii. 5)! ", 

            "But, said Rab Joseph,", 

            "everybody agrees that bara' and bore' mean \"he created.\" Wherein do they differ? About meor and meore [\"light\" and \"lights\"]", 

            " for Bet Shammai hold ", 

            "there is only one light in fire, but Bet Hillel hold ", 

            "there are many[4]. ", 

            "There is a teaching to the same effect : Bet Hillel said to Bet Shammai :", 

            " There are many lights in fire. ", 

            "We may not say the benediction over the light or spices of gentiles. ", 

            "It is quite right [that we do not use] the light [of a gentile] because it has not \"rested[5]\" ; but why not the spices ? ", 

            "Rab Judah said in the name of Rab : ", 

            "We are here dealing with [spices used] at the banquet of gentiles[6], because the assumption is that the banquet of gentiles is dedicated to idolatry. ", 

            "But since he teaches in the sequel : ", 

            "We may not say the benediction over the light or spices of idolatry,", 

            " it is to be inferred that in the first part of the statement we are not dealing with idolatry[7] ! ", 

            "R. Hannina of Sura[8] said : ", 

            "[In the sequel] he merely states the reason : What is the reason that we do not say a benediction over the light or spices of the gentiles ? Because the assumption is the banquet of gentiles is dedicated to idolatry. ", 

            "Our Rabbis have taught : ", 

            "We say a benediction over the light which rested but not if it has not rested. ", 

            "What means \"rested\" and \"not rested\"?  "

        ], 

        [

            "If we would say that it has not rested because of work [which has been done on the Sabbath by its illumination], even if it be work which is permitted[1], there is a teaching : ", 

            "We may say the benediction over the light used [on the Sabbath] by a woman in confinement or an invalid ! ", 

            "Rab Nahman b. Isaac[2] said : ", 

            "What means \"rested\"? It rested from work which is a transgression [on the Sabbath].", 

            " There is a teaching to the same effect : ", 

            "We may at the conclusion of the Sabbath say the benediction over [the light of] a lantern which has been burning the whole day[3]. ", 

            "Our Rabbis have taught :", 

            " We may make the benediction over a light kindled by a gentile from an Israelite or kindled by an Israelite from a gentile, but not over a light kindled by a gentile from a gentile. Why is [the light kindled] by a gentile from a gentile different that one may not [say the benediction over it] ?", 

            " Because it has not \"rested.\" If so, the light kindled by an Israelite from a gentile may likewise not have \"rested\" !", 

            " And shouldest thou say that the light which is prohibited ceases to exist[4] whereas the other is quite a different one and came into being in the hand of the Israelite, there is the teaching :", 

            " Who causes a flame to issue into the public way [on the Sabbath][5] has incurred guilt ; but why has he incurred guilt ?", 

            "What he has taken up he has not set down, and what he has set down he has not taken up[6]! ", 

            "There is", 

            " certainly also a prohibition [about the light kindled by an Israelite from a gentile][7], but when he says the benediction he does so over the additional part which is permitted[8].", 

            " If so, a light kindled by a gentile from a gentile should also be allowed !", 

            " Really that is so ; but there is a fear because of the first gentile[1] and the first torch[2]. ", 

            "Our Rabbis have taught :", 

            " Were one walking [at the conclusion of the Sabbath] outside the town and saw a light, if the majority [of the inhabitants] are gentiles, he should not say the benediction [over that light], but if the majority are Israelites, he may say it.", 

            " This is self-contradictory ! ", 

            "Thou sayest,", 

            " \"If the majority are gentiles, he should not say the benediction,\" hence if they are half [gentiles] and half [Israelites] he may say it. ", 

            "Then it continues,", 

            " \"If the majority are Israelites, he may say it,\" hence if they are half and half, he may not say it ! ", 

            "It is quite right that even if they are half and half, he should also say the benediction ; but since he taught the first clause \"If the majority are gentiles,\" he also adds \"If the majority are Israelites[3].\" ", 

            "Our Rabbis have taught :", 

            "Were one walking [at the conclusion of the Sabbath] outside the town and saw a child holding a torch, he makes inquiries ; if the child is an Israelite, he says the benediction [over the lighted torch], but if a gentile, he does not. ", 

            "Why is a child specified? It is the same even with an adult!", 

            " Rab Judah said in the name of Rab[4]:", 

            " We are here dealing with a point of time near to the setting of the sun[5]; so if it were an adult, it is obvious that he must certainly be a gentile[6]. But in the case of a child, one might say it is an Israelite and it is by chance that he is holding [the torch]. ", 

            "Our Rabbis have taught : ", 

            "Were one walking [at the conclusion of the Sabbath] outside the town and saw a light, if it is as thick as the opening of a furnace he says the benediction over it[7], but if it is not, he does not say the benediction over it.", 

            " One taught: ", 

            "We do say the benediction over the light of a furnace; but there is another teaching : ", 

            "We do not say the benediction over it ! ", 

            "There is no contradiction ;", 

            " because the latter refers to the beginning [of its kindling], the other subsequently[8].", 

            " One taught :", 

            " We do say the benediction over the light of an oven or stove ; but there is another teaching: ", 

            "We do not say the benediction over it!", 

            " There is no contradiction ; ", 

            "because the latter refers to the beginning [of its kindling], the other subsequently. ", 

            "One taught : ", 

            "We do say the benediction over the light of a Synagogue or House of Study ; but there is another teaching :", 

            " We do not say the benediction over it ! ", 

            "There is no contradiction ;", 

            " the latter referring to a case where there is a distinguished person[1] present, the other to a case where there is no distinguished person present. ", 

            "But if thou wilt I can say that ", 

            "both refer to where a distinguished person is present, and still there is no contradiction ;", 

            " the one referring to where there is a beadle[2], the other to where there is no beadle. Or if thou wilt I can say that", 

            " both refer to where there is a beadle, and still there is no contradiction ;", 

            " the one referring to where there is moonlight[3] and the other to where there is no moonlight. ", 

            "Our Rabbis have taught :", 

            " If they were sitting in the House of Study [at the conclusion of the Sabbath] and light is brought to them,", 

            " Bet Shammai declare that ", 

            "each one says the benediction for himself ; ", 

            "but Bet Hillel declare that", 

            " one says the benediction for all, because it is said, ", 

            "\"In the multitude of people is the King's glory\" (Prov. xiv. 28)[4].", 

            " It is quite right that Bet Hillel explain the reason [for their view] ; but what is the reason of Bet Shammai ? ", 

            "They hold that", 

            " it will cause an interruption in the House of Study[5].", 

            " There is a teaching to the same effect : ", 

            "Those who belonged to the school of Rabban Gamaliel used not to exclaim Marpe'[6] in the House of Study because of the interruption it causes. ", 

            "We may not say the benediction over the light or spices of the dead. ", 

            "What is the reason ? ", 

            "The light which is kindled [for the dead] is in its honour[1] and the spices are used to remove the odour[2]. ", 

            "Rab Judah said in the name of Rab[3]: ", 

            "Over a light which they carry before [the corpse] by day or by night[4] no benediction is to be made[5] ; but we may say it over a light which is only carried before it at night[6]. ", 

            "Rab Huna said :", 

            " We may not say the benediction over spices used in a privy[7] or the oil which is used to remove the dirt[8]. ", 

            "That is to say that the benediction [for spices] is not to be pronounced over anything which is not used for the purpose of smelling. Against this is quoted :", 

            " If one enters a perfumer's shop and smells the odour, even though he sit there all day he only pronounces the benediction once ; but if he keeps going in and out, he pronounces it each time. ", 

            "But here [the perfume] was not for smelling[9] and still he says the benediction ! ", 

            "Yes, it is there for smelling, so that people should smell it and come to buy. ", 

            "Our Rabbis have taught : ", 

            "Were one walking outside the town and smelt a fragrant odour, if the majority [of the inhabitants] are gentiles, he must not pronounce a benediction ; but if the majority are Israelites, he does. ", 

            "R. Jose said : ", 

            "Even if the majority are Israelites he must likewise not pronounce a benediction, because the daughters of Israel use incense for purposes of sorcery[10]. ", 

            "But do all of them burn incense for sorcery ? ", 

            "Some for sorcery and some also to perfume their garments ; hence it will be found that the majority [in the town] do not use it for smelling, and where the majority do not use it for smelling, the benediction is not to be pronounced. ", 

            "R. Hiyya b. Abba said in the name of R. Johanan : ", 

            "He who walks on the Sabbath-eve in Tiberias[1] and at the conclusion of the Sabbath in Sepphoris[2] and smells a fragrant odour should not pronounce the benediction because the presumption is that it is only being used to perfume garments. ", 

            "Our Rabbis have taught :", 

            " If one were walking in a street where idolatry [is practised] and takes pleasure in smelling the odour [of incense] he is a sinner.  "

        ], 

        [

            "Nor do we say the benediction over the light until one can make use of its illumination. ", 

            "Rab Judah said in the name of Rab : ", 

            "The phrase \"until one can make use of its illumination\" does not mean that one must actually use it, but ", 

            "if one who stands near to it can use its light, then even those who are at a distance [may say the benediction]. ", 

            "Similarly said Rab Ashe[3] :", 

            " We have learnt that one at a distance [may say the benediction]. ", 

            "Against this is quoted :", 

            " If he had a light hidden in his bosom or in a lantern or saw a flame but made no use of its light or used its light without seeing its flame, he must not say the benediction until he sees the flame and makes use of its light !", 

            " It is quite right that one uses the light without seeing the flame, for it may happen to stand in a corner ; but how is it possible to see the flame without using its light? Is it not when it is far off? ", 

            "No, it refers to when it keeps growing dimmer. ", 

            "Our Rabbis have taught : ", 

            "We may say the benediction over glowing coals, but not over dying coals[4]. ", 

            "What is to be understood by glowing coals? ", 

            "Rab Hisda said :", 

            " When one puts a chip of wood to them and it ignites. ", 

            "The question was asked :", 

            " Is the word for dying coals spelt 'omemot or 'omemot[5]? ", 

            "Come and hear : For Rab Hisda[6] b. Abdemi quoted,", 

            " \"The cedars in the garden of God could not darken ['amam] it\" (Ezek. xxxi. 8)[7]. ", 

            "Raba said :", 

            "[The statement of the Mishnah means] one must actually use the illumination[8].", 

            " And how [near must he be to the light] ?", 

            " 'Ulla said[9] : ", 

            "Sufficient for one to be able to distinguish between an as and a dupondium[1].", 

            " Hezekiah said : ", 

            "Sufficient for one to be able to distinguish between the stamp[2] of a Tiberian coin and a Sepphorian coin. ", 

            "Rab Judah said the benediction over the light in the house of Ada the waiter[3].", 

            " Raba[4] said it over the light in the house of Guria[5] b. Hamma. ", 

            "Abbai said it over the light in the house of Bar Abbuha[6]. ", 

            "Rab Judah said in the name of Rab : ", 

            "One does not go looking for a light[7] as we do for other commandments. ", 

            "R. Zera said :", 

            " At first I used to go about [searching for a light] but since I heard the statement of Rab Judah in the name of Rab, I also do not go searching for it ; but should it chance to me of its own accord, I say the benediction[8]. ", 

            "If one ate and forgot to say Grace, etc. ", 

            "Rab Zebid[9] (another version : Rab Dimai b. Abba) said :", 

            " The dispute is only in the case of one who has forgotten ; but if he omitted it intentionally, all agree that he must return to his place and say Grace. ", 

            "This is obvious, because the Mishnah states \"and forgot\"! ", 

            "Thou mayest, however, argue that ", 

            "the same thing applies[10] to one who omitted it intentionally and the statement \"he forgot\" is only intended to show the extreme view of Bet Shammai ; therefore he informs us[11].", 

            "There is a teaching : Bet Hillel said to Bet Shammai : ", 

            "According to your words, he who ate at the top of the Temple Mount and forgot and descended without saying Grace must return to the top and say it!", 

            " Bet Shammai replied to Bet Hillel : ", 

            "According to your words, if one left a purse at the top of the Temple Mount, should he not go up to fetch it?", 

            " For his own purpose[1] he may go up ; how much more so for the honour of Heaven !", 

            " There were two disciples ; one acted in error according to the view of Bet Shammai[2] and found a purse of gold, and the other acted deliberately according to the view of Bet Hillel[3] and a lion devoured him. ", 

            "Rabbah b. Bar Hannah was journeying with a caravan ; he ate but forgot to say Grace.", 

            " He said [to himself],", 

            " \"How shall I act ?", 

            " If I tell them I have forgotten to say Grace, they will answer, ", 

            "'Say it now ; for wherever thou utterest a benediction it is to the All-merciful thou dost utter it.'", 

            " It is better that I tell them I have lost a golden dove.\" ", 

            "He said to them, ", 

            "\"Wait for me, because I have lost a golden dove.\"", 

            " He went back, said Grace and found a golden dove. Why exactly a dove ? Because the Community of Israel is likened to a dove ; for it is written,", 

            " \"The wings of the dove are covered with silver, and her pinions with the shimmer of gold\" (Ps. Ixviii. 14). Just as a dove only escapes with the aid of its wings, so Israel is only delivered through the aid of the commandments. ", 

            "And what length of time may elapse, etc. ", 

            "What is the length of time for food to be digested ?", 

            " R. Johanan said :", 

            " As long as he is not hungry.", 

            "R. Simeon b. Lakish said : ", 

            "As long as he is thirsty on account of the food he has eaten. ", 

            "Rab Jemar b. Shelamya said to Mar Zotra (another version : Rab Jemar b. Shezbi to Mar Zotra) :", 

            " Did R. Simeon b. Lakish say that?", 

            " For lo, R. Ammi declared in the name of R. Simeon b. Lakish : ", 

            "What is the length of time for food to be digested ? Sufficient time for a person to walk four Mil !", 

            " There is no contradiction, ", 

            "one referring to a heavy meal, the other to a light meal[4]. ", 

            "If wine is brought to them, etc. ", 

            "That is to say an Israelite may respond although he has not heard the whole of the benediction. But since he has not heard it, how can he fulfil his obligation[5]? ", 

            "Hiyya b. Rab[6] said: ", 

            "refers to a man] who has not eaten with them[1].", 

            " Similarly said Rab Nahman in the name of[2] Rabbah b. Abbuha :", 

            " It refers to a man who has eaten with them. ", 

            "Rab[3] said to his son Hiyya,", 

            " \"My son, snatch [the cup of wine] and say Grace[4]\" ;", 

            " and similarly said Rab Huna to his son Rabbah[5],", 

            " \"Snatch [the cup of wine] and say Grace.\" ", 

            "That is to say, he who says Grace is superior to him who just responds \"Amen\"[6] ; but lo, there is a teaching : R. Jose says :", 

            " Greater is he who responds \"Amen\" than he who says Grace! ", 

            "R. Nehorai[7] said to him : ", 

            "By Heaven it is so. ", 

            "Thou canst prove it ;", 

            " for behold the common soldiers go down to open the fight but the veterans go down to win the victory[8].", 

            " This matter is discussed by the Tannaim; for there is a teaching : ", 

            "Both he who says the benediction and he who responds \"Amen\" are implied[9], only he who says the benediction is more quickly [rewarded] than he who responds \"Amen.\" ", 

            "Samuel asked Rab :", 

            " Should one respond \"Amen\" after the children in school[10]?", 

            " He replied : ", 

            "We make the response \"Amen\" after everybody except school-children, because they only utter [the benediction] for the purpose of learning it. ", 

            "This rule applies when it is not the time that they read the Haftarah ; but should it be the time when they read the Haftarah, one does make the response. ", 

            "Our Rabbis have taught : ", 

            "The oil prevents the Grace [from beign said][11] — these are the words of R.[12]Zilai ; ", 

            "but R. Ziwai says ;", 

            " It does not prevent it. ", 

            "R. Aha says :", 

            " Good oil prevents it. ", 

            "R. Zohamai says : ", 

            "Just as one who is dirty is unfit for the Temple-service, so are dirty hands unfit for the Grace.", 

            " Rab Nahman b. Isaac said :", 

            "I know neither Zilai nor Ziwai nor Zohamai ; but I know the following teaching :", 

            " Rab Judah said in the name of Rab (another version : it is taught in a Baraita) :", 

            " \"Sanctify yourselves\" (Lev. xi. 44) — i.e. the washing before the meal[1] ; \"and be ye holy\" (ibid.) — i.e. the washing after the meal ; \"for holy\" (ibid.) — i.e. the oil ; \"I am the Lord your God[2]\" — i.e. the Grace. ", 

            "May we return unto thee : The following are the points of variance ! "

        ], 

        [

            "He who beholds a place where miracles have been wrought for Israel says,", 

            " \"Blessed [art Thou, O Lord our God, King of the Universe] Who wroughtest miracles for our fathers in this place.\" ", 

            "[He who beholds] a place from which idolatry has been uprooted says,", 

            " \"Blessed... Who hast uprooted idolatry from our land.\" ", 

            "For shooting stars, earthquakes, thunders, storms and lightnings he says,", 

            " \"Blessed...Whose strength and might fill the world.\"", 

            " For mountains, hills, seas, rivers and deserts he says, ", 

            "\"Blessed... Who hast made the creation.\" ", 

            "R. Judah states: ", 

            "He who beholds the ocean[1] says,", 

            " \"Blessed... Who hast made the ocean,\" but only when he beholds it at intervals.", 

            " For rain and good tidings he says, ", 

            "\"Blessed... Who art good and dispensest good.\"", 

            " For bad tidings he says, ", 

            "\"Blessed be the true Judge.\" ", 

            "He who has built a new house or bought new vessels says,", 

            " \"Blessed... Who hast kept us in life, hast preserved us and enabled us to reach this season,\"", 

            " One says the benediction for a calamity apart from any attendant good, and for good fortune apart from any attendant evil ;", 

            "but he who supplicates concerning that which is past utters a vain prayer. ", 

            "If his wife is pregnant and he says,", 

            " \"May it be Thy will that my wife bear a son,\" behold that is a vain prayer.", 

            " If he were on the way, and hearing a cry of lamentation in the city, exclaims,", 

            " \"May it be Thy will that it be not within my house,\" behold that is a vain prayer. ", 

            "He who enters a town[2] should offer prayer twice, once on entering and once on leaving. ", 

            "Ben 'Azzai says : ", 

            "Four times, twice on entering and twice on leaving. He gives thanks for what is past and supplicates for what is yet to be. ", 

            "A man is in duty bound to utter a benediction for the bad even as he utters one for the good[3] ; as it is said,", 

            " \"And thou shalt love the Lord thy God with all thy heart, and with all thy soul, and with all thy might\" (Deut. vi. 5) —", 

            " \"with all thy heart,\" i.e. with thy two impulses, with the good and the evil impulse[1] ;", 

            " \"with all thy soul,\" i.e. even if He take thy soul; \"with all thy might,\" i.e. with all thy wealth. ", 

            "Another explanation of ", 

            "\"with all thy might [meodeka]\" — with whatever measure [middah] He metes out to thee, do Thou return Him thanks [modeh]. ", 

            "A man should not behave with levity towards the Eastern Gate [of the Temple], since it is directed towards the Holy of Holies. ", 

            "Nor may one enter the Temple Mount with his staff, his sandal, his wallet, and with the dust upon his feet ; nor may he use it as a short cut, ", 

            "and to expectorate [on the Temple Mount is forbidden] a fortiori. At the conclusion of every benediction in the Sanctuary they used to say", 

            " \"Forever[2]\" ;", 

            " but when the Minim[3] perverted the truth and declared that there is only one world, it was ordained that the wording should be ", 

            "\"From everlasting to everlasting[4].\"", 

            " It was further ordained that a man should greet his friends by mentioning the Divine Name[5] ; as it is said, ", 

            "\"And behold, Boaz came from Bethlehem, and said unto the reapers, ", 

            "The Lord be with you ; and they answered him. ", 

            "The Lord bless thee\" (Ruth ii. 4); ", 

            "and it is said,", 

            " \"The Lord is with thee, thou mighty man of valour\" (Judges vi. 12); ", 

            "and it is said, ", 

            "\"And despise not thy mother when she is old\" (Prov. xxiii. 22)[6];", 

            " and it is said, ", 

            "\"It is time for the Lord to work ; they have made void Thy law\" (Ps. cxix. 126). ", 

            "R. Nathan says : ", 

            "[This means,] They have made void Thy law, because it is time for the Lord to work. ", 

            "GEMARA Whence have we this[1]? ", 

            "R. Johanan said : Because the Scriptures state,", 

            " \"And Jethro said, Blessed be the Lord Who hath delivered you\" etc. (Exod. xviii. 10). ", 

            "Do we say a benediction for the miracle wrought on behalf of the many but not for the miracle wrought on behalf of an individual?", 

            " Lo, there was the man who was journeying by 'Eber Jamina[2] when a lion attacked him, and a miracle was wrought for him and he was rescued. ", 

            "He came before Raba who told him :", 

            " Whenever thou reachest that spot, say \"Blessed... Who hast wrought a miracle for me in this place.\" ", 

            "And Mar b. Rabina was passing through the valley of 'Arabot[3] and thirsted for water ; a miracle was wrought for him and a well was created and he drank. ", 

            "On another occasion, he was passing through the market-place of Mahoza[4] when a wild camel attacked him, and the wall was cleft for him and he went through it. ", 

            "Whenever he came to 'Arabot he said the benediction ", 

            "\"Blessed... Who hast wrought for me a miracle in 'Arabot and with the camel\" ; and whenever he came to the market-place of Mahoza he said,", 

            " \"Blessed... Who hast wrought for me a miracle with the camel and in 'Arabot.\" ", 

            "They answer[5] : ", 

            "In the case of a miracle wrought on behalf of the many, everybody is obliged to utter the benediction[6]; but in the case of a miracle wrought on behalf of an individual, only he[7] is obliged to say it. Our Rabbis have taught : ", 

            "He who beholds the fords of the [Red] Sea, or the fords of the Jordan, or the fords of the valleys of Arnon, or the hail-stones in the descent of Bet Horon[8], or the stone which Og, king of Bashan, sought to cast upon Israel[9], or the stone upon which Moses sat when Joshua fought against Amalek[1], or [the pillar of salt of] Lot's wife[2], or the wall of Jericho which was swallowed up in its place — over all these one must give thanks and praise before the All-present. ", 

            "It is quite right with the fords of the [Red] Sea ; for it is written,", 

            " \"And the children of Israel went into the midst of the Sea upon the dry ground\" (Exod. xiv. 22).", 

            " [It is quite right with] the fords of the Jordan; for it is written, ", 

            "\"And the priests that bare the ark of [the covenant of][3] the Lord stood firm on dry ground in the midst of the Jordan, while all Israel passed over on dry ground, until all the nation were passed clean over the Jordan\" (Josh. iii. 17). ", 

            "But the fords of the valleys of Arnon — whence is it [that a benediction is necessary]? ", 

            "For it is written,", 

            " \"Wherefore it is said in the book of the Wars of the Lord, Et and Heb in the rear[4] and the valleys of Arnon\" etc. (Num. xxi. 14). ", 

            "It has been taught :", 

            " \"Et and Heb in the rear\" were two lepers who journeyed in the rear of the camp. When the Israelites were to pass through [the valleys of Arnon], the Amorites came  "

        ], 

        [

            "and made caves for themselves in which they hid, saying, ", 

            "\"When the Israelites pass here we will kill them.\" But they knew not that the Ark was journeying before Israel and was lowering the rocks in front of them ;", 

            " so when the Ark reached [the spot where the Amorites were in hiding], the rocks clave together, killing them, and their blood descended into the valleys of Arnon. ", 

            "When Et and Heb came and saw blood issuing from between the rocks, they went and told the Israelites and uttered a song. That is what is written,", 

            " \"And he poured out the valleys that incline toward the seat of Ar and lean upon the border of Moab\" (ibid. v. 15)[5]. ", 

            "\"Hail-stones\" abne elgabish. What are abne elgabish ?", 

            " It has been taught : ", 

            "They are stones which remained suspended [in the air] for the sake of a man[6] and descended for the sake of a man.", 

            " They remained suspended for the sake of a man, viz.: Moses; for it is written, ", 

            "\"Now the man Moses was very meek\" (Num. xii. 3), and it is written,", 

            " \"And the thunders and hail ceased[1], and the rain poured not upon the earth\" (Exod. ix, 33). ", 

            "They descended for the sake of a man, viz. Joshua ; for it is written, ", 

            "\"Take thee Joshua the son of Nun, a man in whom is spirit\" (Num. xxvii. 18), and it is written, ", 

            "\"And it came to pass, as they fled from before[2] Israel, while they were at the descent of Beth-horon, that the Lord cast down great stones\" (Josh. x. 11). ", 

            "\"The stone which Og, king of Bashan, sought to cast upon Israel.\" A tradition has been handed down in this connection :", 

            " Og said,", 

            " \"What is the extent of Israel's camp ? Three Parsah. I will go and uproot a mountain of the size of three Parsah, and cast it upon them so that I will kill them.\" ", 

            "He went and uprooted a mountain of the size of three Parsah and carried it upon his head ; but the Holy One, blessed be He, sent ants which bored a hole through it so that it sank about his neck. ", 

            "As he sought to draw it off, his teeth were extended on both sides, so that it was impossible to extricate himself. That is what is written,", 

            " \"Thou hast broken the teeth of the wicked\" (Ps. iii. 8) ;", 

            " and it is in accord with the statement of R. Simeon b. Lakish who said:", 

            " What means that which is written, \"Thou hast broken the teeth of the wicked\"? Read not \"Thou hast broken\" [shibbarta] but \"Thou hast prolonged\" [shirbabta]. ", 

            "What was the height of Moses? Ten cubits[3]. He took an axe ten cubits long, jumped to a height of ten cubits and struck Og on his ankle[4] and killed him. ", 

            "\"The stone upon which Moses sat\"; for it is written, ", 

            "\"But Moses' hands were heavy ; and they took a stone, and put it under him, and he sat thereon\" (Exod. xvii. 12). [Had not Moses a cushion or bolster upon which to sit ? But thus spake Moses : Since Israel are now enduring hardship, I too will endure hardship with them[5].] ", 

            "\"Lot's wife\" ; as it is said,", 

            " \"But his wife looked back from behind him and she became a pillar of salt\" (Gen. xix. 26)[6].", 

            "[not translated]", 

            "[not translated]", 

            " It is quite right with all these miracles[1] ; but that of Lot's wife was a punishment[2] !", 

            " [On beholding it] one should say \"Blessed be the true Judge[3].\"", 

            " But it mentions above thanksgiving and praise !", 

            " It has been taught :", 

            " For Lot and his wife we say two benedictions — for his wife one says, ", 

            "\"Blessed be the true Judge\" ; and for Lot one says,", 

            " \"Blessed... Who rememberest the righteous.\" ", 

            "R. Johanan said : ", 

            "Even at the time of His wrath, the Holy One, blessed be He, remembers the righteous ; as it is said, ", 

            "\"And it came to pass, when God destroyed the cities of the Plain, that God remembered Abraham, and sent Lot out of the midst of the overthrow\" (Gen. xix. 29). ", 

            "\"And the wall of Jericho which was swallowed up.\" ", 

            "And the wall of Jericho which was swallowed up !", 

            " Lo, it fell !", 

            " As it is said,", 

            " \"And it came to pass when the people heard the sound of the horn, that the people shouted with a great shout, and the wall fell down flat\" (Josh. vi. 20).", 

            " Since its breadth and height were equal, it must in consequence have been swallowed up [in the earth][4]. ", 

            "Rab Judah said in the name of Rab[5] :", 

            " Four classes of people must offer thanksgiving : They who go down to the sea, who journey in the desert[6], the invalid who recovers and the prisoner who has been set free.", 

            " \"They who go down to the sea\" — whence have we this ? For it is written,", 

            " \"They that go down to the sea in ships... these saw the works of the Lord... ", 

            "He raised the stormy wind... They mounted up to the heaven, they went down to the deeps... ", 

            "They reeled to and fro, and staggered like a drunken man... ", 

            "They cried unto the Lord in their trouble, and He brought them out of their distresses. ", 

            "He made the storm a calm... ", 

            "Then were they glad because they were quiet...", 

            " Let them give thanks unto the Lord for His mercy, and for His wonderful works to the children of men\" (Ps. cvii. 23-31). ", 

            "\"They who journey in the desert\" — whence have we this ? For it is written,", 

            " \"They wandered in the wilderness in a desert way ; they found no city of habitation...Then they cried unto the Lord... and He led them by a straight way... Let them give thanks unto the Lord for His mercy\" (ibid. vv. 4-8). ", 

            "\"The invalid who recovers\" — whence have we this? For it is written, ", 

            "\"Crazed because of the way of their transgression, and afflicted because of their iniquities, their soul abhorred all manner of food... They cried unto the Lord in their trouble... He sent His word and healed them...Let them give thanks unto the Lord for His mercy\" (Ps. cvii. 17—21).", 

            " \"The prisoner who has been set free\" — whence have we this? ", 

            "For it is written, ", 

            "\"Such as sat in darkness and in the shadow of death... because they rebelled against the words of God...", 

            "Therefore He humbled their heart with travail...", 

            " They cried unto the Lord in their trouble... ", 

            "He brought them out of darkness and the shadow of death... ", 

            "Let them give thanks unto the Lord for His mercy\" (ibid. vv. 10-15). ", 

            "What benediction should he utter?", 

            " Rab Judah said,", 

            " \"Blessed ...Who bestowest lovingkindnesses[1].\" ", 

            "Abbai said :", 

            " It is necessary for him to offer his thanksgiving in the presence of ten ; for it is written,", 

            " \"Let them exalt Him in the assembly of the people\" etc. (ibid. V. 32). ", 

            "Mar Zotra said :", 

            " Two of them must be Rabbis ; as it is said,", 

            " \"And praise Him in the seat of the elders\" (ibid.).", 

            " Rab Ashe[2] retorted :", 

            " Say that they must all be Rabbis ! ", 

            "But is it written, \"In the assembly of elders\" ? ", 

            "No, it is written, \"In the assembly of the people.\" ", 

            "Then say[3]:", 

            " [He must offer thanksgiving] in the presence of ten ordinary persons and two Rabbis ! ", 

            "The question [remains unanswered]. ", 

            "Rab Judah was ill and recovered. Rab Hanna[4] of Bagdat[5] and other Rabbis went in to visit him. They said to him, ", 

            "\"Blessed be the All-merciful Who has given thee back to us and has not given thee to the dust.\" ", 

            "He said to them, ", 

            "\"You have exempted me from the obligation of thanksgiving.\" ", 

            "But lo, Abbai said :", 

            " He must offer thanksgiving in the presence of ten !", 

            " There were ten present. ", 

            "But it was not he who uttered thanksgiving !", 

            " It was not necessary, because he responded \"Amen\" after them. ", 

            "Rab Judah said : ", 

            "Three require guarding[6], viz. :", 

            " an invalid, a bridegroom and a bride. In a Baraita it is taught :", 

            " An invalid[7], woman in confinement, bridegroom and bride. ", 

            "Some say :", 

            " Also a mourner[8]; ", 

            "and others add: ", 

            "Also disciples of the wise at night[9]. ", 

            "Rab Judah also said : There are three things which, if one prolong, lengthen his days and years ; viz. ", 

            "Who prolongs his prayer, his stay at table and in the privy. ", 

            "\"Who prolongs his prayer\" — is that a virtue ? ", 

            "And lo, R. Hiyya b. Abba said in the name of R. Johanan :  "

        ], 

        [

            "Whoever prolongs his prayer and calculates on it will eventually come to pain of heart; as it is said, ", 

            "\"Hope deferred maketh the heart sick\" (Prov. xiii. 12)[1].", 

            " And R. Isaac said: ", 

            "Three things cause the sins of a man to be remembered ; viz. ", 

            "[passing under] a wall threatening to fall[2], calculating on prayer and surrendering one's case against a man to Heaven[3] ! ", 

            "There is no contradiction ; the latter refers to where one calculates [on the prolongation of his prayer], the other to where he does not calculate upon it.", 

            " So how should one act ? He makes many supplications. ", 

            "\"He who prolongs his stay at table\" — perhaps a poor man will come and he will give him [some food] ; for it is written, \"The altar of wood three cubits high... and he said unto me, This is the table that is before the Lord\" (Ezek. xli. 22). He opens with \"altar\" and concludes with \"table\"! ", 

            "R. Johanan and R. Eleazar both say : ", 

            "So long as the Temple was in existence, the altar used to atone for Israel, but now a man's table atones for him[4].", 

            " \"He who prolongs his stay in the privy\" — is that a virtue?", 

            " Lo, there is a teaching : Ten things cause a man piles[5] : ", 

            "Eating the leaves of reeds, the leaves of the vine, the sprouts of the vine, the palate[6] of an animal[7], the backbone of a fish, salted fish which has not been sufficiently cooked, to drink the lees of wine, to wipe oneself [after evacuation] with lime, potters' clay, or pebbles with which another has wiped himself ; and some add : ", 

            "Also unduly to strain oneself in the privy !", 

            " There is no contradiction ; the latter refers to one who stays and strains, the other to one who stays long but does not strain.", 

            " It is like the incident where a certain matron[1] said to R. Judah b. R. El'ai, ", 

            "\"Thy face is like that of pig-rearers and usurers[2].\" ", 

            "He replied,", 

            " \"On my faith !", 

            " Both [occupations] are forbidden me ;", 

            " but there are twenty-four privies from my lodging-place to the House of Study, and whenever I go there I test myself in all of them.\" ", 

            "Rab Judah also said[3] : Three things shorten a man's days and years : ", 

            "To be given a Scroll of the Torah from which to read [a portion in the Synagogue] and decline to read ; to be handed the cup of benediction to say Grace and decline ; and to give oneself an air of superiority[4]. ", 

            "\"To be given a Scroll of the Torah from which to read and decline to read\" — for it is written, \"For that is thy life and the length of thy days\" (Deut. xxx. 20).", 

            " \"To be handed the cup of benediction to say Grace and decline\" — for it is written, \"I will bless them that bless thee\" (Gen. xii. 3)[5]. ", 

            "\"To give oneself an air of superiority\" — for R. Hamma b. R. Hannina[6] said : ", 

            "Why did Joseph die before his brothers[7]? Because he gave himself superior airs. ", 

            "Rab Judah also said in the name of Rab : For three things it is necessary to offer supplication :", 

            " A good king, a good year, and a good dream. ", 

            "\"A good king\" — for it is written, \"The king's heart is in the hand of the Lord as the water-courses\" (Prov. xxi. 1).", 

            " \"A good year\" — for it is written, \"The eyes of the Lord thy God are always upon it, from the beginning of the year even unto the end of the year\" (Deut. xi. 12).", 

            " \"A good dream\" — for it is written, \"Wherefore cause Thou me to dream[8] and make me to live\" (Is. xxxviii. 16). ", 

            "R. Johanan said : ", 

            "There are three things which the Holy One, blessed be He, Himself proclaims, viz. :", 

            " famine, plenty and a good leader.", 

            " \"Famine\" — for it is written, \"The Lord hath called for a famine\" (II Kings viii. 1). \"Plenty\" — for it is written, \"I will call for the corn and will increase it\" (Ezek. xxxvi. 29). \"A good leader\" — for it is written, \"And the Lord spoke unto Moses, saying, See I have called by name Besalel, the son of Uri\" etc. (Exod. xxxi. 1 f.). ", 

            "R. Isaac said :", 

            " \"We must not appoint a leader over the Community without first consulting them ; as it is said, \"See, the Lord hath called by name Besalel, the son of Uri\" (ibid. xxxv. 30).", 

            " The Holy One, blessed be He, asked Moses,", 

            " \"Is Besalel acceptable to thee?\"", 

            " He replied, ", 

            "\"Lord of the universe, if he is acceptable to Thee, how much more so to me!\" ", 

            "He said to him,", 

            " \"Nevertheless, go and tell the people.\" ", 

            "He went and asked Israel,", 

            " \"Is Besalel acceptable to you?\" ", 

            "They answered,", 

            " \"If he is acceptable to the Holy One, blessed be He, and to thee, how much more so to us ! \" ", 

            "R. Samuel b. Nahmani said in the name of R. Jonathan :", 

            " He was called Basalel because of his wisdom : ", 

            "for at the time that the Holy One, blessed be He, said to Moses,", 

            " \"Go, tell Besalel, 'Make for Me a tabernacle, an ark and vessels[1]',\" Moses went and inverted the order, saying to him, ", 

            "\"Make an ark and vessels and a tabernacle[2].\"", 

            " He replied, ", 

            "\"Moses, our teacher, it is the way of the world for a man to build a house and afterwards furnish it ; but thou sayest,", 

            " 'Make for Me an ark, vessels and a tabernacle'! ", 

            "Where shall I place the vessels which I make? ", 

            "Perhaps thus spake the Holy One, blessed be He, unto thee, ", 

            "'Make a tabernacle, an ark and vessels'.\"", 

            " Moses replied,", 

            " \"Perhaps thou wert in the shadow of God[3] and thou knowest this.\" ", 

            "Rab Judah said in the name of Rab :", 

            " Besalel knew how to combine the letters[4] with which the heavens and earth had been created ;", 

            " for it is written here, \"And He hath filled him with the spirit of God, in wisdom and in understanding and in knowledge\" (Exod. xxxv. 31), and it is written elsewhere, \"The Lord by wisdom founded the earth ; by understanding He established the heavens\" (Prov. iii. 19) and \"By His knowledge the depths were broken up\" (ibid. V. 20). ", 

            "R. Johanan said :", 

            " The Holy One, blessed be He, only gives wisdom to him who has wisdom ; as it is said, \"He giveth wisdom unto the wise, and knowledge to them that know understanding\" (Dan. ii. 21 ). ", 

            "Rab Tahlifa the Palestinian[1] heard this and repeated it in the presence of R. Abbahu. He said to him : ", 

            "You learn it from there ; but I learn it from the following, for it is written, \"In the hearts of all that are wise-hearted I have put wisdom\" (Exod. xxxi. 6)[2]. ", 

            "Rab Hisda said : ", 

            "[There is no reality in] any dream without a fast[3].", 

            " Rab Hisda also said : ", 

            "An uninterpreted dream is like an unread letter[4]. ", 

            "Rab Hisda also said :", 

            " Neither a good nor a bad dream is fulfilled in every detail. ", 

            "Rab Hisda also said : ", 

            "A bad dream is preferable to a good dream[5].", 

            " Rab Hisda also said : ", 

            "When a dream is bad, the pain it causes is sufficient [to prevent its fulfilment], and when the dream is good, the joy it brings is sufficient. ", 

            "Rab Joseph said : ", 

            "As for a good dream, even in my own case[6], its cheerfulness frustrates it [so that it is not realised].", 

            " Rab Hisda also said : ", 

            "A bad dream is worse than scourging ; as it is said, \"God hath so made it that men should fear before Him\" (Eccles. iii. 14), and Rabbah b. Bar Hannah said in the name of R. Johanan : ", 

            "This refers to a bad dream[7]. ", 

            "\"The prophet that hath a dream, let him tell a dream ; and he that hath My word, let him speak My word faithfully. What hath the straw to do with the wheat ? saith the Lord\" (Jer. xxiii. 28). What connection has \"straw and wheat\" with a dream ? ", 

            "But said R. Johanan in the name of R. Simeon b. Johai : ", 

            "Just as one cannot have wheat without straw, similarly it is impossible for a dream to be without something that is vain. ", 

            "R. Berekiah said : ", 

            "A dream, though it be fulfilled in part, is never completely realised. Whence is this learnt? From Joseph; for it is written, \"And behold the sun and the moon and eleven stars bowed down to me\" (Gen. xxxvii. 9); "

        ], 

        [

            " but at that time his mother[1] was no longer living. ", 

            "R. Levi said :", 

            " A man should always wait up to twenty-two years for [the fulfilment of] a good dream. ", 

            "Whence is this learnt ? From Joseph ; for it is written, \"These are the generations of Jacob. Joseph, being seventeen years old\" etc. (ibid. v. 2)[2], and it is written, \"And Joseph was thirty years old when he stood before Pharaoh\" (ibid. xli. 46). ", 

            "From seventeen to thirty — how many years is it? Thirteen ; add the seven years of plenty and two of famine[3], hence we get twenty-two. ", 

            "Rab Huna said : ", 

            "A good man is not shown a good dream[4] and a bad man is not shown a bad dream[5]. ", 

            "There is a teaching to the same effect:", 

            " Throughout David's lifetime he never saw a good dream, and throughout Ahitophel's lifetime he did not see a bad dream. ", 

            "But lo, it is written, \"There shall no evil befall thee\" (Ps. xci. 10), and Rab Hisda said in the name of Rab Jeremiah b. Abba : ", 

            "[These words mean,] neither bad dreams nor evil thoughts will trouble thee[6]! [not fully translated]", 

            " Nay;", 

            " the good man sees no evil dream, but others dream about him. ", 

            "And since he sees no [dream] himself, is that an advantage ? ", 

            "For lo, R. Ze'ira[7] said : ", 

            "Whoever abides seven days without a dream is called evil ; as it is said, \"He shall abide satisfied, he shall not be visited by evil\" (Prov. xix. 23). Read not sabea' \"satisfied\" but sheba' \"seven.\"[8]!", 

            " Nay, this is what he means to say :", 

            " The good man sees a dream but [the next morning] he does not know what he has seen[9]. ", 

            "Rab Huna b. Ammi[10] stated that R. Pedat said in the name of R. Johanan :", 

            " He who sees a dream and his soul is depressed[11] should go and have it interpreted in the presence of three. ", 

            "He should have it interpreted ! ", 

            "But Rab Hisda has said : ", 

            "An uninterpreted dream is like an unread letter[1] ! ", 

            "Nay, but say : ", 

            "He should have it turned into good in the presence of three. ", 

            "He should assemble three men and say to them, ", 

            "\"I have seen a good dream\" ; ", 

            "and they should say to him,", 

            " \"Good it is and may it be good. May the All-merciful turn it to good ; ", 

            "seven times may it be decreed concerning thee from Heaven that it should be good, and may it be good.\" ", 

            "Then they should recite three verses in which the word hapak \"turn\" occurs, three in which padah \"redeem\" occurs, and three in which shalom \"peace\" occurs. ", 

            "Three verses in which \"turn\" occurs — \"Thou didst turn for me my mourning into dancing ; Thou didst loose my sackcloth and gird me with gladness\" (Ps. xxx. 12); \"Then shall the virgin rejoice in the dance, and the young men and the old together; for I will turn their mourning into joy, and will comfort them, and make them rejoice from their sorrow\" (Jer. xxxi. 12); \"Nevertheless the Lord thy God would not hearken unto Balaam; but the Lord thy God turned the curse into a blessing unto thee\" (Deut. xxiii. 6). ", 

            "Three verses in which the word \"redeem\" occurs — \"He hath redeemed my soul in peace so that none came nigh me\" (Ps. Iv. 19) ; \"And the redeemed of the Lord shall return and come with singing unto Zion...and sorrow and sighing shall flee away\" (Is. XXXV. 10) ; \"And the people said unto Saul, Shall Jonathan die, who hath wrought this great salvation in Israel?... So the people rescued [padah] Jonathan, that he died not\" (I Sam. xiv, 45).", 

            " Three verses in which the word \"peace\" occurs — \"Peace, peace, to him that is far off and to him that is near, saith the Lord that createth the fruit of the lips ; and I will heal him\" (Is. lvii. 19) ; \"Then the spirit clothed Amasai, who was chief of the captains : Thine are we, David, and on thy side, thou son of Jesse ; peace, peace be unto thee, and peace be to thy helpers; for thy God helpeth thee\" (I Chron. xii. 18); \"Thus ye shall say, All hail! and peace be both unto thee, and peace be to thy house, and peace be unto all that thou hast\" (I Sam. xxv. 6). ", 

            "Amemar, Mar Zotra and Rab Ashe were sitting together; they said:", 

            " Let each one of us relate something which the others have not heard. ", 

            "One of them commenced and said : ", 

            "He who has seen a dream and knows not what he has seen, let him stand before the Kohanim at the time that they spread their hands [to pronounce the priestly benediction] and utter the following[1] : ", 

            "\"Lord of the universe ! I am Thine and my dreams are Thine ; a dream have I dreamed and I know not what it is. Whether I dreamed concerning myself, or my fellows dreamed concerning me, or I dreamed concerning others, if they be good dreams, strengthen and fortify them [and may they be fulfilled][2] like the dreams of Joseph ; but if they require to be remedied, heal them as the waters of Marah [were healed] by the hands of Moses our teacher, as Miriam [was healed] from her leprosy[3], as Hezekiah from his illness, and like the waters of Jericho [sweetened] by the hands of Elisha. And as Thou didst turn the curse of the wicked Balaam into a blessing, so do Thou turn all my dreams for me into good.\" He should conclude [his prayer] simultaneously with the Kohanim, so that the Congregation responds \"Amen.\" ", 

            "But if not[4], let him say the following: ", 

            "\"Thou majestic One in the heights, Who abidest in might, Thou art peace and Thy name is peace. May it be Thy will to grant us peace.\" ", 

            "The next commenced and said : ", 

            "He who enters a town[5] and is afraid of the Evil Eye[6], let him take his right thumb in his left hand and his left thumb in his right hand and say the following: ", 

            "\"I, A the son of B, come from the seed of Joseph against whom the Evil Eye had no power ; as it is said, 'Joseph is a fruitful vine, a fruitful vine by a fountain' (Gen. xlix. 22)[7]. Read not 'ale 'ayin 'by a fountain' but 'ole 'ayin 'overcoming the [Evil] Eye'.\" ", 

            "R. Jose b. R. Hannina said : It may be derived from the verse :", 

            " \"And let them[8] grow [weyidgu] into a multitude in the midst of the earth\" (ibid, xlviii. 16) ; i.e. as the fishes [dagim] in the sea are covered by the water and the Evil Eye cannot have power over them, in similar manner the Evil Eye has no power over the seed of Joseph. ", 

            "Should he, however, be afraid of his own Evil Eye, let him gaze upon the wing of his left nostril. ", 

            "The third of them commenced and said :", 

            " He who is ill should not disclose the fact on the first day so as not to cause himself bad luck, but after that he may disclose it. ", 

            "As when Raba fell ill, on the first day he did not disclose it, but after that be said to his attendant, \"Go, announce that ", 

            "Raba is ill. ", 

            "Let him who loves me pray on my behalf, and let him that hates me rejoice over my plight ; for it is written, 'Rejoice not when thine enemy falleth, and let not thy heart be glad when he stumbleth ; lest the Lord see it and it displease Him, and He turn away His wrath from him' (Prov. xxiv. 17 f.).\" ", 

            "When Samuel had a bad dream, he used to say, ", 

            "\"The dreams speak falsely\" (Zech. x. 2) ; ", 

            "but when he had a good dream, he used to say, ", 

            "\"Do the dreams speak falsely?", 

            " For lo, it is written, 'I [God] do speak with him in a dream' (Num. xii. 6).\" ", 

            "Raba asked :", 

            " It is written, \"I do speak with him in a dream,\" and it is written, \"The dreams speak falsely\" ! ", 

            "There is no contradiction ; the former being through an angel, the latter through an evil spirit. ", 

            "R. Bizna b. Zabda stated that R. 'Akiba said in the name of R. Panda, in the name of R. Nahum, in the name of R. Biryam, in the name of an Elder — and who is he? R. Banaah[1]: ", 

            "There were twenty-four interpreters of dreams in Jerusalem. I once had a dream and went to consult them all ; but the interpretation each gave me differed from that of the others. Nevertheless all their interpretations were realised in me ; to fulfil that which was said", 

            " \"All dreams follow the mouth [of the interpreter][2].\" ", 

            "Is there such a Scriptural passage as \"All dreams follow the mouth[3]\"?", 

            " Yes; and it is like the statement of R. Eleazar who said :", 

            " Whence is it that all dreams follow the mouth ?", 

            " As it is said, \"And it came to pass, as he interpreted to us, so it was\" (Gen. xli. 13). ", 

            "Raba said : ", 

            "That is only so if he interprets it from the content of the dream; as it is said, \"To each man according to his dream he did interpret\" (ibid. v. 12). ", 

            "\"When the chief baker saw that the interpretation was good\" (ibid. xl. 16) — how did he know this[1]? ", 

            "R. Eleazar said : ", 

            "This teaches that each of them was shown the dream and interpretation of the other. ", 

            "R. Johanan said :", 

            " If one wakes up and a verse comes to his mouth[2], it is to be regarded as a minor prophecy.", 

            "R. Johanan also said : Three types of dream are fulfilled — ", 

            "a morning dream, a dream which his friend has about him, and a dream interpreted in the midst of a dream. ", 

            "Some add :", 

            "Also a dream which is repeated ; as it is said, \"And for that the dream was doubled unto Pharaoh twice\" (Gen. xli. 32). ", 

            "R. Samuel b. Nahmani said in the name of R. Jonathan : ", 

            "A man is only shown[3] [in a dream what emanates] from the thoughts of his heart ; as it is said, \"As for thee, O king, thy thoughts  came into thy mind upon thy bed\" (Dan. ii. 29). Or if thou wilt I can say from this passage, \"That thou mayest know the thoughts of thy heart\" (ibid. v. 30). ", 

            "Raba[4] said : ", 

            "Thou mayest know this from the fact that a man is never shown [in a dream] a golden date-palm or an elephant entering the eye of a needle[5]. \n"

        ], 

        [

            "The Roman Emperor said to R. Joshua b. R. Hannina[6], ", 

            "\"You declare that you are wise. Tell me what I shall see in my dream.\" ", 

            "He replied, ", 

            "\"Thou wilt see the Persians enslaving thee, despoiling thee, and making thee pasture unclean animals with a golden crook.\"", 

            " The Emperor reflected upon it the whole day and in the night saw it [in a dream][7]. ", 

            "King Shapor said to Samuel, ", 

            "\"You declare that you are very wise.", 

            " Tell me what I shall see in my dream.\"", 

            " He replied,", 

            " \"Thou wilt see the Romans come and take thee captive and make thee grind date-stones[8] in a golden mill.\" ", 

            "The king reflected upon it the whole day and in the night saw it [in a dream][9]. ", 

            "Bar Hedja was an interpreter of dreams. When one paid him a fee, he interpreted [the dream] favourably ; but if no fee was given him, he interpreted it unfavourably. ", 

            "Abbai and Raba had a dream ; Abbai gave him a Zuz but Raba gave him nothing. ", 

            "They said to him : ", 

            "We were made to read in our dream the words \"Thine ox shall be slain before thine eyes\" (Deut. xxviii. 31).", 

            " To Raba he said : ", 

            "Thy business will fail, and thou wilt have no desire to eat because of the grief of thy heart. To Abbai he said : ", 

            "Thy business will prosper, and thou wilt have no desire to eat because of the joy of thy heart. ", 

            "They said to him : ", 

            "We were made to read in our dream the words \"Thou shalt beget sons and daughters, but they shall not be thine, for they shall go into captivity\" (ibid. V. 41). To Raba he replied in an unfavourable sense. To Abbai he said : ", 

            "Thy sons and daughters will be many, and thy daughters will marry [husbands in distant parts of] the world, so that they will seem to thee as though they had gone into captivity, ", 

            "[They said to him : In our dream] we were made to read the words \"Thy sons and thy daughters shall he given unto another people \" (ibid. v. 32), To Abbai he said : ", 

            "Thy sons and daughters will be many ; thou wilt say [they should marry] thy relatives, but [thy wife] will say they [should marry] her relatives, and she will compel thee to give them to her relatives, and it will seem [as though they had been given] to another people.", 

            " To Raba he said : ", 

            "Thy wife will die, and thy sons and daughters will come under the control of another wife. For Raba[1] said in the name of R. Jeremiah b. Abba in the name of Rab : ", 

            "What means that which is written, \"Thy sons and thy daughters shall be given unto another people\"? This refers to a stepmother. ", 

            "[They said to Bar Hedja] : We were made to read in our dream the words \"Go thy way, eat thy bread with joy\" (Eccles, ix. 7). To Abbai he said : ", 

            "Thy business will prosper and thou wilt eat and drink and read Scriptural verses from the joy of thy heart. ", 

            "To Raba he said :", 

            " Thy business will fail, thou wilt slaughter [cattle] but not eat, and thou wilt drink and read Scriptural verses to banish thy dread. ", 

            "We were made to read the words \"Thou shalt carry much seed out into the field, and shalt gather little in for the locust will consume it\" (Deut. xxviii. 38). To Abbai he gave an interpretation from the first half of the verse ; to Raba from the latter half. ", 

            "We were made to read the words \"Thou shalt have olive-trees throughout all thy borders, but thou shalt not anoint thyself with the oil, for thine olives shall drop off\" (Deut. xxviii, 40). To Abbai he gave an interpretation from the first half of the verse ; to Raba from the latter half. ", 

            "We were made to read the words \"And all the peoples of the earth shall see that the name of the Lord is called upon thee, and they shall be afraid of thee\" (ibid. v. 10). To Abbai he said : ", 

            "Thy fame will go forth as the Principal of the College and the fear of thee will be widespread in the world.", 

            " To Raba he said : ", 

            "The king's treasury will be broken into and thou wilt be arrested as one of the thieves, and everybody will draw an inference from thee[1]. ", 

            "The next day the king's treasury was broken into, and they came and arrested Raba. ", 

            "They said [to Bar Hedja] : ", 

            "We saw [in a dream] lettuce upon the mouth of a jar. ", 

            "To Abbai he said : ", 

            "Thy business will be doubled like the lettuce. To Raba he said :", 

            " Thy business will be bitter like the lettuce. ", 

            "They said to him : ", 

            "We saw [in a dream] meat upon the mouth of a jar.", 

            " To Abbai he said :", 

            " Thy wine[2] will be sweet and everybody will come to buy meat and wine of thee.", 

            " To Raba he said : ", 

            "Thy wine will be sour and everybody will come to buy meat to eat therewith. ", 

            "They said to him : ", 

            "We saw [in a dream] a jug hanging upon a date-palm. To Abbai he said :", 

            " Thy wares will be exalted like the palm. ", 

            "To Raba he said :", 

            " Thy wares will be sweet as dates[3].", 

            " They said to him :", 

            " We saw [in a dream] a pomegranate sprouting on the mouth of a jar. To Abbai he said : ", 

            "Thy wares will be high-priced like the pomegranate. ", 

            "To Raba he said :", 

            " Thy wares will be stale [and taste] like the pomegranate. ", 

            "They said to him : ", 

            "We saw [in a dream] a jug fall into a well. To Abbai he said : ", 

            "Thy wares will be sought as one says, \"A piece of bread fell into a well and cannot be found[4].\" ", 

            "To Raba he said :", 

            " Thy wares will go bad and thou wilt cast them into a well. ", 

            "They said to him : ", 

            "We saw [in a dream] a young ass standing by the side of our pillow and braying. To Abbai he said : ", 

            "Thou wilt become the President of the College and an Amora will stand by thee. ", 

            "To Raba he said : ", 

            "The words \"the firstling of an ass\" (Exod. xiii. 13) have been erased from thy Tefillin[5]. ", 

            "Raba said to him :", 

            " I have myself seen that the words are there. ", 

            "He replied : ", 

            "The letter waw in the word hamor \"ass\" has certainly been erased from thy Tefillin[1]. ", 

            "Later on Raba went to him alone and said :", 

            " I dreamt that the outer door fell. He replied : ", 

            "Thy wife will die[2]. ", 

            "He said :", 

            " I dreamt that my back and front teeth fell out. He replied that ", 

            "his sons and daughters would die. ", 

            "He said :", 

            " I dreamt of two doves flying. He replied :", 

            " Thou wilt divorce two wives[3].", 

            " He said :", 

            " I dreamt of two turnip-tops. He replied : ", 

            "Thou wilt receive two blows[4].", 

            " That day Raba went and sat in the House of Study the whole day[5]. He found there two blind men quarrelling with each other. Raba went to part them, and they struck him twice. They raised [their sticks] to give him another blow ; but he cried,", 

            " \"That's enough! I only dreamt of two!\" ", 

            "Finally Raba came and gave [Bar Hedja] a fee, and said to him :", 

            " I dreamt of a wall falling. ", 

            "He replied : ", 

            "Thou wilt acquire a boundless estate. ", 

            "He said to him : ", 

            " dreamt that Abbai's house collapsed and its dust covered me. He replied : ", 

            "Abbai will die and his [Office as Principal of the] College will revert to thee. ", 

            "He said to him :", 

            " I dreamt that my house collapsed and everybody came to take each a brick. He replied :", 

            " Thy teachings will be scattered throughout the world.", 

            " He said to him :", 

            " I dreamt that my head was split open and my brains fell out. He replied :", 

            " The stuffing will fall out of thy bolster. ", 

            "He said to him : ", 

            "I dreamt that I was made to read the Hallel of Egypt[6]. He replied :", 

            " Many miracles will happen to thee. [Once Bar Hedja] went with Raba on a boat; he said [to himself] ", 

            "\"Why should I accompany a man to whom miracles will happen[7]?\" ", 

            "As he descended [from the boat] a book[8] of his fell. Raba found it and saw written therein, ", 

            "\"All dreams follow the mouth [of the interpreter].\" ", 

            "He exclaimed, \"Thou rascal !", 

            " It rested with thee [whether my dreams were auspicious or not], and thou didst cause me all this pain.", 

            " I forgive thee everything except [what thou didst say about][1] the daughter of Rab Hisda[2].", 

            " May it be His will that this fellow be handed over into the power of the Government and it have no mercy on him!\" ", 

            "Bar Hedja said,", 

            "\"What can I do ? ", 

            "There is a tradition that ", 

            "the curse of a wise man, even when undeserved, comes to pass ; and how much more so that of Raba who has justification for uttering a curse!\" He said [to himself]", 

            " \"I will go into exile[3]; for a teacher has said,", 

            " 'Exile[4] atones for sins'.\"", 

            " He went into exile amoug the Romans, and sat down at the door of the king's treasury[5]. ", 

            "The wardrobe-keeper had a dream and said to him :", 

            " I dreamt that a needle entered my finger. Bar Hedja said,", 

            " \"Give me a Zuz\" ; ", 

            "but he refused, so he gave him no reply. ", 

            "Then the wardrobe-keeper said :", 

            " I dreamt that decay[6] seized two of my fingers. He said,", 

            " \"Give me a Zuz\" ;", 

            " but he refused and received no answer.", 

            " He said to him : ", 

            "I dreamt that decay seized my whole hand. He replied : ", 

            "Decay has seized all the [king's] silken garments. ", 

            "The king's household heard of this and they brought the wardrobe-keeper to put him to death.", 

            " He said to the king, ", 

            "\"Why me? ", 

            "Take him who knew but spoke not.\"", 

            " They took Bar Hedja, and he said to him, ", 

            "\"Because of the Zuz [which I refused thee], destruction has come upon the king's silken garments.\" "

        ], 

        [

            " They tied two cedars", 

            " with a rope, bound one foot to one cedar and the other foot to the other cedar, and then released the rope. When he was decapitated each tree bounded back to its original position, and his body fell in two. ", 

            "Ben Dama, the son of Ishmael's sister, asked R. Ishmael :", 

            " I dreamt that both my cheekbones fell out. ", 

            "He replied :", 

            " Two Roman nobles planned to do thee harm but they died[7].", 

            " Bar Kappara said to Rabbi[8]: ", 

            "I dreamt that my nose fell off. He replied : ", 

            "The divine wrath has departed from thee[9]. ", 

            "He said to him :", 

            " I dreamt that both my hands were cutoff. He replied : ", 

            "Thou wilt not be dependent upon the work of thy hands. ", 

            "He said to him :", 

            " I dreamt that both my legs were amputated. He replied : ", 

            "Thou wilt ride upon a horse. ", 

            "He said to him : I dreamt that somebody told me,", 

            " \"Thou wilt die in Adar and not behold Nisan.\" He replied :", 

            " Thou wilt die in honour [idruta] and not fall into the power of temptation [nissayon]. ", 

            "A certain Min said to R. Ishmael[1] :", 

            " I dreamt that I poured oil upon olives. He replied that ", 

            "he had outraged his mother[2], ", 

            "He said to him :", 

            " I dreamt that I plucked a star. He replied :", 

            " Thou hast stolen the son of an Israelite. ", 

            "He said to him :", 

            " I dreamt that I swallowed a star. ", 

            "He replied : ", 

            "The son of an Israelite thou didst sell and eat up the proceeds. ", 

            "He said to him :", 

            " I dreamt that my eyes kissed one another. He replied that ", 

            "he had outraged his sister. ", 

            "He said to him : I dreamt that I kissed the moon. He replied that ", 

            "he had outraged the wife of an Israelite. ", 

            "He said to him :", 

            " I dreamt that I walked in the shade of a myrtle. He replied that ", 

            "he had outraged a betrothed maiden. ", 

            "He said to him :", 

            " I dreamt there was a shadow over me and yet it was beneath me. He replied that", 

            " he had gratified an unnatural lust. ", 

            "He said to him : ", 

            "I dreamt that ravens came to my bed. He replied : ", 

            "Thy wife has been unfaithful with many men. ", 

            "He said to him:", 

            " I dreamt that doves came to my bed. He replied:", 

            " Many women hast thou defiled. ", 

            "He said to him :", 

            " I dreamt that I held two doves and they flew away. He replied : ", 

            "Thou didst marry two women and parted from them without a document of divorce. ", 

            "He said to him : I dreamt that I was shelling eggs. He replied : ", 

            "The dead hast thou stripped. ", 

            "He said to him, ", 

            "\"I am guilty of all these acts with the exception of the last which is not [true].\"", 

            " Just then a woman came and said to him, ", 

            "\"That cloak which thou art wearing belonged to so-and-so who died and thou didst strip him of it.\" ", 

            "He said to him :", 

            "I dreamt that I was told,", 

            " \"Thy father has left thee property in Cappadocia[3].\" ", 

            "He asked, ", 

            "\"Hast thou property in Cappadocia?\" ", 

            "He replied, ", 

            "\"No.\"", 

            " \"Hast thy father been to Cappadocia?\" ", 

            "He answered,", 

            "\"No.\" ", 

            "\"In that case ", 

            "Kappa means 'a beam' and Deka 'ten.' Go, examine the beam which heads number ten, for it is full of coins[4].\" He went and found it full of coins. ", 

            "R. Hannina said : ", 

            "Who dreams of a well will see peace ; as it is said, \"And Isaac's servants digged in the valley, and found there a well of living water\" (Gen. xxvi. 19)[1]. ", 

            "R. Nathan[2] said : ", 

            "He will find Torah; as it is said, \"Whoso findeth me findeth life\" (Prov. viii. 35), and it is written here \"a well of living water[3].\" ", 

            "Raba said : ", 

            "[It means] life literally. ", 

            "R. Hanan[4] said : There are three [types of dreams which indicate] peace — ", 

            "a river, bird and pot. ", 

            "\"A river\" — for it is written, \"Behold I will extend peace to her like a river\" (Is. Ixvi. 12). \"A bird\" — for it is written, \"As birds hovering, so will the Lord of hosts protect Jerusalem\" (ibid. xxxi. 5). \"A pot\" — for it is written, \"Lord, Thou wilt establish[5] peace for us\" (ibid. xxvi. 12).", 

            " R. Hannina said : ", 

            "But it must be a pot in which there is no meat; for it is said[6], ", 

            "\"They chop them in pieces, as that which is in the pot, and as flesh within the caldron\" (Micah iii. 3)[7]. ", 

            "R. Joshua b. Levi said : ", 

            "Who dreams of a river should on rising say, \"Behold I will extend peace to her like a river\" (Is. Ixvi. 12), before another verse occurs to him, viz. : \"For distress will come  in like a river\" (ibid. lix. 19). ", 

            "Who dreams of a bird should on rising say, \"As birds hovering so will the Lord of hosts protect\" (ibid. xxxi. 5), before another verse occurs to him, viz. : \"As a bird that wandereth from her nest, so is a man that wandereth from his place\" (Prov. xxvii. 8). ", 

            "Who dreams of a pot should on rising say, \"Lord, Thou wilt establish [shapat] peace for us\" (Is. xxvi. 12), before another verse occurs to him, viz. : \"Set on [shapat] the pot, set it on\" (Ezek. xxiv. 3). ", 

            "Who dreams of grapes should on rising say, \"I found Israel like grapes in the wilderness\" (Hos. ix. 10) before another verse occurs to him, viz.: \"Their grapes are grapes of gall\" (Deut. xxxii. 32). ", 

            "Who dreams of a mountain should on rising say, \"How beautiful upon the mountains are the feet of the messenger of good things\" (Is. lii. 7), before another verse occurs to him, viz.: \"For the mountains will I take up a weeping and wailing\" (Jer. ix. 9).", 

            " Who dreams of a horn should on rising say, \"And it shall come to pass in that day, that a great horn shall be blown\" (Is. xxvii. 13), before another verse occurs to him, viz. : \"Blow ye the horn of Gibeah\" (Hos. V. 8). ", 

            "Who dreams of a dog should on rising say, \"But against any of the children of Israel shall not a dog whet his tongue\" (Exod. xi. 7), before another verse occurs to him, viz. : \"Yea, the dogs are greedy\" (Is. Ivi. 11). ", 

            "Who dreams of a lion should on rising say, \"The lion hath roared, who will not fear?\" (Amos iii. 8), before another verse occurs to him, viz. : \"A lion is gone up from his thicket\" (Jer. iv. 7). [is gone up]", 

            "[a lion from his thicket] Who dreams of shaving should on rising say, \"And [Joseph] shaved himself and changed his raiment\" (Gen. xli. 14), before another verse occurs to him, viz. : \"If I be shaven, then my strength will go from me\" (Judges xvi. 17). ", 

            "Who dreams of a well should on rising say, \"A well of living waters\" (Cant. iv. 15), before another verse occurs to him, viz. : \"As a cistern welleth with her waters, so she welleth with her wickedness\" (Jer. vi. 7). ", 

            "Who dreams of a reed should on rising say, \"A bruised reed shall he not break\" (Is. xlii. 3), before another verse occurs to him, viz. : \"Behold, thou trustest upon the staff of this bruised reed\" (ibid, xxxvi. 6). ", 

            "Our Rabbis have taught : ", 

            "Who dreams of a reed [kaneh] may hope for wisdom ; as it is said, \"Get [keneh] wisdom\" (Prov. iv. 5). Who dreams of reeds may hope for understanding ; as it is said, \"With all thy getting get understanding\" (ibid. v. 7)[1].", 

            " R. Zera said: ", 

            "A pumpkin [kara], a palm-heart [kora], wax [kira] and a reed [kanya] are all auspicious in a dream[2]. ", 

            "There is a teaching[3] :", 

            " Nobody is shown a gourd [in a dream] except him who is a fearer of Heaven with all his strength[4]. ", 

            "Who dreams of an ox should on rising say, \"His firstling bullock, majesty is his\" (Deut. xxxiii. 17), before another occurs to him, viz. : \"If an ox gore a man\" (Exod. xxi. 28). ", 

            "Our Rabbis have taught : Five things are said in connection with the ox : ", 

            "Who [dreams that he] eats of its flesh will grow rich; that an ox had gored him, he will have sons who will contend with[5] each other in Torah; that it bit him, sufferings will come upon him ; that it kicked him, a long journey is destined for him ; that he rode upon it, he will ascend to greatness. But there is a teaching :", 

            " [One who dreams of] riding upon an ox will die !", 

            " There is no contradiction, ", 

            "the former referring [to a dream wherein] he rides upon the ox, the latter to when the ox rides on him. ", 

            "Who dreams of an ass may hope for salvation[1] ; as it is said, \"Behold thy king cometh unto thee: he is triumphant and victorious, lowly, and riding upon an ass\" (Zech. ix. 9). ", 

            "Who dreams of a cat in a place where the word for it is Shunnara, a beautiful song [shirah naah] will be composed in his honour ; [but where the word for it is] Shinnara, a change for the worse [shinnui ra'] is in store for him[2]. ", 

            "Who dreams of grapes, if they are white, both in their season and out of season, they are a good omen ; if they are black, in their season they are a good omen, but out of season a bad omen[3]. ", 

            "Who dreams of a white horse, whether standing still or galloping, it is a good omen for him ; if it is roan, should it be standing still, it is a good omen; should it be galloping, it is a bad omen. ", 

            "Who dreams of Ishmael, his prayer will be heard[4]; but only of Ishmael the son of Abraham, and not of an ordinary Arab[5]. ", 

            "Who dreams of a camel, death had been decreed upon him by Heaven, but he has been delivered therefrom.", 

            " R. Hamma[6] b. R. Hannina said : ", 

            "What is the Scriptural authority for this ? \"I will go down with thee into Egypt ; and I will also surely bring thee up again\" (Gen. xlvi. 4)[7].", 

            " Rab Nahman b. Isaac[8] said : It may be derived from the following, \"The Lord also[9] hath put away thy sin; thou shalt not die\" (II Sam. xii. 13). ", 

            "Who dreams of Phineas, a miracle will be wrought for him[10]. Who dreams of an elephant [pil], miracles [pela'ot] will be wrought for him; of elephants, miracles upon miracles will be performed for him. ", 

            "But there is a teaching : ", 

            "To dream of all kinds of animals is a good omen with the exception of the elephant and ape !", 

            " There is no  contradiction ; "

        ], 

        [

            " the former referring to animals which are bridled, the latter to those which are not bridled. ", 

            "Who dreams of the name \"Huna,\" a miracle will be wrought for him[1] ; ", 

            "of \"Hannina, Hananya, Johanan,\" miracles will be wrought for him. ", 

            "Who dreams of a Hasped[2], from Heaven will pity and redemption be vouchsafed him. ", 

            "This only applies [to him who sees in his dream the word Hesped] in writing[3]. ", 

            "[Who dreams] that he makes the response \"May His great name be blessed\" is assured that he is a son of the world to come. [Who dreams] that he recites the Shema' is meet that the Shekinah should rest upon him[4], but his generation is not worthy of it. ", 

            "Who dreams that he lays the Tefillin may hope for greatness ; as it is said, \"And all the peoples of the earth shall see that the name of the Lord is called upon thee, and they shall fear thee\" (Deut. xxviii. 10)[5]; and there is a teaching :", 

            " R. Eliezer the Great says :", 

            " This refers to the Tefillin worn on the head. ", 

            "Who dreams that he is saying the Tefillah, it is a good omen for him ; but this applies only when he does not conclude it[6]. ", 

            "Who dreams of having intercourse with his mother may hope for understanding[7]; as it is said, \"Yea, thou wilt call understanding 'mother'\" (Prov. ii. 3)[8].", 

            " [Who dreams] of having intercourse with a betrothed maiden may hope for Torah, as it is said, \"Moses commanded us a law [Torah], an inheritance of the congregation of Jacob\" (Deut. xxxiii. 4) — read not morashah \"an inheritance\" but me'orasah \"betrothed maiden.\"", 

            " Who dreams of having had intercourse with his sister may hope for wisdom ; as it is said, \"Say unto wisdom, thou art my sister\" (Prov. vii. 4). ", 

            "Who dreams of having had intercourse with a married woman is assured that he is a son of the world to come ; but this applies only if he was not acquainted with her and did not think of her during the evening. ", 

            "R. Hiyya b. Abba said[1] :", 

            " Who dreams of wheat will see peace ; as it is said,", 

            " \"He maketh thy borders peace ; He giveth thee in plenty the fat of wheat\" (Ps. cxlvii. 14). ", 

            "Who dreams of barley, his iniquities will depart[2]; as it is said, \"Thine iniquity is taken away, and thy sin expiated\" (Is. vi. 7). ", 

            "R. Zera said :", 

            " I never went up from Babylon to the Land of Israel without dreaming of barley[3]. ", 

            "Who dreams of a well-laden vine, his wife will not miscarry ; as it is said, \"Thy wife shall be as a fruitful vine\" (Ps. cxxviii. 3). ", 

            "[Who dreams] of a choice vine may hope for the Messiah ; as it is said, \"Binding his foal unto the vine and his ass' colt unto the choice vine\" (Gen. xlix. 11)[4]. ", 

            "Who dreams of the fig, his Torah will be preserved within him ; as it is said, \"Whoso keepeth the fig-tree shall eat the fruit thereof\" (Prov. xxvii. 18)[5]. ", 

            "Who dreams of pomegranates, if small, his business will bear fruit like the pomegranate ; if large, his business will grow like the pomegranate ; if split open, should he be a disciple of the wise, he may hope for Torah ; as it is said, \"I would cause thee to drink of spiced wine, of the juice of my pomegranate\" (Cant. viii. 2); but should he be an 'Am ha'ares, he may hope for commandments [to perform], as it is said, \"Thy temples [rakkah] are like a pomegranate split open\" (ibid. iv. 3). ", 

            "What means rakkah? Even the illiterate [rekanim] amongst thee will be full of commandments as a pomegranate [is full of seeds]. ", 

            "Who dreams of olives, if small, his business will be fruitful and multiply and endure like olives. But this applies only to [dreaming of] the fruit ; if [he dreamt] of olive-trees, then he will have numerous offspring; as it is said, \"Thy children like olive-plants, round about thy table\" (Ps. cxxviii. 3). ", 

            "Some say that", 

            " he who dreams of the olive, a good name will proceed from him; as it is said, \"The Lord called thy name a leafy olive-tree, fair and goodly fruit\" (Jer. xi. 16).", 

            " Who dreams of olive-oil may hope for the light of Torah ; as it is said, \"That they bring unto thee pure olive-oil beaten for the light\" (Exod. xxvii. 20). ", 

            "Who dreams of palms, his iniquities will be ended[1]; as it is said, \"The punishment of thine iniquity is accomplished, O daughter of Zion\" (Lam. iv. 22). ", 

            "Rab Joseph said : ", 

            "Who dreams of a goat, the year will be blessed for him; of goats, years will be blessed for him ; as it is said, \"And there will be goat's milk enough for thy food\" (Prov. xxvii. 27).", 

            " Who dreams of the myrtle[2], his business undertakings will prosper ; and if he has no business undertakings, an inheritance will fall to his lot from some other place. ", 

            "'Ulla said (another version : It was taught in a Baraita) : ", 

            "This only applies when he sees [the myrtle] on its stem. ", 

            "Who dreams of a citron, will be honoured before his Maker; as it is said, \"The fruit of goodly trees, branches of palm-trees\" (Lev. xxiii. 40). Who dreams of a palm-branch has but one heart for his Father in Heaven.", 

            "Who dreams of a goose may hope for wisdom[3]; as it is said, \"Wisdom crieth aloud in the street\" (Prov. i. 20); ", 

            "and he who [dreams of having] intercourse with it will become the Principal of a Seminary. ", 

            "Rab Ashe said : I dreamt of seeing one and having intercourse with it, and I ascended to greatness[4]. ", 

            "Who dreams of a cock may hope for a son, of cocks may hope for sons, of hens[5] may hope for a beautiful rearing [of his children] and rejoicing. ", 

            "Who dreams of eggs, his petition remains in suspense[6] ; if broken, his petition has been granted. Similarly is it with nuts and cucumbers and all glass vessels and all such breakable articles.", 

            " [Who dreams] that he entered a town, his desires will be fulfilled for him ; as it is said, \"And He led them unto their desired haven\" (Ps. cvii. 30). ", 

            "Who dreams of shaving his head, it is a good omen for him\" ; [of shaving] his head and beard, [it is a good omen] for him and all his family. ", 

            "[Who dreams] that he is sitting in a small boat, a good name will proceed from him ; if in a big boat, then from him and all his family ; but that only applies when it is sailing high on the seas. ", 

            "Who dreams that he is performing the functions of nature, it is a good omen for him ; as it is said, \"He that is bent down shall speedily be loosed[1]\" (ls li. 14). But that only applies if he does not [dream of] wiping himself. ", 

            "Who dreams of ascending to the roof will ascend to greatness ; of descending, he will descend from greatness. ", 

            "Abbai and Raba both say : ", 

            "Since he has ascended, he has ascended[2]. ", 

            "Who dreams of rending his garments, the Divine decree will be rent for him. ", 

            "Who dreams of standing naked, if in Babylon he will stand without sin ; but if in the Land of Israel, [he will stand] naked without commandments[3]. ", 

            "Who dreams that he has been arrested by the police[4], the Divine protection will be vouchsafed him. [If he dreamt] that they placed him in neck-chains[5], the Divine protection will be doubly vouchsafed him ; but this applies only to a neck-chain, not to a common cord.", 

            " Who dreams of walking into a pool[6] will be appointed Principal of a Seminary ; into a forest[7], he will be made the head of the Collegiates. ", 

            "Rab Pappa and Rab Huna b. Rab Joshua had a dream. Rab Pappa [dreamt that he] walked into a pool and was appointed the Principal of a Seminary, and Rab Huna b. Rab Joshua that he walked into a forest and was made the head of the Collegiates. ", 

            "Another version is :", 

            " They both [dreamt that they] walked into a pool; but Rab Pappa, who was wearing a drum[8] around his neck, was made Principal of the Seminary, whereas Rab Huna b. Rab Joshua, who had no drum around his neck, was made the head of the Collegiates.", 

            " Rab Ashe said :", 

            " I [once dreamt that I] walked into a pool, with a drum around my neck, and I made a noise therewith[9]. ", 

            "A Tanna taught in the presence of Rab Nahman b. Isaac[1] : ", 

            "Who dreams of blood-letting, his sins will be pardoned him[2].", 

            " But there is a teaching : ", 

            "His sins are set in order for him !", 

            " What means \"set in order\"? Set in order so as to be pardoned. ", 

            "A Tanna taught in the presence of Rab Sheshet ; ", 

            "Who dreams of a serpent, his sustenance will be provided him ; if it bit him, his sustenance will be doubled for him ; if he killed it, his sustenance is lost.", 

            " Rab Sheshet said to him :", 

            " [When he dreams of killing the serpent], how much more likely is it that his sustenance will be doubled ! ", 

            "But it is not so ; and it was Rab Sheshet who dreamt that he saw a serpent and killed it[3]. ", 

            "A Tanna taught in the presence of R. Johanan[4] :", 

            " To dream of any kind of liquids is a good omen, with the exception of wine. Some [dream they] drink it and it is a good omen for them, and some do so and it is a bad omen for them.", 

            " There are some who [dream they] drink it and it is a good omen for them, as it is said, \"Wine that maketh glad the heart of man\" (Ps. civ. 15); and there are some who [dream they] drink it and it is a bad omen for them, as it is said, \"Give strong drink unto him that is ready to perish, and wine unto the bitter in soul\" (Prov. xxxi. 6). R. Johanan said to the Tanna : Teach that in the case of a ", 

            "disciple of the wise, it is always a good omen ; as it is said, \"Come, eat of my bread, and drink of the wine which I have mingled\" (ibid, ix. 5).  "

        ], 

        [

            "R. Johanan said :", 

            " If one wakes up and a verse comes to his mouth, it is to be regarded as a minor prophecy[5]. ", 

            "Our Rabbis have taught : There are three kings [to dream of whom has significance]. Who dreams of David may hope for piety ; of Solomon, may hope for wisdom ; of Ahab, he should be concerned about punishment. ", 

            "There are three prophets [to dream of whom has significance]. ", 

            "(Who dreams of the Book of Kings may hope for greatness;)[6] of Ezekiel, may hope for wisdom ; of Isaiah, may hope for consolation ; of Jeremiah, he should be concerned about punishment.", 

            " There are three major books of the Hagiographa [to dream of which has significance]. ", 

            "Who dreams of the Book of Psalms may hope for piety ; of Proverbs, may hope for wisdom ; of Job, he should be concerned about punishment.", 

            " There are three minor books of the Hagiographa [to dream of which has significance].", 

            " Who dreams of the Song of Songs may hope for piety ; of Ecclesiastes, may hope for wisdom ; of Lamentations, he should be concerned about punishment ; ", 

            "and he who dreams of the Scroll of Esther, a miracle will be wrought for him.", 

            " There are three Sages [to dream of whom has significance]. ", 

            "Who dreams of Rabbi[1] may hope for wisdom ; of R. Eleazar b. 'Azariah[2], may hope for wealth ; of Ishmael b. Elisha[3], he should be concerned about punishment.", 

            " There are three disciples of the wise[4] [to dream of whom has significance]. ", 

            "Who dreams of Ben 'Azzai[5] may hope for piety ; of Ben Zoma, may hope for wisdom ; of Aher[6], he should be concerned about punishment.", 

            "To dream of any species of animal is a good omen with the exception of the elephant, monkey and long-tailed ape[7]. ", 

            "But a teacher has said : ", 

            "Who dreams of an elephant, a miracle will be wrought for him !", 

            " There is no contradiction ; the latter refers to where it is bridled and the other to where it is not bridled[8]. ", 

            "To dream of any kind of metal-tool is a good omen, with the exception of the hoe, the mattock and the axe ; but this applies only when he sees them with their handles.", 

            " To dream of any kind of fruit is a good omen with the exception of unripe dates.", 

            " To dream of any kind of vegetables is a good omen with the exception of turnipheads. ", 

            "But Rab[9] said :", 

            " I did not become rich until I dreamt of turnip-heads !", 

            " When he saw them, he saw them on their stem. ", 

            "To dream of any kind of colour is a good omen with the exception of blue.", 

            " To dream of any kind of birds is a good omen with the exception of the owl, the horned owl and the bat[10]. ", 

            "(The body; The body ; Essence; Restore; Enlarge — mnemonic[11].) ", 

            "Three things enter the body without its deriving any benefit therefrom ;", 

            " melilot[1], date-berries and unripe dates.", 

            " Three things do not enter the body, but it derives benefit therefrom : ", 

            "[they are]", 

            "washing, anointing and regular motions [tashmish]. ", 

            "Three things are of the essence of the world to come : ", 

            "[they are]", 

            "the Sabbath, the sun and tashmish. ", 

            "Tashmish of what? ", 

            "Are we to suppose tashmish of the bed[2]? That weakens ! ", 

            "No ; tashmish of the orifices. ", 

            "Three things restore a man's [tranquillity of] mind : ", 

            "melodious sound, sight and smell. ", 

            "Three things enlarge a man's mind[3]:", 

            " a beautiful home, a beautiful woman and beautiful utensils. ", 

            "(Five and six and ten — mnemonic.) ", 

            "Five things are a sixtieth part of something else :", 

            " fire, honey, the Sabbath, sleep and a dream.", 

            " Fire is a sixtieth part of Gehinnom; honey a sixtieth of manna ; the Sabbath a sixtieth of the world to come ; sleep a sixtieth of death ; a dream the sixtieth of prophecy. ", 

            "Six things are a favourable symptom in an invalid :", 

            " sneezing, perspiration, abdominal motion, seminal emission, sleep and a dream. ", 

            "\"Sneezing\" — for it is written, ", 

            "\"His sneezings flash forth light\" (Job xli. 10). \"Perspiration\" — for it is written, \"In the sweat of thy face shalt thou eat bread\" (Gen, iii. 19). \"Abdominal motion\" — for it is written, \"He that is bent down shall speedily be loosed ; and he shall not go down dying into the pit\" (Is. li. 14). \"Seminal emission\" — for it is written, \"Seeing seed, he will prolong his days\" (ibid. liii. 10). \"Sleep\" — for it is written, \"I should have slept, then had I been at rest\" (Job iii. 13). \"A dream\" — for it is written, \"Thou didst cause me to dream[4] and make me to live\" (Is. xxxviii. 16). ", 

            "Six things cure an invalid from his sickness and their remedy is an [efficacious] remedy, viz. : ", 

            "cabbage, beet, a decoction of dried poley, the maw, the womb and the large lobe of the liver[5]. Some add : ", 

            "Also small fish ;", 

            " more than that, small fish make a man's whole body fruitful and strong[6]. ", 

            "Ten things cause an invalid to relapse and his sickness becomes worse, viz. : ", 

            "to eat the flesh of the ox, fat meat, roast meat, poultry, roasted egg ; also shaving, and partaking of cress, milk, cheese ; and bathing. Some add: ", 

            "Also nuts; others add: ", 

            "Also cucumbers. ", 

            "The school of R. Ishmael taught : ", 

            "Why are they called \"cucumbers\" [kishshuim] ? Because they are injurious [kashim] to the body like swords.", 

            " But it is not so ! ", 

            "For lo, it is written, \"And the Lord said unto her, Two nations are in thy womb\" (Gen. xxv. 23) — read not goyim \"nations,\" but geim \"lords\"; and Rab Judah said in the name of Rab: ", 

            "These are Antoninus and Rabbi[1] from whose table radish, lettuce and cucumbers were never absent either in Summer or Winter ! ", 

            "There is no contradiction ; the large ones [are injurious], the small ones [beneficial]. ", 

            "Our Rabbis have taught :", 

            " [If one dreams] there is a corpse in the house, there will be peace in the house ; that he was eating and drinking in the house, it is an auspicious omen for the house ; that he took a vessel from the house, it is an inauspicious omen for the house. ", 

            "Rab Pappa explained [the \"vessel\" to refer to] a shoe or sandal. ", 

            "Everything that the corpse takes away [if seen in a dream] is auspicious with the exception of a shoe or sandal[2]; and everything that the corpse gives is auspicious with the exception of dust and mustard[3]. ", 

            "[He who beholds] a place from which idolatry has been uprooted. ", 

            "Our Rabbis have taught : (Who sees a statue of Hermes says,", 

            " \"Blessed... Who hast shown long-suffering to those who transgress Thy will[4]\"),", 

            " [If he sees] a place from which idolatry has been uprooted, he should say, ", 

            "\"Blessed... Who hast uprooted idolatry from our land ; and as it has been uprooted from this place, so may it be uprooted from all places of Israel. And do Thou turn the heart of those who serve idols to serve Thee.\" ", 

            "But if this is outside the Land [of Israel], it is unnecessary to say \"And do Thou turn the heart of those who serve idols to serve Thee,\" because most of them are gentiles. ", 

            "R. Simeon b. Eleazar said : ", 

            "The benediction should also be uttered outside the Land, because they will in the future become converted ; as it is said, \"For then will I turn to the peoples a pure language\" (Zeph. iii. 9). ", 

            "Rab Hamnuna expounded :", 

            " Who sees the wicked Babylon should utter five benedictions.", 

            " If he sees Babylon, he says \"Blessed... Who hast destroyed wicked Babylon.\"", 

            " If he sees the palace of Nebuchadnezzar, he says", 

            " \"Blessed...Who hast destroyed the palace of Nebuchadnezzar.\" ", 

            "If he sees the den of lions or the fiery furnace, he says", 

            " \"Blessed ...Who hast performed miracles for our fathers in this place.\"", 

            " If he sees a statue of Hermes, he says", 

            " \"Blessed... Who hast shown long-suffering to those who transgress Thy will.\" ", 

            "If he sees a place [in Babylon] from which dust is being taken away[1], he says", 

            " \"Blessed...Who sayest and doest, Who doth decree and fulfil.\" ", 

            "When Raba saw asses carrying this dust, he struck them upon the back with his hand and exclaimed, ", 

            "\"Run, ye righteous, to perform the will of your Master.\" ", 

            "When Mar b. Rabina came to Babylon, he took up some earth in his mantle and cast it out, to fulfil that which was said, \"I will sweep it with the besom of destruction\" (Is. xiv. 23). ", 

            "Rab Ashe said : ", 

            "I had not heard that of Rab Hamnuna, but from my own mind I said all those benedictions.  "

        ], 

        [

            "R. Jeremiah b. Eleazar said : ", 

            "When Babylon was cursed, her neighbours were cursed ; but when Samaria was cursed, her neighbours were blessed. When Babylon was cursed, her neighbours were cursed ;", 

            " for it is written, \"I will also make it a possession for the bittern, and pools of water\" (ibid.)[2]. ", 

            "When Samaria was cursed, her neighbours were blessed ; for it is written, \"Therefore I will make Samaria a heap in the field, a place for the planting of vineyards\" (Micah i. 6). ", 

            "Rab Hamnuna also said :", 

            " Who beholds crowds of Israelites should say ", 

            "\"Blessed... Who art wise in secrets[3]\";", 

            " but [on beholding] crowds of idolaters he says, ", 

            "\"Your mother shall be ashamed\" etc. (Jer. 1. 12). ", 

            "The Rabbis have taught : ", 

            "Who sees crowds of Israelites should say ", 

            "\"Blessed... Who art wise in secrets,\" ", 

            "because their minds differ and their faces differ. ", 

            "Ben Zoma saw a crowd on top of the ascent of the Temple Mount and said, ", 

            "\"Blessed... Who art wise in secrets, and blessed...Who hast created all these to serve me[4].\" ", 

            "[Ben Zoma] used to say : ", 

            "How much labour Adam must have expended before he obtained bread to eat ! ", 

            "He ploughed, sowed, reaped, piled up the sheaves, threshed, winnowed, selected [the ears], ground, sifted [the flour], kneaded and baked, and after that he ate ; whereas I get up in the morning and find all this prepared for me. ", 

            "And how much labour must Adam have expended before he obtained a garment to wear ! ", 

            "He sheared, washed [the wool], combed, spun, wove, and after that he obtained a garment to wear ; whereas I get up in the morning and find all this prepared for me. ", 

            "All artisans[1] attend and come to the door of my house, and I get up and find all these things before me. ", 

            "He used to declare : ", 

            "What does a good guest say ? \"How much trouble has my host taken on my behalf ! How much meat he set before me ! How much wine he set before me ! How many cakes he set before me ! And all the trouble he took was only for my sake.\" ", 

            "But what does the bad guest say ? \"What trouble has my host taken ?", 

            " I ate one piece of bread ; I ate one slice of meat ; I drank one cup of wine; and whatever trouble my host experienced was only for the sake of his wife and children.\" ", 

            "What does one say concerning a good guest ? \"Remember that thou magnify his work, whereof men have sung\" (Job xxxvi. 24) ; ", 

            "and of a bad guest it is written, \"Men do therefore fear him ; he regardeth not any that are wise of heart\" (ibid. xxxvii 24). ", 

            "\"And the man was an old man in the days of Saul, stricken in years among men\" (I Sam. xvii. 12). Raba (other versions : Rab Zebid, Rab Osha'ya)[2] said : ", 

            "This refers to Jesse, the father of David, who went out with a crowd, came in with a crowd and expounded [Torah] with a crowd. ", 

            "'Ulla said : ", 

            "We have received a tradition that there is no crowd in Babylon.", 

            " It has been taught : ", 

            "A crowd must not consist of less than sixty myriads. ", 

            "Our Rabbis have taught :", 

            " Who beholds the Sages of Israel should say, \"Blessed... Who hast imparted of Thy wisdom to them that fear Thee\" ; but [on beholding] the wise men of other peoples, he says \"Blessed... Who hast given of Thy wisdom to Thy creatures[3].\"", 

            " Who beholds the kings of Israel should say, \"Blessed... Who hast imparted of Thy glory to them that fear Thee\"; but [on beholding] the kings of other peoples he says, \"Blessed... Who hast imparted of Thy glory to Thy creatures[3].\" ", 

            "R. Johanan said : ", 

            "A man should always bestir himself to run to meet the kings of Israel ; and not only the kings of Israel, but even to meet the kings of other peoples, for if he is worthy, he will distinguish between the kings of Israel and of other peoples[4]. ", 

            "Rab Sheshet was blind. Everybody went to greet a king, and Rab Sheshet arose and went with them. ", 

            "A certain Min met him and said,", 

            " \"Pitchers [go] to the river, where [go] the potsherds[1]?\"", 

            " He replied,", 

            " \"Come, see how I know things better than thou[2].\"", 

            " The first troop of soldiers passed by, and when a shout arose, the Min said to him,", 

            " \"Now the king is coming.\" ", 

            "Rab Sheshet answered,", 

            " \"He is not coming yet.\"", 

            " A second troop passed, and when a shout arose, the Min said to him, ", 

            "\"Now the king is coming.\"", 

            " Rab Sheshet answered,", 

            " \"He is not coming.\" ", 

            "A third troop passed, and while there was silence, Rab Sheshet said to him, ", 

            "\"Now certainly the king is coming.\" ", 

            "The Min asked him,", 

            " \"Whence hast thou this?\" ", 

            "He replied, \"Earthly kingship is like the Kingship of Heaven, ", 

            "of which it is written, 'Go forth, and stand upon the mount before the Lord. And behold, the Lord passed by, and a great and strong wind rent the mountains, and broke in pieces the rocks before the Lord ; but the Lord was not in the wind ; and after the wind an earthquake ; but the Lord was not in the earthquake ; and after the earthquake a fire ; but the Lord was not in the fire ; and after the fire a still small voice' (I Kings xix. 11f.).\" ", 

            "When the king arrived, Rab Sheshet began and uttered the benediction for him.", 

            " The Min said to him,", 

            " \"For one whom thou seest not thou dost pronounce a benediction!\" ", 

            "And what happened to that Min? ", 

            "Some say that ", 

            "his associates put his eyes out ; others declare that ", 

            "Rab Sheshet set his eyes upon him and he became a heap of bones. ", 

            "R. Shela flogged a certain man who had had intercourse with a gentile[3] woman ; ", 

            "so he went and laid a charge against him before the king, saying, ", 

            "\"There is a certain Jew who judges without the king's consent.\"", 

            " The king sent an official for him [to appear]. When R. Shela came he was asked,", 

            " \"For what reason didst thou flog this person?\"", 

            " He replied,", 

            " \"Because he had intercourse with a she-ass.\" ", 

            "They said to him,", 

            " \"Hast thou witnesses?\" ", 

            "He answered,", 

            " \"Yes.\"", 

            " Elijah[4] came in human guise and gave evidence. ", 

            "They said to him,", 

            " \"In that case, his punishment is death.\" ", 

            "He said to them, ", 

            "\"From the day we were exiled from our land, we have no power to inflict the death-sentence ; but you do with him as you please.\"", 

            " While they were considering the case, R. Shela commenced saying, ", 

            "\"Thine, O Lord, is the greatness and the power\" etc. (I Chron. xxix. 11). ", 

            "They asked him, ", 

            "\"What is it thou art saying?\"", 

            " He replied, ", 

            "\"I am saying, 'Blessed be the All-merciful Who has made earthly kingship like the Kingship of Heaven and has given you power and love of justice'.\" ", 

            "They said, ", 

            "\"The honour of the kingship is very dear to him.\"", 

            " They thereupon handed to him the staff[1] and said to him, ", 

            "\"Do thou act as judge.\" ", 

            "When he went out, the man said to him,", 

            " \"Does the All-merciful perform a miracle for such liars!\" ", 

            "He replied, ", 

            "\"Thou evil-doer !", 

            " Are not they called 'asses'? ", 

            "For it is written, 'Whose flesh is as the flesh of asses' (Ezek. xxiii. 20).\" ", 

            "[R. Shela] perceived that the man was going to tell them that he called them  asses. He said [to himself], ", 

            "\"That man is a pursuer, and the Torah has stated, If one seeks to kill thee, do thou kill him first[2]\" ; so he smote him with the staff and killed him. ", 

            "He then said,", 

            " \"Since a miracle was wrought for me with this verse, I will expound it.\" [He went to the House of Study and expounded][3]:", 

            " \"Thine, O Lord, is the greatness\" — that refers to the work of Creation ; for so it is stated, \"Who doeth great things past finding out\" (Job ix. 10).", 

            " \"And the power\" — that refers to the Exodus from Egypt ; as it is said, \"And Israel saw the great work\" etc. (Exod. xiv. 31). ", 

            "\"And the glory\" — that refers to the sun and moon which stood still for Joshua; as it is said, \"And the sun stood still, and the moon stayed\" (Josh. x. 13). ", 

            "\"And the victory\" [nesah] — that refers to the overthrow of Rome[4]; for so it is stated, \"And their life-blood [nesah] is dashed against My garments\" (Is. Ixiii. 3).", 

            " \"And the majesty\" — that refers to the battle at the valleys of Arnon ; as it is said, \"Wherefore it is said in the book of the Wars of the Lord : Vaheb in Suphah, and the valleys of Arnon\" (Num. xxi. 14)[5].", 

            " \"For all that is in heaven and earth\" — that refers to the war of Sisera ; as it is said, \"They fought from heaven, the stars in their courses fought against Sisera\" (Judges V. 20).", 

            " \"Thine is the kingdom, O Lord\" — that refers to the war of Amalek ; for so it is stated, \"The hand upon the throne of the Lord, the Lord will have war with Amalek from generation to generation\" (Exod. xvii. 16). ", 

            "\"And Thou art exalted\" — that refers to the war of Gog and Magog[1] ; for so it is stated, \"Behold I am against thee, O Gog, chief prince of Meshech and Tubal\" (Ezek. xxxviii. 3).", 

            " \"As head above all\" — Rab Hanan b. Raba said in the name of Rab[2] :", 

            " Even the waterman[3] is appointed by Heaven.", 

            " In a Baraita it is taught in the name of R. 'Akiba :", 

            " \"Thine, O Lord, is the greatness\" — that refers to the division of the Red Sea. \"And the power\" — that refers to the smiting of the first-born. \"And the glory\" — that refers to the giving of the Torah, \"And the victory\" — that refers to Jerusalem. \"And the majesty\" — that refers to the Temple.  "

        ], 

        [

            "Our Rabbis have taught : ", 

            "Who sees the houses of Israelites when inhabited says, \"Blessed... Who dost set the boundary of the widow[4]\" ; [but when he sees them] in ruins he says, \"Blessed be the true Judge.\"", 

            " [Who beholds] the houses of idolaters when they are inhabited says, \"The Lord will pluck up the house of the proud\" (Prov. xv. 25); [but when he sees them] in ruins he says, \"O Lord, Thou God, to Whom vengeance belongeth. Thou God to Whom vengeance belongeth, shine forth\" (Ps. xciv. 1 ). ", 

            "'Ulla and Rab Hisda were journeying along the road. When they reached the entrance of the house of Rab Hanna b. Hanilai, Rab Hisda broke down and sighed.", 

            " 'Ulla asked him, ", 

            "\"Why dost thou sigh?", 

            " For lo, Rab has said : ", 

            "A sigh breaketh half the body of a man ; as it is said, 'Sigh therefore, thou son of man, with the breaking of thy loins,' etc. (Ezek. xxi. 11); and R. Johanan[5] has said :", 

            " It even breaks the whole body ; as it is said, 'And it shall be, when they say unto thee, Wherefore sighest thou ? that thou shalt say, Because of the tidings, for it cometh ; and every heart shall melt' etc. (ibid. v. 12).\" ", 

            "He answered him, ", 

            "\"How should I not sigh ", 

            "[on beholding] a house in which there were sixty[6] cooks by day and sixty cooks by night and they baked for each person what he desired. ", 

            "Nor did he[7] ever take his hand away from his purse, thinking that ", 

            "perhaps there may come a poor man, the son of respectable people, and while he is reaching for his purse, he would be put to shame. ", 

            "Moreover it had four doors open to the four directions, and whoever entered hungry came out sated. ", 

            "He used also to cast wheat and barley outside during the years of drought, so that anybody who was ashamed to take it by day came and took it by night. ", 

            "And now that it is fallen into ruins, shall I not sigh?\"", 

            " He said to him, \"Thus spake R. Johanan :", 

            "From the day the Temple was destroyed, a decree was issued that the houses of the righteous should be destroyed ; as it is said, 'In mine ears said the Lord of hosts : Of a truth many houses shall be desolate, even great and fair, without inhabitant' (Is. v. 9). ", 

            "Also said R. Johanan[1]:", 

            " The Holy One, blessed be He, will restore them to habitation ; as it is said, 'A Song of Ascents. They that trust in the Lord are as Mount Zion' (Ps. cxxv. 1) — just as the Holy One, blessed be He, will restore Mount Zion to habitation, so will He restore the houses of the righteous to habitation.\"", 

            " He perceived that his mind was still not at rest, so he said to him,", 

            " \"It is enough for the slave to be like his master[2].\" ", 

            "Our Rabbis have taught: ", 

            "\"Who beholds the graves of Israel says[3]: ", 

            "\"Blessed... Who formed you in judgment, Who nourished you in judgment, sustained you in judgment, and gathered you in judgment, and will hereafter raise you in judgment.\" ", 

            "Mar b. Rabina concluded the benediction in the name of Rab Nahman[4] :", 

            " \"And knowest the number of you all in judgment, and will hereafter restore you to life and cause you to survive. Blessed... Who quickenest the dead.\" ", 

            "[Who beholds] the graves of idolaters says, \"Your mother shall be sore ashamed\" (Jer. 1. 12). ", 

            "R. Joshua b. Levi said : ", 

            "Who sees his friend after [an interval of] thirty days says, ", 

            "\"Blessed... Who hast kept us in life, and hast preserved us, and enabled us to reach this season.\" After [an interval of] twelve months he says, \"Blessed... Who quickenest the dead.\" ", 

            "Rab said : ", 

            "The dead is only forgotten from the heart after twelve months[5] ; as it is said, \"I am forgotten as a dead man out of mind ; I am like a lost vessel\" (Ps. xxxi. 13)[6]. ", 

            "Rab Pappa and Rab Huna b. Rab Joshua were journeying along the road and met Rab Hannina b. Rab Ika. They said to him,", 

            " \"Since we have seen thee, we will offer two benedictions on thine account :", 

            " 'Blessed... Who impartest Thy wisdom to them that fear Thee' and 'Blessed... Who hast kept us in life' etc.\"", 

            " He replied, ", 

            "\"I also, since I have seen you, deem you to be in my eyes like the sixty myriads of the house of Israel and say three benedictions on your account : the two you have uttered and also 'Blessed... Who art wise in secrets[1]'. \"", 

            " They said to him,", 

            " \"Art thou as wise as all that?\" ", 

            "They set their eyes on him and he died[2]. ", 

            "R. Joshua b. Levi said : ", 

            "Who beholds men smitten with a leprous eruption says, ", 

            "\"Blessed... Who variest the forms of Thy creatures.\"", 

            " It is quoted in objection :", 

            " Who beholds a negro, a red-spotted or white-spotted person, a hunchback, dwarfed or dropsical person says, \"Blessed... Who variest the forms of Thy creatures\" ;", 

            " but [on beholding] a person with an amputated limb, or blind, or flat-headed, or lame, or smitten with boils or a leprous eruption he says, \"Blessed be the true Judge\" !", 

            " There is no contradiction ; the former refers to one suffering thus from his mother's womb, the other to one suffering thus after birth. ", 

            "This is also proved from the fact that he teaches that [the man afflicted with leprous eruption] is like the person with an amputated limb[3]. Deduce from this [that the leper referred to in the Baraita is one who became diseased after birth]. ", 

            "Our Rabbis have taught : ", 

            "Who beholds an elephant, or monkey or long-tailed ape says, \"Blessed... Who variest the forms of Thy creatures[4].\" ", 

            "If he beholds beautiful works of creation and fine trees he says, \"Blessed... to Whom it is thus in Thy universe.\" ", 

            "For shooting stars [Zikin]. ", 

            "What means Zikin ? ", 

            "Samuel said : ", 

            "Kokeba di-Shebit[5].", 

            " Samuel also said :", 

            " The paths of heaven are as familiar to me as the streets of Nehardea[1], with the exception of the Kokeba di-Shebit, for I know not what that is. ", 

            "There is a tradition that it never passes through the constellation of Orion, for if it did the world would he destroyed. ", 

            "But we see that it does pass through !", 

            " It is its brightness that passes through, and so it seems as though it does actually pass through. ", 

            "Rab Huna b. Rab Joshua[2] said ;", 

            " It is the Veil [ Vilon] which is rent and rolled up, so that the light of the heaven [Rekia'] appears[3]. ", 

            "Rab Ashe said : ", 

            "A star disappears from one side of Orion and [the beholder] sees a companion star [appear] on the other side and is bewildered ; and thus it seems as though it had passed through [the constellation][4]. ", 

            "Samuel asked :", 

            " It is written \"Who maketh the Bear, Orion and the Pleiades\" (Job ix. 9) and it is written \"That maketh the Pleiades and Orion\" (Amos v. 8) ! ", 

            "How is that[5] ? ", 

            "Were it not for the heat of Orion, the world could not exist because of the coldness of the Pleiades, and were it not for the coldness of the Pleiades, the world could not exist because of the heat of Orion[6]. ", 

            "There is also a tradition : Were it not that the tail of the Scorpion was placed in the Fire-River[7], nobody who had been stung by a scorpion could live.", 

            " That is what the All-merciful said to Job, \"Canst thou bind the chains of the Pleiades, or loose the bands of Orion?\" (Job xxxviii. 31). ", 

            "What means Kimah [the Pleiades]? ", 

            "Samuel said : ", 

            "About a hundred [Keme'ah] stars ; ", 

            "some say : Which are gathered together, but others say : ", 

            "Which are scattered.", 

            " What means 'Ash [the Bear]? ", 

            "Rab Judah said : ", 

            "Juta[8]. ", 

            "What is Juta?", 

            " Some say :", 

            " The tail of a ram ; others say :", 

            " The head of a calf. ", 

            "But the more probable view is that of him who said, \"The tail of a ram\" ; for it is written, \"And the 'Ajish will be comforted for her children\" (ibid. V. 32)[9]. Hence it seems as if something is lacking [in the tail] "

        ], 

        [

            "it has the appearance of having been torn away [from the star] ;", 

            " and the reason that the 'Ajish follows the Kimah is that it says to it,", 

            " \"Give me back my children.\" ", 

            "For when the Holy One, blessed be He, sought to bring the flood upon the world. He took two stars from the Pleiades[1] and thus brought the flood upon the world ; and when He sought to stop it, He took two stars from the Bear and stopped it. ", 

            "But He should have restored [the original stars]!", 

            " \"A pit cannot be filled with its own clods[2]\"; or also,", 

            " \"An accuser cannot become a defender[3].\"", 

            " Then He should have created two other stars ! ", 

            "\"There is nothing new under the sun\" (Eccles. i. 9).", 

            " Rab Nahman said :", 

            " The Holy One, blessed be He, will hereafter restore them; as it is said, \"And the 'Ajish will be comforted for her children.\" ", 

            "And for earthquakes. ", 

            "What is an earthquake? ", 

            "Rab Kattina said : ", 

            "A subterranean rumbling.", 

            " Rab Kattina was journeying by the way, and when he reached the entrance of the house of a necromancer a rumbling noise broke forth.", 

            " He said, ", 

            "\"Does the necromancer know what this rumbling is?\" ", 

            "The latter called to him,", 

            " \"Kattina, Kattina ! Why should I not know?", 

            " When the Holy One, blessed be He, remembers His children who dwell in misery among the nations of the world. He causes two tears to descend to the Ocean, and the sound is heard from one end of the world to the other ; and that is the rumbling.\" ", 

            "Rab Kattina said, ", 

            "\"The necromancer lies and his words are false;", 

            " for in that case, there should be one rumbling noise followed by another[4]!\"", 

            " But it is not so ; there is really one rumbling noise followed by another, and the reason that Kattina did not acknowledge the necromancer's statement was that people should not be led astray after him. ", 

            "Rab Kattina himself explained ", 

            "[that the phenomenon was due to God] clapping His hands ; as it is said, \"I will also smite My hands together, and I will satisfy My fury\" (Ezek. xxi. 22).", 

            " R. Nathan says : ", 

            "The rumbling is due to His sighing; as it is said, \"I will satisfy My fury upon them, and I will be eased\" (ibid. v. 13). ", 

            "The Rabbis say : ", 

            "He treads upon the firmament ; as it is said, \"He giveth a noise, as they that tread grapes, against all the inhabitants of the earth\" (Jer. xxv. 30). ", 

            "Rab Aha b. Jacob[5] said : ", 

            "He presses His feet beneath the Throne of Glory ; as it is said, ", 

            "\"Thus saith the Lord, the heaven is My throne, and the earth is My footstool\" (Is. Ixvi. 1). ", 

            "And for thunders. ", 

            "What is thunder? ", 

            "Samuel said : ", 

            "The clouds in a whirl ; as it is said, \"The voice of Thy thunder was in the whirlwind ; the lightnings lighted up the world, the earth trembled and shook\" (Ps. Ixxvii. 19).", 

            " The Rabbis say[1] :", 

            " The clouds pouring water one into the other; as it is said, \"At the sound of His giving a multitude of waters in the heavens\" (Jer. x. 13). ", 

            "Rab Aha b. Jacob said : ", 

            "It is a mighty lightning-flash which strikes against a cloud and the latter is shattered into hail-stones. ", 

            "Rab Ashe said : ", 

            "The clouds are hollow[2] and a blast of wind comes and blows across their mouths, so it is like a blast across the mouth of a jar. ", 

            "The most probable view is that of Rab Aha b. Jacob, that the lightning strikes, the clouds are made to rumble and rain descends. ", 

            "And for storms. ", 

            "What is a storm?", 

            " Abbai said :", 

            " A hurricane ; and further said Abbai : ", 

            "There is a tradition that a hurricane never happens during the night. ", 

            "But we have seen it occurring !", 

            " It must have commenced in the daytime.", 

            " Abbai likewise said: ", 

            "There is a tradition that a hurricane does not last two hours; to fulfil that which was said, \"Trouble shall not rise up the second time\" (Nahum i. 9).", 

            " But we have seen it lasting [longer than that]!", 

            " It stopped in between[3]. ", 

            "For lightnings one says, \"Blessed... Whose strength and might fill the world.\" ", 

            "What is lightning? ", 

            "Raba said :", 

            " A flash.", 

            "Also said Raba[4]:", 

            " A single flash, a white flash, a green flash, and clouds which rise in the western corner and come from the south corner, and two clouds which rise one opposite the other, are all inauspicious. ", 

            "What is to be deduced therefrom? That one should offer supplication. ", 

            "This applies only to the night[5], but in the morning there is no significance in them. ", 

            "Rab Samuel b. Isaac said :", 

            "There is no significance in morning-clouds ; for it is written, \"Your goodness is as a morning cloud\" (Hosea vi. 4).", 

            " Rab Pappa[6] said to Abbai : But there is a proverbial expression,", 

            " \"If on opening the door [in the morning] there is rain, set down thy sack, O ass-driver, and lie on it[1]\"! ", 

            "There is no contradiction ; for this refers to [a sky] covered with heavy clouds, whereas the former refers to [a sky] covered with light clouds. ", 

            "R. Alexander said in the name of R. Joshua b. Levi :", 

            " Thunder was only created to break the pride of the heart ; as it is said, \"God hath so made it that men should fear before Him\" (Eccles. iii. 14). ", 

            "Also said R. Alexander in the nanie of R.[2]Joshua b. Levi :", 

            " Who sees the rainbow should prostrate himself upon his face; as it is said, \"As the appearance of the bow that is in the cloud...and when I saw it, I fell upon my face\" (Ezek. i. 28). In the West[3] they curse one who acts thus, because it has the appearance as though he worships the rainbow ; ", 

            "but he should certainly pronounce a benediction. ", 

            "What is the benediction ? \"Blessed. ..Who remembrest the Covenant.\"", 

            " It has been taught in a Baraita : R. Ishmael, the son of R. Johanan b. Baroka says:", 

            " [The benediction is, \"Blessed...] Who art faithful with Thy Covenant and fulfillest Thy word.\" ", 

            "Rab Pappa said: ", 

            "Let us therefore say both : \"Blessed ... Who remembrest the Covenant, art faithful with Thy Covenant and fulfillest Thy word.\" ", 

            "For mountains and hills...", 

            "he says, \"Blessed...Who hast made the Creation.\" Is it then to be supposed that all the other things hitherto mentioned do not belong to the work of Creation?", 

            " For lo, it is written, \"He maketh[4] lightnings for the rain\" (Ps. cxxxv. 7)! ", 

            "Abbai said : ", 

            "Connect them all and learn them together[5].", 

            " Raba said :", 

            " In the former instances he pronounces two benedictions : \"Blessed...Whose strength fills the world and Who hast made the Creation\" ; but here \"...Who hast made the Creation\" is applicable, but \"Whose strength fills the world\" is not applicable[6]. ", 

            "R. Joshua b. Levi said : ", 

            "Who sees the firmament in its purity[7] says, \"Blessed... Who hast made the Creation.\"", 

            " When is this? ", 

            "Abbai[8] said :", 

            " When it has rained the whole night and in the morning a north wind comes and clears the sky[9]. ", 

            "This is at variance with the statement of Rafram b. Pappa who said in the name of Rab Hisda : ", 

            "Since the Temple was destroyed, the firmament has never been seen in its purity ; as it is said, \"I clothe the heavens with blackness, and I make sackcloth their covering\" (Is. 1. 3). \n"

        ], 

        [

            "Our Rabbis have taught : ", 

            "He who sees the sun [starting] on its new circuit or the moon in its strength, or the stars in their courses, or the planets in their order says, \"Blessed...Who hast made the Creation.\"", 

            " And when is it [that the sun starts on its new circuit]? ", 

            "Abbai said : ", 

            "Every twenty-eight years when the cycle begins again, and the Spring equinox falls in Saturn on the night of the third day of the week, which is the beginning of the fourth day[1]. ", 

            "R. Judah states : ", 

            "He who beholds the ocean says, \"Blessed...Who hast made the ocean\" ", 

            "[but only when he beholds it at intervals.] At intervals of what length? ", 

            "Rammi b. Abba said in the name of R. Issac : ", 

            "Of thirty days. ", 

            "Also said Rammi b. Abba in the name of R. Isaac :", 

            " Who sees the Euphrates up to the Babylonian bridge says, \"Blessed...Who hast made the Creation\" ; ", 

            "but nowadays since the Persians have altered it[2], [that benediction is only to be said] from Be Shapor[3] onwards. Rab Joseph said :", 

            " From Ihi Dekira[4] onwards. ", 

            "Further said Rammi b. Abba : ", 

            "Who sees the Tigris from the bridge of Shaporstan[5] says, \"Blessed...Who hast made the Creation.\" ", 

            "Why [is the Tigris called] Hiddekel (Gen. ii. 14). ", 

            "Rab Ashe said :", 

            " Its waters are sharp [had] and swift [kal][6]. ", 

            "Why [is the Euphrates called] Perat? Because its waters are fruitful [parah] and multiply.", 

            " Rab said : ", 

            "The reason why the inhabitants of Mahoza[7] are so shrewd is because they drink the waters of the Tigris ; the reason why they are red-spotted is because they indulge in sexual intercourse in the daytime ; and the reason why their eyes are unsteady is because they dwell in dark houses[8]. ", 

            "For rain and good tidings he says, \"Blessed... Who art good and dispensest good.\" ", 

            "But is the benediction for rain \"Who art good and dispensest good\"? ", 

            "For lo, R. Abbahu has said (another version : It was taught in a Baraita) :", 

            " From what time do we say the benediction over rain ? From the time the bridegroom goes forth to meet his bride[1] ;", 

            " and what is the wording of the benediction ?", 

            " Rab Judah said : ", 

            "\"We give thanks unto Thee for every drop which Thou hast caused to descend for us\" ; and R. Johanan concluded it thus : ", 

            "\"Though our mouths were full of song as the sea... we could not sufficiently thank Thee, O Lord our God\" etc. until \"shall prostrate itself before Thee[2]. Blessed art Thou, O Lord, to Whom abundant thanksgivings are due.", 

            "\" Is it \"abundant thanksgivings\" and not \"all thanksgivings\"?", 

            " Raba declared:", 

            " I say \"God of thanks-givings.\" ", 

            "Rab Pappa said :", 

            " Let us therefore say both : \"Abundant thanksgivings and God of thanksgivings.\"", 

            " Still there is a contradiction[3]!", 

            " No, there is not; [the formula in the Mishnah] applies when he heard [that it had been raining], the other when he actually sees it. ", 

            "But if he heard [that it had been raining] it is good tidings, and our Mishnah states :", 

            " For good tidings one says, \"Blessed... Who art good and dispensest good[4]\"!", 

            " Nay, ", 

            "they both refer to when he actually sees it ; and there is no contradiction, [the formula in the Mishnah] applying when little rain fell, the other when there was a heavy downpour.", 

            " Or if thou wilt I can say that ", 

            "both refer to a heavy downpour ; and there is no contradiction, [the formula in the Mishnah] applying to a landowner[5], the other to one who is not. ", 

            "If he be a landowner, does he say the benediction \"Who art good and dispensest good\"?", 

            " For lo, our Mishnah teaches : ", 

            "He who has built a new house or bought new vessels says, \"Blessed... Who hast kept us in life, preserved us and caused us to reach this season.\" [If, however, the house had been built or the vessels bought] for himself and others, he says \"Who art good and dispensest good[6]\"! ", 

            "There is no contradiction; one refers to where there is a partnership, the other to where there is no partnership. And there is a teaching :", 

            " The summary of the matter is : Over things of his own he says \"Blessed... Who hast kept us in life and preserved us\" etc. ; over things which belong to him and another he says \"Blessed... Who art good and dispensest good.\" ", 

            "But in a case where there is not another [sharing] with him, does he not use the benediction \"Who art good and dispensest good\"? ", 

            "Lo, there is a teaching : Should they announce to him", 

            " \"Thy wife has given birth to a son,\" he says \"Blessed... Who art good and dispensest good[1]\" !", 

            " Even here, his wife [shares the joy] with him, because she has a preference for a son[2].", 

            " Come and hear : ", 

            "If his father dies and he is his heir, he first says, \"Blessed be the true Judge\" and then \"Blessed... Who art good and dispensest good\"! ", 

            "Here also there are brothers who share the inheritance with him[3]. ", 

            "Come and hear :", 

            " If the wine is changed [for a better kind during the meal] there is no necessity to utter another benediction; but if he changed his place[4] [and other wine is brought to him] he should utter a further benediction ; ", 

            "and Rab Joseph b. Abba said in the name of R. Johanan[5] :", 

            " Although it has been stated that if the wine is changed another benediction is unnecessary, still he says, \"Blessed... Who art good and dispensest good\" !", 

            " Here also there are the other members of the company who drink with him. ", 

            "He who has built a new house or bought new vessels, etc. ", 

            "Rab Huna said : ", 

            "This only applies if he has not similar vessels, but if he has similar vessels[6] there is no need for him to say a benediction.", 

            " R. Johanan declared : ", 

            "Even if he has similar vessels, he must say the benediction. "

        ], 

        [

            "From this it is to be deduced that if he bought and then made a further purchase, all agree that there is no necessity for a benediction[7]. ", 

            "Another version : Rab Huna said : ", 

            "his only applies where he did not buy and make a further purchase ; but if he bought and made a further purchase, there is no necessity for a benediction[1]. ", 

            "R. Johanan said : ", 

            "Even if he bought and made a further purchase, it is necessary to say the benediction. ", 

            "From this it is to be deduced that if he possesses vessels[2] and purchases more, all agree that he must say the benediction[3].", 

            " Against this is quoted : ", 

            "If he built a new house and he has not a similar one, or bought new vessels without possessing the like, he must say a benediction ; but if he has the like, he need not say the benediction. These are the words of R. Meir ;", 

            " R. Judah says :", 

            " In either case, a benediction is necessary !", 

            " It is quite right according to the first version ; for then Rab Huna agrees with R. Meir and R. Johanan with R. Judah. According to the latter version, however, it is right that Rab Huna agrees with R. Judah, but with whom is R. Johanan. in agreement[4]? ", 

            "Neither with R. Meir nor R. Judah[5]! ", 

            "R. Johanan can reply to thee :", 

            " It is obvious that according to R. Judah, if a man made a purchase and then a fresh purchase, he also must say a benediction [for the latter][6]; but the point of variance [between R. Judah and R. Meir] is where the man already possessed the article[2] and made a fresh purchase, to show the extreme view taken by R. Meir; for even if he made a purchase, already possessing a similar article, there is no necessity for a benediction, how much more unnecessary is it if he purchased and then made a fresh purchase. ", 

            "But let the conflict of opinion [in the Baraita between R. Meir and R. Judah] be in the case where the man bought an article and then purchased another and no benediction is necessary[7], to show the extreme view taken by R. Judah[8]! ", 

            "It is preferable to take the extreme view on the side of leniency. ", 

            "One says the benediction for a calamity apart from any attendant good. ", 

            "How is this ?", 

            " For instance, if a freshet swept his field[9], although it may be [eventually] beneficial inasmuch as the land is covered with alluvium and improves [in fertility], still for the time being it is a calamity. ", 

            "And for good fortune apart from any attendant evil. ", 

            "[How do we understand this?]", 

            "For instance, if he found treasure trove, although it is bad for him because the king will hear and deprive him thereof, still for the time being it is good for him.", 

            "If his wife is pregnant and he says, \"May it be Thy will that my wife bear a son,\" behold that is a vain prayer. ", 

            "Then prayer [in such circumstances] is of no avail !", 

            " Rab Joseph[1] quoted in objection : ", 

            "\"And afterwards she bore a daughter and called her name Dinah\" (Gen. xxx. 21). What means \"and afterwards\"? ", 

            "Rab said[2]: ", 

            "After Leah passed judgment on herself, saying, ", 

            "\"Twelve tribes are destined to issue from Jacob — six have issued from me and four from the handmaids, that makes ten ; if this child [which is expected from me] be a male, my sister Rachel will not even be like one of the handmaids[3].\"", 

            " Immediately [the child in the womb] was changed to a daughter; as it is said, \"And she called her name Dinah [judgment]\"! ", 

            "We may not quote a miraculous event [against the Mishnah]. ", 

            "Or if thou wilt I can say that the incident of Leah occurred within forty days [of conception], ", 

            "according to the teaching : ", 

            "During the first three days [of the conjugal act] a man may pray that [his seed] should not become abortive ; from the third to the fortieth day he may pray that a male-child shall be born to him ; from the fortieth day to the third month he may pray that it should not be a monstrosity[4]; from the third to the sixth month he may pray that it should not be a premature birth ; from the sixth to the ninth month he may pray that it should issue in safety.", 

            " But is it of any avail to pray [during the first forty days that it should be a male child]? ", 

            "For lo, R. Isaac b. R. Ammi[5] has said : ", 

            "If it is the man who first emits seed his wife bears a daughter ; but if the woman first emits seed she gives birth to a son ; as it is said, \"If a woman emits seed[6] and bare a male child\" (Lev. xii. 2)! ", 

            "With what are we here dealing ? For instance, if they both emit seed simultaneously. ", 

            "If he were on the way.", 

            "Our Rabbis have taught : It happened that Hillel the Elder was returning from a journey and heard a cry of lamentation in the city", 

            " and said, \"I am confident that it is not in my house\" ; ", 

            "and to him the Scriptural verse applies, \"He shall not be afraid of evil tidings ; his heart is steadfast, trusting in the Lord\" (Ps cxii. 7). ", 

            "Raba[1] said : ", 

            "Whenever thou expoundest this verse, it is to be explained from the first clause to the second and from the second to the first.", 

            " It is to be explained from the first clause to the second, thus : \"He shall not be afraid of evil tidings.\" Why? \"His heart is steadfast, trusting in the Lord.\"", 

            "It is to be explained from the second clause to the first, thus :", 

            " \"His heart is steadfast, trusting in the Lord\"; [therefore] \"he shall not be afraid of evil tidings.\" ", 

            "A certain disciple was following R. Ishmael b. R. Jose in the market-place of Zion. ", 

            "The latter noticed that he was afraid and said to him,", 

            " \"Thou art a sinner; for it is written, 'The sinners in Zion are afraid' (Is. xxxiii. 14).\" ", 

            "He replied,", 

            " \"But it is written, 'Happy is the man that feareth always' (Prov. xxviii. 14)!\" ", 

            "He said to him.", 

            " \"This is written in connection with words of Torah[2].\" ", 

            "R. Judah b. R. Nathan took up [his cloak] and followed Rabbi in the market-place of Tiberias. The latter noticed that he was afraid and sighed ; ", 

            "so he said[3], ", 

            "\"That fellow wants sufferings to befall him ;", 

            " for it is written, 'For the thing which I did fear is come upon me, and that which I was afraid of hath overtaken me' (Job iii. 25).\" ", 

            "[He replied,] \"But lo, it is written, ", 

            "'Happy is the man who feareth always'!\"", 

            " \"That is written in connection with words of Torah.\" ", 

            "He who enters a town should offer prayer twice. ", 

            "Our Rabbis have taught : On entering, what does he say?", 

            " \"May it be Thy will, O Lord our God, that Thou cause me to enter this town in peace\"", 

            " Having entered, he says, ", 

            "\"I give thanks before Thee, O Lord my God, for that Thou hast caused me to enter this town in peace.\" ", 

            "On desiring to depart, he says,", 

            " \"May it be Thy will, O Lord my God and God of my fathers, that Thou cause me to depart from this town in peace.\" ", 

            "Having left he says, ", 

            "\"I give thanks before Thee, O Lord my God, for that Thou hast caused me to depart from this town in peace ; and as Thou hast caused me to depart in peace, so do Thou conduct me in peace, uphold me in peace, and direct my steps in peace, and deliver me from every enemy and ambush by the way. [Let me obtain grace, loving-kindness, and mercy in Thine eyes and in the eyes of all who behold me. Blessed art Thou, O Lord, Who hearkenest unto prayer][1].\" ", 

            "Rab Mattenah said : ", 

            "This prayer only applies to a town where they do not administer justice and sentence to death[2]; but in a town where they do administer justice and sentence to death, there is no need for such a petition. ", 

            "Another version is : Rab Mattenah said : ", 

            "Even in a town where they administer justice and sentence to death [the prayer is necessary] ; because sometimes there may not chance to be anybody to plead in his favour[3]. ", 

            "Our Rabbis have taught : Who enters a bath-house says,", 

            " \"May it be Thy will, O Lord my God, to deliver me from this and anything similar, and may no disgrace or iniquity befall me; but should any disgrace or iniquity befall me, may my death be an atonement for all my sins.\" ", 

            "Abbai said : ", 

            "Let not a man speak thus, so as not to open his mouth to Satan[4]. ", 

            "For said R. Simeon b. Lakish, and it has been similarly taught in the name of R. Jose :", 

            "A man should never open his mouth to Satan. ", 

            "Rab Joseph said[5]: ", 

            "What is the Scriptural authority? For it is written, \"We should have been as Sodom, we should have been like unto Gomorrah\" (Is, i. 9). What did the prophet answer them? \"Hear the word of the Lord, ye rulers of Sodom\" (ibid. v. 10). ", 

            "When he leaves [the bathhouse], what does he say? ", 

            "R. Aha said[6] :", 

            " \"I give thanks before Thee, O Lord my God, because Thou hast delivered me from the fire.\" ", 

            "R. Abbahu entered a bath-house, and its floor gave way beneath him. A miracle occurred, and he stood upon a pillar and rescued a hundred and one men with one arm[7]. He exclaimed, ", 

            "\"This is what R. Aha meant[8].\" ", 

            "[As R. Aha said:]", 

            "Who goes in to have himself cupped should say,", 

            " \"May it be Thy will, O Lord my God, that this operation be a cure for me, and do Thou heal me for Thou art a faithful Healer and Thy cure is certain, since it is not the way of human beings to cure, but thus are they accustomed[1].\" ", 

            "Abbai declared :", 

            " Let not a man speak thus ; for there is a teaching of the school of R. Ishmael : ", 

            "[It is written,] \"Only he shall pay for the loss of his time, and shall cause him to be thoroughly healed\" (Exod. xxi. 19) ; from this [it follows] that a physician is given permission [by God] to cure.", 

            " When he rises [from the cupping], what does he say? ", 

            "R. Aha[2] declared, ", 

            "\"Blessed be He Who heals without pay.\"  "

        ], 

        [

            "Who enters a privy says[3], ", 

            "\"Be honoured, ye honoured and holy Beings who minister to the Most High ! Give glory ", 

            "to the God of Israel ; leave me while I enter and do my will, then shall I come unto you.\" ", 

            "Abbai said : ", 

            "Let not a man speak thus[4], lest they leave him and depart; ", 

            "but let him say, ", 

            "\"Guard me, guard me, help me, help me, support me, support me, wait for me, wait for me until I enter and come out, for such is the way of human beings.\" ", 

            "When he comes out, he says, ", 

            "\"Blessed... Who hast formed man in wisdom and created in him many orifices and vessels. It is revealed and known before the throne of Thy glory, that if one of these be opened, or one of those closed, it would be impossible [to exist and][5] to stand before Thee.\"", 

            " How is it to be concluded?", 

            " Rab said,", 

            " \"[Blessed art Thou, O Lord,] Who healest the sick.\" ", 

            "Samuel said: ", 

            "Does Abba[6] regard the whole world as sick[7]? ", 

            "Nay,", 

            " [the conclusion of the benediction should be : \"Blessed...] Who healest all flesh.\" ", 

            "Rab Sheshet said : [It should conclude : \"Blessed...] ", 

            "Who doest wondrously.\"", 

            " Rab Pappa said : ", 

            "Let us therefore say both : \"Who healest all flesh and doest wondrously.\" ", 

            "Who goes in to sleep upon his bed says from \"Hear, O Israel\" to \"And it shall come to pass, if ye shall hearken diligently\" ;", 

            " then he says[8] : \"Blessed... Who makest the bands of sleep to fall upon mine eyes, and slumber upon mine eyelids, and givest light to the apple of the eye. ", 

            "May it be Thy will, O Lord my God, to suffer me to lie down in peace and place my portion in Thy Torah ; and do Thou accustom me to the performance of the commandments and not to transgression ; and bring me not into the power of sin, iniquity, temptation or contempt ; and let the good impulse have dominion over me but not the evil impulse ; and do Thou deliver me from evil occurrence and sore diseases ; and let not evil dreams and lustful thoughts trouble me; and let my bed be perfect before Thee, and give light to mine eyes lest I sleep the sleep of death. Blessed art Thou, O Lord, Who givest light to the whole world in Thy glory.\" ", 

            "When he awakens he says : ", 

            "\"O my God, the soul which Thou hast given me is pure. Thou didst create it within me, Thou didst breathe it into me, Thou preservest it within me, and Thou wilt take it from me, but wilt restore it unto me hereafter. So long as the soul is within me, I will give thanks unto Thee, O Lord my God and God of my fathers, Sovereign of all worlds, Lord of all souls. Blessed art Thou, O Lord, Who restorest souls unto dead bodies[1].\" ", 

            "When he hears the cry of the cock let him say :", 

            " \"Blessed...Who hast given the cock intelligence to distinguish between day and night[2].", 

            "\" When he opens his eyes let him say: ", 

            "\"Blessed... Who openest the eyes of the blind.\"", 

            " When he straightens himself and sits up let him say : ", 

            "\"Blessed...Who loosest them that are bound.\"", 

            " When he has clothed himself let him say :", 

            "\"Blessed... Who clothest the naked.\"", 

            " When he raises himself let him say :", 

            " \"Blessed... Who raisest up them that are bowed down.\" ", 

            "When he descends [from the bed] to the ground ", 

            "let him say: \"Blessed... Who spreadest forth the earth above the waters.\" ", 

            "When he walks let him say : ", 

            "\"Blessed... Who hast made firm the steps of man.\" ", 

            "When he has tied up his shoes let him say: ", 

            "\"Blessed... Who hast supplied my every want.\"", 

            " When he has fastened his girdle", 

            " let him say : \"Blessed... Who girdest Israel with might.\" ", 

            "When he spreads the cloth upon his head let him say :", 

            " \"Blessed... Who crownest Israel with glory[3].\" ", 

            "When he wraps himself with the Sisit let him say :", 

            " \"Blessed... Who hast sanctified us by Thy commandments and hast commanded us to enwrap ourselves in the fringed garment.\" ", 

            "When he places the Tefillin upon his arm let him say :", 

            " \"Blessed... Who hast sanctified us by Thy commandments, and hast commanded us to lay the Tefillin\" ; ", 

            "upon the head let him say : ", 

            "\"Blessed... Who hast sanctified us by Thy commandments, and hast commanded us concerning the precept of the Tefillin.\" ", 

            "When he has washed his hands let him say :", 

            " \"Blessed... Who hast sanctified us by Thy commandments and commanded us concerning the washing of the hands.\" ", 

            "When he has washed his face let him say :", 

            " \"Blessed... Who removest the bands of sleep from mine eyes and slumber from mine eyelids. May it be Thy will, O Lord my God, to accustom me to Thy Torah and cause me to cleave to Thy commandments, and lead me not into the power of sin, iniquity, temptation or contempt ; and subdue my will that it be subservient to Thee ; and keep me far from an evil man and evil companion ; and cause me to cleave to the good impulse and a good companion in Thy universe ; and let me obtain this day, and every day, grace, favour and mercy in Thine eyes and in the eyes of all who behold me; and bestow loving kindnesses upon me. Blessed art Thou, O Lord, Who bestowest lovingkindnesses upon Thy people, Israel[1].\" ", 

            "A man is in duty bound, etc. ", 

            "What means : A man is in duty bound to utter a benediction for the bad even as he utters one for the good? ", 

            "Are we to suppose that", 

            " as for the good he says the benediction \"...Who art good and dispensest good,\" he is to make the same benediction for the bad? For lo, our Mishnah teaches :", 

            " For good tidings he says \"Who art good and dispensest good\" and For bad tidings he says \"Blessed be the true Judge\"! ", 

            "Raba said :", 

            " It is only necessary that he should receive [the bad] with gladness.", 

            " R. Aha[2] said in the name of R. Levi:", 

            "What is the Scriptural authority? \"I will sing of mercy and justice ; unto Thee, O Lord, will I sing praises\" (Ps. ci. 1) — if it be mercy[3], I will sing ; and if it be justice[4], I will sing.", 

            " R. Samuel b. Nahmani[5] said : ", 

            "It may be derived from the following: \"In the Lord, I will praise His word ; in God, I will praise His word\" (ibid. Ivi. 11)[6] — \"In the Lord, I will praise His word\" refers to His attribute of goodness; \"In God, I will praise His word\" refers to His attribute of retribution. ", 

            "R. Tanhum[7] said :", 

            " It may be derived from the following : \"I will lift up the cup of salvation and call upon the name of the Lord\" (ibid. cxvi. 13) [and] \"I found trouble and sorrow, but I called upon the name of the Lord\" (ibid. vv. 3f). ", 

            "The Rabbis say : It may be derived from the following : \"The Lord gave, and the Lord hath taken away ; blessed be the name of the Lord\" (Job i. 21). ", 

            "Rab Huna stated that Rab said[1] in the name of R. Meir, (and it has been similarly taught in the name of R. 'Akiba) :", 

            " A man should always accustom himself to say, \"Whatever the All-merciful does, He does for the best[2].\" ", 

            "As when R.'Akiba was journeying by the way, he came to a certain town and asked for hospitality, but it was refused him ; ", 

            "so he exclaimed, \"Whatever the All - merciful does is for the best.\" ", 

            "He went and spent the night in the field, having with him a cock, an ass and a lamp[3]. ", 

            "A gust of wind came and extinguished the lamp, a cat came and ate the cock, and a lion came and devoured the ass ; ", 

            "but he exclaimed,", 

            " \"Whatever the All-merciful does is for the best.\" ", 

            "That same night a band of robbers came and captured the town[4]. ", 

            "He thereupon said to them[5], ", 

            "\"Did I not tell you that whatever the Holy One, blessed be He, does is   "

        ], 

        [

            "all for the best!\" ", 

            "Rab Huna stated that Rab said[1] in the name of R. Meir : ", 

            "A man's words should always be few before the Holy One, blessed be He ; as it is said, \"Be not rash with thy mouth, and let not thy heart be hasty to utter a word before God ; for God is in heaven, and thou upon earth, therefore let thy words be few\" (Eccles. v. 1). ", 

            "Rab Nahman b. Rab Hisda expounded : ", 

            "What means that which is written, \"Then the Lord God formed man\" (Gen. ii. 7), the word wayyiser \"and He formed\" being spelt with two letters yod? The Holy One, blessed be He, created two impulses[6], one good and the other evil.", 

            " Rab Nahman b. Isaac objected :", 

            " Therefore since the word wayyiser is not mentioned in connection with the animal[7] it has no evil impulse,", 

            " and yet we see it injuring and biting and kicking ! ", 

            "Nay [the double yod is to be explained] according to the statement of R. Simeon b. Pazzi who said : ", 

            "Woe to me because of my Creator [yoseri][8], and woe to me because of my impulse [yisri][9].", 

            " Or [it may be explained] ", 

            "according to the statement of R. Jeremiah b. Eleazar who said : ", 

            "The Holy One, blessed be He, made Adam with two faces[1] ; as it is said, \"Behind and before hast Thou formed me\" (Ps. cxxxix. 5)[2]. ", 

            "\"And the rib, which the Lord God had taken from the man, made He a woman\" (Gen. ii. 22). Rab and Samuel [comment upon this] :", 

            " One declared that", 

            " it was a face [from which Eve was made] ; the other declared that", 

            " it was a tail[3]. It is right according to him who says that it was a face; that is what is written, \"Behind and before hast Thou formed me[4].\" But according to him who said it was a tail, what means \"Behind and before hast Thou formed me\"? It is [to be explained]", 

            " according to the statement of R. Ammi who said : ", 

            "\"Behind[5]\" refers to the work of creation, \"before\" to retribution[6]. ", 

            "It is right that \"behind\" may refer to the work of creation, for Adam was not created until the eve of the Sabbath ; but that \"before\" refers to retribution — retribution for what?", 

            " Are we to suppose the punishment of the serpent-incident? Lo, there is a teaching : Rabbi says :", 

            " With [the award of] greatness we begin with the most important ; but with a curse, we begin with the least important. ", 

            "With greatness we begin with the most important — for it is written, \"And Moses spoke unto Aaron, and unto Eleazar and unto Ithamar, his sons that were left, Take the meal-offering that remaineth\" etc. (Lev, x. 12). ", 

            "With a curse we begin with the least important — first the serpent was cursed, then Eve and then Adam[7]! ", 

            "Nay, the retribution in connection with the flood [is referred to] ; for it is written, \"And He blotted out every living substance which was upon the face of the ground, both man and cattle\" (Gen. vii. 23)[8]. ", 

            "It is quite right according to him who says that [Eve was created from] a face ; that is what is written wayyiser \"And He formed,\" spelt with a double yod. But according to him who said that it was from a tail, what means wayyiser? ", 

            "It is [to be explained] according to the statement of R. Simeon b. Pazzi who said :", 

            " Woe to me because of my Creator and woe to me because of my impulse.", 

            " It is quite right according to him who says that it was a face ; that is what is written, \"Male and female created He them\" (Gen. V. 2)[1]. But according to him who said it was a tail, what means \"Male and female created He them\"? It is [to be explained]", 

            " according to R. Abbahu who asked :", 

            " It is written \"Male and female created He them,\" and it is written, \"For in the image of God made He man\" (ibid. ix. 6). ", 

            "How is this? At first He planned to create two, but in the end only one was created. ", 

            "It is quite right according to him who says it was a face ; that is what is written, \"He closed up the place with flesh instead thereof \" (ibid. ii. 21). But according to him who said it was a tail, what means \"He closed up the place with flesh instead thereof\"?", 

            " R. Jeremiah (other versions : Rab Zebid ; Rab Nahman b. Isaac) said :", 

            " That was only necessary in the place of the wound[2]. ", 

            "It is quite right according to him who said it was a tail ; that is what is written, \"And He made [lit. built]\" (ibid. v. 22)[3]. But according to him who said it was a face, what means \"He made\"?", 

            " It is [to be explained] according to R. Simeon b. Menasya who expounded : ", 

            "What means, \"And the rib which the Lord God had taken from the man, made He [banah] a woman\"? It teaches that the Holy One, blessed be He, plaited her hair and brought her [adorned] to Adam ; for so in the sea-towns[4] they call plaits binyata[5]. ", 

            "Another explanation", 

            " of \"And He made [lit. built]\" — Rab Hisda said (another version : It was taught in a Baraita) :", 

            " This means that the Holy One, blessed be He, fashioned Eve like a store-building ; as the store is narrow above and broad below so as to receive the fruits, similarly is a woman narrow above and broad below so as to receive the child.", 

            " \"And He brought her unto the man\" (ibid.). R. Jeremiah b. Eleazar said[6] : ", 

            "This means that the Holy One, blessed be He, constituted Himself Adam's \"best man\"; ", 

            "hence the Torah teaches a rule of conduct, viz. : that an eminent man should accompany one of less importance as \"best man,\" and it will not injure [his dignity]. ", 

            "According to him who said [Eve was made from] a face, which of them[1] went in front? ", 

            "Rab Nahman b. Isaac said :", 

            " It is more probable that the masculine countenance went in front ; for there is a teaching :", 

            " A man should never walk behind a woman along the road, even his own wife[2]. Should a woman meet him on a bridge he should let her pass by on the side ; and whoever crosses a stream behind a woman will[3] have no portion in the world to come. ", 

            "Our Rabbis have taught:", 

            " He who pays money to a woman counting it from his hand into hers for the sake of gazing at her, even if he possess Torah and good deeds like Moses our teacher, he will not escape the punishment of Gehinnom ; as it is said, \"Hand to hand[4] the evil man shall not be unpunished\" (Prov. xi. 21) — he shall not escape the punishment of Gehinnom. ", 

            "Rab Nahman said : ", 

            "Manoah was an 'Am ha'ares; for it is written, \"And Manoah went after his wife\" (Judges xiii. 11).", 

            " Rab Nahman b. Isaac[5] retorted : ", 

            "But that is likewise true of[6] Elisha ; for it is written, \"And he arose and followed her\" (II Kings iv. 30) — here also he actually walked behind her ! ", 

            "Nay ; [it means that Elisha] followed her words and advice, and so also [in the instance of Manoah] he followed her words and advice. ", 

            "Rab Ashe said : ", 

            "With reference to what Rab Nahman said, viz. that Manoah was an 'Am ha'ares, he had not even learnt [the Scriptures which are taught] in an elementary school; as it is said, \"And Rebekah arose, and her damsels, and they rode upon the camels, and followed the man\" (Gen. xxiv. 61) — they went behind the man, not in front of him. ", 

            "R. Johanan said[7] : ", 

            "A man should walk behind a lion rather than behind a woman, behind a woman rather than behind an idolater, behind an idolater rather than behind a Synagogue when the Congregation is at prayer[8]. ", 

            "But this last is only meant when he is not carrying a load ; should he, however, be carrying a load, there is no objection. It is only meant when there is no other entrance ; but should there be another entrance, there is no objection. It is further only meant when he is not riding upon an ass ; but should he be riding upon an ass, there is no objection. It is likewise only meant when he is not wearing Tefillin ; but if he is wearing Tefillin, there is no objection. ", 

            "Rab said : ", 

            "The evil impulse is like a fly and dwells between the  two entrances of the heart ; as it is said, \"Dead flies make the ointment of the perfumers fetid and putrid\" (Eccles. x. 1). ", 

            "Samuel said :", 

            " It is like a kind of wheat [hittah] ; as it is said, \"Sin [hatt'at] croucheth at the door\" (Gen. iv. 7)[1]. ", 

            "Our Rabbis have taught : ", 

            "There are two reins in man, one prompting him to good, the other to evil.", 

            " It is probable that the good is on the right side and the bad on the left ; for it is written, \"A wise man's understanding is at his right hand; but a fool's understanding at his left\" (Eccles. x. 2). ", 

            "Our Rabbis have taught :", 

            " The reins prompt [the thought], the heart exercises intelligence, the tongue pronounces, the mouth completes [the words]. The gullet lets in and brings out all kinds of food[2], the windpipe produces voice, "

        ], 

        [

            " the lungs absorb all kinds of liquids, the liver arouses anger, the gall lets a drop fall upon it and stills it, the milt produces laughter, the large intestine grinds [food], the maw induces sleep and the nose awakens. Should the organ which induces sleep arouse from sleep, ", 

            "or should the organ which arouses from sleep induce sleep, the person pines away.", 

            " It has been taught : ", 

            "Should both of them induce sleep or arouse from sleep simultaneously, one immediately dies. ", 

            "There is a teaching : R. Jose of Galilee says[3] : ", 

            "The good impulse controls the righteous ; as it is said, \"My heart is wounded within me\" (Ps. cix. 22)[4]. ", 

            "The evil impulse controls the wicked ; as it is said, \"Transgression speaketh to the wicked, in the midst of the heart, There is no fear of God before his eyes\" (ibid, xxxvi. 2). Both impulses control average people ; as it is said, \"Because He standeth at the right hand of the needy, to save him from them that judge his soul\" (Ps. cix. 31)[1]. ", 

            "Raba said, ", 

            "\"The average people are, for instance, ourselves.\" ", 

            "Abbai said to him, ", 

            "\"The master does not leave life for any creature[2]!\" ", 

            "Raba also said :", 

            " The universe was only created for the completely wicked or the completely righteous[3]. Raba said :", 

            " Let a man know himself whether he is completely righteous or not. ", 

            "Rab said[4] :", 

            " The universe was only created for Ahab the son of Omri and for R. Hannina b. Dosa — ", 

            "for Ahab the son of Omri, this world[5]; and for R. Hannina b. Dosa, the world to come[6]. ", 

            "\"And thou shalt love the Lord thy God\" (Deut. vi. 5). ", 

            "There is a teaching : R. Eliezer says :", 

            " If it is stated \"With all thy soul,\" why is it stated \"With all thy might\"? ", 

            "And if it is stated \"With all thy might,\" why is it stated \"With all thy soul\"? ", 

            "But ", 

            "should there be a man whose body is dearer to him than his money[7], therefore it is stated \"With all thy soul[8]\"; and should there be a man whose money is dearer to him than his body, therefore it is stated \"With all thy might.\" ", 

            "R. 'Akiba says: ", 

            "\"With all thy soul\" [means,] even if He take thy soul[9]. ", 

            "Our Rabbis have taught : ", 

            "Once the wicked[10] government decreed that Israel should no longer occupy themselves with Torah. There came Pappos b. Judah and found R. 'Akiba attracting great assemblies and studying Torah. ", 

            "He said to him, ", 

            "\"'Akiba, art thou not afraid of the wicked government?\"", 

            " He replied,", 

            " \"I will tell thee a parable : To what is the matter like ? To a fox who was walking along the bank of the stream and saw some fishes gathering together from one place to another. He said to them,", 

            " 'From what are you fleeing?'", 

            " They answered, ", 

            "'From nets which men are bringing against us.' ", 

            "He said to them, ", 

            "'Let it be your pleasure to come up on the dry land, and let us, me and you, dwell together even as my fathers dwelt with your fathers.'", 

            " They replied, ", 

            "'Art thou he of whom they tell that thou art the shrewdest of animals?", 

            " Thou art not clever but a fool !", 

            " For if we are afraid in the place which is our life-element, how much more so in a place which is our death-element!' ", 

            "So also is it with us ; Now while we sit and study Torah, in which it is written, 'For that is thy life, and the length of thy days' (Deut. xxx. 20), we are in such a plight, how much more so if we go and neglect it!\" ", 

            "It is related that ", 

            "but a few days passed when they arrested R. 'Akiba and bound him in prison, and they arrested Pappos b. Judah and bound him by his side. ", 

            "'Akiba said to him,", 

            " \"Pappos, ", 

            "who brought thee here?\" ", 

            "He replied, ", 

            "\"Happy art thou, R. 'Akiba, inasmuch as thou hast been arrested on account of the Torah! But woe to me, Pappos, who has been arrested on trivial grounds!\" ", 

            "When they brought R. 'Akiba out to execution, it was the time for reading the Shema' ; and though they were combing his flesh with iron combs, he kept receiving upon himself the yoke of the Kingdom of Heaven[1]. ", 

            "His disciples said to him,", 

            " \"Our master, thus far[2]!\" ", 

            "He answered them,", 

            " \"Throughout my life I have been troubled about this verse, '[And thou shalt love the Lord thy God...] and with all thy soul' which means : Even if He take thy life. For said I,", 

            " 'When will it be in my power to fulfil it?' But now that the opportunity is mine, shall I not fulfil if?\"", 

            " He prolonged the word ehad[3] until his soul left [the body] with the word ehad [on his lips]. ", 

            "A Bat Kol issued forth and announced, ", 

            "\"Happy art thou, R. 'Akiba, that thy soul went out with the word ehad!\" ", 

            "The ministering angels spake before the Holy One, blessed be He, ", 

            "\"Such Torah, and such a reward?", 

            " 'From men, by Thy hand, O Lord, from men' etc. (Ps. xvii. 14)[4].\" ", 

            "He replied to them,", 

            " \"Their portion is in this life\" (ibid.). ", 

            "A Bat Kol issued forth and announced, ", 

            "\"Happy art thou, R. 'Akiba, for thou art destined for the life of the world to come!\" ", 

            "A man should not behave with levity towards the East Gate [of the Temple], since it is directed towards the Holy of Holies, etc. ", 

            "Rab Judah said in the name of Rab[5] : ", 

            "This is only meant from Sophim[6] inwards, and only applies to one who can see [the Temple].", 

            " It has been similarly reported : R. Abba b. R. Hijya. b. Abba said : Thus declared R. Johanan[1] : ", 

            "This is only meant from Sophim inwards, and only applies to one who can see [the Temple] and when there is no barrier [between him and it], and at the time when the Shekinah rests [upon the Sanctuary][2]. ", 

            "Our Rabbis have taught : ", 

            "He who wishes to exercise his natural functions, if in Judea he should not face East or West[3] but North or South ; if in Galilee, he should only face East or West. ", 

            "R. Jose, however, permits it [in any direction] because he used to say that", 

            " the prohibition only applies to one who can see [the Temple], when there is no barrier, and at the time when the Shekinah rests [upon the Sanctuary]. ", 

            "But the Sages prohibit it. ", 

            "Then the Sages agree with the first Tanna[4]!", 

            " The question of the side divides them[5]. ", 

            "There is another teaching :", 

            " He who wishes to exercise his natural functions, if in Judea he must not face East or West, but North or South ; but in Galilee, North and South are prohibited, East or West is permitted.", 

            " R. Jose, however, permits it [in any direction], because he used to say that", 

            " the prohibition only applies to one who can see [the Temple]. ", 

            "R. Judah says :", 

            " It is prohibited while the Temple is standing ; but when the Temple is no longer standing it is permitted. ", 

            "R. 'Akiba prohibits it in all circumstances.", 

            " Then R. 'Akiba agrees with the first Tanna! ", 

            "The question of outside the [Holy] Land is between them[6]. ", 

            "Rabbah[7] had bricks set up for him facing East and West[8]. Abbai went and put them facing North and South[9] ; but Rabbah[7] proceeded to put them right,", 

            " exclaiming,", 

            " \"Who is it that is troubling me ?", 

            " I agree with R. 'Akiba's view when he declared that", 

            " it is prohibited in all circumstances.\"  "

        ], 

        [

            "There is a teaching : R. 'Akiba said : ", 

            "Once I went into a privy behind R. Joshua and learnt from him three things.", 

            " I learnt that we should not evacuate East or West, but North or South. I learnt that we should not expose ourselves standing but sitting. I also learnt that we should not wipe ourselves with the right hand but with the left[1].", 

            " Ben 'Azzai said to him,", 

            " \"Wert thou so impudent with thy master?\" ", 

            "He replied,", 

            " \"It was a matter of Torah and I wished to learn.\" ", 

            "There is a teaching : Ben 'Azzai said :", 

            " I once went into a privy behind R. 'Akiba and learnt from him three things.", 

            " I learnt that we should not evacuate East or West, but North or South. I learnt that we should not expose ourselves standing but sitting. I also learnt that we should not wipe ourselves with the right hand but with the left. ", 

            "R. Judah said to him, ", 

            "\"Wert thou so impudent with thy master?\"", 

            " He replied, ", 

            "\"It was a matter of Torah and I wished to learn.\" ", 

            "Rab Kahana went and hid himself under Rab's bed ", 

            "and heard him converse [with his wife] and laugh and have intercourse. Rab Kahana said to him,", 

            " \"Abba's[2] mouth is like that of one who has never sipped a dish[3].\" ", 

            "Rab exclaimed,", 

            "\"Kahana, art thou here?", 

            " Go out ; for it is not proper!\" ", 

            "He replied, ", 

            "\"It is a matter of Torah and I wished to learn[4].\" ", 

            "Why should we not wipe with the right hand but only with the left? ", 

            "Raba said : ", 

            "Because the Torah was given with the right hand ; ", 

            "as it is said, \"At His right hand was a fiery law unto them\" (Deut. xxxiii. 2). ", 

            "Rabbah b. Bar Hannah said[5] : ", 

            "Because it is near the mouths[6]. ", 

            "R. Simeon b. Lakish said : ", 

            "Because he binds the Tefillin with it. ", 

            "Rab Nahman b. Isaac said:", 

            " Because he points to the accents of the Torah with it[7].", 

            " It is like [the discussion of] the Tannaim. R. Eliezer says : ", 

            "Because he eats with it. ", 

            "R. Joshua says : ", 

            "Because he writes with it. ", 

            "R. 'Akiba said : ", 

            "Because he points to the accents of the Torah with it. ", 

            "R. Tanhum b. Hanilai said : ", 

            "Whoever is modest in a privy is delivered from three things :", 

            " from serpents, scorpions and evil spirits[8] ; ", 

            "some say : Also his dreams will be such that his mind will be set at ease. ", 

            "There was a privy in Tiberias[1] which if two people entered, even by day, they came to harm. R. Ammi and R. Assi entered it separately and no harm befell them.", 

            " The Rabbis said to them, ", 

            "\"Were you not afraid?\" ", 

            "They answered, ", 

            "\"We were taught a charm[2]: a charm for the privy is modesty and silence ; a charm against sufferings is silence and prayer,\"", 

            " Abbai reared a lamb to accompany him into the privy[3]. ", 

            "But he should have roared a goat[4]! ", 

            "A satyr may be changed into a goat. ", 

            "Before Raba was appointed Principal [of the Seminary], the daughter of Rab Hisda[5] used to rattle a nut in a flask for him[6]; but afterwards when he ruled [over the Seminary] she made an aperture for him [in the wall] and placed her hand upon his head[7]. ", 

            "'Ulla said :", 

            " Behind a fence one may ease himself immediately[8]; but in an open place[9] [he may do it] so long as he can break wind without anybody hearing it.", 

            " Issi b. Nathan[10] taught as follows : Behind a fence [he may ease himself] so long as he can break wind without anybody hearing, but in an open place so long as nobody sees him. ", 

            "Against this [latter teaching] is quoted : ", 

            "They[11] may go out from the entrance of the olive-press and ease themselves behind a fence[8], and they remain in a state of ritual purity !", 

            " They take a more lenient view in connection with [those who supervise] ritual purity[12].", 

            " Come and hear:", 

            " [It has been taught:] To what distance may they[11] go and remain clean? So long as one can see them[13]!", 

            " It is different with food-stuffs whose purity [must be supervised], because the Rabbis take a more lenient view in such a case.", 

            " Rab Ashe asked :", 

            " What means \"so long as nobody sees him,\" as stated by Issi b. Nathan? So long as his neighbour cannot see the exposed part of the body, but he may see the man himself. ", 

            "A certain funeral-orator who went down [to deliver an address] in the presence of Rab Nahman said,", 

            " \"How modest was [the deceased] in his habits!\" ", 

            "Rab Nahman said to him, ", 

            "\"Didst thou ever go into a privy with him that thou knowest whether he was modest or not? ", 

            "For there is a teaching : He only is called modest who is so in a privy.\" ", 

            "But what had Rab Nahman to care about in this matter?", 

            " Because there is a teaching : As the dead are called to account [for their deeds], so are the funeral-orators[1] and they who respond [\"Amen\"] after them called to account. ", 

            "Our Rabbis have taught : ", 

            "Who is modest ? He who relieves himself at night in the same place where he relieves himself by day[2]. ", 

            "But it is not so ! ", 

            "For lo, Rab Judah said in the name of Rab : ", 

            "A man should always accustom himself [to perform his natural functions] morning and evening[3] so that it will be unnecessary for him to go far [and find a secluded spot]. ", 

            "And further, Raba used to go as far as a Mil by day ; but at night he would say to his attendant,", 

            " \"Prepare for me a place in the street of the town.\"", 

            " Similarly used R. Zera to say to his attendant,", 

            " \"See whether there is anybody behind the Seminary, as I wish to relieve myself\"! ", 

            "Read not [in the Baraita] \"in the same place,\" but read \"in the same manner that he relieves himself by day[4].\" ", 

            "Rab Ashe said : ", 

            "Even if thou retainest the words \"the same place\" [there is no contradiction, because it means,] it is only necessary [to proceed] to a corner[5]. ", 

            "It was stated above : \"Rab Judah said in the name of Rab : ", 

            "A man should always accustom himself [to perform his natural functions] morning and evening, so that it will be unnecessary for him to go far [and find a secluded spot].\" ", 

            "There is a teaching to the same effect : Ben 'Azzai says : ", 

            "Rise early and go out, and act likewise after dusk so that thou needest not go a distance ; ", 

            "feel the need and then sit down, but do not sit down and then [wait to] feel the need, for whoever does so, even should they practise sorcery in Aspamia[6] it will befall him. ", 

            "But should he through forgetfulness act thus, what is his remedy ?", 

            " On rising, let him say as follows, ", 

            "\"Not to me, not to me[1] ; no Tahim and no Tahtim[2] ; not these and not from these[3] ; no charms of a sorcerer and no charms of a sorceress.\" \n"

        ], 

        [

            " There is a teaching : Ben 'Azzai says : ", 

            "Lie upon any couch but not on the floor ; sit upon any seat except a beam[4]. ", 

            "Samuel said : ", 

            "Sleeping at dawn is like a steel edge to iron[5] ; evacuation at dawn is like a steel edge to iron. ", 

            "Bar Kappara used to sell proverbs for denarii : ", 

            "\"While thou art hungry, eat ; while thou art thirsty, drink ; while the cauldron is still hot, pour out[6].\" ", 

            "\"When the horn is sounded in [the market of] Rome[7], O son of a fig-seller, sell thy father's figs[8].\" ", 

            "Abbai said to the Rabbis : ", 

            "When you pass through the alleys of a town to go into the country, look neither to the one side nor the other, lest women be sitting there, and it is not proper to gaze at them. ", 

            "Rab Safra entered a privy. R. Abba came and emitted a sound at the door[9]. Rab Safra said to him,", 

            " \"Let the master enter.\"", 

            " After leaving, R. Abba said to him,", 

            " \"So far thou hast not brought in the demon ; but thou hast received the tradition about the demon[10]. ", 

            "Have we not learnt thus in the Mishnah : ", 

            "There was an open fire-place there [in the Temple-court], and a splendid privy ; and this was its splendid feature :", 

            " if it was found locked, it was known that somebody was in there, but if it was found open, it was known that it was vacant[11]. ", 

            "Hence infer that", 

            " it is not proper [to speak in a privy]!", 

            " But Rab Safra thought that", 

            " it was dangerous[12]; for there is a teaching[13] : Rabban Simeon b. Gamaliel says :", 

            " If the fecal discharge is kept back it causes dropsy, ", 

            "and if the fluid in the urinary duct is kept back it causes jaundice. ", 

            "R. Eleazar[1] entered a privy ; a certain Roman[2] came and pushed him. R. Eleazar got up and went out ; ", 

            "and a serpent came and tore out the [Roman's] gut. R. Eleazar applied to him the verse : ", 

            "\"Therefore will I give a man under thee\" (Is. xliii. 4) — read not adam \"a man\" but Edom \"an Edomite[3].\" ", 

            "\"And he said to kill thee, but it spared thee\" (I Sam. xxiv. 11)[4]. \"And he said\"!", 

            " It ought to be \"And I said\"; ", 

            "\"but it spared\"!", 

            " It ought to be \"but I spared.\" ", 

            "R. Eleazar said : Thus spake David to Saul, ", 

            "\"According to the Torah, thou art liable to be put to death, because thou art a pursuer ; and the Torah declares that ", 

            "if one comes to kill thee, kill him first[5]. ", 

            "But the modesty which is manifest in thee has spared thee.\" In what did [Saul's modesty] consist? For it is written, \"And he came to the sheep-cotes[6] by the way, where was a cave ; and Saul went in to cover his feet\" (ibid. V. 4).", 

            " It has been taught that", 

            " it was a fence within a fence and a cave within a cave.", 

            " \"To cover\" — R. Eleazar said: ", 

            "This teaches that he covered himself like a booth[7]. ", 

            "\"Then David arose, and cut off the skirt of Saul's robe privily\" (ibid. V. 5). ", 

            "R. Jose b. R. Hannina[8] said :", 

            " Whoever deals contemptuously with garments will in the end derive no benefit from them ; as it is said, \"Now King David was old and stricken in years ; and they covered him with clothes but he could get no heat\" (I Kings i. 1). ", 

            "\"If it be the Lord that hath stirred thee up against me, let Him accept an offering\" (I Sam. xxvi. 19). R. Eleazar said[9]: ", 

            "Thus spake the Holy One, blessed be He, to David, Thou callest Me a \"stirrer-up,\"", 

            " behold I will cause thee to stumble in a matter which even school-children know ; for it is written, \"When thou takest the sum of the children of Israel, according to their number, then shall they give every man a ranson for his soul unto the Lord... that there be no plague among them, when thou numberest them\" (Exod. xxx. 12). ", 

            "Immediately \"Satan stood up against Israel\" (I Chron. xxi. 1); for it is written, \"He stirred up David against them, saying, Go, number Israel and Judah\" (II Sam. xxiv. 1). ", 

            "But when he numbered them, he took no ransom from them ; and it is written, \"So the Lord sent a pestilence upon Israel from the morning even to the time appointed\" (ibid. v. 15).", 

            " What means \"the time appointed\" ?", 

            " Samuel[1] the Elder, the son-in-law of R. Hannina, said in the name of R. Hannina : ", 

            "From the time of slaying the continual offering until the time of the sprinkling of the blood. ", 

            "R. Johanan said : ", 

            "[It means] precisely until noon. ", 

            "\"And He said to the angel that destroyed the people, It is enough [rab]\" (ibid. v. 16). R. Eleazar said: Thus spake the Holy One, blessed be He, to the angel, ", 

            "Take for me the chief [rab] among them, so that through him I can punish them for their sins[2]. ", 

            "At that moment Abishai b. Zeruiah died, who was equal [in worth] to the majority of the Sanhedrin. ", 

            "\"And as he was about to destroy, the Lord beheld, and He repented Him\" (I Chron. xxi. 15). What did He behold? ", 

            "Rab said :", 

            " He beheld our father Jacob ; for it is written, \"And Jacob said when he beheld them\" (Gen. xxxii. 3). ", 

            "Samuel said :", 

            " He beheld the ashes of [the sacrifice substituted for] Isaac ; as it is said, \"God will provide[3] Himself the lamb\" (ibid. xxii. 8).", 

            " R. Isaac the Smith[4] said :", 

            " He beheld the money of the atonement; as it is said, \"And thou shalt take the atonement money from the children of Israel\" etc. (Exod. xxx. 16). ", 

            "R. Johanan said: ", 

            "He beheld the Temple ; for it is written, \"In the mount where the Lord is seen\" (Gen. xxii. 14). ", 

            "R. Jacob b. Iddi and R. Samuel b. Nahmani[5] differ in this matter; one declaring that ", 

            "He beheld the atonement money, the other declaring that ", 

            "He beheld the Temple. ", 

            "The more probable view is that of him who said that He beheld the Sanctuary ; because it is said, \"As it is said to this day, In the mount where the Lord is seen.\" ", 

            "Nor may one enter the Temple Mount with his staff\"...; nor may he use it as a short cut [koppendaria]. ", 

            "What means koppendaria? ", 

            "Raba said : ", 

            "A short cut, as the word implies[6]. ", 

            "But Rab Hanna[7] b. Adda said in the name of Rab Samma b. R. Mari: ", 

            "It is as people say, \"Instead of going round the row of houses[1], I will go through it\" ", 

            "Rab Nahman said in the name of Rabbah b. Abbuha:", 

            " If one enters a Synagogue not for the purpose of making it a short cut, he may use it in that manner. ", 

            "R. Abbahu said :", 

            " If it was originally a public path[2], it is permitted [as a short cut for all]. ", 

            "R. Helbo said in the name of Rab Huna: ", 

            "Who enters a Synagogue to pray is allowed to use it as a short cut ; as it is said, \"But when the people of the land shall come before the Lord in the appointed seasons, he that entereth by the way of the north gate to worship shall go forth by the way of the south gate\" (Ezek. xlvi. 9). ", 

            "And to expectorate on the Temple Mount is forbidden a fortiori. ", 

            "Rab Bebai said in the name of R. Joshua b. Levi[3] : ", 

            "Whoever expectorates on the Temple Mount in this time[4] is as though he expectorates into the pupil of his eye[5]; as it is said, \"And Mine eyes and My heart shall be there perpetually\" (I Kings ix. 3). ", 

            "Raba said : ", 

            "Expectoration is allowed in a Synagogue, because it is analogous to [the wearing of] a shoe —", 

            " just as [the wearing of] a shoe is prohibited on the Temple Mount but is permitted in a Synagogue, so is expectoration forbidden on the Temple Mount but permitted in a Synagogue.", 

            " Rab Pappa said to Raba (other versions : Rabina to Raba ; Rab Adda b. Mattena to Raba) : ", 

            "Why should one derive it [by analogy] from a shoe ; let him derive it from the short cut ! ", 

            "He replied : ", 

            "The Tanna derives it from the shoe, and thou sayest [it should be derived] from the short cut — ", 

            "how can that be?", 

            " For there is a teaching : ", 

            "A man must not enter the Temple Mount with his staff in his hand, his shoe upon his foot, and his money tied up in his cloth or in his money-bag thrown over his shoulder, nor may he make it a short cut ; and [the prohibition of] expectoration is derived a fortiori from the shoe — as in the case of a shoe which is not in itself contemptible the Torah declares, \"Put off thy shoes from off thy feet\" (Exod. iii. 5), must not expectoration, which is in itself contemptible, be all the more forbidden !", 

            " R. Jose b. Judah[6] says :", 

            " [This reasoning] is unnecessary ; for it is stated, \"For none might enter within the king's gate clothed with sackcloth\" (Esther iv. 2) — and is there not here an a fortiori deduction :", 

            " If it is thus with sackcloth which is not a disgusting thing in the presence of human beings, must not expectoration, which is disgusting in the presence of the supreme King of kings, be all the more prohibited !", 

            " [Rab Pappa] answered : This is the position I take up :", 

            " Let us derive a strict conclusion[1] from the instance, [of the shoe] and also from the instance [of the short cut] "

        ], 

        [

            "and I say that ", 

            "with reference to the Temple Mount where [the wearing of] a shoe is forbidden, let one derive [the prohibition against expectoration] from a shoe; but with reference to the Synagogue[2] where one is permitted [to wear] shoes, instead of deriving permission [to expectorate, by analogy] from a shoe, let him derive a prohibition [against expectoration, by analogy] from the short cut !", 

            " But, answered Raba :", 

            " [The Synagogue]", 

            " is analogous to his own house — as a man is concerned about anybody using his house as a short cut but is not concerned about expectoration or [the wearing of] shoes, so also with the Synagogue, ", 

            "as a short cut it is prohibited, but expectoration and [the wearing of] shoes are allowed. ", 

            "At the conclusion of every benediction in the Sanctuary they used to say \"For ever,\" etc. ", 

            "\"Why all this[3]? Because the response \"Amen\" was never made in the Sanctuary. ", 

            "Whence is it that \"Amen\" was never used as a response in the Sanctuary? As it is said, \"Stand up and bless the Lord your God from everlasting to everlasting\" (Nehem. ix. 5), ", 

            "and it continues, \"And let them say: Blessed be Thy glorious Name, that is exalted above all blessing and praise\" (ibid)[4].", 

            " It is possible to think that all benedictions should have one praise[5]; therefore there is a teaching to state, \"Above all[6] blessing and praise\" — for each benediction give Him praise. ", 

            "It was further ordained that a man should greet his friends by mentioning the Divine Name, etc. ", 

            "What means \"And it is said[7]\"? ", 

            "Shouldest thou argue that ", 

            "Boaz mentioned [the Divine Name in his salutation] of his own accord[8], come and hear: \"The Lord is with thee, thou mighty man of valour\" (Judges vi. 12). ", 

            "Shouldest thou argue that", 

            " it was an angel that spake to Gideon[1], come and hear : \"Despise not thy mother[2] when she is old\" (Prov. xxiii. 22). ", 

            "And it is stated, \"It is time for the Lord to work ; they have made void Thy Law\" (Ps. cxix. 126). ", 

            "Raba said : ", 

            "This verse is to be explained from the first clause to the second, and from the second to the first. ", 

            "It is to be explained from the first clause to the second, thus : ", 

            "\"It is time for the Lord to work\" ; why? Because \"they have made void Thy Law.\"", 

            " It is to be explained from the second to the first, thus:", 

            " \"They have made void Thy Law\"; why? Because \"It is time for the Lord to work.\" ", 

            "There is a teaching : Hillel the Elder says : ", 

            "When people collect [learning], do thou scatter ; when they scatter [learning], do thou collect[3].", 

            " If thou seest a generation to which Torah is dear, do thou scatter ; as it is said, \"There is that scattereth, and yet increaseth\" (Prov. xi. 24); but if thou seest a generation to which Torah is not dear, do thou collect ; as it is said, \"It is time for the Lord to work ; they have made void Thy Law.\" ", 

            "Bar Kappara expounded[4] : ", 

            "\"If goods are cheap, hasten[5] and buy them.\" \"In a place where there is no man, be a man[6].\" ", 

            "Abbai said ; Infer from this that ", 

            "where there is a man, do not be a man[7]. ", 

            "This is evident ! ", 

            "No, it is necessary for the case where the two of them are of equal standing[8]. ", 

            "Bar Kappara expounded : ", 

            "Which is a brief Scriptural passage upon which all the principles of the Torah depend? \"In all thy ways acknowledge Him, and He will direct thy paths\" (ibid. iii. 6). ", 

            "Raba said :", 

            " Even for a matter of transgression[1].", 

            " Bar Kappara expounded : ", 

            "A man should always teach his son a clean and light trade[2].", 

            "Which is such?", 

            " Rab Hisda[3] said : ", 

            "Needle-stitching[4]. ", 

            "There is a teaching: Rabbi[5] says : ", 

            "A man should never multiply friends[6] in his house; as it is said, \"There are friends that one hath to his own hurt\" (Prov. xviii. 24). ", 

            "There is a teaching : Rabbi says :", 

            " Let not a man appoint a steward over his house ; for if Potiphar had not appointed Joseph steward over his house, he would not have experienced the incident [of his wife's temptation]. ", 

            "There is a teaching : Rabbi says : ", 

            "Why does the section of the Nazirite adjoin the section of the woman suspected of adultery[7]? To tell thee that whoever sees such a woman in her disgrace should separate himself from wine[8]. ", 

            "Hezekiah b. R. Parnak said in the name of R. Parnak[9] in the name of R. Johanan : ", 

            "Why does the section of the woman suspected of adultery adjoin the section of the offerings and tithes ? To tell thee that", 

            " whoever has offerings and tithes and does not hand them to the priest will in the end require the services of a priest in the matter of his wife; as it is said, \"And every man's hallowed things shall be his[10]\" (Num. v. 10) and next to it is, \"If any man's wife go aside\" (ibid. v. 12). ", 

            "Not only that, but in the end he will be in need of the offerings and tithes[11] ; as it is said, \"And every man's hallowed things shall be his[12].\" ", 

            "Rab Nahman b. Isaac[13] said : ", 

            "Should he duly hand them over, in the end he will grow rich ; as it is said, \"Whatever any man giveth the priest, it shall be his\" (Num. v. 10) — i.e. much wealth shall be his. ", 

            "Rab Huna b. Berekiah said in the name of R. Eleazar ha-Kappar : ", 

            "Whoever associates the name of Heaven with his trouble[1], his substance will be doubled for him ; as it is said, \"And the Almighty be thy treasure, and precious[2] silver unto thee\" (Job xxii. 25). ", 

            "R. Samuel b. Nahmani said : ", 

            "His sustenance will fly to him like a bird ; as it is said, \"And precious silver unto thee.\" ", 

            "[3]R. Tabi said in the name of Josiah : ", 

            "Whoever relaxes from words of Torah will have no strength to stand in the day of trouble; as it is said, \"If thou faint in the day of adversity, thy strength is small indeed\" (Prov. xxiv. 10). ", 

            "R. Ammi[4] b. Mattenah said in the name of Samuel : ", 

            "Even [if he relax from] a single commandment ; as it is said, \"If thou faint\" — i.e. in any single instance. ", 

            "Rab Safra said : R. Abbahu related that", 

            " when Hananyah[5], the nephew of R. Joshua, went to the Diaspora[6], he used to intercalate the years[7] and fix the new moons outside the [Holy] Land.", 

            " They sent two disciples of the wise to him, R. Jose b. Kippar, and the grandson of Zechariah b. Kabutal. ", 

            "When he saw them, he asked, ", 

            "\"Why have you come?\"", 

            " They answered, ", 

            "\"To study Torah have we come.\"", 

            " He issued a proclamation[8].", 

            " \"These men are the famous men of the generation and their fathers ministered in the Temple ; as we have learnt : ", 

            "Zechariah b. Kabutal says,", 

            " 'Often have I read from the Book of Daniel before [the High Priest][9]'.\" ", 

            "Hananyah began to declare certain things unclean, and they pronounced them clean ; he forbade certain things, and they declared them permissible. ", 

            "He thereupon proclaimed concerning them, ", 

            "\"These men are worthless and men of no standing [and their fathers defiled the High Priesthood][10].\"", 

            " They said to him, ", 

            "\"Thou hast already built up [our reputation here] and thou canst not pull down ; thou hast already raised a fence and thou canst not make a breach.\" ", 

            "He said to them,", 

            " \"Why, when I declare something unclean, do you pronounce it clean, and when I forbid you permit?\" ", 

            "They said to him,", 

            " \"Why dost thou intercalate years and fix new moons outside the [Holy] Land?\" ", 

            "He replied,", 

            " \"Did not 'Akiba b. Joseph act similarly[1]?\"", 

            " They said to him, ", 

            "\"Keep R. 'Akiba out of it, because he left not his equal in the land of Israel[2].\" ", 

            "He said to them,", 

            " \"I also have not left my equal in the land of Israel.\" ", 

            "They said to him, ", 

            "\"The kids which thou didst leave behind have grown into goats with horns; and they have sent us to thee, saying to us", 

            " 'Go, tell him in our name[3];", 

            " if he obeys, well and good ; but if not, let him be excommunicated.  "

        ], 

        [

            " Tell also our brethren in the Diaspora[4];", 

            " if they obey, well and good ; but if not, let them ascend a mountain[5], let Ahiyyah[6] build an altar and Hananyah play the harp[7], and let them all repudiate [their Judaism], declaring that", 

            " they have no lot with the God of Israel'.\"", 

            " Immediately all the people broke forth into loud weeping and said,", 

            " \"God forbid!", 

            " We have a lot with the God of Israel.\" ", 

            "Why all this? ", 

            "Because it is said, \"For out of Zion shall go forth the law, and the word of the Lord from Jerusalem\" (Is. ii. 3). ", 

            "It is quite right that Hananyah declared something unclean and they pronounced it clean ; that is merely taking the stricter view. But how could he declare anything unclean and they pronounce it clean? ", 

            "For lo, there is a teaching: ", 

            "If a Sage declares anything unclean, his colleague is not allowed to pronounce it clean ; and if he declares it forbidden, his colleague is not allowed to pronounce it permissible! ", 

            "They thought [to act thus] ", 

            "so that the people may not be led by him. ", 

            "Our Rabbis have taught : ", 

            "When our Rabbis entered the vineyard of Jabneh[8], there were present R. Judah, R. Jose, R. Nehemiah and R. Eliezer[1], the son of R. Jose of Galilee. They all began to expound Torah in honour of the hospitality [which had been extended to them].", 

            " R. Judah, the chief of orators[2] in every place, began with the honour of the Torah and expounded : ", 

            "\"Now Moses used to take the tent and pitch it without the camp\" (Exod. xxxiii. 7). Can we not use here an a fortiori argument : If of the Ark of God, which was never more than twelve Mil[3] distant, the Torah declares, ", 

            "\"Everyone that sought the Lord went out unto the tent of meeting, which was without the camp\" (ibid.), how much more so[4], the disciples of the wise who go from city to city and from province to province to study Torah! ", 

            "[5]\"And the Lord spoke unto Moses face to face\" (ibid. v. 11). ", 

            "R. Isaac said : ", 

            "The Holy One, blessed be He, spake unto Moses, ", 

            "\"Moses, I and thou will discuss aspects[6] of Halakah.\"", 

            " Another version : Thus spake the Holy One, blessed be He, unto Moses,", 

            " \"In the same manner that I have shown thee a cheerful countenance, do thou likewise show Israel a cheerful countenance, and restore the tent to its place.\"", 

            " \"And he would return into the camp\" etc. (ibid.). ", 

            "R. Abbahu said : The Holy One, blessed be He, spake to Moses,", 

            " \"Now will they say, The Master is angry[7] and the disciple is angry[8]; what will become of Israel?", 

            " If thou wilt restore the tent to its place [within the camp], well and good ; but if not, Joshua the son of Nun, thy disciple, will minister in thy stead.\" ", 

            "That is what is written, \"And he would return into the camp[9].\" ", 

            "Raba said :", 

            " Nevertheless the word did not go forth from Him in vain ; as it is said, \"But his minister Joshua, the son of Nun, a young man, departed not out of the tent\" (ibid.). ", 

            "Further did R. Judah begin with the honour of the Torah and expound : ", 

            "\"Attend and hear; this day thou art become a people unto the Lord thy God\" (Deut. xxvii. 9). ", 

            "But was it on that day that the Torah had been given to Israel[10]? ", 

            "Was that not the completion of forty years! ", 

            "But it is intended to teach thee that ", 

            "every day is the Torah endeared to them who study it as on the day that it was given on Mount Sinai. ", 

            "R. Tanhum b. R. Hiyya, of the town of Acco, said : ", 

            "Thou mayest know from this that should a man recite the Shema' morning and evening, but omit it a single evening, he is like one who has never recited it at all. ", 

            "\"Attend [hasket]\" — i.e. \"form classes[1]\" and occupy yourselves with Torah, because Torah is only acquired in a class. ", 

            "This is in accord with the statement of R. Jose b. R. Hannina who said :", 

            " What means that which is written, \"A sword is upon the boasters [baddim] and they shall become fools\" (Jer. 1. 36)? A sword is upon the enemies of the disciples of the wise[2] who sit separately [bad wa-bad] and study Torah.", 

            " Not only so, but they become foolish ; for it is written here \"And they shall become fools\" and in another passage it is written, \"For that we have done foolishly\" (Num. xii. 11)[3].", 

            "[not translated]", 

            " If thou wilt I can quote the following: \"The princes of Zoan are become fools\" (Is. xix. 13). ", 

            "Another explanation of", 

            " \"Attend [hasket] and hear, O Israel\" (Deut. xxvii. 9) — i.e. submit to blows [kattetu] on behalf of the words of Torah ; according to the statement of R. Simeon b. Lakish ", 

            "who said : ", 

            "Whence is it learnt that the words of Torah endure only with him who would suffer death on its behalf? As it is said, \"This is the law : when a man dieth in a tent\" (Num. xix. 14)[4]. ", 

            "Another explanation of ", 

            "\"Attend [hasket] and hear, O Israel\": Be silent [has] and then discuss [kattet];", 

            " according to the statement of Raba who said : ", 

            "A man should always study Torah first and afterwards meditate thereon. ", 

            "The school of R. Jannai said : ", 

            "What means that which is written, \"For the churning of milk bringeth forth curd, and the wringing of the nose bringeth forth blood ; so the forcing of wrath bringeth forth strife\" (Prov. xxx. 33)? ", 

            "With whom dost thou find the cream of Torah? With him who spat out for its sake the milk which he sucked from his mother's breast[5]. ", 

            "\"And the wringing of the nose bringeth forth blood\" — a disciple with whom his master is the first time angry[6] but he remains silent [under the rebuke] is worthy to distinguish between impure and pure blood[7].", 

            " \"So the forcing of wrath bringeth forth strife\" — a disciple with whom his master is the first and second time angry but he remains silent [under the rebuke] is worthy to distinguish between suits involving money and suits involving life.", 

            " For there is a Mishnaic teaching: R. Ishmael says : ", 

            "Who wishes to grow wise should study money-suits, for there is no branch of Torah more [complex] than these ; they are like a well[1]. ", 

            "R. Samuel b. Nahmani said : ", 

            "What means that which is written, \"If thou hast done foolishly in lifting up thyself, or if thou hast planned devices [zamam], lay thy hand upon thy mouth\" (Prov. xxx. 32)? Everyone who makes himself foolish[2] for the sake of words of Torah will in the end be lifted up ; but if he muzzles [zamam] his mouth[3], he will have to put his hand to his mouth[4]. ", 

            "R. Nehemiah began [to speak] in honour of the hospitality and expounded : ", 

            "What means that which is written, \"And Saul said unto the Kenites, Go, depart, get you down from among the Amalekites, lest I destroy you with them ; for ye showed kindness to all the children of Israel, when they came up out of Egypt\" (I Sam. XV. 6)? Can we not use here an a fortiori argument :", 

            " If Jethro[5], who only befriended Moses for his own honour, is treated with so much consideration, how much more so one who entertains a disciple of the wise in his house, giving him to eat and drink, and allowing him to enjoy his possessions! ", 

            "R. Jose began [to speak] in honour of the hospitality and expounded :", 

            " \"Thou shalt not abhor an Edomite, for he is thy brother; thou shalt not abhor an Egyptian, because thou wast a stranger in his land\" (Deut. xxiii. 8). Can we not use here an a fortiori argument?", 

            " If the Egyptians are not to be abhorred, who only befriended the Israelites for their own needs — as it is said, \"And if thou knowest any able men among them, then make them rulers over my cattle\" (Gen. xlvii. 6) — how much more so, one who entertains a disciple of the wise in his house, giving him to eat and drink, and allowing him to enjoy his possessions! ", 

            "R. Eliezer, the son of R. Jose of Galilee, began [to speak] in honour of the hospitality and expounded : ", 

            "\"And the Lord blessed Obed-Edom and all his house...because of the Ark of God\" (II Sam. vi. llf.). Can we not use here an a fortiori argument?", 

            " If the Ark which neither ate nor drank, but which Obed-Edom swept and besprinkled[1], brought him a blessing, how much more so one who entertains a disciple of the wise, giving him to eat and drink, and allowing him to enjoy his possessions !", 

            " What was the blessing wherewith He blessed him ? ", 

            "R. Judah b. Zebida said :", 

            " It refers to Hamot[2] and her eight daughters-in-law who each bore six children at one birth ;  "

        ], 

        [

            "as it is said, \"Peullethai the eighth son\" (I Chron. xxvi. 5), and it is written \"For God blessed him\" (ibid.), \"All these were the sons of Obed-Edom, they and their sons and their brethren, able men in strength for the service ; threescore and two of Obed-Edom\" (ibid. v. 8)[3]. ", 

            "R. Abin the Levite[4] said :", 

            " Whoever forces fate[5], fate will force him; but whoever yields to fate, fate yields to him. So was it with Rabbah and Rab Joseph ;", 

            " for Rab Joseph [was nicknamed] \"Sinai[6]\" and Rabbah \"the uprooter of mountains[7].", 

            "\"The time needed them[8]; so [the electors] sent [a message] there[9],", 

            " \"Of 'Sinai' and 'the uprooter of mountains,' which should be given preference?\" ", 

            "They returned answer, ", 

            "\"'Sinai' should be preferred, because all stand in need of an owner of wheat[10].\" ", 

            "Nevertheless Rab Joseph did not accept the offer, because the Chaldeans[11] told him,", 

            " \"Thou wilt reign only two years[12].\"", 

            " Rabbah ruled two and twenty years[13], and then Rab Joseph two and a half; ", 

            "but all the years that Rabbah ruled he never called a cupper to his house[14]. ", 

            "R. Abin the Levite also said :", 

            " What means that which is written, \"The Lord answer thee in the day of trouble; the name of the God of Jacob set thee up on high\" (Ps. xx. 2)? The God of Jacob, but not the God of Abraham and Isaac ! From this we learn that the owner of a beam should go in with the heaviest part of it[1]. ", 

            "R. Abin the Levite also said : ", 

            "Whoever partakes of a meal at which a disciple of the wise is present is as though he partakes of the lustre of the Shekinah; as it is said, \"And Aaron came, and all the elders of Israel, to eat bread with Moses' father-in-law before God\" (Exod. xviii. 12). ", 

            "Did they eat before God? ", 

            "Was it not before Moses that they ate? ", 

            "But it means to tell thee that ", 

            "whoever partakes of a meal at which a disciple of the wise is present is as though he partakes of the lustre of the Shekinah. ", 

            "R. Abin the Levite also said : ", 

            "One who takes leave of his friend should not say to him, \"Go in peace\" but \"Go to peace\"; ", 

            "because in the case of Jethro who said to Moses \"Go to peace\" (Exod. iv. 18), the latter advanced and prospered ; but in the case of David who said to Absalom \"Go in peace\" (II Sam. xv. 9), the latter went and was hanged. ", 

            "R. Abin the Levite also said : ", 

            "One who takes leave of the dead should not say to him, \"Go to peace\" but \"Go in peace\" ; as it is said, \"But thou shalt go to thy fathers in peace\" (Gen. xv. 15). ", 

            "R. Levi b. Hiyya said[2]: ", 

            "He who goes out from the Synagogue and enters the House of Study to occupy himself with Torah is worthy to receive the presence of the Shekinah; as it is said, \"They go from strength to strength, every one of them appeareth before God in Zion\" (Ph. Ixxxiv. 8). ", 

            "R. Hiyya b. Ashe said in the name of Rab[3] : ", 

            "The disciples of the wise have rest neither in this world nor in the world to come; as it is said, \"They go from strength to strength, every one of them appeareth before God in Zion.\" ", 

            "R. Eleazar said in the name of R. Hannina: ", 

            "The disciples of the wise increase peace in the world; as it is said, \"And all thy children shall be taught of the Lord ; and great shall be the peace of thy children\" (Is. liv. 13). Read not banayik \"thy children\" but bonayik \"thy builders[1]\"", 

            " \"Great peace have they that love Thy law; and there is no stumbling for them\" (Ps. cxix. 165). \"Peace be within thy walls, and prosperity within thy palaces\" (ibid, cxxii. 7). \"For my brethren and companions' sakes, I will now say, Peace be within thee\" (ibid. v. 8). \"For the sake of the house of the Lord our God, I will seek thy good\" (ibid. v. 9). \"The Lord will give strength unto His people ; the Lord will bless His people with peace\" (ibid. xxix. 11)[2] ", 

            "May we return unto thee : He who beholds! And finished is the Tractate Berakot.\n"

        ]

    ]
for i in range(len(berakhot_array)):
	x={
	"versionSource": "http://primo.nli.org.il/primo_library/libweb/action/dlDisplay.do?vid=NLI&docId=NNL_ALEPH002182132",
	"versionTitle": "Tractate Berakot by A. Cohen, Cambridge University Press, 1921",
	"language": "en",
	"text": berakhot_array[i]
	 }
	post_text("Berakhot."+AddressTalmud.toStr("en", i+3), x)