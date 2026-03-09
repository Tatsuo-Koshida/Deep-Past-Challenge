# Discussion / Comments Capture Log

目的: Kaggle の Discussions やコメントを「手動採集」した内容を、再現・参照しやすい形で保存する（一次メモ）。

- 派生/要約の置き場所:
  - 横断的な学び: `.codex/docs/public_insights.md`
  - ノート/スレッド単位の要点: `.codex/docs/notebook_digest.md`
  - すぐ試す実験: `.codex/docs/experiments_log.md`

前提："Entry"は一つのディスカッションのトピックを表します。"Comments"は"Entry"で投稿されたコメントを意味します。
また、ディスカッションに登場する@deeppastと@ryanholbrookはこのコンペティションのホストです。

---

## Entry: `680446`
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/680446
- タイトル: (pdf)-Translation sometimes different from train.csv translation
- 投稿者: @mariusheuser
- 投稿日時: 2026-03-08
- upvote: 2
- 本文: Hi, this might have already been answere in one of the many topics, but I didn't find it. There is so much to catch up on… I noticed that sometimes the translation in the provided pdfs is very different from the translation in the train.csv. And I dont mean missing pieces or wrong alignment. It is clearly a translation about the same thing, but very different. Here two examples I found:

1."4ff5b1df-abae-4b3c-a1eb-2a0e3db160ab":

train_csv:

you sent to me and I shall not meet with the man while he is (still) alive. I shall sell your goods at any price and then I shall come (with) what silver I receive from your outstanding claims, and I shall see your eye there, with you and serve you. Although I did not reach that realisation(?), my dear father, do not be angry. Since they bring šikku-copper and washed copper, one package after another, you owe him favours for me

Akt 6e (kt 94/k 1486):

… you did not send to me and I shall not meet with the man any more as long as he is alive. I shall sell your goods, cheap or dear, and then I shall come (with) what silver I receive from your outstanding claims, and I shall see your eye there, … with you and serve you.

Notice that not only it is formulated differently, in the first part it says "you sent to me" and in the pdf "you did NOT send to me"

2."6e1f457c-74c0-4e35-8d9b-64dcde103453":

train_csv:

why, someone from among my sons bought the house. Lamassī lives in it.

Akt 6e (kt 94/k 1325):

… Indeed, if someone from among my sons should buy the house, Lamassī will live in it.

Which one is more accurate?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/680446#3418512
- 投稿者: @mpware
- 投稿日時: 2026-03-02
- upvote: 3
- 本文: It happens in even in small translation, for instance:

PDF: 

CSV: 

If you ask Gemini for this example, it will report that PDF is accurate but CSV is not wrong.

---

## Entry: `680256`
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/680256
- タイトル: eBL text divergence
- 投稿者: @davidochoacorrales
- 投稿日時: 2026-03-07
- upvote: 1
- 本文: It's a little script for the eBL text divergence, it is not perfect - it may be seen as a brutal force attack to the eBL dictionary, but it works.

the tool

I build this readme as explanation for the code with Google Gemini - can have errors.

eBL to OARE Mimation Restorer
This script provides an automated solution for converting Standard Babylonian (eBL) lexemes into Old Assyrian (OARE) lexemes by restoring historical mimation.

Overview
In the context of Assyriology, Old Assyrian (OA) preserves the proto-semitic mimation, whereas Standard Babylonian (SB) lost it during the post-Old Babylonian period. This tool helps bridge the gap between these two linguistic conventions:

eBL format: Uses SB conventions, often including Roman numeral suffixes (e.g., "šakānu I").
OARE format: Adheres to OA conventions, which include the characteristic final "-m" (e.g., "šakānum").
This converter was developed based on an empirical analysis of 585 verified pairs with a 92.8% precision rate regarding the consonant skeleton.

Conversion Logic
The script employs a three-tier priority system to handle various grammatical patterns:

Tier	Strategy	Description
Tier 1	Simple Addition	Appends "-m" to standard endings (covers ~87% of cases).
Tier 2	III-weak Reversal	Reverses contractions in verbs (e.g., -û → -ā'um).
Tier 3	Passthrough	Retains words that already possess mimation.
Normalization
To ensure high-fidelity matching, the script includes a normalize_for_matching utility. This function handles diacritic mapping (e.g., ḫ → h, š → sz) and removes parenthetical data or alternative formatting, creating a uniform basis for comparison.

Usage Example
The script is designed to process individual strings. It produces candidate forms that can then be validated against the OARE dataset.

from mimationRestorer import ebl_to_oare

# Simple conversion
print(ebl_to_oare("šakānu I"))
# Output: [('šakānum', 'nominative mimation -u→-um', 1)]

# Verb III-weak conversion
print(ebl_to_oare("qabû II"))
# Output: [("qabā'um", 'III-weak: -û → -āʾum (inf) or -ium (adj)', 2), ...]
Credits
Author: David ok.
Date: 2026-02-26.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/680256#3418149
- 投稿者: @angantyr
- 投稿日時: 2026-03-07
- upvote: 2
- 本文: š → sz

If this is not a typo, I'd advise to reverse the direction to "sz → š" as a standard ASCII fallback to DPC format substitution and leave it be otherwise.


---

## Entry: `679766`
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/679766
- タイトル: Old Assyrian Tokens
- 投稿者: @davidochoacorrales
- 投稿日時: 2026-03-03
- upvote: 3
- 本文: I made this short list: it contains all the syllables that appear in the OARE database. This can be useful in token problems; I use it with the unicodedata library in Python, simply normalizing it.

https://www.kaggle.com/datasets/davidochoacorrales/oare-tokens

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/679766#3416735
- 投稿者: @davidochoacorrales
- 投稿日時: 2026-03-03
- upvote: 0
- 本文: Unicode Normalization
def canonical(text):
    return unicodedata.normalize("NFC", text)

---

## Entry: `679497`
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/680041
- タイトル: 0.78% Train Transliterations Found in eBL_Dictionary?
- 投稿者: @ottpocket
- 投稿日時: 2026-03-05
- upvote: 1
- 本文: I imagine I am doing something obviously wrong here, but I just don't know what:

Of 11,583 unique transliterations in the train, only 9 are in eBL_Dictionary.csv.

#transliterations in Train (with frequency counts)
word_counts = pd.read_csv('/kaggle/input/competitions/deep-past-initiative-machine-translation/train.csv')\
    ['transliteration'].str.split(expand=True).stack().reset_index()[0].value_counts()\
    .reset_index().rename(columns={0:'transliteration'}) 

#cleaned words from eBL_Dictionary
dct = pd.read_csv('/kaggle/input/competitions/deep-past-initiative-machine-translation/eBL_Dictionary.csv')
dct['word2'] = dct['word'].str.replace(r'\s+I$', '', regex=True) #remove the ' |' at the end of the word

#matching
word_counts['in_dictionary'] = word_counts['transliteration'].isin(dct['word2'].values)
print(word_counts.in_dictionary.mean())
>> 0.000777
Below are the words that appear in dictionary from train, along with their frequency counts:

transliteration    count   
    ša  3441    
    i   453 
    la  56  
    šu  34  
    iš  10  
    wa  4   
    u   2   
    ul  2   
    mu  2   

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/680041#3417658
- 投稿者: @tennogh
- 投稿日時: 2026-03-06
- upvote: 2
- 本文: I think they just use different transliteration systems, and also the words can take different forms depending on the grammatical context. I can usually find the words when I'm looking for translations.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/680041#3417501
- 投稿者: @fx6300
- 投稿日時: 2026-03-05
- upvote: 0
- 本文: Hi, I think we should narrow the data down to records that include OA, since vocabulary from different periods is getting mixed in. Also, regardless of whether a lemmatizer is actually effective for this competition, I don’t think the terms will match the dictionary unless we lemmatize them.

---

## Entry: `679497`
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/679497
- タイトル: Lora on ByT5 large
- 投稿者: @pshikk
- 投稿日時: 2026-03-01
- upvote: 4
- 本文: Just wanted to try out lora on a model bigger than ByT5-small, didn't really work well, the best submission caps out at 18.0 . Notebook - https://www.kaggle.com/code/pshikk/ffn-lora-deep-past Outputs - https://www.kaggle.com/datasets/pshikk/lora-5-byte

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/679497#3417009
- 投稿者: @adarsh2626
- 投稿日時: 2026-03-04
- upvote: 0
- 本文: LoRA is best for adapting or specializing a pretrained model. It can learn new behaviors, but teaching completely new knowledge or capabilities is much harder than with full fine tuning

---

## Entry: `678899`
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899
- タイトル: A Stitch in Time Saves Nine
- 投稿者: @deeppast
- 投稿日時: 2026-02-26
- upvote: 19
- 本文: If only the ancients who wrote these texts could imagine how difficult it would be to train computers to translate their work! Working with data from 1950-1750 BCE is not for the faint of heart. From 1927 CE until today, modern scholars have been working with the editing and publication of these ca. 8,000 documents in many different languages, and despite (or because of) almost 100 years of scholarly scrutiny, the datasets are more complicated and in a more convoluted format, than what the ancients originally wrote. These editions were migrated into a database, which became the foundation of the data we used for the training and supplemental data for this challenge. Unbeknownst to them, we are now re-purposing their editions for training ML models, and the messiness of the data is palpable for all to see. That said, this is the first benchmark for a significant ML application with the Old Assyrian data, so with great struggle comes greater pioneering outcomes.

The purpose of this final update is to level the number of markers for gaps from two to one. The hope is that by making some small, but significant adjustments, this will improve the scores for everyone. What we refrained from doing was making any additional changes which could introduce new inconsistencies if not done uniformly. So for the final month of the competition, we will include a clear and concise list of recommendations for the training dataset for alignment with the test data.

Gap Change: Replaced all the following with a single <gap>

x —> <gap>
[x] —> <gap>
… —> <gap>
(break) —> <gap>
(large break) —> <gap>
(n broken lines) —> <gap>
<gap> <gap> —> <gap>
Results of these changes: no more <big_gap> and no more duplicates for <gap> Before the change took place, these types of gaps were found in the test and training data. This recent change reduced all these duplicates to a single <gap>.

Gap	Count
<gap> <gap>	30
-<gap> <gap>	9
-<gap>-<gap>	1
<gap> <gap>-	15
<gap> <big_gap>	6
<gap> <gap> <gap>	2
<gap> <big_gap> <gap>	1
-<big_gap> <gap>-	4
-<big_gap> <big_gap>	13
<big_gap> <big_gap>	15
<big_gap> <big_gap>-	12
<big_gap> <gap> <big_gap>	2
<big_gap> <big_gap> <big_gap> <big_gap>-	3
<big_gap> <big_gap> <big_gap> <gap> <gap>	1
-<big_gap> <big_gap> <gap> <big_gap> <big_gap>-	1
Alignment of Determinatives to match test data:

(d) —> {d}
(ki) —> {ki}
(TÚG) —> TÚG
Shortening of long floats to four places after the decimal

1.3333300000000001 —> 1.3333
2.6666600000000003 —> 2.6666
The rest is up to you. Here are some recommendations, but there's no guarantee that these will improve your score on the leader board:

Some of the transliteration text in the training data is missing, which is unfortunate, but fixable. You can find what is missing from the training data by matching the unique OARE_Text_ID with the equivalent OARE IDs in the published_texts.csv dataset. Do this by matching the unique IDs in the training data to the OARE IDs and find the publication (e.g. AKT 8, 130 = AKT volume 8, text number 130). The PDFs have also been provided, if you find there are missing elements in the translations (https://www.kaggle.com/datasets/deeppast/old-assyrian-kltepe-tablets-in-pdf/data).

Here are some recommended options for changes to the training data:

Remove from translations:

fem.
sing.
pl.
plural
(?)
any stray marks you find (e.g., .., ?, x, xx, << >>, < > except around <gap> of course)
some of the translations equivocate two optional translations using /, it might be better to choose one or the other options provided, rather than including both with a / (e.g. "you / she brought" —> "you brought" ).
Do not remove from translations (as these are in the test too):

quotation marks " "
apostrophes '
meaningful question marks ? or exclamation marks !
Replace in translations:

PN —> <gap>
-gold —> pašallum gold
-tax —> šadduātum tax
-textiles —> kutānum textiles
1 / 12 (shekel) —> 15 grains
5 / 12 shekel —> ⅔ shekel 15 grains
5 11 / 12 shekels —> 6 shekels less 15 grains
7 / 12 shekel —> ½ shekel 15 grains
Decimals to Fractions:

0.5 —> ½
0.25 —> ¼
0.3333 —> ⅓
0.8333 —> ⅚
0.625 —> ⅝
0.6666 —> ⅔
0.75 —> ¾
0.1666 —> ⅙
Change Roman numerals to integer numbers for months: e.g., month V —> month 5

Month	Roman	MN	forms	AKA
Month 2	III	ša-sarratim	ša sá-ra-tim	
Month 3	III	Kenātim	ke-na-tim	ša kēnātim
Month 4	IV	Mahur-ilī	Ma-hu-ur-DINGIR; ma-ḫu-ur-ì-lí	
Month 5	V	Abšarrani	áb-ša-ra-ni; áb ša-ra-ni; áb-ša-ra-nu	ab šarrāni; abšarrani
Month 6	VI	Hubur	Hu-bu-ur	
Month 7	VII	Ṣip'um	ṣí-ip-im	ṣipum
Month 8	VIII	Qarrātum	qá-ra-a-tí; qá-ra-a-tim	
Month 9	IX	Kanwarta	kán-bar-ta; Kà-an-ma-ar-ta	Kanmarta
Month 10	X	Te’inātum	té-i-na-tim	
Month 11	XI	Kuzallum	ku-zal-li; ku-zal-lu	
Month 12	XII	Allanātum	a-lá-na-tum; a-lá-na-tim	
Optional changes in transliterations:

Ḫ → H
ḫ → h
KÙ.B. —> KÙ.BABBAR
Change unicode subscript numbers to normal integers in transliterations:

₀ → 0
₁ → 1
₂ → 2
₃ → 3
₄ → 4
₅ → 5
₆ → 6
₇ → 7
₈ → 8
₉ → 9
Decimals to Fractions for transliterations:

0.5 —> ½
0.25 —> ¼
0.3333 —> ⅓
0.8333 —> ⅚
0.625 —> ⅝
0.6666 —> ⅔
0.75 —> ¾
0.1666 —> ⅙
Examples of the Outcomes for Test

Transliteration	Translation
1 e-ma-ar-šu <gap>	1 donkey of his <gap>
<gap> a-na Ú-<gap> a-dí-in	<gap> I gave it to U-<gap>.
<gap> ⅓ ma-na a-na En-na-nim DUMU Am-ri-a áš-qúl	I paid <gap> ⅓ mina (silver) to Ennānum, son of Amriya.
Examples of the Optimal Outcomes for Train

Transliteration	Translation
<gap> ma-na KÙ.BABBAR ṣa-ru-pá-am <gap> GÍN KÙ.GI pá-ša-lam	<gap> minas of refined silver, <gap> shekels of pašallum gold
<gap> GÚ SÍG.HI.A <gap> 5 maš-ku <gap> 22 na-ru-qá-tum 4 ANŠE ṣa-la-mu	<gap> talents of wool, <gap> 5 hides, <gap> 22 sacks, 4 black donkeys
⅓ ma-na 2 ½ GÍN KÙ.BABBAR 20 NINDA i-ṣé-er tù-wa-ra-a-ah-šu a-lá-hu-um i-šu	Tuwar-ahšu owes ⅓ mina 2 ½ shekels of silver (and) 20 loaves of bread to Ali-ahum.


### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414058
- 投稿者: @ryanholbrook
- 投稿日時: 2026-02-26
- upvote: 2
- 本文: The updated data is now live on the site. I will commence the rescore of existing submissions shortly.

UPDATE 02/26/2026: The rescore is now complete. Please let us know if you have any questions or concerns.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414351
- 投稿者: @nlztrk
- 投稿日時: 2026-02-27
- upvote: 1
- 本文: Our score on LB is 34.1 but the best scoring sub in our sub history seems to be 33.5. I don't understand. 😅

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414411
- 投稿者: @ryanholbrook
- 投稿日時: 2026-02-27
- upvote: 4
- 本文: Hi @nlztrk,

Something seems to have gone wrong with the LB update. We are investigating.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414443
- 投稿者: @mattiaangeli
- 投稿日時: 2026-02-27
- upvote: 0
- 本文: Also the scores of some public NBs have not been updated

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414524
- 投稿者: @guoqingu
- 投稿日時: 2026-02-27
- upvote: 0
- 本文: Hi, my LB rank changed again (40+->30+) after rerun, is there new update?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414535
- 投稿者: @chenwenqiang001
- 投稿日時: 2026-02-27
- upvote: 0
- 本文: transliteration:2- translation: 2+ or 2- translation of test is 2- or 2+ or 2(+gap) ??? please let me know.thank you

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3416596
- 投稿者: @llkh0a
- 投稿日時: 2026-03-03
- upvote: 1
- 本文: question about (n broken lines), do the lines between "Nimar-Istar." and "When he returns from Mamma he will bring it to me" counts as n broken lines?

If I understand correctly, the translation should be:

I furthermore gave 1 mina of good, native copper for an allu’āru-container of sweet wine from Mamma to Puzur-Amurrum son of Nimar-Ištar. <gap> When he returns from Mamma he will bring it to me. (This was) apart from the 4 allu’āru-containers, the proceeds from the silver and washed copper that they have received (previously). Witnessed by Šu-Bēlum son of Kuzizia.



### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3416050
- 投稿者: @cengricardoperez
- 投稿日時: 2026-03-02
- upvote: 2
- 本文: Thanks for the comprehensive update and all the clarifications in the comments. After applying the v3 changes, a few things that helped on my end:

Recovering truncated transliterations: Confirmed that ~10% are affected. Matching oare_id against published_texts.csv and cross-referencing with the AKT PDFs recovered most of them. Be careful, though, some entries aren't just truncated; the translation doesn't match the transliteration at all (as MPWARE pointed out for AKT 8, 55), so it's worth doing a length-ratio sanity check before blindly patching.

The -textiles / -gold / -tax replacements: Based on the host's clarification, these only apply when preceded by a space (i.e., -textiles to kutānum textiles), not in the middle of a word, like import-tax or kutānu-textiles. A naive str.replace will break things, regex with word boundaries or explicit space matching is safer here.

Straight quotes: Curly quotes to straight quotes for both " and '. Small thing, but easy to miss if your text editor or PDF extraction reintroduces curly ones.

Still working through the fraction conversions and subscript normalization. Good luck to everyone in the final stretch!

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3415275
- 投稿者: @mpware
- 投稿日時: 2026-03-01
- upvote: 1
- 本文: I'm trying to identify the mapping between oare_id in train.csv and the AKT PDF in order to complete broken sections, I've found 1561 matches:

AKT 5 = 77 oare_id
AKT 6a = 304 oare_id
AKT 6b = 222 oare_id
AKT 6c = 201 oare_id
AKT 6d = 139 oare_id
AKT 6e = 255 oare_id
AKT 8 = 363 oare_id (e.g. 0123a9b9-e81e-4d7a-a79b-10e7c0aacbb9 Kt 91/k 471, page 213)
Someone with similar results? @jackvd You was saying around 400 items was broken?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3415360
- 投稿者: @angantyr
- 投稿日時: 2026-03-01
- upvote: 4
- 本文: I have similar results with regard to AKT 5 and AKT 6a. I still have to verify a few ids to be sure but when I do I can post it in the updated train.csv dataset to make everyone lives a bit easier.

Edit: The dataset with sources included should be up and running.

Publication	page
AKT 5	76
AKT 6a	295
AKT 6b	218
AKT 6c	196
AKT 6d	137
AKT 6e	233
AKT 8	355

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3415774
- 投稿者: @mpware
- 投稿日時: 2026-03-01
- upvote: 4
- 本文: I've updated my list:

pub_pd = pd.read_csv("data/published_texts.csv")

train_df = pd.read_csv("data/train.csv")

akt_pd = pub_pd[(pub_pd['oare_id'].isin(train_df["oare_id"].unique()))][["oare_id", "label", "excavation_no", "transliteration"]]
akt_pd["pdf"] = akt_pd["label"].str.extract(
    r"\bAKT\s+(\d+[a-zA-Z]?)",
    expand=False
)
pdf
5      77
6a    304
6b    222
6c    201
6d    139
6e    255
8     363
Some rows in train.csv are more than broken, the translation just does not match the transliteration at all. For instance: AKT8, 55. Kt 91/k 304 (1-161-91) oare_id: 5f088d12-ed99-434a-a113-65deab7e1426

In the PDF: 

In train.csv: whatever v1,v2 or v3 

After RE-OCR: 

oare_ids from AKT 6e are one of the most broken.

This competition is about normalization and cleaning.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3416194
- 投稿者: @angantyr
- 投稿日時: 2026-03-02
- upvote: 0
- 本文: I wonder for how many of such cases we could employ a set match filtering, e.g., 'a-na'/'from', 'ku.babbar'/'silver', etc.

It would not be a guarantee but a first stage flag to have a manual check and there are many words that have a 1:1 equivalent with English.


### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414925
- 投稿者: @tennogh
- 投稿日時: 2026-02-28
- upvote: 1
- 本文: Regarding the terms "pašallum gold", "šadduātum tax", "kutānum textiles", those appear in different forms in the texts. Are those the forms that are expected from the test data (e.g. "kutanum-textile", "kutanu textile" -> "kutānum textiles")?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414939
- 投稿者: @qifeihhh666
- 投稿日時: 2026-02-28
- upvote: 0
- 本文: I don’t think that’s the case.

First, words like pašallum, šadduātum, and kutānum do not exist in train.csv at all.

Second, submissions that do not include words such as pašallum, šadduātum, and kutānum have achieved higher scores.

The host only seemed to suggest that we do this. :)

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414946
- 投稿者: @chenwenqiang001
- 投稿日時: 2026-02-28
- upvote: 0
- 本文: when i drop the '[', ['] in the train, my scores would drop. Normally, if dropping the "[" and "]" , the scores would have been improved. I don't know why it is like this.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3415026
- 投稿者: @jackvd
- 投稿日時: 2026-02-28
- upvote: 0
- 本文: In your transliterations or translations?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414479
- 投稿者: @steveroberts
- 投稿日時: 2026-02-28
- upvote: 3
- 本文: The new update seems to have truncated the longer transliteration strings. The previous training data had the following long training entries:

index	oare_id	transliteration_length	translation_length
177	1c428f5b-15b5-463a-8e27-f9b2f0d858fc	592	746
647	64f3382c-cb81-41af-99c9-36854585b747	338	588
927	937e71fb-57c8-46c0-afbc-48f9429886e4	343	537
968	991eef40-f139-4206-90ed-7fb45648b197	408	593
1090	adb0573b-20fb-469d-8343-0ace8e2489e0	357	626
1260	c97bb594-a5a1-4674-9496-48496e91c2ee	29	602
1378	dff850c8-ccd4-44a9-9994-2834ca832a6d	379	603

The new data has truncated these to be:

index	oare_id	transliteration_length	translation_length
177	1c428f5b-15b5-463a-8e27-f9b2f0d858fc	138	739
647	64f3382c-cb81-41af-99c9-36854585b747	107	587
927	937e71fb-57c8-46c0-afbc-48f9429886e4	114	537
968	991eef40-f139-4206-90ed-7fb45648b197	108	593
1090	adb0573b-20fb-469d-8343-0ace8e2489e0	107	625
1377	dff850c8-ccd4-44a9-9994-2834ca832a6d	120	585

I'm not sure if this applies to the other rows too, but it certainly seems to have lost a lot of data.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414484
- 投稿者: @mpware
- 投稿日時: 2026-02-27
- upvote: 1
- 本文: Around 10% of transliterations are truncated. We've to fix that ourself according to the instructions.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414560
- 投稿者: @steubk
- 投稿日時: 2026-02-27
- upvote: 1
- 本文: which instructions?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414580
- 投稿者: @mpware
- 投稿日時: 2026-02-27
- upvote: 1
- 本文: Some of the transliteration text in the training data is missing, which is unfortunate, but fixable. You can find what is missing from the training data by matching the unique OARE_Text_ID with the equivalent OARE IDs in the published_texts.csv dataset. Do this by matching the unique IDs in the training data to the OARE IDs and find the publication (e.g. AKT 8, 130 = AKT volume 8, text number 130). The PDFs have also been provided, if you find there are missing elements in the translations (https://www.kaggle.com/datasets/deeppast/old-assyrian-kltepe-tablets-in-pdf/data).

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414593
- 投稿者: @steveroberts
- 投稿日時: 2026-02-27
- upvote: 3
- 本文: 
It's a bit bad though that data that was there, and which I spent a large amount of time working out how to split, has now suddenly disappeared from the data set.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3415110
- 投稿者: @edwardxiao01
- 投稿日時: 2026-02-28
- upvote: 0
- 本文: 
A large number of data where the ratio between the lengths of transliteration and translation seem weird have wrong/truncated transliteration/translation, e.g. 8376cbda-b423-42d4-abb5-188d04896392. Can follow the instruction to find the raw pdf and amend these data case by case.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414364
- 投稿者: @yaroshevskiy
- 投稿日時: 2026-02-27
- upvote: 1
- 本文: 
Can't describe an amount of confusion when comparing a new train dropped last week and a new train from yesterday and now I'm trying do understand how to merge those two

upd: sorry, my humble verdict is that these updates last week made things worse…

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414370
- 投稿者: @yaroshevskiy
- 投稿日時: 2026-02-27
- upvote: 0
- 本文: 
how to understand this:

before: 31 kutānu-textiles of Iddin-Suen, 30 kutānu-textiles of Ah-šalim, 46 kutānu-textiles of hinnāya and Uṣurānum, 21 kutānu-textiles of Aššur-rēī, 36 kutānu-textiles of Šu-Ištar, 28 kutānu-textiles of Ennam-Suen, 24 kutānu-textiles of Lā-qēp, 18 kutānu-textiles of the merchant, 7 kutānu-textiles without seals, 14 textiles import-tax, 17 textiles as pre-emption.
after:  31 -textiles of Iddin-Suen, 30 -textiles of Ah-šalim, 46 -textiles of hinnāya and Uṣurānum, 21 -textiles of Aššur-rē'ī, 36 -textiles of Šu-Ištar, 28 -textiles of Ennam-Suen, 24 -textiles of Lā-qēp, 18 -textiles of the merchant, 7 -textiles without seals, 14 textiles import-tax, 17 textiles as pre-emption.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414465
- 投稿者: @deeppast
- 投稿日時: 2026-02-27
- upvote: 0
- 本文: 
Yes, you can see in the post above, I recommend making some small changes, egg. -textiles --> kutānum textiles, but this should be checked with the AKT volumes in PDF to be certain. The interum data (v2) update did this, but it introduced new errors because of a simple search / replace. Those changes were rolled back in the lates update (v3), and instructions were provided how to deal with those (above).

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414732
- 投稿者: @yaroshevskiy
- 投稿日時: 2026-02-27
- upvote: 0
- 本文: 
do you recommend to take V3 and manually update it based on the tutorial or to take V2 and just fix 's and quotes?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414898
- 投稿者: @tennogh
- 投稿日時: 2026-02-28
- upvote: 1
- 本文: 
Maybe even v1 is the least flawed, especially if you have already done the work to fix the gaps on it.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414927
- 投稿者: @deeppast
- 投稿日時: 2026-02-28
- upvote: 0
- 本文: 
v3 = v1 with the gaps fixed.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414169
- 投稿者: @edwardxiao01
- 投稿日時: 2026-02-26
- upvote: 5
- 本文: 
@deeppast hihi,

Regarding the unit conversions that you mentioned below, I suspect that the right-hand-side of the first two rows should be interchanged

1 / 12 (shekel) —> ⅔ shekel 15 grains
5 / 12 shekel —> 15 grains
5 11 / 12 shekels —> 6 shekels less 15 grains
7 / 12 shekel —> ½ shekel 15 grains
Is it that 1/12 shekel == 15 grains ?

if so, then the conversions should instead be

1 / 12 (shekel) —> 15 grains
5 / 12 shekel —> ⅔ shekel 15 grains
5 11 / 12 shekels —> 6 shekels less 15 grains
7 / 12 shekel —> ½ shekel 15 grains
is it?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414891
- 投稿者: @deeppast
- 投稿日時: 2026-02-28
- upvote: 2
- 本文: 
yes that's right

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414997
- 投稿者: @takuji
- 投稿日時: 2026-02-28
- upvote: 0
- 本文: 
Isn't it 5 / 12 shekel —> ⅓ shekel 15 grains instead of 5 / 12 shekel —> ⅔ shekel 15 grains?

There are probably many similar mistakes in the test data.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414172
- 投稿者: @chenwenqiang001
- 投稿日時: 2026-02-26
- upvote: 6
- 本文: 
I think you should update these data from the beginning.Some samples from train.csv were aligned by hand. To revise these one more is really a challenging work.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414894
- 投稿者: @deeppast
- 投稿日時: 2026-02-28
- upvote: 1
- 本文: 
There will be no further updates, I'm sorry.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414072
- 投稿者: @mpware
- 投稿日時: 2026-02-26
- upvote: 11
- 本文: 
@deeppast Thanks for the update. Some clarification to be 101% sure:

About double quotes:

Do not remove from translations (as these are in the test too):

quotation marks " "

In the previous update:

quotations " “= removed

The final rule is keep all quotation marks, correct? And for curly double quotes, we have to convert them to plain double quotes or not?

About parentheses:

In the previous update:

parentheses ( )= removed

Now, we need to keep parenthesis as for the examples outcomes you've provided, right?

For instance: 0faa50f7-b86c-466c-a8ab-3a6f48fcb00a

"at 52.5 grains (of silver) each, 0.5 shekel" we must keep the parenthesis around of silver, right?

We must not do: "at 52.5 grains of silver each, 0.5 shekel"

About replacements:

-tax —> šadduātum tax

-gold —> pašallum gold

textiles —> kutānum textiles (are you sure it's not -textiles —> kutānum textiles )?

And it's textiles and -tax and -gold surrounded by spaces? If not then in 198e428d-f51b-40d1-96d8-aee4bfa60d8d:

"of Ennam-Suen, 8 textiles as import-tax, 10 textiles are pre-emption"

would become:

"of Ennam-Suen, 8 kutānum textiles as importšadduātum tax, 10 kutānum textiles are pre-emption".

and it 229be03b-c772-4a6c-8792-c3f80948a97d:

"received 28 kutānu-textiles and 1 black donkey"

would become:

"received 28 kutānu-kutānum textiles and 1 black donkey"

Which would look weird, please confirm.

About <gap>:

In previous update:

added space around gap in translations (not transliterations)

Is it still true? Do we need to add space around <gap> except if glued with a dash?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414734
- 投稿者: @deeppast
- 投稿日時: 2026-02-27
- upvote: 2
- 本文: 
the questions about quotes and parentheses are extremely important

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414893
- 投稿者: @yaroshevskiy
- 投稿日時: 2026-02-28
- upvote: 1
- 本文: 
Yes, keep parentheses and quotations should be dead quotes, no curl, same for apostrophes / scare quotes.

Do not remove from translations (as these are in the test too): quotation marks " " apostrophes ' meaningful question marks ? or exclamation marks !

As for the words which begin with -: words which appear with an initial hyphen have a space before them, rather than those words which are joined to another word with a hyphen. These suggestions are meant to provide some context for the missing words, but the only way to know for sure is to check in the PDFs, which is why they were not replaced in v3. These missing parts were removed in the OARE database, and should be replaced in an ideal situation by checking the PDFs.

-gold —> pašallum gold
-tax —> šadduātum tax
-textiles —> kutānum textiles

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414139
- 投稿者: @epiktistes
- 投稿日時: 2026-02-26
- upvote: 6
- 本文: 
I am a bit confused about the table that follows 'Results of these changes: no more <big_gap>'. That table still says <gap> <gap>: 30, <gap> <big_gap>: 6, etc. Does this mean that there's till 30 occurrences of <gap> <gap>, 6 occurrences of <gap> <big_gap>, etc. in the test set?

I thought I had understood that all of the <big_gap> had been replaced by <gap> and neighboring gaps had been merged together, but I'm less certain I understand right now.

Edit: it seems that some time since this post Results of these changes: no more <big_gap> was changed to Results of these changes: no more <big_gap> and no more duplicates for <gap> Before the change took place, these types of gaps were found in the test and training data. This recent change reduced all these duplicates to a single <gap>. so it's now clearer. Thank you for the clarification!

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414148
- 投稿者: @epiktistes
- 投稿日時: 2026-02-26
- upvote: 0
- 本文: 
In this very post, i can't find any info about merging gap…

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414146
- 投稿者: @honganzhu
- 投稿日時: 2026-02-26
- upvote: 0
- 本文: 
That's what had been mentioned in last week's update:

Gaps, damage markers, and parallel alignment [update: 2/18/26]

Another recurring source of confusion concerns damaged text and gap markers in the data:

    x represents a single broken sign,
    sequences like x x x x or ... represent a larger lacuna.

For modeling purposes we reduced all breaks to a single marker: <gap>

 we removed the tag for <big_gap> from the train and test (and other transliterations). We also deduplicated instances multiple sequential gaps (e.g. <gap> <gap, <gap>-<gap>, <gap> <gap>, <gap>. <gap>, etc.
Source: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414149
- 投稿者: @epiktistes
- 投稿日時: 2026-02-26
- upvote: 2
- 本文: 
thanks, i'm aware, just thought this post is a comprehensive summary of all the changes, which apparently is not…

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414179
- 投稿者: @steubk
- 投稿日時: 2026-02-26
- upvote: 1
- 本文: 
just for the record, this update does not include all the changes made in the previous update
For example unicode subscript numbers are now present in the train transliteration:
0064939c-59b9-4448-a63d-34612af0a1b5 -> 1 TÚG ša qá-tim i-tur₄-DINGIR il₅-qé ...

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414173
- 投稿者: @rejk11
- 投稿日時: 2026-02-26
- upvote: 2
- 本文: 
Remove from translations:

    fem.
    sing.
    pl.
    plural
    (?)
    any stray marks you find (e.g., .., ?, x, xx, << >>, < > except around <gap> of course)
You recommend removing these words but would these words be included in the test set?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3416494
- 投稿者: @deeppast
- 投稿日時: 2026-03-03
- upvote: 0
- 本文: 
no, they are not included in the test set

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414001
- 投稿者: @deeppast
- 投稿日時: 2026-02-26
- upvote: 0
- 本文: 
Yes, both test and train will be updated shortly.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3415113
- 投稿者: @fx6300
- 投稿日時: 2026-02-26
- upvote: 0
- 本文: 
It looks like the “Change Roman numerals to integer numbers for months” table is misaligned/broken: Month 2 is labeled as Roman III, and III appears twice.

According to Kouwenberg (Introduction to Old Assyrian, p. 182), the Old Assyrian calendar starts with Month 1 = I (Bēlat ekallem/Bēltekallem), followed by Month 2 = II (ša sarrātim) and Month 3 = III (ša kēnātim). Could you add Month 1 and shift/correct the Roman numerals accordingly?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414239
- 投稿者: @alturutin
- 投稿日時: 2026-02-26
- upvote: 0
- 本文: 
Hi! Can you clarify these examples in translation:

I paid <gap> ⅓ mina (silver) to Ennānum, son of Amriya.
Tuwar-ahšu owes ⅓ mina 2 ½ shekels of silver (and) 20 loaves of bread to Ali-ahum.
Why are we using curved parenthesis? I looked at train.csv on datasets page and there are no examples of "(silver)". Or examples of parenthesis usage.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414462
- 投稿者: @deeppast
- 投稿日時: 2026-02-27
- upvote: 2
- 本文: 
The parentheses are used by translators to fill in words that are missing in the Akkadian transliteration, but which provides sometimes necessary context.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414137
- 投稿者: @edwardxiao01
- 投稿日時: 2026-02-26
- upvote: 0
- 本文: 
Thanks for the update!

May I ask about a specific case: 33773ec0-e74f-41bf-b985-f3e35b0f26c9

From what Amur-Aššur (owes?)
will such case of (some word?) appear in the test set?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414460
- 投稿者: @deeppast
- 投稿日時: 2026-02-27
- upvote: 0
- 本文: 
yes, unfortunately, that does exist.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3413999
- 投稿者: @alejopaullier
- 投稿日時: 2026-02-26
- upvote: 0
- 本文: 
Thanks @deeppast for your ongoing efforts. What does this exactly mean?

PN —> < gap >

Does this mean that every personal name to be found must be replaced by a gap tag? Or just the literal PN?

Also,

Shortening of long floats to four places after the decimal

I am a bit confused by this since later you suggest converting them to unicode fractions. Does the hidden test set (both translations and transliterations) contain floating point numbers or only unicode fractions?

Thanks in advance

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414000
- 投稿者: @deeppast 
- 投稿日時: 2026-02-26
- upvote: 3
- 本文: 
That's a literal PN token, there are some of these in Veenhof's translations from AKT 8.

I already shortened the floats, so that the conversion to fractions will be easier for you, if you choose to do so. As seen in the example at the end, the test contains only unicode fractions (no decimals at all).

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678899#3414003
- 投稿者: @alejopaullier
- 投稿日時: 2026-02-26
- upvote: 0
- 本文: 
Perfect, thanks a lot!

---

## Entry: `673352`
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/673352
- タイトル: Why does everyone use the “final-byt5” model?
- 投稿者: @yuanyuan98
- 投稿日時: 2026-02-14
- upvote: 2
- 本文: I’ve just started this competition recently. Could someone please explain how “final-byt5” became the mainstream approach?

final-byt5

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/673352#3406118
- 投稿者: @tonylica
- 投稿日時: 2026-02-14
- upvote: 5
- 本文: My guess : final-byt5 became mainstream in this comp because it’s the first strong, public, reproducible baseline: easy to run, stable LB, and ByT5 is robust to messy characters.

Once it worked, everyone copied it and stacked small improvements (normalization/decoding/ensembles) on top.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/673352#3406703
- 投稿者: @yuanyuan98
- 投稿日時: 2026-02-14
- upvote: 0
- 本文: Thank you for the response! I was curious about how the approach shifted from an ensemble of multiple models to a single final-byt5 model.

---

## Entry: `674136`
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136
- タイトル: Dataset Update - Mind the Gaps
- 投稿者: @ryanholbrook
- 投稿日時: 2026-02-19
- upvote: 20
- 本文: Hi everyone,

I just posted an update to the dataset that regularizes <gap> conventions. The train.csv, published.csv, the (hidden) test.csv, and the test set labels have all been updated. The competition host will follow up soon with more details.

I will also be initiating a rescore of all current submissions tomorrow. I will keep you updated as this progresses. All new submissions will be scored against the updated labels.

UPDATE 02/20/2026: We are working on another (hopefully final) update that should address some of the issues raised here. I hope to have it out soon, likely Monday. We will delay the rescore until then.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3408209
- 投稿者: @deeppast
- 投稿日時: 2026-02-20
- upvote: 7
- 本文: Thank you all for your quick observations in the updates, especially of the training data. I made a second update which should resolve most of the issues. I'll provide a complete list here of updates for the training data:

parentheses ( )= removed
quotations " “= removed
scare quotes ’ ‘= removed
fem. = removed
sing. = removed
pl. = removed
grammatical term plural = removed
PN = <gap>
added space around <gap> in translations (not transliterations)
added some of the missing words before hyphens (i.e. -gold —> pašallu-gold & -tax —> šaddutu-tax & -textile --> kutānu-textile)
removed some stray ?, but not able to do so completely (feel free to continue this on your own)
returned fractions to decimals, for alignment purposes
added missing transliterations, and some of the missing translations (but not all, so feel free to continue this on your own as well)

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3408248
- 投稿者: @steubk
- 投稿日時: 2026-02-20
- upvote: 5
- 本文: @deeppast Thanks for clarifying the updates to the train set translations. I have a few questions:

Were the same updates applied to the test set?
How are fractions represented in the test set—decimals (e.g., 0.5) or Unicode characters (e.g., ½)?
What does PN = <gap> mean? Was the literal string “PN” replaced with <gap>, or were all personal names replaced with <gap>?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3408317
- 投稿者: @kishorevishal
- 投稿日時: 2026-02-20
- upvote: 1
- 本文: Just checking, is the data section updated? I can still see fem. sing. pl. in translations

Edit - I noticed the apostrophe was removed, but I think it’s important for translation quality. ref- The current train.csv has "Šāt-Annas representative", but the previous version had "Šāt-Anna's representative".

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3417480
- 投稿者: @kkashyap14
- 投稿日時: 2026-03-06
- upvote: 1
- 本文: Dear Ryan Holbrook, can we have BLEU and ChrF scores along with GM? This will greatly help us to see our model's performance in a transparent manner and thereby help us to diagnose our models well. You can keep GM as the final LB scoring mechanism. Thank you.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3408858
- 投稿者: @mpware
- 投稿日時: 2026-02-21
- upvote: 6
- 本文: While waiting the update of update, I've reviewed the update and I'm getting lost now:

What is the final policy for fraction? I see some fractions in translation and also just float numbers (rounded or not rounded): 2 minas 13.5, 1.8333300000000001, @deeppast You was saying in another post that we should convert all floating number to fraction, right? Why it's not normalized now?
Some transliteration in english: 9a208f3b-1cbb-43a6-b870-566abe5ea9a1 (noticed by @yaroshevskiy)
ד still here (009fb838-8038-42bc-ad34-5f795b3840ee)
Many x that shoud be < gap >: 04dd324f-120e-44fd-9dbd-93a144906902 (Um-x took), 1b89399d-d4f8-4347-b88b-94f5eec0886f (shekels for x shekels; 15 grain), 476e6eef-f0a4-44fd-b3f8-65e6337a9a51 (When Ana-xs son and Ili-pi-usurs)
Random possessive usage: 054fdba4-0cff-4153-969d-c77e42413e1c (to our own Amur-Ištar's sons)
What should we do with /: 1252b18d-4b89-4af9-b6b9-199b40c13848 (qí-bi-ma um-ma SIG5-pí-/i-a-/šur-ma). Why it's not normalized now?
brackets: 19052127-2c2e-479d-b666-f1ea0ed27cb2, their right on a share < by giving them > a house-plot. Is that normal we still have them in the cleaned translation?
A lot of not allowed chars in translation (according to the previous list that was provided)
fem. pl. sing. a44f089e-2645-4aa2-b5e4-ba75e70fdf78, 7e525e12-c226-4c00-9c6e-de303e676771 (I shall return your grain to you fem. pl.. Send me), b64a5273-3e7c-4fe9-9824-bc5cd5e67586 (the cannot give in! As soon as youpl. have heard), 26ebe582-a312-4b63-8138-b7a19b12f277 (I have written to you fem. sing. five times)
Orphans curly bracket: 8c1f39b5-5b71-4171-b0ef-d4db031a5802 (as follows: Of the 57 skekels of silver} that are available)
Roman numbers: c84fb0b6-45c9-4e6d-8923-51eddf50c2d7 (dated to the IVth month of the eponymy), Do we have to convert them to just number?
Parenthesis removed: e76705fe-094c-4fa3-8506-2bca4d4e7b7c ==> to your representatives (with) Aluwa, then I shall act in

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3408859
- 投稿者: @samson8 (tg @pansh1n)
- 投稿日時: 2026-02-21
- upvote: 1
- 本文: @mpware by fractions he meant 1 / 3 or 1 / 6. stuff like this. So these fractions are substituted with floats now. I have already lost a sub thinking about unicode fractions. Policy for fractions is unchanged

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3408872
- 投稿者: @mpware
- 投稿日時: 2026-02-21
- upvote: 2
- 本文: Hi @samson8 , so we should not try to convert 0.3333 to ⅓ and but only for 1 / 3 ? Look at the 2 examples below, sometimes we've to convert, sometimes not. It makes no sense to me. The instructions and the examples are not going in the same direction.

Look at this one:

0b84671a-8753-49d9-859d-b42c3d8944ae

Transliteration: 2 né-pí-šu 15 ma-na.TA ú iš-tí-in né-pí-šu-um 10 ma-na ni-is-ha-sú DIRI ša-du-a-sú ša-bu-ú ŠU.NÍGIN 42.3333 ma-na KÙ.BABBAR ṣa-ru-pá-am ku-nu-ki-a a-na a-lu-wa ù e-ni-ša-ri-im áp-qí-id-ma a-na a-lim{ki} a ma-lá tí-ir-tí-šu a-ṣé-er ša-lim-a-šùr ú-šé-bi-il5-šu-nu a-ha-ma 13.3333 ma-na URUDU SIG5 a-na ga-am-ri-šu-nu ù 5 GÍN KÙ.BABBAR a-na ú-ku-ul-tí-šu-nu a-dí-in IGI ili5-ba-ni DUMU ba-ší-lam IGI a-hu-qar DUMU zu-ur-zu-ur IGI tù-ra-am-ì-lí DUMU e-dí-na-a-šùr a-ha-ma 10.3333 ma-na 3.5 GÍN KÙ.BABBAR ṣa-ru-pá-am tum ni 0.5 GÍN ṣí-ba-tim ša i-na ṣé-ri-a il5-qé-ú-ni a-na hu-bu-li-šu a-na kà-ri-im wa-ah-šu-ša-na áš-qúl ṣí-ba-at KÙ.GI ša ší-ip-kà-at a-šur-bé-el-a-wa-tim i-ší-tù

Translation: "2 packages of 15 minas each plus a single package of 10 minas, its import duty added, its transport tariff paid - in all 42 ⅓ minas of refined silver under my seal, I entrusted to Aluwa and Enišārum, and I sent them to the City to Šalim-Aššur in accordance with his orders. Furthermore, I paid 13 ⅓ minas of good copper for their expenses and 5 shekels of silver for their food. Witnessed by Ilī-bāni son of Baši-ilum, by Ahu-qar son of Zurzur, by Tūram-ilī son of Eddin-Aššur. Furthermore, 10 ⅓ minas 3 ½ shekels of refined silver ½ shekel interest that they took on my account, I paid for his debt to the Wahšušana colony. The interest on the gold that remained of Aššur-bēl-awātims investment.

And then this one: Some are kept as floating number, some are fraction. 0.3333 ==> 0.3333, 0.16666 ==> ⅙, 0.5 ==> 0.5,

0faa50f7-b86c-466c-a8ab-3a6f48fcb00a:

Transliteration: 4 GÍN a-na ší-iṭ-ri-im ša pu-ki-im 1.3333 GÍN a-na e-re-qí-im qá-nu-e áš-qúl 1.6666 GÍN a sú-ba-ri-im áš-qúl 0.3333 ma-na KÙ.BABBAR a-na a-bar-ni-im áš-qúl 0.16666 GÍN a-na um-ṣí-im 0.25 GÍN a šu-um-ki na-ru-uq GIG GÍN a-na ha-áš-lá-tim a-wa-ar-nu-a-lim 0.6666 GÍN a-na e-ṣé áš-qúl 0.6666 GÍN a pá-e ú-ša-qí-il5 1 bi-il5-té-en 0.5 GÍN áš-qúl 0.25 GÍN a-na na-pá-hi-im 95 ki-ra-tim a-na 0.25 GÍN.TA ù 7.5 ŠE.TA 0.5 GÍN a-na 0.16666 GÍN a-na a-na

Translation: "I paid 4 shekels for a scarf of -weave, 1.3333 shekel for a wagonload of reed; I paid 1.6666 shekel for ; I paid 0.3333 mina of silver for an Abarnian textile, ⅙ shekel for a piece of dried meat, ¼ shekel for onions, x shekels for bags of wheat ;I paid shekels for ? , for a ; I paid 0.6666 shekel for firewood; 0.6666 shekels I paid for chaff, for a double load I paid 0.5 shekel; ¼ shekel for the blacksmith. I supplied 95 drinks to at 52.5 grains of silver each, 0.5 shekel for ⅙ shekel for for

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3408878
- 投稿者: @vinprofessionalapps
- 投稿日時: 2026-02-21
- upvote: 1
- 本文: Have the same question: submission must use ½ or 0.5? Reading above: "returned fractions to decimals, for alignment purposes" seems to indicate using 0.5, but scoring doesn't seem to be aware :)

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3408879
- 投稿者: @samson8 (tg @pansh1n)
- 投稿日時: 2026-02-21
- upvote: 1
- 本文: Hidden test translations use ⅓ instead of 0.3333 and 1 / 3. And that holds for all the other numbers

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3408886
- 投稿者: @mpware
- 投稿日時: 2026-02-21
- upvote: 4
- 本文: Thanks @samson8 , I've just spent a sub too to double check on transliterations, no 0.3333 in hidden test for transliterations. You've checked that's the same for translations so I think I'm good now as it was my initial understanding.

I don't understand why the cleaned train data does not reflect that behavior and reflects other important normalization rules.

Update: All should be fixed on the next data update next week. Wait and see …

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3408959
- 投稿者: @angantyr
- 投稿日時: 2026-02-21
- upvote: 3
- 本文: My advice would be to leave the normalization replacements for current cases. It won't hurt and there is no single guideline on what the fractions, signs, gaps, months, broken sections etc. should look like. There are many but I've lost count and I'm sorry too say, but a silent update of the existing "stumbling blocks" thread without a clear "EDIT/UPDATE" section makes everything all the more confusing.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3417712
- 投稿者: @dingolingo
- 投稿日時: 2026-03-06
- upvote: 0
- 本文: What will be ease guid for this

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3410865
- 投稿者: @skathaitrooney
- 投稿日時: 2026-02-24
- upvote: 1
- 本文: Have the same question. Does the private test set now have decimals (0.333 for example) versus fractions ? @deeppast

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3408408
- 投稿者: @tarekziad
- 投稿日時: 2026-02-20
- upvote: 11
- 本文: Honestly ,am really frustrated. I’ve been working on many patterns (like […-Suffix] and several others). Now with every dataset update, these patterns are gone or changed. My work on them is basically useless ,it feels like all my time was wasted.

This cannot keep happening. If the dataset isn’t stable, the competition should start only when it’s ready. Also, are you planning to update the data one day before the competition ends? We need a stable dataset so our work actually counts.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3408114
- 投稿者: @mpware
- 投稿日時: 2026-02-20
- upvote: 15
- 本文: First, thank you for providing the updated, cleaner dataset - it’s clear that a lot of effort went into improving data quality, and it will ultimately benefit the challenge.

I do have a couple of concerns I’d like to share:

Mid-competition changes: Updating the data and rules partway through the competition can be challenging for participants who have been working since the start of the Deep Past Challenge. Many of us invested significant time normalizing and adapting to the original data, and these efforts may no longer be applicable. While I understand the intent to improve the dataset, this kind of change can feel discouraging from a fairness standpoint.

Information consistency across platforms: Some important clarifications appear to be shared on Discord but not reflected in the official Kaggle discussion or data description. For participants who rely solely on the Kaggle platform, this creates an uneven playing field. It would be very helpful if all critical information were consolidated in the official documentation.

That said, I’m still enjoying the challenge and plan to continue participating.

To help avoid further rework, especially for normalizing re-OCR data such as Larsen, could you please provide a detailed list of the normalization changes that were applied? A quick diff of train.csv suggests that, beyond replacing with , there were also changes such as quote removal, number fractions, Hh, subscripts, and possibly other text adjustments. Having a clear summary would help participants align their preprocessing steps with the updated data. Could you provide the updated list of characters allowed in transliteration and translation?

Finally:

"Dataset instructions" had not been updated and still ask us to use big_gap.
fem. plur. are still here but you recommended to remove them

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3408383
- 投稿者: @samson8 (tg @pansh1n)
- 投稿日時: 2026-02-20
- upvote: 4
- 本文: The thing is. This is obviously a good change that eliminates 2-token preprocessing gamble and should have been done in the first week. I'm sure Adam is a professional and knows his domain perfectly. Just sometimes people are unfamiliar with how many GPU/human hours could be burnt by solving a problem within a particular setting and that changing this setting could be a bit painful.

Nevertheless, I'm sure that 'transitivity' of a translation quality still holds (in general) for the new test. Let's just hope that it is the last change~~

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3408391
- 投稿者: @jackvd
- 投稿日時: 2026-02-20
- upvote: 4
- 本文: Yes, it's a good change, but wowee I spent a lot of time on stuff that is now useless 🫠

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3408390
- 投稿者: @fabiendaniel
- 投稿日時: 2026-02-20
- upvote: 1
- 本文: Concerning the removal of the quotes in translations, (many, all ?) possessive english structures as brother's, father's, Šalim-Aššur's …became brothers, fathers, Šalim-Aššurs … Was it intended and will we have the same in the hiddent test set ?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3408017
- 投稿者: @takuji
- 投稿日時: 2026-02-20
- upvote: 3
- 本文: It looks like there are still some -x left.

Also, although the translation of c97bb594-a5a1-4674-9496-48496e91c2ee was originally correct, it has now been completely incorrect.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3408070
- 投稿者: @deeppast
- 投稿日時: 2026-02-20
- upvote: 3
- 本文: Thanks for pointing this out. I'll fix it and share a new update shortly.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3407809
- 投稿者: @yaroshevskiy
- 投稿日時: 2026-02-19
- upvote: 4
- 本文: I've spent just a few minutes on this:

1) Why is that you fem. plur. have written me, saying this one is confusing, same that I acquired for myself(?) -> that I acquired for myself? etc

2) (ki) -> {ki}

3) is in Iddin-Aššur's possession -> is in Iddin-Aššurs possession

4) subscripts

5) ḫ

6) some texts were extended (?)

7) quotations dropped

8) many digits normalized (?)

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3407831
- 投稿者: @yaroshevskiy
- 投稿日時: 2026-02-19
- upvote: 3
- 本文: 9a208f3b-1cbb-43a6-b870-566abe5ea9a1," <gap> talents of wool, <gap> 5 hides, <gap> 22 sacks, 4 black donkeys, 3 saddle-rugs for each, plus their harness - all this I gave to Ewarimuša.","From Ikūn-pīya to Ali-ahum: Earlier I gave a slave-girl to Buziya son of Asaya and he brought her to you. He did not give you the slave-girl, but returned and here I wrote his tablet about the price of the slave-girl, 0.5 mina 5 shekels of silver. My dear brother, there <gap> "
both english

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3407967
- 投稿者: @deeppast
- 投稿日時: 2026-02-19
- upvote: 0
- 本文: That's correct, these tablets are copies, so they are different objects with almost the same text on them.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3407967
- 投稿者: @deeppast
- 投稿日時: 2026-02-20
- upvote: 1
- 本文: Thanks Oleg, yes your observations are correct. Thanks for catching that, I will make the update for the training data this week and post another update shortly.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3407800
- 投稿者: @anaphase21
- 投稿日時: 2026-02-20
- upvote: 1
- 本文: Does this mean <big_gap> will no longer be part of the hidden test.csv? I can see that they are not in the updated train.csv.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3407970
- 投稿者: @deeppast 
- 投稿日時: 2026-02-19
- upvote: 3
- 本文: Yes, exactly, the test set was updated as well, no longer <big_gap>. You can see an updated post about that here: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3407901
- 投稿者: @shreyasadhari123
- 投稿日時: 2026-02-19
- upvote: 2
- 本文: @ryanholbrook certain questions regarding new data:

are <big_gap> eliminated.
should we merge multiple <gap> into one <big_gap> just in case they appear
are …(epilses) also removed.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3408068
- 投稿者: @deeppast
- 投稿日時: 2026-02-20
- upvote: 1
- 本文: Yes, that's right. <big_gap> has been replaced with <gap> and then deduplicated, so you should merge multiples. All ellipses should be removed as well and replaced with <gap. I updated the guidance for that here: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3408258
- 投稿者: @steubk
- 投稿日時: 2026-02-20
- upvote: 5
- 本文: @deeppast Perhaps the new guidance would be clearer if presented in a new post rather than updating a month-old thread whose replies are no longer valid.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3408392
- 投稿者: @jackvd
- 投稿日時: 2026-02-20
- upvote: 0
- 本文: @ryanholbrook any update on rescoring? Also, will this wipe the leaderboard as well?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3408416
- 投稿者: @ryanholbrook
- 投稿日時: 2026-02-21
- upvote: 5
- 本文: There's another update incoming to address a couple other things pointed out here. I'll start the rescore once it's up. All of the submissions will be rescored, and the new scores will be reflected on the leaderboard. The new scores are posted as they are available, so while the rescore is ongoing the leaderboard will be a mix of old and new -- I don't think it should take more than an hour or two to complete, though.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3408435
- 投稿者: @aman1391 
- 投稿日時: 2026-02-21
- upvote: 0
- 本文: @ryanholbrook : is there a possiblity for extension or a possiblity of increasing the submssion per day , given the data is updated after 2 months of running ..

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3408439
- 投稿者: @samson8 (tg @pansh1n)
- 投稿日時: 2026-02-21
- upvote: 2
- 本文: Data is basically not updated, It's just a clear 2-token related change~~ And still there is one more month left. It's not worth it

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3408441
- 投稿者: @aman1391 
- 投稿日時: 2026-02-21
- upvote: 0
- 本文: Yes, you are right .. :)

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3408831
- 投稿者: @samson8 (tg @pansh1n)
- 投稿日時: 2026-02-21
- upvote: 1
- 本文: @ryanholbrook I'm pretty sure that another update only adresses train issues and test will be unchanged. May be delay is not a necessity

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3409126
- 投稿者: @steubk
- 投稿日時: 2026-02-22
- upvote: 1
- 本文: I'm not so sure test will be unchanged 😀

if so why @ryanholbrook said

I'll start the rescore once it's up. ?

I think that at least 's issue must be address on test test.

Hopefully @deeppast will be clear in the changes that were made to the final test set compared to the initial test set.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674136#3413233
- 投稿者: @cody11null
- 投稿日時: 2026-02-24
- upvote: 1
- 本文: Yeah still looking forward to this to ensure that all of the work I am doing actually translates.

---

## Entry: `678836`
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678836
- タイトル: Is this competition becoming a 'Regex Guessing Game'?
- 投稿者: @daylighth
- 投稿日時: 2026-02-25
- upvote: 14
- 本文: I recently noticed this discussion about the dataset update. While I am genuinely grateful to the Kaggle staff and the host for their continuous efforts to improve the data quality, I must admit I am starting to lose motivation and feel a bit exhausted by this process… Even after the recent updates, the dataset still lacks a fully unified and consistent standard.

I joined this competition to focus my energy on trying new LLM/Seq2Seq strategies, experimenting with advanced NMT training methods, and learning meaningful domain knowledge from both the host and other competitors. Instead, I find myself spending massive amounts of time reading discussion threads just to bridge the information gap, and writing endless Regex pipelines to guess the correct data format.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678836#3414126
- 投稿者: @epiktistes
- 投稿日時: 2026-02-26
- upvote: 2
- 本文: The latest post makes the formatting very clear for everyone, so that's good. But there is a lot to learn from this competition about data cleaning and dataset building, so I'm not sure why it would make you lose motivation. In real life situations, you are often handled a bunch of terrible files to work with, it's just how it is. The organizer does the best they can with what they have, and there is a lot to learn from working with this data. Making it all work is part of the challenge. Just keep at it.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678836#3414135
- 投稿者: @daylighth
- 投稿日時: 2026-02-26
- upvote: 4
- 本文: Hi @epikt,
Thank you for reading my post and sharing a rational perspective!
In real life situations, you are often handled a bunch of terrible files to work with, it's just how it is.
You are right. Real-world data is often terribly formatted. However, in reality, you can agree on a unified target output with your boss. This gives you a clear direction when cleaning the data. For example, you know to filter out samples with inappropriate lengths, remove outliers, or prepend specific prompts to the model input.
The problem here is that the "direction" of this competition has been entirely uncertain. It was only "finalized" a few hours ago, and we still might need to wait for further clarifications from the host. For instance, whether a fraction should be formatted as 0.3333 or 1/3 has absolutely nothing to do with a model's actual translation ability. What can we learn from this specific formatting toggle? To be more precise, at this point, it feels less like data cleaning and more like reverse engineering.
the organizer does the best they can with what they have,
I completely understand that, but I feel it would have been much better to explicitly define the expected target data format at the very beginning of the competition. I am sure many participants have already invested significant GPU resources and time into this. If the Ground Truth keeps shifting, that money and time are essentially wasted.
Regardless, I really appreciate your encouragement. Best of luck to you in the competition!😀

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678836#3414145
- 投稿者: @epiktistes
- 投稿日時: 2026-02-26
- upvote: 1
- 本文: The changes in the ground truth data do force us to readjust, but I think that on the opposite, it has the accidental benefit of limiting the usefulness of leaderboard probing, which has been an issue with some past competitions. Probing is its own skill, but it's no fun trying to compete when the top n scores are all there just because they found a way to exploit the metric by probing constantly since day 1. If these are the two choices, as long as they remain reasonable and not too last minute, I'll take the small changes along the way.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678836#3414373
- 投稿者: @yaroshevskiy
- 投稿日時: 2026-02-27
- upvote: 4
- 本文: The latest post makes the formatting very clear for everyone

IMHO quite the opposite, we've seen 3 different train.csv with different formatting and now it's more confusing than before

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678836#3414396
- 投稿者: @epiktistes
- 投稿日時: 2026-02-27
- upvote: 0
- 本文: You're right, after having read through the post more carefully carefully, it does bring as many new questions as it answers. In any case, I've been enjoying this competition, so I just hope this it stays fun. It's true though that with just about 20 days to go it should be the time for the instructions to be clear.


### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/678836#3413794
- 投稿者: @skathaitrooney
- 投稿日時: 2026-02-25
- upvote: 3
- 本文: I agree, and there is too much confusion on how the data in the actual dataset is. Its just a guessing game right now

---

## Entry: `674469`
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674469
- タイトル: Why 300-350 people are stuck at 35.1 score?
- 投稿者: @adarsh2626
- 投稿日時: 2026-02-21
- upvote: 6
- 本文: In the public leader board i can see around 350 people stuck at 35.1 score. I have trained my model with 77k rows high quality self made dataset, written massive codes to extract data from different pdf , book , website etc which took me 2.5 weeks still i am at 34 idk is there something i am missing or 800 people above are also collecting that much data like akkadian data is not easy to find and extract
if you see the board under 34 score at increase of 1 point you will mostly cross 40-50 teams but here between 34 and 35 you are crossing 700 teamssss , i dont have any words The score is accommodated between 34 and 35 how is that possible???????/
please someone tell me what is happening up there

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674469#3408489
- 投稿者: @alejopaullier
- 投稿日時: 2026-02-21
- upvote: 7
- 本文: All those people are just unoriginal forkers, people who are not truly interested in competing and rather copy/paste other people's best scoring public notebooks and submit them. That is why you see so many people with the same score. Don't worry, those public notebooks almost always are heavily overfitting the public leaderboard so in the end they get all shaked down.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674469#3408489
- 投稿者: @adarsh2626
- 投稿日時: 2026-02-21
- upvote: 1
- 本文: Feeling good after hearing that
But there should be some moderation over what is submitted like the people who are genuinely doing the hard work are betten buy someone who is just copy and pasting model no real work

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674469#3410547
- 投稿者: @pelinkeskin
- 投稿日時: 2026-02-23
- upvote: 3
- 本文: This post shows how grim the situation is right now (https://www.kaggle.com/discussions/product-feedback/671127#3400122) and it feels like Kaggle doesn't really care… moth said public LB toppers "almost always" overfit, but honestly, that hasn't happened in most of the comps I've joined lately.
There's a lot of medal corruption going on. Even some gold medal write-ups basically say "oh I admit just merged the highest scoring public model in to my own and got lucky lol." From my experience, out of 5 competitions in the last year, only one actually had a real shake down for the copy-cats. If you go into a competition expecting a fair leaderboard, you’re gonna be disappointed when public notebook forkers fill up the silver/bronze tiers at the end. The reality is the leaderboard (outside of the top few genuinely innovative gold notebooks) is mostly just based on who forked the highest score kernel fastest and who got lucky with a random seed. That’s just a fact at this point.
Also, many gold solutions at the top don't come from a standard 16gb consumer gpu. When the write ups come out, you will see massive ensembles that required burning hundreds of gpu hours (I am not denying building at huge scale also requires an expertise, having access to hardware capacity isn't equal to win ofcourse but if we are talking about fairness lets put it down). They are not usually something a typical home user can do without spending a fortune on cloud costs. If we’re lucky, maybe 1 or 2 real experts actually beat the game with a clever approach that fits on a normal scale, and we get to read and learn from them. Unless you are real expert in field so that you can beat the scale with innovation, IMO the only reason to even attend a competition now is for the learning opportunity and getting your hands dirty on a new subject. Expecting a fair rank for hard work is just asking for a headache. Sorry to hear that you spent alot of time doing the boring data extraction & cleaning staff, lets hope there will be a shakedown and genuinely hard work like yours gets rewarded this time. 🍀

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674469#3410584
- 投稿者: @adarsh2626
- 投稿日時: 2026-02-21
- upvote: 1
- 本文: i see but i need to keep going as if i leave now whole progress will be lost , so lets hope for a medal and good rank

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674469#3408498
- 投稿者: @honganzhu
- 投稿日時: 2026-02-21
- upvote: 2
- 本文: that score is pre-update, if you submit now it is after-update score, which means your 34 is a solid score. once the rescoring is underway you will likely see those public score got dropped by a lot probably.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674469#3408612
- 投稿者: @adarsh2626
- 投稿日時: 2026-02-21
- upvote: 0
- 本文: I see so they have over fitted on test set right?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674469#3408626
- 投稿者: @honganzhu
- 投稿日時: 2026-02-22
- upvote: 1
- 本文: the previous test set yes, not the new one

---

## Entry: `674843`
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674843
- タイトル: A small doubt related to private test set
- 投稿者: @adarsh2626
- 投稿日時: 2026-02-22
- upvote: 2
- 本文: will final test.csv for private board would have the column like id, text_id, line_start and line_end other then main text My notebook depend on those if set doesnt have those then my model wont work so should i change it now or it would be there

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674843#3410526
- 投稿者: @yeoyunsianggeremie
- 投稿日時: 2026-02-22
- upvote: 0
- 本文: During submission, your code is run on both the public and private test sets. If you successfully get a score on the public LB, you will also get a score on the private LB

---

## Entry: `674348`
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674348
- タイトル: Cuneiform base model
- 投稿者: @leedrake
- 投稿日時: 2026-02-20
- upvote: 12
- 本文: Hi all,
I've been working the past couple years on training cuneiform models - I think a couple folks here are using some. Just pushed a new one: https://huggingface.co/Thalesian/cuneiformBase-400m. It includes Sumerian, Akkadian (Oracc + CDLI), Hittite, Linear B, and a little bit of Elamite.
This one is built from UMT5-base, but ties embeddings to keep it small. I got decent performance for Akkadian. The Hittite performance I suspect is due to data leakage from a new dataset I added for English, but the German performance is consistent with past models.
This model was trained on four flavors of input:
Cuneiform glyph -> English
Transliteration (CDLI notation) -> English
Complex transliteration (diacritics) -> English
"Simple" transliteration (hyphens removed, syllables joined to form words) -> English
Feel free to use, I checked and none of the old Assyrian data present in the training documents here was used to train this model. It is prompt-based like all T5-style models. The functions I use to prepare text can be found in text_pipeline.py.
Another tool which might help you is TokenpackTrainer - I developed this to train the base model. It is designed to adjust batch size based on the length of inputs and make training more computationally efficient without padding a bunch of 0s on short sequences. It should calibrate the right number of tokens per step based on your hardware, when it OOMs it just goes to a fallback setting then ramps back up until it finds the right limits. It integrates with transformers and requires no new training arguments. I find it really useful for cuneiform datasets which can have extremely variable document lengths.

---

## Entry: `673904`
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/673904
- タイトル: Insights from the Akkademia Codebase & PNAS Paper for the Deep Past Challenge
- 投稿者: @jamesmcguigan
- 投稿日時: 2026-02-18
- upvote: 9
- 本文: insights from https://github.com/gaigutherz/Akkademia/blob/master/akkadian/ -> https://claude.ai/chat/ae982bc5-0d2e-41ea-a35c-c5e5f2dfccf3

Insights from the Akkademia Codebase & PNAS Paper for the Deep Past Challenge Here's what you can extract and apply from the Akkademia project:

1. Architecture & Models
Akkademia uses HMM, MEMM and BiLSTM neural networks for transliteration, achieving accuracy rates of 89.5% with HMM, 94% with MEMM, and 96.7% with BiLSTM on the trained corpora. GitHub But the translation work (the 2023 PNAS Nexus paper) used something different — a Fairseq convolutional model (fconv) for the NMT task, as CNNs have been shown to work well for low-resource and character-level machine translation, with shorter training time compared with transformers. PubMed Central

Key takeaway for you: Their SOTA results used CNNs, not transformers. This is a 2023 result. Modern transformers (especially ByT5, mT5, or NLLB) with proper fine-tuning should be able to beat 37.47 BLEU4. The competition is essentially asking you to outperform this benchmark on a different (Old Assyrian) corpus.

2. Two Translation Pipelines — and Why C2E ≈ T2E
The repo supports two tasks:

C2E (Cuneiform Unicode → English): Character-based tokenization with a small vocabulary of ~400 characters
T2E (Transliteration → English): BPE tokenization via SentencePiece — 1,000 vocab for transliteration, 10,000 for English
Interestingly, though they anticipated the results of T2E to be better, there was little to no substantial degradation of the results compared with C2E. PubMed Central This means going directly from cuneiform Unicode to English is viable — you don't necessarily need a two-stage transliteration → translation pipeline. If the competition data includes Unicode cuneiform, consider training C2E directly.

3. Data Pipeline & Preprocessing (Critical for the Competition)
From the paper and codebase:

Training data: They used ORACC corpora — RINAP, RIAo, RIBo, SAAo, and Suhu — totaling 8,056 tablets and ~56,160 sentences for T2E. PubMed Central
Data split: 90% train / 5% validation / 5% test
Sentence definition: They treat each line as an independent "sentence" — even if it's a single word, phrase, or group of phrases. The shortest sentences are 3 characters, the longest 237, with a median of 118 characters. PubMed Central
Cleaning steps applied:
Verified no text appears more than once (deduplication)
Removed examples without proper translation (flagged "No translation possible," "No translation warranted," "broken for translation")
Kept examples with restorations (partially reconstructed text)
Handled alignment mismatches between Akkadian lines and English translations
Takeaway: Apply the same cleaning rigorously to the competition data. Also, a cleaned version of the Akkademia training corpus is available as a HuggingFace dataset in the veezbo/akkadian_english_corpus repo GitHub — use it for supplementary pre-training.

4. Tokenization Strategy Matters Enormously
For cuneiform (C2E), they used character-based tokenization with a small vocabulary of 400. For transliteration (T2E), they used BytePair Encoding (BPE) with SentencePiece, vocabulary sizes of 1,000 for transliteration and 10,000 for English. PubMed Central

Insight for the competition:

The tiny source vocabulary (400 for cuneiform, 1,000 for transliteration) suggests that byte-level or character-level models (ByT5) are a natural fit, since they inherently handle small-vocabulary scripts well.
The 10:1 ratio of English-to-source vocab size reflects the asymmetry — Akkadian has a compact sign system while English output needs rich vocabulary. Consider asymmetric architectures or tuning BPE sizes differently for source vs. target.
5. Genre Sensitivity & the Old Assyrian Angle
The more formulaic the genre of the source, the more accurate the translation. Administrative and divinatory texts tend to be very formulaic. PubMed Central The competition specifically targets Old Assyrian business records — contracts, letters, loans, receipts — which are highly formulaic.

However, the great majority of Akkademia's training data is Neo-Assyrian (7,327 out of 8,056 tablets), with only 122 Old Assyrian texts. PubMed Central This is a critical domain mismatch — the model was trained overwhelmingly on Neo-Assyrian data, but the competition wants Old Assyrian.

What this means for you:

Pre-training on Akkademia data gives you Akkadian language structure, but you need to fine-tune aggressively on the competition's Old Assyrian corpus
Old Assyrian has distinct orthographic conventions and vocabulary — expect significant distribution shift
The formulaic nature of business records is your advantage: learn the templates ("X minas of silver," "sealed by Y," "in the presence of Z")
6. The Hallucination Problem
The model produces both intrinsic hallucinations (factual but incorrectly phrased) and extrinsic hallucinations (fabricated content not in the source). PubMed Central From the actual output examples in the repo, we can see cases where the model:

Substitutes deity names (e.g., "Nikkal" for "Ninegal")
Fabricates content when input is fragmentary (fills gaps with plausible-sounding but wrong text)
Truncates long translations
Takeaway: Add constrained decoding or length penalties. For proper nouns, consider a copy mechanism or dictionary-based post-processing. For the chrF++ component of your score, getting names character-close matters.

7. Key Hyperparameters from Their Best Run
Their tuned hyperparameters: architecture fconv, dropout 0.1, label smoothed cross-entropy criterion, label smoothing 0.1, NAG optimizer, clip-norm 0.1, fixed learning rate scheduler, force-anneal at 50, max-tokens 4000, learning rate 0.1. PubMed Central

If you're using Fairseq as a starting point, these are your baseline settings. But I'd recommend switching to a modern framework (HuggingFace Transformers) and using their seq2seq pipeline with the following models as strong starting points: google/byt5-large, google/mt5-base, or facebook/nllb-200-distilled-600M.

Supplementary Data Sources to Mine From the paper and related repos:
ORACC (oracc.org): RINAP, RIAo, RIBo, SAAo, Suhu — all have parallel transliteration + English
veezbo/akkadian_english_corpus: Pre-cleaned Akkademia data on HuggingFace
Electronic Babylonian Library (eBL): Additional cuneiform data
Cuneiform Digital Library Initiative (CDLI): cdli.ucla.edu — metadata and some translations
cuneiform_to_unicode_fixed.csv in the Akkademia repo — mapping table for cuneiform sign → Unicode, useful for any preprocessing pipeline
Bottom Line: Competitive Strategy
The Akkademia team's CNN-based approach from 2023 is your floor. To beat it on Old Assyrian:

Pre-train on the full Akkademia/ORACC corpus (mostly Neo-Assyrian, but it teaches Akkadian structure)
Fine-tune on the competition's Old Assyrian business records
Use a modern architecture — ByT5-large or mT5 will likely outperform fconv
Exploit formulaic patterns — Old Assyrian business records are highly templated
Post-process — dictionary lookup for proper nouns, length normalization, consistent punctuation to maximize both BLEU and chrF++


---

## Entry: `674708`
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674708
- タイトル: How should we tokenize?
- 投稿者: @woosungyoon
- 投稿日時: 2026-02-22
- upvote: 0
- 本文: I’m not participating in this competition,
but it feels like the real challenge begins when we tokenize Akkadian text.

I think experimenting with tokenizers and transformer architectures
might be the easier direction for this competition.

What’s the best way to get better at it?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/674708#3409133
- 投稿者: @steubk
- 投稿日時: 2026-02-22
- upvote: 1
- 本文: best LB public notebooks use byteT5 model that operates directly on UTF-8 bytes without use of a explicit tokenizer

---

## Entry: `672511`
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/672511
- タイトル: Akkadian Translation Competition - Community Knowledge Synthesis
- 投稿者: @prayagp1
- 投稿日時: 2026-02-09
- upvote: 34
- 本文: ⚠️ Important Context
Transparency: This is a synthesis of community discussions and public notebooks, not original research. I'm currently ranked at 35.1 score and learning from the community myself.

Timing Note: Many insights here are from early-to-mid January discussions. The community's understanding has evolved since then. If you're in the top 50, you probably know more than what's written here.

Target Audience: This consolidation is aimed at competitors who are:

New to the competition
Stuck at baseline scores (30-35)
Looking for a starting point before diving deeper
What I HAVE tested personally: AKK-300m failure, bucket batching, length penalty variations, the 35.1 optimization stack.

What I'm synthesizing from others: Training recipes, data quality insights, overfitting analysis.

Request to Top Competitors: If anything here is outdated or wrong, please comment! I want this to be accurate and helpful, not misleading.

Purpose of This Post

After weeks of testing, collaboration, and learning from the community, I wanted to consolidate what's actually working (and what's not) to help everyone still pushing for improvements. This is a synthesis of public discussions, shared notebooks, and systematic testing.

TL;DR: We're at an interesting inflection point. The public model ceiling is ~35.1, and breaking past it requires either custom training data, novel techniques, or collaboration. Here's what we know.

Current State of the Leaderboard

The 35.1 Plateau:

100s of competitors clustered at exactly 35.1
Why: Everyone using the same model (Assia Benkedia's byt5-akkadian-optimized-34x) with minor variations
Implication: To break 35.5+, you need something different
Score Distribution:

Top tier (36.5-38.1): Likely custom training on private Old Assyrian data
Competitive cluster (35.1-36.4): Public model + optimizations
Copy-paste crowd (34.9-35.0): Direct Assia model usage
Baseline methods (<34.9): Older approaches
Critical Insight from Aaron Bornstein:

"High scores on the visible 33% of the test set are likely to degrade significantly on the hidden 67% if they are out of domain"

Public LB (34% of test) ≠ Private LB (66% of test). Conservative, semantically-accurate approaches may outperform pattern-matching models on final evaluation.

Proven Optimization Stack (34.9 → 35.1)

1. Base "Model": Assia Benkedia's byt5-akkadian-optimized-34x (34.9)
IMPORTANT CORRECTION (Thanks to Musa Peker for catching this):

This is actually an ENSEMBLE of three models, not a single model:

/kaggle/input/byt5-akk-gap-sentence-v4-cp-final (likely Assia's)
/kaggle/input/byt5-akkadian-model
/kaggle/input/byt5-base-big-data2
Implication: The 34.9 baseline is achieved through ensemble combination, not a single checkpoint. This means:

Single model ceiling is probably ~33-34
To beat 35.5, you need either a better base model OR different ensemble components
The 35.1 "plateau" makes sense - everyone using the same 3-model ensemble + minor optimizations
Credit: Assia Benkedia for the ensemble approach, plus the contributors of the three base models Availability: Kaggle dataset final-byt5

2. Bucket Batching (+0.1)
Credit: Sera Ria Gomes
What it does: Groups similar-length samples together in batches
Why it works: Reduces padding waste by 20-40% → model sees less noise
Implementation:
class BucketBatchSampler(Sampler):
    """Groups samples by similar length to minimize padding"""
    def __init__(self, lengths, batch_size, num_buckets=4):
        self.lengths = lengths
        self.batch_size = batch_size
        self.num_buckets = num_buckets

        # Sort indices by length
        sorted_indices = sorted(range(len(lengths)), key=lambda i: lengths[i])

        # Divide into buckets
        bucket_size = len(sorted_indices) // num_buckets
        self.buckets = []
        for i in range(num_buckets):
            start = i * bucket_size
            end = start + bucket_size if i < num_buckets - 1 else len(sorted_indices)
            self.buckets.append(sorted_indices[start:end])

    def __iter__(self):
        for bucket in self.buckets:
            indices = bucket.copy()
            for i in range(0, len(indices), self.batch_size):
                yield indices[i:i + self.batch_size]

    def __len__(self):
        return sum(len(bucket) // self.batch_size for bucket in self.buckets)
3. Length Penalty = 1.3-1.5 (+0.1)
Credit: manwithacat (discovered optimal range)
Why it works: Encourages longer, more complete translations
Testing results:
1.3: 35.1 ✅ (conservative)
1.5: 35.1 ✅ (also works)
1.7: 35.0 ❌ (too aggressive)
4. Optimal Configuration
CONFIG = {
    "model": "byt5-akkadian-optimized-34x",
    "num_beams": 8,
    "max_new_tokens": 512,
    "length_penalty": 1.3,  # or 1.5
    "early_stopping": True,
    "batch_size": 8,
    "use_bucket_batching": True,
    "num_buckets": 4
}
Novel Technique: MBR Decoding (Untested Potential)
Credit: Hikari_30
What it does: Minimum Bayes Risk - generates 20 diverse candidates, scores each against all others using chrF++, selects consensus winner
Why it could help:
Reduces hallucination risk (single beam search can hallucinate)
Combines diversity (sampling) + quality (beam search)
No training required - pure inference technique
Validated in NMT research literature
Cost: ~3-4x slower inference
Status: Only 1 person testing it publicly - could improve private LB robustness
Implementation outline:

# Generate 15 diverse candidates (temperature=0.7)
# Generate 5 beam search candidates
# Score each candidate against all others using chrF++
# Select candidate with highest average similarity
❌ Failed Optimizations (Save Your Time!)
1. Onomasticon Name Replacement (0.0 gain)
5,973 Akkadian→English name mappings
Expected: +0.5 to +1.0 (host claimed "biggest single improvement")
Actual: 34.9 → 34.9 (no change)
Why: Model already outputs English names correctly
2. Submission Blending (0.0 gain)
Attempted: Blend Assia's 34.9 with older 34.6 ensemble
Result: Assia's model dominated 100%
Conclusion: Need equal-quality models to blend effectively
3. Hyperparameter Tuning via Optuna (Minimal Impact)
Credit: HARUKI HARADA
Tested 20 combinations on validation set
Best found: length_penalty=1.788, beams=6 → validation score 25.97
Baseline: length_penalty=1.5, beams=8 → validation score 25.58
BUT: They still used baseline for submission (didn't trust Optuna)
Conclusion: Limited impact (~0.4 max), not worth compute time
4. AKK-300m Model (Complete Failure - AVOID!)
Credit: Thalesian/Akkademia Project
Tested Feb 8, 2026
Result: Outputs only <big_gap> tokens (complete garbage)
Why it failed:
Wrong dialect mix (all Akkadian periods, not Old Assyrian specific)
Context window only 64 tokens (vs ByT5's 512)
Multi-task confusion (7+ different tasks)
Cannot submit: Requires internet to download, not in Kaggle datasets
Downloads: 744 in 2 days, but ZERO public successes >35.1
Recommendation: Skip this entirely
5. BetterTransformer
Not accessible in Kaggle environment (deprecated in newer optimum versions)
Multiple workaround attempts failed
Stop pursuing
Critical Warnings & Insights
Data Quality Issues
From Angantyr:

163/1,561 training samples (~10%) have incomplete translations
Pattern: Long Akkadian → First item only, then "…"
Example: 66 tokens → "1 talent … …" (3 words)
Host Confirmation:

"By no means an error-free dataset. Many of these databases are worked on by students with little oversight"

The Overfitting Crisis
From Aaron Bornstein's Systematic Perturbation Testing:

Top models (34-38 scores) are ~40% pattern matchers, not true translators
They hallucinate generic trade sentences from corpus templates
Public LB (34%) ≠ Private LB (67%)
Implication: Conservative, semantically-accurate models may rank higher on private LB
The Metric Trap
From Musa Peker:

Compared two models:
"The Parrot" (pattern matcher): 34.2 score, complete nonsense
"The Domain Expert" (semantic translator): 11.8 score, accurate translations
Key insight: BLEU/chrF++ rewards n-gram overlap, NOT semantic accuracy
Quote: "We are optimizing for a metric that measures 'Vibes' rather than 'Translation'"
Domain Mismatch: EvaCun = ORACC Data
CRITICAL FINDING:

EvaCun corpus IS the ORACC dataset
Time Period: Neo-Assyrian (~911-539 BCE)
Competition: Old Assyrian (~1950-1750 BCE)
Gap: 1,000 years wrong!
Host Quote: "Would you include Middle English to train modern English? Probably not."
Recommendation: ❌ DO NOT USE for training
💻 Working Code: Complete Inference Pipeline
"""
ASSIA'S MODEL + BUCKET BATCHING + OPTIMAL LENGTH PENALTY
Expected Score: 35.1

NOTEBOOK SETUP:
- Accelerator: GPU T4 x2
- Internet: OFF  
- Datasets: deep-past-initiative-machine-translation, final-byt5
"""

import re
import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader, Sampler
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# ============================================================
# CONFIGURATION
# ============================================================
CONFIG = {
    "test_path": "/kaggle/input/deep-past-initiative-machine-translation/test.csv",
    "model_path": "/kaggle/input/final-byt5/byt5-akkadian-optimized-34x",
    "device": torch.device("cuda" if torch.cuda.is_available() else "cpu"),
    "max_length": 512,
    "batch_size": 8,
    "num_buckets": 4,

    "generation": {
        "num_beams": 8,
        "max_new_tokens": 512,
        "length_penalty": 1.3,  # or 1.5
        "early_stopping": True
    }
}

# ============================================================
# BUCKET BATCH SAMPLER (SERA'S OPTIMIZATION)
# ============================================================
class BucketBatchSampler(Sampler):
    def __init__(self, lengths, batch_size, num_buckets=4):
        self.lengths = lengths
        self.batch_size = batch_size
        self.num_buckets = num_buckets

        sorted_indices = sorted(range(len(lengths)), key=lambda i: lengths[i])

        bucket_size = len(sorted_indices) // num_buckets
        self.buckets = []
        for i in range(num_buckets):
            start = i * bucket_size
            end = start + bucket_size if i < num_buckets - 1 else len(sorted_indices)
            self.buckets.append(sorted_indices[start:end])

    def __iter__(self):
        for bucket in self.buckets:
            indices = bucket.copy()
            for i in range(0, len(indices), self.batch_size):
                yield indices[i:i + self.batch_size]

    def __len__(self):
        return sum(len(bucket) // self.batch_size for bucket in self.buckets)

# ============================================================
# PREPROCESSING & POSTPROCESSING
# ============================================================
def preprocess_input(text):
    """Minimal preprocessing for test data"""
    if pd.isna(text):
        return ""
    text = str(text)
    text = re.sub(r'(\.{3,}|…+)', '<big_gap>', text)
    text = re.sub(r'(xx+|\s+x\s+)', '<gap>', text)
    return text

def postprocess_output(text):
    """Clean model output - proven effective stack"""
    if not isinstance(text, str) or not text.strip():
        return ""

    # 1. Normalize ḫ/Ḫ → h/H (test set uses h)
    text = text.replace('ḫ', 'h').replace('Ḫ', 'H')

    # 2. Subscript numbers → regular
    subscript_map = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")
    text = text.translate(subscript_map)

    # 3. Normalize gaps in output
    text = re.sub(r'(\[x\]|\(x\)|\bx\b)', '<gap>', text, flags=re.I)
    text = re.sub(r'(\.{3,}|…)', '<big_gap>', text)

    # 4. Remove scribal annotations
    text = re.sub(r'\((fem|plur|pl|sing|\?|!)\.?\)', '', text, flags=re.I)

    # 5. Protect gap markers, remove forbidden chars
    text = text.replace('<gap>', '\x00GAP\x00')
    text = text.replace('<big_gap>', '\x00BIG\x00')
    forbidden = '!?()"—–<>⌈⌋⌊[]+ʾ/;'
    text = text.translate(str.maketrans('', '', forbidden))
    text = text.replace('\x00GAP\x00', ' <gap> ')
    text = text.replace('\x00BIG\x00', ' <big_gap> ')

    # 6. Unicode fractions
    text = re.sub(r'(\d+)\.5\b', r'\1 ½', text)
    text = re.sub(r'(\d+)\.25\b', r'\1 ¼', text)
    text = re.sub(r'(\d+)\.75\b', r'\1 ¾', text)

    # 7. Remove word repetitions
    text = re.sub(r'\b(\w+)(?:\s+\1\b)+', r'\1', text)

    # 8. Final cleanup
    text = re.sub(r'\s+', ' ', text).strip()

    return text

# ============================================================
# DATASET CLASS
# ============================================================
class AkkadianDataset(Dataset):
    def __init__(self, df):
        self.ids = df['id'].tolist()
        self.texts = [
            "translate Akkadian to English: " + str(t) 
            for t in df['transliteration']
        ]
        self.lengths = [len(t.split()) for t in self.texts]

    def __len__(self):
        return len(self.ids)

    def __getitem__(self, idx):
        return self.ids[idx], self.texts[idx]

# ============================================================
# MAIN INFERENCE
# ============================================================
print("Loading test data...")
test_df = pd.read_csv(CONFIG['test_path'])
test_df['transliteration'] = test_df['transliteration'].apply(preprocess_input)

print("Loading model...")
model = AutoModelForSeq2SeqLM.from_pretrained(CONFIG['model_path']).to(CONFIG['device']).eval()
tokenizer = AutoTokenizer.from_pretrained(CONFIG['model_path'])

print("Creating dataset with bucket sampling...")
dataset = AkkadianDataset(test_df)
sampler = BucketBatchSampler(dataset.lengths, CONFIG['batch_size'], CONFIG['num_buckets'])

def collate_fn(batch):
    ids = [item[0] for item in batch]
    texts = [item[1] for item in batch]
    encoded = tokenizer(texts, max_length=CONFIG['max_length'], 
                       padding=True, truncation=True, return_tensors="pt")
    return ids, encoded

dataloader = DataLoader(dataset, batch_sampler=sampler, collate_fn=collate_fn, num_workers=2)

print("Running inference...")
predictions = []
with torch.inference_mode():
    for batch_ids, encoded_inputs in dataloader:
        outputs = model.generate(
            input_ids=encoded_inputs.input_ids.to(CONFIG['device']),
            attention_mask=encoded_inputs.attention_mask.to(CONFIG['device']),
            **CONFIG['generation']
        )
        decoded = tokenizer.batch_decode(outputs, skip_special_tokens=True)
        cleaned = [postprocess_output(text) for text in decoded]
        predictions.extend(zip(batch_ids, cleaned))

# Create submission
submission = pd.DataFrame(predictions, columns=['id', 'translation'])
submission.to_csv('submission.csv', index=False)
print(f"Done! Saved {len(submission)} translations. Expected score: 35.1")
🎯 Strategic Insights
For Breaking Past 35.1
You need ONE of these:

Custom Training Data (3,000-5,000 clean Old Assyrian sentence pairs)

Top scorers manually extracted from PDFs (40-100+ hours of work)
Could potentially automate with LLM-assisted extraction
Novel Inference Techniques

MBR decoding (Hikari_30's approach - untested by most)
Ensemble of equal-quality models (not just Assia + older models)
Collaboration

Aaron Bornstein climbed from #48 → #24 (his methods work!)
Combine complementary skills: data processing + inference optimization
Training Insights (If You Go That Route)
From Jean-Louis Roy (#5) - Validated Recipe:

EPOCHS = 10-15  # NOT 26+
MAX_LENGTH = 512  # NOT 256
BATCH_SIZE = 4
GRADIENT_ACCUMULATION_STEPS = 4
LEARNING_RATE = 5e-5
FP16 = False  # Critical - prevents NaN errors
From Jack (#2) - CORRECTED (Thanks to hongan for catching this):

What I originally wrote was WRONG. Jack clarified his actual approach:

✅ What Jack actually does:

"95% is preprocessing/formatting" - BUT this means CAREFUL MANUAL REVIEW
Manually reviewed EVERY document in train.csv (where he gained most score)
Follows recommended formatting guidelines
Tests different approaches on training data
Ensures meaning alignment in samples
❌ What Jack does NOT do:

Keep training data "as is" without review
Avoid cleaning training data
Only preprocess test data
Key quote (Feb 2026): "I really started to gain in score when I manually reviewed (briefly - still finding things I've missed) each and every document in the train.csv."

About sentence alignment: "Sentence alignment didn't work for me because my sentences sucked 😭" (This was about HIS implementation, not the approach itself)

Critical insight: "If your formatting is off, especially on translations, nothing else you do will matter since your model isn't matching the desired output format."

From 耶✌ :

Gap preprocessing applied to BOTH columns (transliteration AND translation)
Sentence alignment from Sentences_Oare_FirstWord_LinNum.csv improved score +0.5
MAX_LENGTH progression validated: 385 → 475 → 512 (each step +0.2-0.3)
Safe Data Sources
✅ SAFE TO USE
train.csv (1,561 samples) - Original competition data
Sentences_Oare_FirstWord_LinNum.csv (9,782 alignments) - If verified against first_word matching
⚠️ USE WITH CAUTION
published_texts.csv (7,953 samples) - Transliterations only, unknown time period mix
❌ DO NOT USE
EvaCun Corpus / ORACC Data - Neo-Assyrian (911-539 BCE), 1,000 years wrong!
Medal Zone Strategy
Gold (Top 15): Requires custom data OR collaboration OR breakthrough technique

Silver (Top 50): Achievable with proven optimization stack (35.1-35.3)

(Top 200): Public model baseline (34.9-35.0)

Key Decision: Private LB shake-up probability ~60% (per Aaron Bornstein's analysis). Conservative, semantically-accurate approaches may outperform pattern-matching models on final evaluation.

🙏 Credits & Acknowledgments
Major Contributors (in alphabetical order):

Aaron Bornstein - Overfitting analysis, perturbation testing
Angantyr - Incomplete translation analysis
Assia Benkedia - byt5-akkadian-optimized-34x model (publicly released)
HARUKI HARADA - Optuna hyperparameter tuning, chunked beam search
Hikari_30 - MBR decoding technique
Jack - Preprocessing insights ("95% is preprocessing")
Jean-Louis Roy - Validated training recipe
manwithacat - Length penalty optimization discovery
MPWARE - ḫ/h issue discovery, determinative inconsistency
Musa Peker - Metric trap analysis
Sera Ria Gomes - Bucket batching optimization
Thalesian/Akkademia - AKK-300m model (tested and documented as failed)
耶✌ - Gap preprocessing methodology, sentence alignment
Host (DeepPast Initiative) - For hosting this fascinating competition and providing clarifications throughout

Apologies
If I missed giving proper credit to anyone or misattributed any techniques, please let me know in the comments and I'll update immediately. This synthesis is based on public discussions and notebooks—if you contributed something I didn't mention, that's my oversight, not intentional!

Good luck to everyone in the final push! 51 days to go.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/672511#3403657
- 投稿者: @jackvd
- 投稿日時: 2026-02-09
- upvote: 5
- 本文: I made a lot of mistakes in my preprocessing early on.. I’m not totally sure when that quote is from but it was probably early.

I’d still argue 95% of this will be preprocessing/formatting your transliterations/translations.. but, I’d follow the recommended guidelines. Also, sentence alignment didn’t work for me because my sentences sucked 😂

If your formatting is off, especially on translations, nothing else you do will matter since your model isn’t matching the desired output format.

I would start off with minimal changes to the train.csv but you should 100% test different things and ensure meaning is aligned in your samples as well. I really started to gain in score when I manually reviewed (briefly - still finding things I’ve missed) each and every document in the train.csv.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/672511#3403583
- 投稿者: @musapeker
- 投稿日時: 2026-02-09
- upvote: 3
- 本文: Great synthesis! This is a very comprehensive summary of the current state of the competition. Thanks for putting this together.

I just wanted to add a small technical correction regarding the "Base Model" section (Assia Benkedia's byt5-akkadian-optimized-34x). Upon inspecting the model files and configuration, it appears this is actually an ensemble technique rather than a single model.

The code references a list of BASE_MODELS that includes:

/kaggle/input/byt5-akk-gap-sentence-v4-cp-final (Likely Assia's) /kaggle/input/byt5-akkadian-model /kaggle/input/byt5-base-big-data2

So, the 34.9+ baseline is achieved by ensembling these public models. It’s worth acknowledging that the performance comes from combining the work of multiple contributors/models, not just a single checkpoint.

Thanks again for the great overview!

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/672511#3403590
- 投稿者: @prayagp1
- 投稿日時: 2026-02-09
- upvote: 1
- 本文: Thank you for the correction.

This is a great info! This also explains why submission blending didn't work for me (I was trying to blend an ensemble with another ensemble)

Quick clarifications:

Is the ensemble using simple averaging, or weighted voting?
Do you know if the 3 base models were trained on different data splits, or different approaches?
Does this mean a well-trained single model could potentially reach around 34 on its own?
Updated the post with this info. Really appreciate this technical detail!

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/672511#3403592
- 投稿者: @musapeker
- 投稿日時: 2026-02-09
- upvote: 1
- 本文: This is not a classic inference-time ensemble; instead, it merges the model weights. The parameters of three different ByT5 checkpoints were averaged using Weighted Parameter Averaging with predefined ratios, producing a single new model.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/672511#3404133
- 投稿者: @musapeker
- 投稿日時: 2026-02-10
- upvote: 0
- 本文: Thanks so much for the technical details about the ensemble! I updated my post to mention it's weighted parameter averaging(without specific weights or code though).

This explains why submission blending didn't work for me(I was trying to ensemble an already-ensembled model with another ensemble).

One question if you don't mind: do you know if the 3 base models were trained on different data or just different hyperparameters/random seeds? Trying to figure out if I should be aiming for diversity in training data or diversity in model architecture for my own attempts.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/672511#3406687
- 投稿者: @musapeker
- 投稿日時: 2026-02-16
- upvote: 0
- 本文: I don’t have definitive information on whether these models were trained on different datasets or whether the differences arise from architectural choices, hyperparameters, or random seeds.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/672511#3403581
- 投稿者: @honganzhu
- 投稿日時: 2026-02-09
- upvote: 3
- 本文: respect the effort. However, I believe many of your quotes and suggestions are not entirely accurate, mainly because they are comments made 2 months ago (!) and I believe we, as a community, have gained a better understanding of the data since then… IMO you need to be prepared to spend many more hours on this task in order to beat the public model and understand why you are doing better, but i could be wrong😀 And until you have gone through the train data at least once, i would refrain from giving any advice to other people…

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/672511#3403585
- 投稿者: @prayagp1
- 投稿日時: 2026-02-09
- upvote: 0
- 本文: Really appreciate the feedback! You're absolutely right that:

I haven't yet gone through the training data line-by-line myself
many of these insights are from early jan discussions (2 months old)
im synthesizing community knowledge, not presenting original research My intent was to consolidate scattered information(added additional context to the post) for people entering the competition now, but I should have been clearer about what I've personally tested vs. what I'm reporting from others.
Quick question, what have you learned in the past 2 months that contradicts or updates the insights here? I'm genuinely curious what the top competitors know now that we didn't know in January. Happy to update the post with newer findings!

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/672511#3403591
- 投稿者: @honganzhu
- 投稿日時: 2026-02-09
- upvote: 0
- 本文: for example, i believe the "insight" you are giving here is very far from being true:

"95% is preprocessing. Every attempt to follow instructions for cleaning data led to worse performance." Keep training data as close to original as possible Heavy preprocessing ONLY for test/inference data Adding sentence-level data from published_texts.csv made his model WORSE

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/672511#3404132
- 投稿者: @prayagp1
- 投稿日時: 2026-02-10
- upvote: 0
- 本文: Yeah, good catch on that one.

Turns out I completely misread what Jack meant. Pretty much the opposite of what I wrote lol.

Updated the post with the correction.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/672511#3403740
- 投稿者: @hikari30
- 投稿日時: 2026-02-10
- upvote: 2
- 本文: I unintentionally made one of my notebooks public. While it wasn't my initial intention, I would be happy if it could contribute to the community's learning and discussion.

Currently, I suspect that the top scores on the Public LB might be overfitting. Therefore, I believe the key to success in this competition—beyond just improving raw model performance—is focusing on robustness. In other words, our goal should be to minimize the "shake" and ensure the model generalizes well to the private data.

P.S. We are looking for teammates! If you are passionate about LLMs or interested in translation tasks, let’s team up! Please feel free to reach out.

Happy Kaggling!

---

## Entry: `673455`
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/673455
- タイトル: Public tool for easier OCR of PDF documents
- 投稿者: @angantyr
- 投稿日時: 2026-02-14
- upvote: 9
- 本文: A public notebook on lighter/faster OCR of PDF docs is now live. Hopefully, this will make many of the documents more accessible.

The biggest and heartful thanks to @mpware for starting a thread on OCR experiments with The Assur-nada Archive (Larsen 2002), sharing their results as a public dataset, starting the discussion (Any luck with letters from Larsen PDF?) and being an inspiration for using the GLM-OCR model. Without all of the above this work would not be possible.

The notebook constitutes a minimum working example for anyone attempting to OCR the PDF documents for the Deep Past Challenge by using nothing more than a T4 machine provided by Kaggle. The code base was created with the help of Gemini 3 on Google Colab. It is not the cleanest, not the prettiest but I strived to make it leaner and faster than it would be for loading an entire page. Current output is pretty good and typically needs only a bit of manual work to be fully compliant.

Known issues
The GLM-OCR struggles to capture emphatic s (ṣ) and t (ṭ), and sometimes even vowels. It will typically use HTML tags for sub/superscripts (<sub></sub> and <sup></sup>) but may use LaTeX notation as well (e.g., $ gu_{5} $ for gu₅). It's also not consitent about it, so be on the lookout.

Format
The OCR result is a list of translations for each block. This is intentional and is meant to be the most general to work with most PDF documents. In some cases like The Assur-nada Archive (Larsen 2002) the transliterations form a leftmost column, while translations for a right-most column. For such cases it is trivial to use the extracted block position metadata (saved to a metadata.csv file) to filter out the transliteration/translation blocks and re-arrange/join the text. It is not the case for the AKT series, for which the both transliterations and translations come after one another and occupy the full width (at least for AKT 1990; I have not checked all of them).

Input
Larsen 2002 p.73 AKT 1 1990 p.34

Output
Reconstructed text (left) compared with the original text (right). There are still some errors. but not too many. Sub/supersctipts formatted to the _/^ notation. 

Good luck!

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/673455#3406097
- 投稿者: @mpware
- 投稿日時: 2026-02-15
- upvote: 3
- 本文: Very good! I've started to work on AKT PDF files. I hope to get better results with Larsen and AKT as soon as Kaggle and the sponsor will annonce the rules about < gap > < big_gap >. It looks like that bad (or good) handling of them could lead to -+2 or 3 on LB. From what I've read on discord it should be next week.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/673455#3406172
- 投稿者: @angantyr
- 投稿日時: 2026-02-15
- upvote: 1
- 本文: Good news, everyone!

Due to a mistake on my end, I happened to verify that the notebook is able to work without a GPU.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/673455#3406084
- 投稿者: @nlztrk
- 投稿日時: 2026-02-15
- upvote: 0
- 本文: This seems excellent! I appreciate your effort.

---

## Entry: `668402`
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/668402
- タイトル: Compiled Discussions To Read (Avoid Bad Advice)
- 投稿者: @jackvd
- 投稿日時: 2026-01-17
- upvote: 82
- 本文: If you feel stuck or have any questions, here are all the discussions you should read over:

Two practical stumbling blocks in Akkadian → English MT (and how to address them)
The translation column of the final test predictions into the corresponding and tags
How To Handle These Examples
Other Public Data
Incomplete translations
Unicode Fractions vs Decimals: LB Score Unchanged?
How to handle dot h/H?
Question about OA_Lexicon_eBL.csv - Personal Name Spelling Inconsistency with Ground Truth
You should also review the dataset instructions section of the overview page.

---

## Entry: `665209`
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209
- タイトル: Two practical stumbling blocks in Akkadian → English MT (and how to address them)
- 投稿者: @deeppast
- 投稿日時: 2026-01-31
- upvote: 61
- 本文: Based on recent experiments and discussions with several participants, I want to share a set of observations about what appear to be the primary bottlenecks in this competition. These are not model-architecture issues per se, but data- and representation-level issues that strongly affect downstream training, evaluation, and reinforcement learning.

After multiple iterations, debugging sessions, and failed-but-informative experiments, two main stumbling blocks consistently emerge:

(1) Named entities (personal names, place names, divine names) (2) Inconsistent ASCII / transliteration formats across Akkadian datasets

Both issues disproportionately affect tokenization, alignment, and reward stability, and in practice they limit performance more than model size or optimizer choice.

1. Named entities are a dominant source of error
Personal names, geographic names, and divine names behave very differently from ordinary lexical items:

They are often transliterated inconsistently across editions.
They frequently preserve older orthographic conventions.
They are semantically opaque to the model unless explicitly supported.
In experiments, many otherwise reasonable translations fail almost entirely because a name is mangled, dropped, or hallucinated. This affects not only final accuracy but also reward-based methods, where small orthographic deviations can collapse a sentence-level score.

To address this, I have prepared an onomasticon (a curated list of names and attested spellings), which I will share as supplemental data. Participants may find it useful to:

add it as a lookup or constraint layer,
bias decoding for known names,
or use it for post-generation repair.
Even partial normalization of named entities tends to improve both perceived translation quality and metric stability.

2. Transliteration format normalization is not optional
A second, and often underestimated, issue is ASCII-format variation in Akkadian transliteration. Different corpora encode the same underlying text using different conventions, many of which are not interchangeable without loss.

A concrete example that came up in a private discussion illustrates the problem. One approach converted diacritics into ASCII sequences (e.g., š → sz, ú → u2, etc.) before training. This is a reasonable instinct, but in this case it was done in the wrong direction: the evaluation data already contains diacritics, and reducing the alphabet removed distinctions that are semantically meaningful in Akkadian.

For example, the evaluation data expects forms like:

i-ṣí-ba-at rather than i-Si₂-ba-at
KÙ-pì-a rather than KU₃-pi₃-a
KIŠIB rather than KISZIB
The key takeaway is that the competition data uses an extended alphabet by design, and collapsing it into ASCII can degrade both meaning and alignment. While this increases tokenization difficulty, preserving distinctions such as s / ṣ / š and t / ṭ is preferable to losing them.

The recommended strategy is therefore:

keep diacritics,
convert ASCII substitutes (e.g., sz) into diacritics,
and normalize everything toward the format used in the training and evaluation sets.
Gaps, damage markers, and parallel alignment [update: 2/18/26]
Another recurring source of confusion concerns damaged text and gap markers in the data:

x represents a single broken sign,
sequences like x x x x or ... represent a larger lacuna.
For modeling purposes we reduced all breaks to a single marker: <gap>

we removed the tag for <big_gap> from the train and test (and other transliterations). We also deduplicated instances multiple sequential gaps (e.g. <gap> <gap, <gap>-<gap>, <gap> <gap>, <gap>. <gap>, etc.
Ideally, these gap markers would be parallelized between transliteration and translation whenever possible. However, this was not completely accomplished, as the translation we had access to did not pay strict attention to the gaps. This will be an aspect of the challenge in which a significant advantage will remain for those who have controlled for this data. If a large gap appears in one side but not the other, the model is forced to learn misalignment rather than translation.

This also applies to edge cases such as <gap> attached to a word (e.g., <gap>-A-šùr), which should be preserved rather than blindly removed.

Why this matters for training and RL-based methods
Many participants have observed that standard supervised fine-tuning produces reasonable loss curves, while reinforcement or preference-based methods fail to improve or show no reward signal. In nearly all cases examined so far, this traces back to output non-conformance caused by the issues above.

If the model is penalized for:

orthographic mismatches,
bracket artifacts,
inconsistent gap handling,
or malformed named entities,
then reward functions cannot reliably distinguish “closer” from “farther” outputs. Addressing normalization and alignment first makes rewards smoother and learning signals usable.

Closing note
None of this is meant as criticism of existing approaches; these are difficult problems, and much of the complexity comes from the philological nature of the data itself. The hope in sharing this publicly is to reduce duplicated effort and make preprocessing choices more transparent across submissions.

I will continue to share supplemental resources (including the onomasticon) as they are finalized, and I’m happy to discuss normalization or alignment strategies further if helpful to others.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3417055
- 投稿者: @souhardyatalukdar
- 投稿日時: 2026-03-04
- upvote: 2
- 本文: @deeppast , while going through your onomasticon and the train labels, i noticed that there are some differences in the naming convention.

Example 1 — Different name entirely:

Akkadian token: šu-{d}EN.LÍL , Onomasticon canonical form: Šu-Enlil , Actual training label: Šu-Illil

Example 2 — Geminate consonant:

Akkadian token: šu-ku-tum , Onomasticon canonical form: Šukatum , Actual training label: Šukkutum

(The onomasticon drops the geminate kk that the training labels preserve.)

Example 3 — Long vowel:

Akkadian token: ṣí-lu-lu , Onomasticon canonical form: Ṣilulu , Actual training label: Ṣilūlu

(The onomasticon omits the macron on the ū that the training labels include.)

these are some examples pointed out by claude. which convention do the test labels follow — the onomasticon's or the training data's?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3417798
- 投稿者: @angantyr
- 投稿日時: 2026-03-06
- upvote: 1
- 本文: @deeppast Clarification needed.

I'm going through the glossaries and find that in Summerian the nasal "ŋ" is used somewhat often. This appears, e.g., in the determinative for wood {ŋeš}, which for this competition is written as {geš}. Can we safely assume ŋ -> g substitution as valid?

Another question is about treating Summerian words from the ORACC glossary, e.g., {na₄}za-gin₃-ŋu₁₀. Intuitively I would change that into: NA₄.ZA.GÌN-gu₁₀, i.e.:

treat the base as a summerogram -> uppercase, no {}, .-joined
treat the rest as a --joined suffix
What would be the approach to best match the data in train.csv and other sources?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3402145
- 投稿者: @tatamikenn 
- 投稿日時: 2026-01-31
- upvote: 11
- 本文: @deeppast Regarding normalization, could you clarify which of the following is true for the test set?

Both transliterations and translations are already normalized (i.e., tokens like and are already present in both columns).
Only the translations are normalized. Participants must implement their own logic to convert x or ... into <gap> or <big_gap> for the test transliterations.
If Case 2 is true, the final scores will be highly sensitive to specific preprocessing choices. This could turn the competition into a "preprocessing lottery" and encourage over-fitting to the Public LB rather than improving the actual MT model.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3384015
- 投稿者: @nlztrk
- 投稿日時: 2026-01-31
- upvote: 8
- 本文: I want to be sure on these cases:

<big_gap> <gap> → <big_gap>
<gap> <big_gap> <gap> → <big_gap>
<big_gap> <big_gap> → <big_gap>
<gap> <gap> → <big_gap>
someword-<gap> <gap>-someword → someword-<gap> <gap>-someword OR someword-<big_gap>-someword ?
<big_gap> <gap>-A-šùr → <big_gap> <gap>-A-šùr
xxxx-kam (train.csv line 43) → <big_gap>-kam OR <big_gap> <gap>-kam ?
It would be good to take feedback on these from you.

I think that having to figure out the normalization logic you are using prevents us from focusing on the actual goal of the competition. There is some processing happening in the background that also affects the original “ground truth” translations you have, so instead of focusing on the machine learning part we end up spending our effort on reverse-engineering your normalization logic. Can't you share the transliteration-translation preprocessors you're using?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3384059
- 投稿者: @mpware
- 投稿日時: 2026-01-31
- upvote: 1
- 本文: I'm wondering how to interpret this section that is unclear to me about "?", "!", and ":" for translations :

https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/overview/dataset-instructions

Formatting Suggestions for Transliterations and Translations:

Remove (modern scribal notations):

! (certain reading)
? (questionable reading)
/ (line divider) - Now we now there is none of these according to @deeppast
: OR . (word divider)
We've a lot of ?!: in training set translations. But do we have the same in test set?

Should we apply the suggestion above => Remove all !?: from translations in training set. Or only if they are enclosed with parenthesis.

Some make sense to me with ":" usage for a rate and "?" for a question in translation. It does not look questionable reading for the question marks below.

ff9442fd-9e7d-449c-a2d6-0cc35921cd65: Šalim-Aššur answered: "And what if I have tin and from my goods remaining in his possession? Will he pay me at the rate 6:1 for my tin and 15 shekels per in silver?"

Here the ":" make sense too. If I remove ":" then I should remove ";" too here.

00f0d841-eb7a-46f8-86fc-bf9fd7d52cbf: From Šu-Tammuzī, Elaya, Ennam-Aššur and Lamassī to Ennam-Aššur and Ali-ahum: In accordance with your missive we have hired a attorney for you; Abiya son of Bebe is our attorney.

I would just remove things like: "(?)", "(!)", "(fem. plur.)", "(fem.)", "(plur.)", "(pl.)", "(sing.)", "(plural)"

Can't you share the transliteration and translation list of characters you're using / allowing?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3384200
- 投稿者: @deeppast
- 投稿日時: 2026-01-05
- upvote: 8
- 本文: Good questions, here's the character list for transliterations:

Transliterations Characters

-
a
A
i
I
u
U
m
M
š
Š
n
N
b
B
r
R
t
T
l
L
k
K
G
g
í
Í
D
d
Ù
ù
á
Á
.
ú
Ú
p
P
e
E
h
H
q
Q
1
ṣ
Ṣ
é
É
<
>
à
À
4
z
Z
s
S
ì
Ì
5
_
2
0
½
w
W
3
{
}
ṭ
Ṭ
6
⅓
8
⅔
7
è
È
⅚
9
¼
!
+
⅙
ı
…
ş
İ
:
Translations Characters

'
?
e
E
a
A
i
I
t
T
n
N
s
S
o
O
r
R
l
L
h
H
u
U
m
M
d
D
F
f
š
Š
-
p
P
w
W
b
B
g
G
y
Y
.
K
k
,
C
c
v
ā
1
)
(
<
>
z
Z
_
Q
q
2
ī
ṭ
Ṭ
0
:
3
½
5
;
x
ē
4
ū
6
ṣ
Ṣ
⅓
8
’
!
7
j
J
⅔
“
”
9
–
⅚
¼
⅙
"
‘
ı
—
[
]
ğ
â
+
à
ş

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3384450
- 投稿者: @steubk
- 投稿日時: 2026-01-05
- upvote: 2
- 本文: did you actually publish the test set in plain chars ? 🧐

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3384470
- 投稿者: @angantyr
- 投稿日時: 2026-01-05
- upvote: 1
- 本文: The frequency counts are the same for upper and lower case -- the counter looks like it's case-insensitive. Is it intentional?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3384470
- 投稿者: @qifeihhh666 
- 投稿日時: 2026-01-05
- upvote: 1
- 本文: I have the same confusion, but I’ve been submitting consistently to check if the LB score improves. I can now say it helps – after fixing a lot of formatting issues, my LB score has gone up to 32.3.Happy new year!

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3384712
- 投稿者: @deeppast
- 投稿日時: 2026-01-05
- upvote: 1
- 本文: Thanks, yes those numbers were way off, the formula I used was wrong. I'll see if I can get the right counts, but at least the character set should help.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3384718
- 投稿者: @deeppast
- 投稿日時: 2026-01-05
- upvote: 3
- 本文: these are all unicode characters (UTF-8)

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3387378
- 投稿者: @anaphase21
- 投稿日時: 2026-01-07
- upvote: 3
- 本文: Does the translation character list apply to the target test translations, or it only applies to the train translations? Specifically, do you expect our generated translations to use unicode fractions (e.g., ¼) or normal texts (e.g., 1/4)?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3387879
- 投稿者: @nofreewill
- 投稿日時: 2026-01-08
- upvote: 0
- 本文: I suppose this is the hidden test set, right? Are there missing characters because the data source for it is different, or it just happened to be this way because of the random split got it this way (I doubt it)? If the data source is different, are there other such crucial characteristic differences that we should know of? Is public set a subset of the hidden test set?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3384718
- 投稿者: @deeppast
- 投稿日時: 2026-01-08
- upvote: 3
- 本文: Yes, that's correct. The test set wasn't in an online database for starters. I realize these formatting issues are frustrating, but our long-term hope is that the resulting MT model will be able to handle these different formatting differences, and not just overfit on the test set. For this reason the 8k published texts were provided to give a larger sample of these different formats.

It's worth mentioning here that the other databases out there (e.g. CDLI, ORACC, eBL, Archibab) also have different transliteration formats. It is perhaps too ambitious to hope that all of these formats can be harmonized at this time / for this challenge, but it is a long-term goal within my research.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3394612
- 投稿者: @angantyr
- 投稿日時: 2026-01-21
- upvote: 3
- 本文: Transliterations Characters
!+-.0123456789:<>ABDEGHIKLMNPQRSTUWZ_abdeghiklmnpqrstuwz{}¼½ÀÁÈÉÌÍÙÚàáèéìíùúİışŠšṢṣṬṭ…⅓⅔⅙⅚

Translations Characters
!"\'()+,-.0123456789:;<>?ABCDEFGHIJKLMNOPQRSTUWYZ[]_abcdefghijklmnopqrstuvwxyz¼½àâāēğīışŠšūṢṣṬṭ–—‘’“”⅓⅔⅙⅚

(Characters sorted for brevity and a better view)

@deeppast

I wanted to come back to this as new question appeared regarding the character set.

Several of those characters do not appear in the train.csv or are extremely rare and I'd like to know more on how to handle those cases, as it appears the normalization steps needed may affect scoring.

Unknown special characters (şİıâ)
Conversing with Gemini gave me the following clues:

ş = ṣ (used in older publications)
İ = I (Uppercase i written with dot - typical for Turkish sources)
ı = i (Lowercase i but dotless - typical for Turkish sources)
Not normalized characters (…:!{})
As per Formatting suggestions for Transliterations and Translations we should treat these as artifacts from the normalization process:

… - replace with <big_gap>
: - replace with a dot (.)
! - remove (scribal note for certain reading of a sign)
{} - replaces () determinatives (predominant use in train.csv and OA_lexicon.eBL.csv)
Same fractions (¼½⅓⅔⅙⅚) in transliterations/translations
This strongly suggests that at least part of the translations do not recalculate the fractions, i.e., 1.83333 ma-na 3.5 GÍN becomes 1⅚ ma-na 3½ GÍN in test but becomes 1⅚ mina 3½ shekels while in train.csv it is recalculated to 1 mina 56.5 shekels (1 mina 56½ shekels with Unicode fraction notation).

Should we retain the fractions as they are in the transliterations or should we recalculate them?

Translation characters àâğ\'()‘’“”
à = ā ?
â = ā ?
ğ = g ?
\ - a line divider (remove), alternative reading?
' - glottal stop?
() - additional information, e.g. (fem. plur.)
‘’ - should be standardized to ''?
“” - should be standardized to ""?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3384067
- 投稿者: @qifeihhh666
- 投稿日時: 2026-01-31
- upvote: 3
- 本文: From my LB results, not merging <gap> <big_gap>performs a bit better.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3384210
- 投稿者: @deeppast 
- 投稿日時: 2026-01-31
- upvote: 9
- 本文: Yes, sorry for the confusion. Here's what I have found in terms of co-occurrances of gaps with

P.S. This is not an exhaustive list, but a representative one.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3384436
- 投稿者: @nlztrk
- 投稿日時: 2026-01-31
- upvote: 3
- 本文: You said

In practice, collapsing combinations such as <gap> <big_gap> or <big_gap> <gap> into a single <big_gap> on both sides improves sentence-level alignment and reduces noise.

but the list you shared includes non-merged combinations.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3385136
- 投稿者: @deeppast
- 投稿日時: 2026-01-31
- upvote: 2
- 本文: As for the two questions you posed here:

Both of these can be found: someword-< gap > < gap >-someword AND someword-< big_gap >-someword
xxxx-kam → < big_gap >-kam
x-kam → < gap >-kam

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3386031
- 投稿者: @mpware
- 投稿日時: 2026-01-31
- upvote: 1
- 本文: @nlztrk Did it work for you to collapse gaps? CV is stable but LB is worse here with simple gap/big_gap merge:

def collapse_gaps(text):
    """
    Collapse consecutive <gap>/<big_gap> into a single <big_gap>.
    Keep single isolated <gap> as-is.
    """
    tokens = text.split()

    collapsed = []
    i = 0
    n = len(tokens)

    while i < n:
        if tokens[i] in {"<gap>", "<big_gap>"}:
            j = i
            while j < n and tokens[j] in {"<gap>", "<big_gap>"}:
                j += 1

            run_len = j - i

            # If more than one gap marker => big gap
            if run_len >= 2:
                collapsed.append("<big_gap>")
            else:
                collapsed.append(tokens[i])

            i = j
        else:
            collapsed.append(tokens[i])
            i += 1

    return " ".join(collapsed) 

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3386115
- 投稿者: @nlztrk
- 投稿日時: 2026-01-31
- upvote: 3
- 本文: Im collapsing all big gaps into one big gap and all adjacent big gaps and gaps into a big gap. For now it works as the best. But the examples of the organizator violates this logic, we still don't know theirs.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3385720
- 投稿者: @leedrake
- 投稿日時: 2026-01-04
- upvote: 4
- 本文: This is my main worry about participating in this contest. I've been working on cuneiform LLMS for the past two years, and a good text pipeline has to standardize the presentation from multiple script types (on my end I'm also working with Elamite, Sumerian, and Hittite). Getting it to align with ASCII helps learnability tremendously if one wants to leverage pre-trained models like T5 or NLLB. But I don't know how we prepare the unknown text - can we write an input pipeline (and prompt structure) to take in the unknown data with a submission?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3385029
- 投稿者: @edwardxiao01
- 投稿日時: 2026-01-02
- upvote: 2
- 本文: For the subscripts used in the determinatives, do they also need to be transformed to either diacritics or plain numbers?

e.g. should it be {tug₂} or {tug2} ?
On second thought, since the determinatives appear only in the transliteration text, I can pick either scheme. Then, during inference, I can detect the determinatives in the test set input (should be fairly easy) and transform them according to the scheme I pick.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3385134
- 投稿者: @deeppast
- 投稿日時: 2026-01-03
- upvote: 6
- 本文: The expected format for {tug₂} or {tug2} is actually {túg}

For background, in ASCII ATF (CDLI) they don't use diacritics for ú = u2, and ù = u3, and so on. Further, in Oracc these numbers become subscripts: ú = u₂, etc. That second comment was intended to indicate that for the readings with 2 or 3 this dataset used diacritics instead of numbers or subscripted numbers (i.e. á à é è í ì ú ù; NOT a2, a3, etc.; NOT a₂, etc.). However, sign values with 4, 5, 6, …, 10, 12, 13, etc. are found in the dataset (e.g., DU10). So aside from sign values with these readings á à é è í ì ú ù, this dataset uses integer numbers, not subscripted numbers.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3385744
- 投稿者: @nlztrk
- 投稿日時: 2026-01-04
- upvote: 4
- 本文: {túg} or {TÚG}? there is no lowercased {túg} in any guide you've shared. Please just give a reproducible normalization script or a very clear and strict conversion table. Most of your statements contradict each other.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3387872
- 投稿者: @deeppast
- 投稿日時: 2026-01-08
- upvote: 1
- 本文: TÚG, without brackets (in the test data), but {tug2} in the CDLI data and {tug₂} in the Oracc data, in case you choose to use those.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3387880
- 投稿者: @nlztrk
- 投稿日時: 2026-01-08
- upvote: 5
- 本文: In the overview tab you are saying:

{tug₂} = (TÚG) preceding textiles and other woven objects

TÚG is being used with parentheses there but you are now saying without brackets. I think you need to clarify the exact form for that list. What should we expect for these in the test set:

{d} = dingir ‘god, deity’ — d preceding non-human divine actors
{mul} = ‘stars’ — MUL preceding astronomical bodies and constellations
{ki} = ‘earth’ — KI following a geographical place name or location
{lu₂} = LÚ preceding people and professions
{e₂} = {É} preceding buildings and institutions, such as temples and palaces
{uru} = (URU) preceding names of settlements, such as villages, towns and cities
{kur} = (KUR) preceding lands and territories as well as mountains
{mi} = munus (f) preceding feminine personal names
{m} = (1 or m) preceding masculine personal names
{geš} / {ĝeš) = (GIŠ) preceding trees and things made of wood
{tug₂} = (TÚG) preceding textiles and other woven objects
{dub} = (DUB) preceding clay tablets, and by extension, documents and legal records
{id₂} = (ÍD) (a ligature of A and ENGUR, transliterated: A.ENGUR) preceding names of canals or rivers or when written on its own referring to the divine river
{mušen} = (MUŠEN) preceding birds
{na₄} = (na4) preceding stone
{kuš} = (kuš) preceding (animal) skin, fleece, hides
{u₂} = (Ú) preceding plants

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3383782
- 投稿者: @ulasdesouza
- 投稿日時: 2025-12-31
- upvote: 0
- 本文: do not convert diacritics to ASCII (information loss!) do not remove subscripts (semantic meaning!) Evaluation data contains diacritics - be compatible with this

am i right?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3383787
- 投稿者: @deeppast
- 投稿日時: 2025-12-31
- upvote: 4
- 本文: Close, but let me be clear:

(1) with the exception of ḫ, the test data has diacritics (š ṣ ṭ ā á à ī í ì ū ú ù - and upper case versions). If you're obtaining data from CDLI or ORACC, you will need to convert their formatted transliterations to this diacritic style (conversions are listed in the overview) — note ā ī ū are in translations, not transliteration text.
(2) there are no subscripted numbers in the test data, so expect A-šùr-DU10 for example.
(3) keep diacritics for transliterations, but normalize them for translations of named entities, for example: A-šùr-DU10 (transliteration) --> Aššur-ṭāb (translation)

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3384017
- 投稿者: @mpware
- 投稿日時: 2025-12-31
- upvote: 4
- 本文: @deeppast

(2) there are no subscripted numbers in the test data, so expect A-šùr-DU10 for example.

You said something a bit different in another post:

Subscript digits are converted to normal digits, except for 2 and 3, which are represented by diacritic marks over the vowels (see overview for more details)

https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664518#3382901

Do I miss something?
Answer to myself: Now we know that first assertion it True and second is False.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665209#3384721
- 投稿者: @deeppast
- 投稿日時: 2025-12-31
- upvote: 4
- 本文: Yes, right, the ack of specificity in that second statement is problematic. For background, in ASCII ATF (CDLI) they don't use diacritics for ú = u2, and ù = u3, and so on. Further, in Oracc these numbers become subscripts: ú = u₂, etc. That second comment was intended to indicate that for the readings with 2 or 3 this dataset used diacritics instead of numbers or subscripted numbers (i.e. á à é è í ì ú ù; NOT a2, a3, etc.; NOT a₂, etc.). However, sign values with 4, 5, 6, …, 10, 12, 13, etc. are found in the dataset (e.g., DU10). So aside from sign values with these readings á à é è í ì ú ù, this dataset uses integer numbers, not subscripted numbers.

---

## Entry: `664948`
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948
- タイトル: The translation column of the final test predictions into the corresponding <gap> and <big_gap> tags
- 投稿者: @qifeihhh666
- 投稿日時: 2025-12-29
- upvote: 50
- 本文: Note: The dataset has been updated. The <big_gap> tag and certain symbols are no longer included. For details, please refer to the official update announcement and the latest dataset released by the organizers.

2025.12.29: I trained the model by replacing all instances of … [x], x, etc. in the transliteration column of train.csv with <gap> and <big_gap>, then made predictions on test.csv. Meanwhile, I replaced all … in the prediction results with <big_gap>and all x with <gap>.

My LB score reached 30.3, and I have released the training code, the converted datasets as well as the submission code. :)

I’ll share my scoring progress and implementation details here in the next steps, and hope this helps you all.

LB	size	submit time	epoch	Training Loss	Validation Loss	Chrf	progress
31.3	725B	-	10	0.290900	0.418788	5.175934	revised the <gap> <big_gap>
31.0	569B	19min	10	0.304600	0.421686	5.082081	revised the <gap> <big_gap>, determinatives, fraction such as ¼, curly braces {} and delete parentheses ().
31.5	762B	21min	10	0.282200	0.389588	5.320788	Shortened and aligned the 14 sentences with length exceeding 512, resulting in a total of 1595 pieces of data; meanwhile, revised the <gap> <big_gap>, determinatives, fraction such as ¼, curly braces {} ,and delete slash /, parentheses ().
31.8	749B	-	10	0.297200	0.400207	5.364566	Shortened and aligned the 14 sentences with length exceeding 512, resulting in a total of 1595 pieces of data; meanwhile, revised the <gap> <big_gap>
32.3	695B	19min	10	0.296600	0.385465	5.364575	Shortened and aligned the 16 sentences with length exceeding 512, resulting in a total of 1604 pieces of data; meanwhile, revised the <gap> <big_gap>,determinatives, fraction such as ¼, curly braces {} ,keep ! ? (),and delete slash / ,fem. plur. sing. pl.
The Second Stage

I'm back—but actually, I never left. 32.8 This result is definitely not up to my expectations, lol, but the task isn’t finished yet, so there should still be room for improvement.

LB	size	submit time	epoch	Training Loss	Validation Loss	Chrf	progress
32.8	797B	17min	10	0.277100	0.370077	6.596245	MAX_LENGTH=385,revised the <gap> <big_gap>,Ensure that the <gap> on both sides exist simultaneously or are absent simultaneously, All subscript numbers uppercase, keep determinatives(Ḫ,ḫ), delete ! ? () " ; — - – < > ⌈ [ ] + ʾ / ,fem. plur. sing. pl. , total of 1703 pieces of data
33.0	699B	17min	10	0.276200	0.353537	5.957525	MAX_LENGTH=475,revised the <gap> <big_gap>,Ensure that the <gap> on both sides exist simultaneously or are absent simultaneously, All subscript numbers uppercase, keep determinatives(Ḫ,ḫ), delete ! ? () " ; — - – < > ⌈ [ ] + ʾ / ,fem. plur. sing. pl. , total of 1703 pieces of data
33.3	820B	18min	10	0.284400	0.351412	5.638265	MAX_LENGTH=512,revised the <gap> <big_gap>,Ensure that the <gap> on both sides exist simultaneously or are absent simultaneously, All subscript numbers uppercase, keep determinatives(Ḫ,ḫ), delete ! ? () " ; — - – < > ⌈ [ ] + ʾ / ,fem. plur. sing. pl. , total of 1703 pieces of data
At present, I have basically aligned the 94 filtered documents with lengths exceeding 512 characters, and revised nearly 100 documents with abnormal length ratios. As for why MAX_LENGTH is set to 385, the reason is CUDA out of memory.

Note:After the new update, <big_gap> has been permanently removed.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3406412
- 投稿者: @gauravbrills
- 投稿日時: 2026-2-16
- upvote: 1
- 本文: Yes, right, the ack of specificity in that second statement is problematic. For background, in ASCII ATF (CDLI) they don't use diacritics for ú = u2, and ù = u3, and so on. Further, in Oracc these numbers become subscripts: ú = u₂, etc. That second comment was intended to indicate that for the readings with 2 or 3 this dataset used diacritics instead of numbers or subscripted numbers (i.e. á à é è í ì ú ù; NOT a2, a3, etc.; NOT a₂, etc.). However, sign values with 4, 5, 6, …, 10, 12, 13, etc. are found in the dataset (e.g., DU10). So aside from sign values with these readings á à é è í ì ú ù, this dataset uses integer numbers, not subscripted numbers.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3406455
- 投稿者: @gqifeihhh666
- 投稿日時: 2026-2-16
- upvote: 1
- 本文: It actually doesn’t have much to do with the batch size. The main issue is that the data has a lot of truncation and inconsistency, which leads to large score fluctuations. So standardizing the data well is the key to this competition.good luck.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3406472
- 投稿者: @gauravbrills
- 投稿日時: 2026-2-16
- upvote: 1
- 本文: Thanks ya but run same seed diff batch size also seeing this but ya think you are right .. larger models also on same pipes give different results was stranger

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3406319
- 投稿者: @yshunt
- 投稿日時: 2026-2-15
- upvote: 1
- 本文: Thank you for sharing. This discussion is very helpful for me. I'm a beginner, so please excuse my question, but why does your training strategy table only show chrF? In my own training, the BLEU score is extremely low, like 0.00… Since the final evaluation metric is the geometric mean of BLEU and chrF, is this really okay?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3406452
- 投稿者: @qifeihhh666
- 投稿日時: 2026-2-15
- upvote: 0
- 本文: It doesn’t really matter much. Although this can’t directly reflect the leaderboard score, it still gives us a general idea of how the model is performing, and I think that’s sufficient for now.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3406319
- 投稿者: @yshunt
- 投稿日時: 2026-2-15
- upvote: 1
- 本文: Thank you for your response. I have another question. Looking at public inference notebooks, I noticed that many people are using almost the same training models. Why is this the case? Also, is it considered a best practice to take these publicly available models and fine-tune them as a starting point (pre-trained model) on a new dataset that has been pre-processed with tags like ?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3384498
- 投稿者: @saouza007
- 投稿日時: 2026-01-01
- upvote: 1
- 本文: i can ask u? what u use method for solve problems hallucination and repetition word???

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3384503
- 投稿者: @qifeihhh666
- 投稿日時: 2026-01-01
- upvote: 0
- 本文: I haven't reached the stage of solving this problem yet. The maximum token capacity of my current code model is 512, and hallucinations tend to come with repeated words when the text length increases. I think this issue can be addressed through the following two approaches:

Increase the token capacity, which however requires greater computing power.
Truncate long sentences into smaller ones by semantic meaning for training, but it will take some time to do.
good luck

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3384601
- 投稿者: @jackvd
- 投稿日時: 2026-01-02
- upvote: 1
- 本文: How the heck are you aligning sentences to actually improve your score? I’ve spent hours going through the sentence alignment file to create sentences and manually verified everything and all it did was lower my score.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3384626
- 投稿者: @qifeihhh666
- 投稿日時: 2026-01-02
- upvote: 2
- 本文: 
That's a great question, and I'll break down the answer into three points:

First, the sentences I’m currently processing: sentences where both the transliteration and translation columns exceed 512 characters, and their oare_id exists in Sentences_Oare_FirstWord_LinNum.csv (the critical basis for my segmentation). So far, I’ve filtered out only 94 sentences that meet the above criteria.

How I process these sentences: I perform truncation using the sentence start words and English translations from Sentences_Oare_FirstWord_LinNum.csv, while striving to preserve semantic integrity and avoiding truncation of single isolated sentences. Minor punctuation adjustments may be made during truncation—for example, removing or reinserting the closing quotation mark if there is no matching " after said:". Additionally, translations in Sentences_Oare_FirstWord_LinNum.csv may have slight discrepancies with those in train.csv, and the two datasets are complementary to each other. Ultimately, the only requirement is that the truncated length does not exceed 512 characters, as I aim to avoid losing semantic information of the entire passage.

On score improvement: I remain somewhat skeptical here. Although truncating sentences alone boosted my score by 0.5, my random seed is still set to 42. As the total number of rows in train.csv increases, the split results for the validation and training sets will change. This may cause the model to train on and learn new content, which could be the actual reason for the score increase.

Conclusion: I will continue aligning partial sentences and monitor the LB score. A significant LB score improvement will confirm the effectiveness of this approach. In fact, with the current token limit of 512, a large volume of data is undoubtedly omitted. Sentence alignment should yield certain benefits, but it requires meticulous execution (there is no definitive rule for this task).Hope this helps you.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3384086
- 投稿者: @qianyuu
- 投稿日時: 2025-12-31
- upvote: 1
- 本文: "Shortened and aligned the 14 sentences with length exceeding 512, resulting in a total of 1595 pieces of data"

How is this implemented?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3384090
- 投稿者: @qifeihhh666
- 投稿日時: 2025-12-31
- upvote: 2
- 本文: 
I implemented this manually. Although the organizer released the file Sentences_Oare_FirstWord_LinNum.csv, I noticed that the truncation logic does not seem to include numeric characters, which prevented me from truncating sentences accurately. (It is also possible that I misunderstood the usage instructions.) Therefore, I manually truncated the translation and transliteration columns with content length exceeding 512 to achieve sentence-level alignment. This process also helped me gain a better understanding of Akkadian.

The current 0.5-point improvement has boosted my confidence significantly. My next task will likely be to further optimize sentence alignment. Given my lack of computing resources and reliance on Kaggle's GPU, a 512 token limit is currently the optimal choice.:)

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3388612
- 投稿者: @qianyuu
- 投稿日時: 2026-01-09
- upvote: 0
- 本文:Your 33.0 LB is really great. I believe 33.0 is definitely not your limit. Currently, I haven't made any significant breakthroughs in sentence alignment. I'll study it some more.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3388614
- 投稿者: @qifeihhh666
- 投稿日時: 2026-01-09
- upvote: 0
- 本文:Aligning documents with a length of over 512 characters should only serve to expand vocabulary. For score improvement, it is still necessary to truncate the corresponding erroneous sentences in the transliteration and translation columns. These errors can be easily identified using the ratio metric. Thank you for your response.:)

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3388632
- 投稿者: @qianyuu
- 投稿日時: 2026-01-09
- upvote: 2
- 本文:Yes, I found that many character lengths didn't match. I thought it was because my character segmentation wasn't good enough, haha, turns out that just deleting those characters solved the problem.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3388632
- 投稿者: @angantyr
- 投稿日時: 2026-01-09
- upvote: 2
- 本文:Some transliterations or translations are truncated and don't match. I made a list of the transliteration OARE IDs along with a short analysis based on the texts covering train.csv and Sentences_Oare_FirstWord_LinNum.csv.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3388637
- 投稿者: @qifeihhh666
- 投稿日時: 2026-01-09
- upvote: 0
- 本文:Yes, direct deletion is the fastest method. However, attempting truncation allows us to retain a great deal of semantic information.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3387147
- 投稿者: @saouza007
- 投稿日時: 2026-01-06
- upvote: 0
- 本文:i think mayby domain in test very difference train set and format text diff. i trained model by sentence level. i sentence alignment 8000 sentence can more gm in val set so high (train 80% val 20%) but submit get score 30

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3387149
- 投稿者: @saouza007
- 投稿日時: 2026-01-06
- upvote: 0
- 本文:i think preprocess and postprocess more important than model

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3387157
- 投稿者: @saouza007
- 投稿日時: 2026-01-06
- upvote: 0
- 本文:i think preprocess and postprocess more important than model

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3387182
- 投稿者: @qianyuu
- 投稿日時: 2026-01-06
- upvote: 4
- 本文:Haha, this competition has become a challenge of understanding and processing data, and has little to do with the model.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3406413
- 投稿者: @gauravbrills
- 投稿日時: 2026-02-16
- upvote: 0
- 本文:Ya 💯 Seems s as of now

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3383333
- 投稿者: @einherjer
- 投稿日時: 2025-12-30
- upvote: 0
- 本文:@qifeihhh666 what is the rationale of replacing all instances of … [x], x, etc. in the transliteration column only and not in the translation column as well?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3383395
- 投稿者: @qifeihhh666
- 投稿日時: 2025-12-30
- upvote: 0
- 本文:The translation column needs to be converted into<gap><big_gap>

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3397014
- 投稿者: @einherjer
- 投稿日時: 2025-12-30
- upvote: 1
- 本文:@qifeihhh666 Yes, I get that the translation needs to be converted to <gap> and <big_gap>. However, if I understood correctly, you are predicting translations with x, [x], .. (i.e. without <gap> and <big_gap>) and then as a post-processing step, you are converting the predictions with x, [x], … to <gap> and <big_gap> (am I right?).

I wonder why one would do this as a post-processing step. Why not just clean the transliteration and translation before training in the first place? Is there some logic behind that?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3397265
- 投稿者: @qifeihhh666
- 投稿日時: 2026-01-27
- upvote: 0
- 本文:That was the case at the very beginning, but it’s totally different now, ever since the score of 31.3.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3383317
- 投稿者: @aaronbornstein
- 投稿日時: 2025-12-30
- upvote: 0
- 本文:It's strange i tried this and dropped to from 28.3 to 27.6 I wonder what I did wrong

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3383396
- 投稿者: @qifeihhh666
- 投稿日時: 2025-12-30
- upvote: 0
- 本文:The translation column needs to be converted into <gap><big_gap>

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3383491
- 投稿者: @aaronbornstein
- 投稿日時: 2025-12-30
- upvote: 1
- 本文:Strange I did this though I did it for both the translation and transliteration.

Then based on your comment in another notebook i did only the transliteration.

Neither work for me I really wonder what i'm missing.

def replace_gaps(text):
    if pd.isna(text): 
        return text

    text = re.sub(r'\[\.{3}(?:\s+\.{3})+\]\s+\.{3}(?:\s+\.{3})+', '<big_gap>', text)
    text = re.sub(r'\[\.{3}(?:\s+\.{3})+\]', '<big_gap>', text)
    text = re.sub(r'\.{3}(?:\s+\.{3})+', '<big_gap>', text)

    text = re.sub(r'\[x\]', '<gap>', text)
    text = re.sub(r' x ', ' <gap> ', text)
    text = re.sub(r'\[…\]', '<big_gap>', text)
    text = re.sub(r'\[\.\.\.\]', '<big_gap>', text)
    text = re.sub(r'…', '<big_gap>', text)
    text = re.sub(r'\.\.\.', '<big_gap>', text)

    return text

 train_expanded = simple_sentence_aligner(train_df)

 train_expanded['transliteration'] = train_expanded['transliteration'].apply(lambda x:replace_gaps(x))
#train_expanded['translation'] = train_expanded['translation'].apply(lambda x:replace_gaps(x))

 train_expanded.head()

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3383494
- 投稿者: @qifeihhh666
- 投稿日時: 2025-12-30
- upvote: 0
- 本文:You're doing the right thing. When I used this code on Kaggle, I found the results inconsistent with those processed on my local machine. I first completed the processing locally and double-checked all formatting details like x, xx… […], and everything was perfect. So I recommend processing on your local machine as it’s easier to verify. I’ll publish the 31.3 train.csv dataset shortly, and you can compare the differences with your processed version.good luck

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3383496
- 投稿者: @qifeihhh666
- 投稿日時: 2025-12-30
- upvote: 2
- 本文:This is the dataset I used for training.train data

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3383501
- 投稿者: @qifeihhh666
- 投稿日時: 2025-12-30
- upvote: 2
- 本文:[3510/3510 1:22:44, Epoch 10/10]

Epoch	Training Loss	Validation Loss	Chrf
1	0.786000	0.640140	4.082023
2	0.616300	0.551597	4.468811
3	0.536500	0.497410	4.932824
4	0.456200	0.455575	5.027439
5	0.397200	0.426659	5.080146
6	0.353600	0.415668	5.103130
7	0.332700	0.410799	5.150165
8	0.312800	0.409823	5.140119
9	0.294000	0.410092	5.141407
10	0.287300	0.410267	5.161873

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3383523
- 投稿者: @aaronbornstein
- 投稿日時: 2025-12-30
- upvote: 3
- 本文:I appreciate all the support and advice here i'll give that a try now by the way one thing i noticed in your training notebook. I'm not sure the simple_sentence_aligner is doing anything I get the same number of rows before and after running it after i get this gap trick to work I plan to pivot to alignment.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3383530
- 投稿者: @qifeihhh666
- 投稿日時: 2025-12-30
- upvote: 4
- 本文:Yes, because the final test.csv is in a sentence-aligned format, rather than the document-level alignment used in the current train.csv. Meanwhile, the maximum input length of the model being trained is 512, which results in truncation of a large amount of training data. Converting document-level data into sentence-level alignment is a crucial method to boost performance in subsequent experiments.

This is also one of the sources for supplementing data.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3383781
- 投稿者: @aaronbornstein
- 投稿日時: 2025-12-31
- upvote: 2
- 本文:Good news i trained on the set you provided and it worked I'm now at 31.1. I'm transitioning to work on the sentence alignment challenge I have some ideas of how to do this if I am able to make progress I will share with you the segmented sentence pairs.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3383786
- 投稿者: @qifeihhh666
- 投稿日時: 2025-12-31
- upvote: 0
- 本文:Congratulations! Yes, At the begining I try sentence alignment, but the results were unsatisfactory (probably because the format hasn't been properly adjusted). So I've been following up on the discussion to fix the formatting issues continuously.Through these days' efforts, tomorrow I'll retry the sentence-aligned dataset with the corrected format conversion. Good luck!

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3383960
- 投稿者: @qianyuu
- 投稿日時: 2025-12-31
- upvote: 1
- 本文:I'm doing the same job as you.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3384038
- 投稿者: @qifeihhh666
- 投稿日時: 2025-12-31
- upvote: 0
- 本文:Something amazing—I did maybe exactly these things and got an LB score of 31.5.lol

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3384309
- 投稿者: @qifeihhh666
- 投稿日時: 2026-01-01
- upvote: 1
- 本文:I digged into the issue @einherjer posted earlier: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664177#3383842

There's a portion of texts where (2 broken lines) string is clearly counted as x x x instead of .... I'm guessing that if the problem is present in Sentences_Oare_FirstWord_LinNum.csv and in the hidden test then taking that into account could boost the score a bit further (at least until the issue is resolved :D).

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3384309
- 投稿者: @ilanwang
- 投稿日時: 2026-01-01
- upvote: 0
- 本文:Can I ask you how to deal with the oare_id ?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3384597
- 投稿者: @angantyr
- 投稿日時: 2026-01-02
- upvote: 0
- 本文:@ilanwang What do you mean by "dealing with the oare_id"?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3384636
- 投稿者: @qifeihhh666
- 投稿日時: 2026-01-02
- upvote: 1
- 本文:I convert any broken lines and large break to <big_gap>.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3385432
- 投稿者: @angantyr
- 投稿日時: 2026-01-03
- upvote: 4
- 本文:The oare_id from the train.csv matches the text_uuid from the Sentences_Oare_FirstWord_LinNum.csv.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664948#3385436
- 投稿者: @qifeihhh666
- 投稿日時: 2026-01-03
- upvote: 2
- 本文:The oare_id from the train.csv matches the text_uuid from the Sentences_Oare_FirstWord_LinNum.csv.

---

## Entry: `664795`
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664795
- タイトル: How To Handle These Examples
- 投稿者: @jackvd
- 投稿日時: 2025-12-28
- upvote: 22
- 本文: After working on cleaning the text for modelling, I've found some transliteration/translation pairs that seem weird and was hoping to get some clarification on if this stuff will be seen in the hidden test set or if it has been cleaned in a certain way that we should replicate.

I'm bolding the text I'm questioning in the following examples. These examples were not cleaned.

Example

Transliteration: KIŠIB šu-(d)EN.LÍL DUMU šu-ku-bi-im KIŠIB ṣí-lu-lu DUMU ú-ku i-nu-mì i-dí-a-bu-um a-wa-sú iq-bi-ú 10 ma-na KÙ.BABBAR a-na ša-lim-a-šùr i-dí-in um-ma šu-ut-ma i-ṣí-ba-at KÙ-pì-a li-il₅-qé

Translation: Seal of Šu-Illil son of Šu-Kūbum, seal of Ṣilūlu son of Uku. When Iddin-abum spoke his will, he gave 10 minas ofדsilver to Šalim-Aššur. He said: He may take it from the interest on my silver.""

Example

Transliteration: um-ma šu-ku-tum-ma a-na IŠTAR-lá-ma-sí ù ni-ta-aḫ-šu-šar qí-bi₄-ma mì-šu ša ta-áš-pu-ra-ni-ni um-ma a-tí-na-ma É-tum a-na lá be-tim i-tù-ar a-pu-tum a-na en-um-a-šùr i-xx-ni-ma e ší-na ga x ša lá ta-ḫa-dì-ri a-na IŠTAR-lá-ma-sí qí-bi₄-ma šu-ma a-ḫa-tí a-ta li-ba-am dì-ni-ší-im lá ta-ḫa-da-ar a-na ni-ta-aḫ-šu-šar qí-bi₄-ma TÚG-pì-ri-kà-ni ša e-zi-bu na-pí-ší-šu-nu ù ṭup-pu-ú lu ša-ṣú-ru pì-ri-kà-nu ša ma-tí ù tí-bu-lá ma-a-x iš-ta-ú-mu-ni a-dí en-um-a-šùr i-lá-kà-ni a ma-ma-an lá tù-šé-ri x GÍN KÙ.BABBAR (d)UTU-tap-pá-i ub-lá-ki-im 1 GÍN KÙ.GI ù x GÍN KÙ.BABBAR i-ku-pì-a ub-lá-ki-im

Translation: From Šukkutum to Ištar-lamassī and Nitahšušar: Why is that you (fem. plur.) have written me, saying: The house is no longer a house." Urgent, to Ennam-Aššur … Do not fear!. To Ištar-lamassī: If you are truly my sister, then encourage her. Do not fear. To Nitahšušar: Air the -textiles that I left. Also, the tablets should be guarded. The which Mati? and Tibula … have bought do not release (them) to anyone before Ennam-Aššur arrives. Šamaš-tappā'ī brought you x shekels of silver. Ikūn-pīya brought you 1 shekel of gold and x shekels of silver. "

Example

Transliteration: 30 ma-na KÙ.BABBAR ni-is-ḫa-sú DIRI ša-du-a-sú ša-bu ku-nu-ki-a a-na um-mì-a-ni-a ša ki-ma i-a-tí ù ḫi-na-a šu-ku-bu-um ú-bi₄-il₅ IGI a-mur-(d)UTU DUMU mì-šar-ra-bí IGI a-mur-(d)UTU DUMU ḫa-ri-im-tim 2 ma-na KÙ.BABBAR i-a-am 1 ma-na KÙ.BABBAR ša ḫi-na-a a pá-ni ILLAT-tim 1.5 ma-na KÙ.BABBAR ša um-mì-iš-ḫa-ra 15 GÍN KÙ.KI ša lá-ma-sí-tim ú a-šur-iš-tí-kál ŠÀ.BA 0.5 ma-na 5 GÍN ša lá-ma-sí-tim 0.33333 ma-na 5 GÍN KÙ.BABBAR ša ik-ri-bi-a mì-ma a-nim ni-is-ḫa-sú DIRI ša-du-a-sú ša-bu ku-nu-ki-a a ša ki-ma i-a-tí šu-ku-bu-um ú-bi₄-il₅ IGI lá-qé-ep DUMU i-zi-za-am-ì-lí IGI a-šur-na-da

Translation: 30 minas of silver, its excise [added], his transport fee paid, under my seals, Šu-Kūbum brought to my investors and my representatives and to hinnāya. (Entrusted to him) in the presence of Amur-Šamaš, son of Mīšar-rabi, of Amur-Šamaš, son of harimtum. 2 minas of silver belonging to me; 1 mina of silver belonging to hinnāya, (sent) to meet the caravan; 1.5 mina of silver of Ummī-Išhara; 15 shekels of gold of Lamassutum and Aššuriš-tikal, thereof 35 shekels of silver of Lamassutum (and?) 25 shekels of [silver] being [my?] temple funds - all this, its import tax [added], his transport fee [paid], under my seals, Šu-Kūbum brought to my representatives. In the presence of Lā-qēp, son of Izzizam-ilī, of Aššur-nādā.

Example (it's the fractions)

Transliteration: 2 né-pí-šu 15 ma-na.TA ú iš-tí-in né-pí-šu-um 10 ma-na ni-is-ḫa-sú DIRI ša-du-a-sú ša-bu-ú ŠU.NÍGIN 42.33333 ma-na KÙ.BABBAR ṣa-ru-pá-am ku-nu-ki-a a-na a-lu-wa ù e-ni-ša-ri-im áp-qí-id-ma a-na a-lim(ki) a ma-lá tí-ir-tí-šu a-ṣé-er ša-lim-a-šùr ú-šé-bi-il₅-šu-nu a-ḫa-ma 13.33333 ma-na URUDU SIG₅ a-na ga-am-ri-šu-nu ù 5 GÍN KÙ.BABBAR a-na ú-ku-ul-tí-šu-nu a-dí-in IGI ili₅-ba-ni DUMU ba-ší-lam IGI a-ḫu-qar DUMU zu-ur-zu-ur IGI tù-ra-am-ì-lí DUMU e-dí-na-a-šùr a-ḫa-ma 10.33333 ma-na 3.5 GÍN KÙ.BABBAR ṣa-ru-pá-am x tum ni x x x 0.5 GÍN ṣí-ba-tim ša i-na ṣé-ri-a il₅-qé-ú-ni a-na ḫu-bu-li-šu a-na kà-ri-im wa-aḫ-šu-ša-na áš-qúl ṣí-ba-at KÙ.GI ša ší-ip-kà-at a-šur-bé-el-a-wa-tim i-ší-tù

Translation: 2 packages of 15 minas each plus a single package of 10 minas, its import duty added, its transport tariff paid - in all 42 ⅓ minas of refined silver under my seal, I entrusted to Aluwa and Enišārum, and I sent them to the City to Šalim-Aššur in accordance with his orders. Furthermore, I paid 13 ⅓ minas of good copper for their expenses and 5 shekels of silver for their food. Witnessed by Ilī-bāni son of Baši-ilum, by Ahu-qar son of Zurzur, by Tūram-ilī son of Eddin-Aššur. Furthermore, 10 ⅓ minas 3 ½ shekels of refined silver …, … ½, shekel interest that they took on my account, I paid for his debt to the Wahšušana colony. The interest on the gold that remained of Aššur-bēl-awātim's investment.

Example

Transliteration: 4 GÍN a-na ší-iṭ-ri-im ša pu-ki-im 1.3333300000000001 GÍN a-na e-re-qí-im qá-nu-e áš-qúl 1.66666 GÍN a sú-ba-ri-im áš-qúl 0.33333 ma-na KÙ.BABBAR a-na a-bar-ni-im áš-qúl 0.16666 GÍN a-na um-ṣí-im 0.25 GÍN a šu-um-ki xxx x na-ru-uq GIG xxxx […] xx GÍN a-na … ḫa-áš-lá-tim xxx a-wa-ar-nu-a-lim 0.66666 GÍN a-na e-ṣé áš-qúl 0.66666 GÍN a pá-e ú-ša-qí-il₅ 1 bi-il₅-té-en 0.5 GÍN áš-qúl 0.25 GÍN a-na na-pá-ḫi-im 95 ki-ra-tim a-na x 0.25 GÍN.TA ù 7.5 ŠE.TA 0.5 GÍN a-na xxxx 0.16666 GÍN a-na xxxx a-na xxxx

Translation: I paid 4 shekels for a scarf of -weave, 1.3333 shekel for a wagonload of reed; I paid 1.6666 shekel for ; I paid 0.3333 mina of silver for an Abarnian textile, 1 / 6 shekel for a piece of dried meat, 1 / 4 shekel for onions, [x shekels for] [x] bags of wheat… …;[I paid … … … … … …] shek[els for] ?, [… … … …] for a … … … …; I paid 0.6666 shekel for firewood; 0.6666 shekels I paid for chaff, for a double load I paid 0.5 shekel; 1 / 4 shekel for the blacksmith. I supplied 95 drinks to .. at 52.5 grains (of silver) each, 0.5 shekel for … … … 1 / 6 shekel for … for … … … … … … …

Example

Transliteration: 1.25 GÍN KÙ.BABBAR i-na li-bi₄ lu-lu

Translation: 1 1 / 4 shekel of silver is owed by Lulu.

Example

Transliteration: […] x šu-a-x-… um-ma … … … … en-nam-a-šur … bi-ma … tám-kà-ri-im … ḫu-a … … KÙ.BABBAR IGI e-ni-iš-ta-ru-um … ni AN.NA-ki … ší-a-ni … … ma x ku-un-kà-ma a-na e-ni-iš-ta-ri-im dí-na-ma iš-tí ba-tí-qí-im ša a-na pá-ni ILLAT-tim i-lá-kà-ni lá i-sà-ḫu-ur ṭù-ur-da-ni-šu a-na-kam we-da-ku a-ḫu-a a-tù-nu e-ni-iš-ta-ra-am lá i-sà-ḫu-ur ṭù-ur-da-ni-šu mì-li-ik lu-qú-tim x x bi-ri-im mì-il₅-kà sà-ḫe-er-tám ša 5 GÍN KÙ.BABBAR x x nim a-na ší-im … … … … mì-li-ik-šu-nu mì-il₅-kà

Translation: [Obverse too broken for translation]

Example

Transliteration: lu-lu en-nam-a-šur ù a-bu-um-ša-lim ša ki-ma a-šùr-DU₁₀ DUMU e-lá-ma a-na a-šur-DU₁₀ DUMU a-lá-ḫi-im iṣ-bu-tù-ni-a-tí-ma um-ma šu-nu-ma ší-im 21 GÚ 9 ma-na URUDU ma-sí-im ša a-šur-DU₁₀ DUMU e-lá-ma ša i-na É-tí-kà i-ni-id-ú a-na ší-mì-im ta-dí-šu um-ma a-šur-DU₁₀-ma a-dí-šu-ma 17.83333 ma-na 2 GÍN KÙ.BABBAR ší-im-šu na-áš-a-ku eq-lam a šu-mì a-šur-DU₁₀ DUMU e-lá-ma KÙ.BABBAR e-tí-iq a-na a-wa-tim a-ni-a-tim kà-ru-um bu-ru-uš-ḫa-tum i-dí-ni-a-tí-ma ší-bu-tí-ni IGI GÍR ša a-šur ni-dí-in IGI i-ku-pì-a IGI ú-ṣú-ur-ša-a-šur

Translation: Lullu,

There's a lot more, like transliterations with lots of gaps but no '…' in the translation or the opposite scenario. I may share a notebook that contains more examples if there's any interest. Any help would be appreciated.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664795#3382916
- 投稿者: @deeppast
- 投稿日時: 2025-12-25
- upvote: 5
- 本文:Thank you for your comment Jack! These errors and oversights in the data stem from the nature of the databases we used to gather enough texts for this challenge. Many of these databases are worked on by students with little oversight. That goes for the CDLI database as well. As mentioned elsewhere, English translations are rarely paired with transliterations in these databases. So what we have provided is the first attempt for Old Assyrian, but by no means an error-free dataset.

Regarding the specifics you mention:

Example 1. The parentheses used as determinatives (e.g. (d)UTU) should be replaced with curly brackets (e.g. {d}UTU). This came from a different dataset which we attempted to harmonize with the rest, but this was one difference which we missed.

Example 2. The first example includes scribal insertions in parentheses (fem. plur.). We have made sure to remove these from the hidden evaluation translations. So it would be best to remove the modern scribal insertions when you encounter them.

Example 3. For instances of bracketed insertions like, "its excise [added]", it is sufficient to simply remove the brackets, since the specific phraseology is what we're hoping to train in a MT model, rather than a strict adherence to which words in the text is broken for this challenge.

Example 4 & 6. The fractions are retained in the hidden test dataset. There you will find 2 ½ minas = 2 ½ ma-na, and NOT 2.5 ma-na. I realize this is a problem and I'm working on providing a supplemental dataset of texts with integer (and fraction) numbers, rather than floats. I also made sure to use the same single character fractions for ⅓ ⅔ etc. But there is a larger issue at hand in aligning these numerical values, and that is sometimes the translators do some math to convert the fractions to whole numbers in shekels, instead of a literal translation of minas and shekels (e.g. "3 ⅔ ma-na ⅓ GÍN KÙ.B."--> "23 minas 40 ⅓ shekels of silver"). The bad news is that this is going to pose a challenge for ML in working with the number systems in use at that time. The good news is this will likely negatively impact everyone's score equally.

Example 5. This is a very broken (and messy text). The aspect you highlighted has an additional closed square bracket due to one of the ellipses having a closed bracket I believe (i.e. [I paid … … … … … …] shek[els for] ?). This can be remedied by using the substitutions described in the data, i.e. … = , and remove the square brackets (retaining the English translations).

Example 7 & 8. Texts like this should probably have been removed, an oversight on my part. I look forward to working together to get the best "gold standard" ML dataset for these texts!

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664795#3383162
- 投稿者: @jackvd
- 投稿日時: 2025-12-29
- upvote: 0
- 本文:Apologies, but here are some more little snippets that I'd like to confirm should be removed without concern: "ofדsilver","myself()","< lil >", "< of firewood >"

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664795#3383194
- 投稿者: @deeppast
- 投稿日時: 2025-12-30
- upvote: 1
- 本文:yes, I have no idea how a Hebrew dalet ד got in there!

"ofדsilver" --> of silver "myself()" --> myself "< lil >" --> -lil — I'm assuming it is the end of a name like En-lil : Note that modern scribes / editors use these pointy brackets to insert signs which they think are missing in the text (i.e. ancient scribal omission). "< of firewood >" --> of firewood

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664795#3383335
- 投稿者: @mpware
- 投稿日時: 2025-12-30
- upvote: 1
- 本文:For example:

Aššur-ṣulūlī took 5 11 / 12 shekels of silver.
for wheat, we added; 7/12 shekel for 2 jars of beer we paid; 1 shekel silver we paid for a sheep

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664795#3383673
- 投稿者: @deeppast
- 投稿日時: 2025-12-31
- upvote: 5
- 本文:Let me put it this way, there are no instances of '/' in either the transliterations or translations of the public or private evaluation data.

---

## Entry: `663357`
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/663357
- タイトル: Other Public Data
- 投稿者: @manwithacat
- 投稿日時: 2025-12-18
- upvote: 27
- 本文: This might be useful:

https://www.kaggle.com/datasets/manwithacat/oracc-akkadian-english-parallel-corpus

I’m sharing ORACC Akkadian–English Parallel Corpus with the community as a clean, ready-to-use set of aligned Akkadian transliteration → English pairs extracted from ORACC. The material here is drawn from major ORACC projects focused on royal inscriptions and state/administrative archives (RIAo, RINAP, RIBo, SAAo), so it is not a purpose-built corpus of Old Assyrian / Old Akkadian merchant records. In other words: this dataset is best treated as a broad, high-quality Akkadian–English parallel resource—particularly relevant to Neo-Assyrian / Neo-Babylonian-style language and genres—useful for pretraining, baseline NMT, alignment experiments, and tooling, rather than a direct proxy for the Kaneš trade letters.

ORACC Akkadian–English Parallel Corpus

This dataset contains parallel pairs of Akkadian transliteration (source) and English translation (target), extracted and aligned from the Open Richly Annotated Cuneiform Corpus (ORACC).

Source Projects

RIAo (Royal Inscriptions of Assyria online): Assyrian royal inscriptions ~2500-609 BCE RINAP (Royal Inscriptions of the Neo-Assyrian Period): Neo-Assyrian royal texts 744-609 BCE RIBo (Royal Inscriptions of Babylonia online): Babylonian royal inscriptions ~2500-539 BCE SAAo (State Archives of Assyria online): Letters and administrative texts 911-612 BCE

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/663357#3378237
- 投稿者: @deeppast
- 投稿日時: 2025-12-18
- upvote: 7
- 本文:How very resourceful you are. As a matter of fact, I am quite familiar with this dataset, and I would urge caution in using it, mainly because these texts from Oracc are very different from the Old Assyrian archives, in terms of time period and genre. First, there are no other Old Assyrian texts in the Oracc data, and only very few texts of a contemporary time period. The vast majority of these texts are from the first millennium, and therefore are about 1000 years later in time, which makes a huge impact on the use of the language. Second, we found in using this dataset that there were a large number of lexical lists, which were used in antiquity to record Akkadian to Sumerian equivalencies. Many of these lexical lists are also quite late (i.e. Late Babylonian), and therefore they will contain words which have no bearing on the Old Assyrian texts or the ways in which they wrote / spoke.

I understand that it is desirable to find as much data as possible for this challenge, but consider this. If you were building a Machine Translation model for modern English, would you also include Middle English texts, or maybe Old English lexicons? Probably not, but that's just my point of view.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/663357#3378252
- 投稿者: @manwithacat
- 投稿日時: 2025-12-18
- upvote: 1
- 本文:I felt it was the least worst option available to try and add something to my model that was vaguely Akkadian. I suppose using your analogy if I was trying to build a machine translation model for modern English and all I had was middle English then maybe I could at least extract some nouns or names or guess at some grammar rules from it.

Sumer Is Icumen In…

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/663357#3378267
- 投稿者: @deeppast
- 投稿日時: 2025-12-18
- upvote: 2
- 本文:I understand, in fact I tried this myself. I found that the genre is lost / muddled in translation by including all of this royal inscription text. Some words are generic enough that they are used in many different contexts, so when there's a bunch of examples from the first millennium of words with contexts like kings, conquests, priests, sacrifices, and the like, it creates a very different vector for words which in Old Assyrian are used with economic contexts (almost exclusively). To put it in another way, the sentence in Old Assyrian: "he should send the money to me, and I will pay the tax", under the influence of Neo-Assyrian or Neo-Babylonian royal inscriptions might come out as "he shall send me the tithes, and I will make an offering". This is a made up example, but it is very apparent in the AICC translations from 2023 of the CDLI (https://aicuneiform.com/).

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/663357#3378275
- 投稿者: @manwithacat
- 投稿日時: 2025-12-18
- upvote: 0
- 本文:Out of interest , I’ve got a plan and I’m wondering if I’m covering territory that’s already been tried before :

I’m proposing to try, very explicitly as an experimental modelling convenience rather than a claim about historical phonology, to introduce a parallel, highly normalised representation of the Akkadian input in which syllabic spellings are partially collapsed toward an abstract consonantal layer—either by stripping vowels entirely or by mapping consonants onto coarse articulatory classes (e.g. labial, dental/alveolar, sibilant, guttural)—and to feed this alongside the original transliteration rather than in place of it.

I’m not sure if that’s a silly idea or not, but I’m thinking cuneiform writing system might (does?) encode phonemic material in a deliberately lossy, syllabic way which creates extreme “surface variability” over underlying lexical and morphological regularities a model would ideally learn.

Anyway, worst case scenario, I burn a few GPU hours testing it out.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/663357#3378342
- 投稿者: @deeppast
- 投稿日時: 2025-12-18
- upvote: 0
- 本文:That is not a silly idea at all, in fact it makes good sense when you consider how tokenization works. The hyphens certainly pose an issue for subword tokenization, so normalizing the transliteration could be a good work-around for getting a better tokenization, and perhaps better embeddings too, depending on the size of the model.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/663357#3384424
- 投稿者: @jofatmofn
- 投稿日時: 2025-12-18
- upvote: 0
- 本文:I’m proposing to try, very explicitly as an experimental modelling convenience rather than a claim about historical phonology, to introduce a parallel, highly normalised representation of the Akkadian input in which syllabic spellings are partially collapsed toward an abstract consonantal layer—either by stripping vowels entirely or by mapping consonants onto coarse articulatory classes (e.g. labial, dental/alveolar, sibilant, guttural)—and to feed this alongside the original transliteration rather than in place of it.

@manwithacat, is this normalized transliteration idea related to your thought of using ORACC royal inscriptions and state/administrative archives as data?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/663357#3386486
- 投稿者: @manwithacat
- 投稿日時: 2026-01-01
- upvote: 0
- 本文:It was, but as the competition host noted above there’s a lot that is lost in translation. Also by their nature these types of inscriptions/proclamations are repetitive which is kind of counter-productive for model training.

My best score is currently using the public model trained by @jeanjean111

---

## Entry: `663849`
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/663849
- タイトル: Incomplete translations
- 投稿者: @angantyr
- 投稿日時: 2025-12-21
- upvote: 15
- 本文: There is a possible set of up to 163 incomplete translations.



The number is a very rough upper limit based on a rule that len(transliteration) < len(translation). While I cannot know how much wiggle room there is, I see a pattern of some transliteration not being fully translated.

Based on this rule of thumb one can see that some translations are too short for the respective transliterations

First 5 examples
The examples were sorted based on the translation length, so the first examples are the most showing:

/------------------------------------------------------------
| Entry: 2e1ab3e9-90ef-48f9-9517-fc9b7329f311  |
|----------------------------------------------/
|
|    TRANSLITERATION:
|        1 GÚ … … … … … … … at-lá+lá-x … KI PUZUR₄.IŠTAR a-ḫi-šu a-ḫa-ma 15 ma-na URUDU SIG₅ ší-im tí-sà-pì-im 14 ma-na URUDU SIG₅ ší-im pí-ri-kà-ni KI PUZUR₄.IŠTAR-ma
|
|    TRANSLATION:
|        1 talent ... ... 
\------------------------------------------------------------


/------------------------------------------------------------
| Entry: 629f1e04-a93d-429b-bdb1-aa6e02278659  |
|----------------------------------------------/
|
|    TRANSLITERATION:
|        10 ma-na … a-šur … a-na … … … … 2.5-GÍN KÙ.BABBAR aḫ-bu-ul-šu-um IGI ku-ra DUMU na-ra-am-ZU IGI a-šùr-DU₁₀ DUMU lu-lu-ú
|
|    TRANSLATION:
|        10 minas ... ...
\------------------------------------------------------------


/------------------------------------------------------------
| Entry: 194a79ff-646e-41a4-9f8b-670620da1e54  |
|----------------------------------------------/
|
|    TRANSLITERATION:
|        a-na na-áb-sú-en en-um-a-šur ù li-bur-be-lí DUMU ás-qú-di-a KIŠIB ÌR-dim DUMU ku-zi-a
|
|    TRANSLATION:
|        To Nabi-Suen,
\------------------------------------------------------------


/------------------------------------------------------------
| Entry: 821b6253-72c8-43a5-93e1-0b40b5f9a7fb  |
|----------------------------------------------/
|
|    TRANSLITERATION:
|        1 ki-ra-am a-šur-na-da 1 ki-ru-um x ša-lim-be-li …-áš-tí … zi-a
|
|    TRANSLATION:
|        1 drink: Aššur-nādā;
\------------------------------------------------------------


/------------------------------------------------------------
| Entry: f1ff7ea8-3705-4f1c-86ff-e0d2be46edbd  |
|----------------------------------------------/
|
|    TRANSLITERATION:
|        1 GÍN KÙ.BABBAR be-lúm-ba-ni 1.5 GÍN KÙ.BABBAR a-šur-iš-tí-kál 1.5 GÍN en-na-sú-in 1 GÍN KÙ.BABBAR be-lá-num 1 GÍN e-lá-lí 1.5 GÍN a-šur-ma-lik 1 GÍN šu-sú-in
|
|    TRANSLATION:
|        1 shekel of silver: Bēlum-bāni;
\------------------------------------------------------------
For example, the first translation is clearly partially translated as: * […] 15 minas of refined copper […] 14 minas of refined copped … PUZUR-IŠTAR]*

Last 5 examples:
The last 5 examples are less problematic /------------------------------------------------------------ | Entry: e87112af-3a74-4aa1-956c-8ac7f88828ba | |----------------------------------------------/ | | TRANSLITERATION: | a-na a-mur-a-šur ù a-lá-ḫi-im qí-bi-ma um-ma a-šùr-nim-ri-ma šu-ma ta-áš-ta-na-me ší-i-mu ša AN.NA ù TÚG.ḪI-tí i-na pu-ru-uš-ḫa-dim ma-aḫ-ṣú ku-ku-a na-pá-ḫa-am tù-ma-na a-ḫu-šu ú ma-la … na-pá-ḫa-am-ma … ù 2 ša-na x … a-wi-li ki-… a-ṣé-ri-šu-nu li-xx-nim-ma ša KÙ.BABBAR 10 ma-na.TA AN.NA x GÍN.TA a-na KÙ.BABBAR ṣa-ru-pí-im a-dí 5 ITU.KAM ù 6 ITU.KAM xx ku-nu-tí ma i-… xxx li … […] | | TRANSLATION: | To Amur-Aššur and Ali-ahum from Aššur-nimrī: You may have heard that trade in tin and textiles is ruined in Purušhaddum. The smith Kukuwa, his brother Tumana and Mala…, also a smith, … and two … the men … to them they should … and for each some 10 minas of silver … tin at the rate … to refine the silver. In 5 or 6 months … ------------------------------------------------------------

ku-nu-tí ma i- is not translated

/------------------------------------------------------------ | Entry: a6683271-8080-4571-a2aa-95bce559f023 | |----------------------------------------------/ | | TRANSLITERATION: | […] xxxx 20-x xx TÚG šu-ra-am a-na 11 GÍN a-na É kà-ri-im a-dí-i i-na 2 ma-na 10 GÍN KÙ.BABBAR ša i-na ni-kà-sé a-na e-lá-ma i-na-pu-lu-ni-im ŠÀ.BA 1.3333300000000001 ma-na 3 GÍN KÙ.BABBAR al-qé ší-tí KÙ.BABBAR 0.66666 ma-na 7 GÍN KI a-šùr-ma-lik ì-lí-a-lim ù la-qé-ep a-lá-qé 2 ma-na 14 GÍN KÙ.BABBAR i-na ša a-šur-be-el-a-wa-tim i-na … x […] xxxxxxx x-ma x xx | | TRANSLATION: | … … … … … … one dark colored textile I deposited for 11 shekels at the colonial office. Of the 2 minas 10 shekels of silver that one will balance to Elamma at the accounting, 1 mina 23 shekels thereof I took; the rest of the silver, 47 shekels, I will collect from Aššur-mālik, Ilī-ālum and Lā-qēp. 2 minas 14 shekels of silver from what belongs to Aššur-bēl-awātim, from / in […] ------------------------------------------------------------

/------------------------------------------------------------ | Entry: 9350a297-15d7-4564-9d0b-f00f0a0338db | |----------------------------------------------/ | | TRANSLITERATION: | 1 me-at NINDA a-mur-IŠTAR 1 me-at NINDA a-šur-mì-tì 1 me-at NINDA tù-pì-zi 1 me-at NINDA šu-ku-bu-um 50 NINDA a-lá-ḫu-um 50 NINDA en-na-be-lí 1 me-at NINDA a-šur-i-mì-tí DUMU a-ta-a 1 me-at NINDA PUZUR₄-(d)a-šùr 50 NINDA šál-ma-a-šùr 50 NINDA im-dí-DINGIR 50 NINDA DUMU ḫa-lá-bi₄-im 50 NINDA bu-zu-zu-um 50 NINDA lá-qé-ep 1 me-at NINDA kur-ub-IŠTAR 1 me-at NINDA a-šur-ma-lik 50 NINDA a-šùr-ṣú-lu-li 50 NINDA a-ni-num 50 NINDA a-šur-SIPA 1 me-at NINDA a-šur-na-da 50 NINDA en-nam-a-šur DUMU a-ḫi-a | | TRANSLATION: | 100 breads Amur-Ištar, 100 breads Aššur-imittī, 100 breads Tupizi, 100 breads Šu-Kūbum, 50 breads Ali-ahum, 50 breads Ennam-bēlī, 100 breads Aššur-imittī, [son of Ataya, 100 breads Puzur-Aššur, 50 breads Šalim-Aššur, 50 breads Imdī-ilum, 50 breads the son of hali-abum, 50 breads Buzuzum, 50 breads La-qēp, 100 breads Kurub-Ištar, 100 breads Aššur-mālik, 50 breads Aššur-ṣulūlī, 50 breads Anīnum, 50 breads Aššur-rē'ī, 100 breads Aššur-nādā, 50 breads Ennam-Aššur, son of my brother ------------------------------------------------------------

no problems with the translation?

/------------------------------------------------------------ | Entry: b0bce1f2-91d5-4812-88ca-715f51e96c4e | |----------------------------------------------/ | | TRANSLITERATION: | a-na e-lá-ma qí-bi₄-ma um-ma a-šur-na-da ù a-šur-i-mì-tí-ma 1 me-at 2 TÚG.ḪI.A ku-ta-nu qá-dí ša x x li-wi-tum 4 GÚ x ma-na AN.NA ku-mu-ki 6 ANŠE xxxx (large break) ù x … a-na ni-is-ḫa-tim ni-iš-qú-ul ki-ma x ma-na AN.NA 0.5 ma-na KÙ.BABBAR a-na qá-tí a-šùr-mu-ta-pì-il₅ ni-dí-in 0.33333 ma-na AN.NA a-šur-i-mì-tí il₅-qé 3 TÚG a-wi-il₅-tum tal-qé 0.33333 ma-na 7 GÍN ší-im ANŠE 2 GÍN ṣí-tum KÙ.BABBAR aḫ-ša-lim il₅-qé 2 TÚG ša kà-ṣa-ri-im KI aḫ-ša-lim ni-kà-sí ni-ša-sí | | TRANSLATION: | Say to Elamma, thus Aššur-nādā and Aššur-imittī: 102 -textiles inculding those … [for wrapp]ing, 4 talents [x minas of seal]ed [tin], 6 donkeys? … as import-tax … we paid. [Instead of x minas] of tin we handed over to Aššur-mūtappil 0.5 mina of silver. Aššur-imittī took 0.3333 mina of tin. The lady took 3 textiles. 27 shekels was the price of a donkey, 2 shekels, expenditures? in silver, Ah-šalim t[ook?]. 2 textiles of the harnesser. We will settle accounts with Ah-šalim." ------------------------------------------------------------

ni-kà-sí ni-ša-sí is not translated

/------------------------------------------------------------ | Entry: a5114979-d798-46a7-9943-6bba8ddf7382 | |----------------------------------------------/ | | TRANSLITERATION: | um-ma … ù lá-ma-sí-ma a-na … a-dí-da a-ba-ba ù a-la-ḫi-im qí-bi₄-ma ta-áš-pu-ra-nim-ma i-na na-áš-pè-er-tí-ku-nu um-ma a-tù-nu-ma a-lu-wa u₄-ma-kál lá i-sà-ḫu-ur a pá-ni-a a ḫa-ra-ni li-ik-šu-dam u₄-ma-am iš-tù ITU.3.KAM a-lu-wa ni-iṭ-ru-da-ma ù a-na u₄-mì-im a-nim mì-ma ša x … lá ni-iš-me ù šu-ma-mì-in i-na É a-lim(ki) a-bu-ku-nu … lá ša-sí um-ma né-nu-ma iš-tí li-bi₄-šu li-li-kam … x-mu-ma tù x ut ri ba … x la KÙ.BABBAR … x (large break) … ù a-lá-ḫi-im qí-bi₄-ma … a-dí-da ší-be a-ḫu-… … KÙ.BABBAR-pì-a ma-… | | TRANSLATION: | From … and Lamassī to Adida, Ababa and Ali-ahum: You have written and in your missive you said: Aluwa must not delay a single day. Let him catch up with me on the journey." Today it is 3 months since we sent Aluwa and until this day we have heard nothing concerning … Also, if your (plur.) father had not settled accounts in the City Hall, when we said: "Let him come when he wishes(?), … To … and Ali-ahum: … Adida … witnesses … of my silver … ------------------------------------------------------------

The list of possibly faulty translations
As for the OARE_ID, these are the following:

ref. num	OARE_ID
1	2e1ab3e9-90ef-48f9-9517-fc9b7329f311
2	629f1e04-a93d-429b-bdb1-aa6e02278659
3	194a79ff-646e-41a4-9f8b-670620da1e54
4	821b6253-72c8-43a5-93e1-0b40b5f9a7fb
5	f1ff7ea8-3705-4f1c-86ff-e0d2be46edbd
6	02d16b63-3fab-4c1d-8262-4cd74f6532f1
7	27a814ba-f860-4468-8986-16e7ba2faaaa
8	84183318-0d21-4f37-96d0-a30811e06873
9	c45f0b9e-0e0c-4d20-aded-91fd0587928c
10	1b7347d9-66f4-4f15-9a03-45fcad0a6c09
11	5db6ccde-0832-482f-8dcd-e4da3138cf06
12	da4b9647-bf01-4d97-9c3d-75d26535ddbc
13	b24f8913-70f0-4422-847f-12e4c8d5bb36
14	2e4043ed-4d34-49ef-a267-0fa524b6d9b3
15	ee7397e8-13a5-44c1-9674-1276d42c7ff4
16	5bf906ac-870f-4a27-951e-e54cd64dd9f2
17	529fcbd8-9122-4d49-9cb9-021545dd9fb1
18	8597f793-fd5a-4b97-a812-b4d292031227
19	473b198b-7acb-44d3-a15e-705e22aa13f4
20	c227c990-44a9-41d6-81f3-243b1ef86e2b
21	20b29d15-b88e-4905-9c55-2294749474af
22	9c7e32b3-fc22-41cb-a43a-60cd04266022
23	d011d482-42d7-41f3-a8ae-716820d975ff
24	e0474415-9913-4c7f-ba5d-1924c9b53846
25	3a883563-aa24-454f-b0cc-710508f835e9
26	ac4e0163-b6b0-47b2-b286-1d6a0f794849
27	f09d22e9-efb1-4145-b5df-bc85afeb29cb
28	103e6d83-27e6-4dcf-ac7f-747f9674e37c
29	a3e13df6-4313-45e6-9749-402acd8ea3c6
30	aa4c3709-35c5-4e70-a368-f0582dce6441
31	bcdc31ca-9e37-4576-bb62-3336edb673c5
32	e05f20dc-7a27-4b71-8d0f-628a8757091d
33	382c0b6b-3b55-4673-8054-9ce3b48da6f6
34	3b85ccd0-aa16-49ad-a7e8-db0c5a63d373
35	a9f48c23-483a-4f68-8930-25eaf746029d
36	7d9a743f-d211-4afa-a173-347c5b4731a3
37	f122aa32-3fdd-479d-b182-dfbe45d621d8
38	b712b838-cdf5-42d7-80bb-c32200dbfc37
39	ef2c3a21-2451-436b-b1a3-16b8574ff27a
40	d38ae78c-c321-4e83-8c0f-264ef6e0ef78
41	3ebbad20-ee06-478f-8340-bd6244bd40c1
42	3809e5da-963a-4926-9b86-80e60b641a4c
43	c123d89e-9e69-4523-874b-052f4eb885cc
44	fc15e06d-312d-4f77-87f2-7004dd734d6a
45	306e3b37-ecfb-479e-a93d-32283393f1fe
46	0b94fbc1-0422-4849-9bca-53197403585b
47	8dad8a7c-a628-432a-9058-e66805874554
48	2137ea96-fe90-4188-ba36-6a53d4c689e3
49	e46ab6a3-1fe7-471b-96c3-6c4f14e6a7e5
50	342453f4-7335-40b9-8fa1-fe0cc66f2345
51	8316cc0f-8ee3-43e4-8057-cd0fdbefd948
52	f6235a36-85bc-420d-bf1e-e6d3d6f42c8a
53	48e6dc98-bc89-4f90-abba-736226b498b9
54	9864ddf0-99b1-4eae-855c-d33288497f81
55	dd9930f0-816c-4db8-8764-076d725f252f
56	57949d3d-cab0-4007-b0b2-4ddcf053bcb6
57	ba4a0bcd-4396-45d3-982d-3cac8f813cbb
58	9506ffe6-93e8-443a-9aae-f562614216cc
59	d604d277-4d17-492e-9f1b-0357108bb99b
60	fd870d99-4620-4248-820a-3ff9b63f0287
61	a7e83126-95c9-44b2-9cc7-a3771a009138
62	6e1f457c-74c0-4e35-8d9b-64dcde103453
63	3ac2d1b1-471b-4973-8e6b-11e8c08d6246
64	16830cc1-253e-40d2-b904-2b3ab6234675
65	a1f0269a-c1d6-44bf-8ceb-1cd699399cef
66	c0944669-25ba-4ed3-8e48-6e7f307f0f6a
67	697fdae3-abd6-4de6-89ac-03796381be51
68	e5f3d822-808d-46ff-bb56-785a45a5614c
69	fcf5a0e5-2a2f-4651-8b46-5e860167dc10
70	82155dda-2e35-4568-a6ab-99b0a8158586
71	99552f43-f500-4605-b650-5e18dd30a4c4
72	0f3acc15-a065-4431-93e1-0166842af8d8
73	40662ba6-ce99-40d3-907d-36900d6d5930
74	7017170b-b6fa-4537-a64e-e010c9306db6
75	afe3e836-87a1-40f7-9860-9c256f83b325
76	b7117c1f-8b81-425b-89eb-b6f44990cbec
77	c19f345f-7459-4bd8-a6ea-a2393c656520
78	f7c0535b-c527-4289-911a-c2a3f26ba2cf
79	49dc6944-022d-4b48-80b6-5d3c71ee08d1
80	3390188c-dad0-4b6d-8acd-e03ab75970de
81	341e367f-59bf-403d-8b44-17cbc6038df8
82	8c737557-7e47-4193-a739-13e261a9ea99
83	56ccb672-f4dc-4a2c-bea9-5ad9cbf3af9b
84	b5bd80f4-1c55-4950-b13a-5b6cc97199b3
85	d8d8160b-6497-4d75-909b-1d94f5ea2498
86	f0a43241-7539-4c9b-baaa-4e39090e08fe
87	2c3f9fcf-57c7-461e-86ec-cfa093e5e353
88	6131d12a-0906-4306-95a3-e0ea57efaac4
89	2ada8b49-900d-4495-ae33-feb7be12f7b4
90	7a82f70f-9993-4163-9112-ffba86455ded
91	81f1a9f0-544f-4939-8510-2128c98764b7
92	6efd3486-9a20-45d6-94dc-862b0035fa1e
93	72dac38d-d82a-42ec-99b3-9cfc49a6d134
94	a65d5c7b-e9a1-4366-bdd0-9a74e17edccd
95	77431f30-8a85-4922-898b-0573d41a272a
96	45a2b191-1aac-4bf9-b306-d401002516b5
97	6e47ef61-8f1b-4a48-b4a6-a759d5be37b8
98	36cafb3f-2d3b-44e1-af48-608bec6caae3
99	fe95294d-1ef5-49aa-b6a9-5062bb2678a9
100	508f160f-9e73-43b3-a19f-80c05f246e21
101	bb0df83b-506b-4c81-a5ad-f82172f7f251
102	a4519c6a-effc-4805-a055-9db66f1ad72d
103	89b3ddad-7210-442d-b4e5-192b36f840d5
104	1d0c7278-13ef-42e9-814f-0412eecadf20
105	0d22e71e-ab7e-4bb7-83bc-052b25789dba
106	035670c1-3504-4084-a2e6-1ff68ade4c74
107	5d138f2b-7e45-47d9-b002-34f9df1ad681
108	0d9cc172-1feb-46bd-94c3-23c00a6e83f1
109	c048ccc5-e069-4c74-81b8-63332b1c1db5
110	477ce87f-8585-4113-bf83-611ddf62de8a
111	d93fadca-089c-4135-8228-bc755873b2bf
112	3d8d933c-85b8-41d6-af30-76743babaa1a
113	6378ae62-bf08-4b93-9d90-370b0fff6e38
114	77bb9313-13f7-4539-a8e4-4019d7abf4ee
115	45b357d1-83f3-4c32-ae77-648fe544f96c
116	934614c3-ecfc-4ecd-897c-78ce45c055d6
117	d5e10e2c-1179-4d03-8ac5-7bd7692d9547
118	c5d8a8b7-2b71-4a3a-abf2-4ac84910e219
119	ee18ffb2-0f9e-4c31-8bd2-e7bd20de62ab
120	bf9f567f-0cd1-416d-8015-aa4db3a8c8f2
121	9d8527d7-0033-45f2-8e42-910c1a1b3ad4
122	0a563c7c-797f-4ca6-b937-cd2be4d3465a
123	e67e6f74-63c3-4940-8e9d-788c10d9fa1d
124	629af763-bae3-40e9-915b-a95e6bf4d158
125	31c8ab5f-59f9-425e-9f34-2f1a8e5e9665
126	7b05ef05-e0c2-4123-905a-da6d2c3301eb
127	5c5db0da-18fc-41f3-b744-41f23fb2db09
128	107b536a-b713-474f-a2b3-cb3852ef839e
129	87359b53-a607-4cd1-a3fb-a6c46bb03596
130	ce441de3-20bb-4ae3-aebc-40bd092368e6
131	0a737259-8186-4ace-a2bf-1dd76c27563e
132	ad6b0cb2-201b-4747-9c02-a86ba3d15ed6
133	cb0b6fbf-5ca6-4c46-a677-a9935a698f1a
134	a1251a33-431a-401a-b678-d8b20181ddda
135	13018eed-d30f-42a7-a3a0-2c2e73e7673d
136	f3a64bb2-f00a-47d6-ace4-92993e69f2a1
137	e987ed38-8dc5-435f-8e3e-455f18558f4c
138	28ee69cf-a620-42c7-a976-4e0bbf43b988
139	eef5c820-6603-4fbf-920a-80eb1fa19a05
140	cfcc7f6c-d48f-4ffd-948f-248a3a397ffc
141	7d68ad7e-c614-4087-880e-666eca930a18
142	42b314af-c18c-438e-9cce-feaddc0af869
143	03826c8c-3727-4caf-b781-1cc5f6ab56e6
144	aeaf09ae-c57d-4206-acb2-3d9a687cbbc4
145	5f088d12-ed99-434a-a113-65deab7e1426
146	3a677ce1-bc5a-49b4-bbcb-4abb1e93b626
147	f98df4c2-0e1f-487e-bbbb-e43a454f66ff
148	234cb7c6-b8f2-4289-99a0-7a7575d31b83
149	64d4ae91-42f3-4244-a38e-8700d2bb9af5
150	02de3489-7e0e-40fb-878d-141b28b7d6ff
151	4c32e34e-79ea-4529-bb6b-2050e2fdcdc0
152	34be41c8-248f-4a41-8a36-1ef840ca9490
153	5b9b8f63-9cad-4d21-8290-5e1bca2f60b9
154	4bffd286-1300-4d02-837a-13296fbac02f
155	331e44ee-fb14-418b-b41c-55abefe272ce
156	f40f51b2-cb9e-4f55-96ec-d545c6d3cd6f
157	d936c8ee-0394-4b1c-9873-6419aa9a99d2
158	1f922cf5-3381-4e27-8473-d3ae9ce4e85a
159	e87112af-3a74-4aa1-956c-8ac7f88828ba
160	a6683271-8080-4571-a2aa-95bce559f023
161	9350a297-15d7-4564-9d0b-f00f0a0338db
162	b0bce1f2-91d5-4812-88ca-715f51e96c4e
163	a5114979-d798-46a7-9943-6bba8ddf7382
Obviously a better limit should be used for the translation length but I went with a simple one to get a quick and simple hold on the problem.

@deeppast Any thoughts on how to solve the problem?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/663849#3381029
- 投稿者: @deeppast
- 投稿日時: 2025-12-24
- upvote: 3
- 本文:Thank you for this detailed observation and assessment of the translations. I'm sure this will be a great benefit for all involved! You're absolutely right to check these translations for completeness. Some of these texts will have more complete translations in the publications.csv in English or other languages. In the publications the editor(s) of the text will often include comments and notes about why a section or word is problematic. Unfortunately, there is not a simple solution for this at this time. This challenge has brought to the fore that the scholarly emphasis for cuneiform has been primarily focused on photographs and transcriptions, in the form of transliteration, and the main databases reflect this (especially the CDLI). But what is woefully lacking is a database of translations, which is precisely what would be of most benefit for training machine translation for Akkadian and the other languages using the cuneiform writing system.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/663849#3381094
- 投稿者: @angantyr
- 投稿日時: 2025-12-24
- upvote: 1
- 本文:Thank you so much for a detailed answer. I have an idea how to possibly tackle the problem. I'll share the news once I verify it will make sense to implement.

---

## Entry: `665101`
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665101
- タイトル: Unicode Fractions vs Decimals: LB Score Unchanged?
- 投稿者: @hrithik22122
- 投稿日時: 2025-12-30
- upvote: 9
- 本文: Hi everyone, Following the host's comment regarding the hidden test dataset using Unicode fractions (e.g., ½, ⅓, 2 ½) instead of decimals/floats, I implemented a post-processing step to align my model's output with the expected format.

The Context
In the discussion How To Handle These Examples, the host mentioned:

"The fractions are retained in the hidden test dataset... you will find 2 ½ minas... and NOT 2.5 ma-na."
My Approach
I wrote a script to dynamically convert decimal patterns in my predictions to their closest Unicode fraction equivalents (using limit_denominator to catch 0.333... as ⅓). Visually, the script seems to work perfectly on the sample items:

Example 1: 42.33333 ma-na -> 42 ⅓ ma-na
Example 2: 1.25 GÍN -> 1 ¼ GÍN
The Issue
Despite this correction clearly matching the host's description of the ground truth format, my LB score remained exactly the same (to the 4th decimal) compared to the submission with raw floats.

My Code
Here is the function I used. Is there an edge case I am missing, or is the spacing logic (Integer[space]Fraction vs IntegerFraction) different from what I assumed?

import re
from fractions import Fraction
def process_fractions_dynamic(row, target_col="prediction"):
   text_to_process = row.get(target_col, "")
   if not isinstance(text_to_process, str):
       return str(text_to_process)
   # Standard unicode map
   fraction_lookup = {
       (1, 2): "½", (1, 3): "⅓", (2, 3): "⅔",
       (1, 4): "¼", (3, 4): "¾",
       (1, 5): "⅕", (2, 5): "⅖", (3, 5): "⅗", (4, 5): "⅘",
       (1, 6): "⅙", (5, 6): "⅚",
       (1, 8): "⅛", (3, 8): "⅜", (5, 8): "⅝", (7, 8): "⅞"
   }
   def replacer(match):
       full_str = match.group(0)
       try:
           val = float(full_str)
           integer_part = int(val)
           decimal_part = val - integer_part
           # Return integer if decimal is negligible
           if decimal_part < 0.0001: 
               return str(integer_part)
           # Limit denominator handles 0.3333 -> 1/3
           frac = Fraction(decimal_part).limit_denominator(12) 

           unicode_frac = fraction_lookup.get((frac.numerator, frac.denominator))
           if unicode_frac:
               if integer_part == 0:
                   return unicode_frac
               else:
                   # Current logic: Space between Integer and Fraction
                   return f"{integer_part} {unicode_frac}"

           return full_str 
       except ValueError:
           return full_str
   processed_text = re.sub(r'\b\d+\.\d+\b', replacer, text_to_process)
   return processed_text
Ouput
[4] 
2 ne2-pi2-szu 15 ma-na.TA u2 isz-ti2-in ne2-pi2-szu-um 10 ma-na ni-is-ha-su2 DIRI sza-du-a-su2 sza-bu-u2 SZU.NÍGIN 42.33333 ma-na KÙ.BABBAR s,a-ru-pa2-am ku-nu-ki-a a-na a-lu-wa u3 e-ni-sza-ri-im a2p-qi2-id-ma a-na a-lim{ki} a ma-la2 ti2-ir-ti2-szu a-s,e2-er sza-lim-a-szu3r u2-sze2-bi-il5-szu-nu a-ha-ma 13.33333 ma-na URUDU SIG5 a-na ga-am-ri-szu-nu u3 5 GÍN KÙ.BABBAR a-na u2-ku-ul-ti2-szu-nu a-di2-in IGI ili5-ba-ni DUMU ba-szi2-lam IGI a-hu-qar DUMU zu-ur-zu-ur IGI tu3-ra-am-i3-li2 DUMU e-di2-na-a-szu3r a-ha-ma 10.33333 ma-na 3.5 GÍN KÙ.BABBAR s,a-ru-pa2-am <gap> tum ni <gap> 0.5 GÍN s,i2-ba-tim sza i-na s,e2-ri-a il5-qe2-u2-ni a-na hu-bu-li-szu a-na ka3-ri-im wa-ah-szu-sza-na a2sz-qu2l s,i2-ba-at KÙ.GI sza szi2-ip-ka3-at a-szur-be2-el-a-wa-tim i-szi2-tu3
Translation : 2 packages of 15 minas each plus a single package of 10 minas, its import duty added, its transport tariff paid - in all 42 ⅓ minas of refined silver under my seal, I entrusted to Aluwa and Enišārum, and I sent them to the City to Šalim-Aššur in accordance with his orders. Furthermore, I paid 13 ⅓ minas of good copper for their expenses and 5 shekels of silver for their food. Witnessed by Ilī-bāni son of Baši-ilum, by Ahu-qar son of Zurzur, by Tūram-ilī son of Eddin-Aššur. Furthermore, 10 ⅓ minas 3 ½ shekels of refined silver   <big_gap> ,   <big_gap> ½, shekel interest that they took on my account, I paid for his debt to the Wahšušana colony. The interest on the gold that remained of Aššur-bēl-awātim's investment.
Precdiction : 2 packages of 15 minas each and a single package of 10 minas - its import duty added, its transport tariff paid - in all 42 ⅓ minas of refined silver under my seal I entrusted to Aluwa and Enišārum, and I sent them to the City in accordance with his instructions to Šalim-Aššur. Further, I gave 13 ⅓ minas of good copper for their expenses and 5 shekels of silver for their food. Witnessed by Ilī-bāni son of Bašilum, by Ahu-waqar son of Zurzur, by Tūr.
==============================
[6] 
1.25 GÍN KÙ.BABBAR i-na li-bi4 lu-lu
Translation : 1 1 / 4 shekel of silver is owed by Lulu.
Precdiction : 1 ¼ shekel of silver owed by Lulu.
Queries
Metric Sensitivity: Is the evaluation metric sensitive enough that correcting 0.33 (4 chars) to ⅓ (1 char) results in a score change too small to see on the public LB?
Formatting: Does the ground truth use a space between the integer and the fraction (e.g., 2 ½) or are they concatenated (2½)?
Normalization: Is there a hidden normalization step in the metric that might be converting ½ back to numbers or ignoring these differences?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665101#3383555
- 投稿者: @mpware
- 投稿日時: 2025-12-30
- upvote: 3
- 本文:It's similar for me the LB remains the same with or without floats to fractions conversion. However, if I sort public LB by score then I can see it's a bit better for the submission with fractions conversion. @hrithik22122 Is it the same for you? If 2 submissions are strictly equal then the first one (oldest) should be the first. Otherwise it's sorted by best score (even if it displays only a single digit as far as I know)

Second, impact for floats to fractions conversion on geometric_mean is quite low on a single fold OOF for me:

Floats + limited fractions in ground truth: 45.53 (we've some fractions already in ground truth)
Fractions only in ground truth: 44.22
Let's wait for the official voice of organizer. There are for sure other reasons for such a big gap between CV / LB we need to discover.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665101#3383557
- 投稿者: @qifeihhh666
- 投稿日時: 2025-12-30
- upvote: 1
- 本文:lol,yes, decimal places aren’t shown, but the submission clearly reflects the actual values of the three same scores.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665101#3383570
- 投稿者: @hrithik22122
- 投稿日時: 2025-12-30
- upvote: 2
- 本文:Nah , when I sort it , my first submission(one without fraction post processing) comes up first

I was expecting an LB increase of around 0.2–0.6 because the penalty for raw decimals should be massive:

BLEU: A mismatch like 13.3333 vs 13 ⅓ means zero overlap for that token. By fixing it, we should recover the unigram match, plus the associated bi-grams and tri-grams ("paid 13.333 silver" vs "paid 13 ⅓ silver").

chRF++: The character edit distance between 13.3333 (7 chars) and 13 ⅓ (3-4 chars) is very large. Normalizing this should have significantly reduced the edit distance penalty.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665101#3383671
- 投稿者: @deeppast
- 投稿日時: 2025-12-31
- upvote: 4
- 本文:The ground truth uses a space between the integer and the fraction (e.g., 2 ½). Let me put it this way, there are no instances of '/' in either the translation or transliteration, this goes for both the public and private evaluation data.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665101#3383682
- 投稿者: @qifeihhh666
- 投稿日時: 2025-12-31
- upvote: 0
- 本文:Oh, this is really a highly potential point, I can try it again tomorrow.Thanks

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665101#3383499
- 投稿者: @hrithik22122
- 投稿日時: 2025-12-30
- upvote: 1
- 本文:With and without space has the same LB

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665101#3383527
- 投稿者: @angantyr
- 投稿日時: 2025-12-30
- upvote: 2
- 本文:If the test set is similar to the train.csv set, then it will matter for ca. 38% of the transliterations / ca. 33% of translations: 

For those that it will, it won't give a large impact, since in most cases fractions account for less than 5% of words: 

The code for the above fractions:

number_of_fractions = train.loc[:,'transliteration'].apply(lambda row: len(re.findall(r'\b([0-9]+\.33[3]*|[0-9]+\.5|\.25|[0-9]+\.75)\b', row)))
number_of_words = train.loc[:,'transliteration'].apply(lambda row: len(re.findall(r'\b([\w\-\.]+)\b', row)))
fraction_to_words_ratio = number_of_fractions/number_of_words

number_of_fractions_t = train.loc[:,'translation'].apply(lambda row: len(re.findall(r'\b([0-9]+\.33[3]*|[0-9]+\.5|\.25|[0-9]+\.75)\b', row)))
number_of_words_t = train.loc[:,'translation'].apply(lambda row: len(re.findall(r'\b([\w\-\.]+)\b', row)))
fraction_to_words_ratio_t = number_of_fractions_t/number_of_words_t
I haven't consulted the metrics so I can't give the estimates of how they would change but this would be my guess as to why the observed changes are not very impactful.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665101#3383499
- 投稿者: @hrithik22122
- 投稿日時: 2025-12-30
- upvote: 1
- 本文:With and without space has the same LB

---

## Entry: `665949`
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665949
- タイトル: How to handle dot h/H?
- 投稿者: @mpware
- 投稿日時: 2026-01-05
- upvote: 9
- 本文: Hi all,

Transliteration normalization is a challenge both train set and test set. I'm entering an endless loop with ḫ and Ḫ 😁

We know that test set contains h and H but not ḫ nor Ḫ
Our train set (train.csv, same for published_text.csv) contains zero h nor H but many ḫ and Ḫ
How to manage this headache?

Convert all ḫ / Ḫ into h / H in train set, no changes on test set.
Keep ḫ / Ḫ in train set, convert h / H to ḫ / Ḫ in test set.
Try also variants reported here below in test set:
# H variants
"h,": "ḫ",
"H,": "Ḫ",
".h": "ḫ",
".H": "Ḫ",
"hh": "ḫ",
"HH": "Ḫ",
Any feedback on these approaches or other are welcome.

@deeppast Does your normalization function convert any ḫ or Ḫ to h / H? Is it possible in Akkadian transliteration to have h / H that are not ḫ / Ḫ?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665949#3387816
- 投稿者: @nofreewill
- 投稿日時: 2026-01-08
- upvote: 1
- 本文:"We know that test set contains h and H but not ḫ nor Ḫ" wait what? is this true?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665949#3387824
- 投稿者: @qifeihhh666
- 投稿日時: 2026-01-08
- upvote: 1
- 本文:Maybe,At least the characters published by the organizer do not show ḫ and Ḫ. there

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665949#3387917
- 投稿者: @mpware
- 投稿日時: 2026-01-08
- upvote: 1
- 本文:I hope, the allowed chars list has been provided by organizer.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665949#3386127
- 投稿者: @nlztrk
- 投稿日時: 2026-01-05
- upvote: 1
- 本文:well well well 😄 have you tried any of these options?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665949#3386149
- 投稿者: @mpware
- 投稿日時: 2026-01-05
- upvote: 1
- 本文:I'm trying all these but no real changes:

Baseline: Keep ḫ / Ḫ in train set, no change on test set: LB=34.0
Baseline: Keep ḫ / Ḫ in train set, option #3 (H variants) on test set: LB=34.0+
Baseline: Keep ḫ / Ḫ in train set, option #3 (H variants) + convert remaining h / H to ḫ / Ḫ in test set: LB=34.0-
Baseline: Keep ḫ / Ḫ in train set, convert h / H to ḫ / Ḫ in test set: LB=34.0--
Retrain: Convert all ḫ / Ḫ into h / H in train set, no changes on test set: LB=33.5
Last one sounds interesting but I believe it looses information because LB drops a bit. I think there is no "plain h" in the Akkadian language. Experiment#2 with the H variant alone looks better but we would need to know if the transliteration normalization converts Ḫ into .H or H, or H @deeppast ?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665949#3387334
- 投稿者: @mpware
- 投稿日時: 2026-01-07
- upvote: 0
- 本文:@deeppast Any information about your dot h/H transliteration normalization would help. Let's us know if you can provide it. Thanks a lot.

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665949#3387348
- 投稿者: @jackvd
- 投稿日時: 2026-01-07
- upvote: 0
- 本文:Is this saying that keeping the ḫ / Ḫ makes your score 0.5 better?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665949#3387363
- 投稿者: @mpware
- 投稿日時: 2026-01-07
- upvote: 1
- 本文:Currently I keep ḫ / Ḫ as is in the training set knowing that they do not exist in test set and it looks better than replacing them by h / H (but it was on a single submission).

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/665949#3387452
- 投稿者: @jackvd
- 投稿日時: 2026-01-07
- upvote: 0
- 本文:Are you leaving anything else? I've spent countless hours going through this data and reading the competition recommendations only to make changes and see reduced performances.. I'd be curious to know how you're handling punctuation, fractions, and the text within angled brackets/parenthesis for the train.csv data. My recent experiments are definitely not giving outcomes I'd expect

## Entry: `664905`
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664905
- タイトル: Question about OA_Lexicon_eBL.csv - Personal Name Spelling Inconsistency with Ground Truth
- 投稿者: @ruichardliu
- 投稿日時: 2025-12-29
- upvote: 4
- 本文: Hi everyone, I've been trying to use the "OA_Lexicon_eBL.csv" lexicon for post-processing to verify personal names in translations. However, I noticed that the norm field in the lexicon often differs from the actual spelling used in the ground truth translations.

Examples: Source (transliteration) Lexicon norm Ground Truth spelling

šu-ku-bi-im Šu-Kūbim Šu-Kūbum
šu-ta-mu-zi Šu-Tammazi Šu-Tammuzī
e-lá-a Elā(ya) Elaya
a-bi₄-lá Abela Abila
Statistics:

Total personal names detected in training data: 11,381
Exact match with lexicon norm: 37.2%
Fuzzy match (85% similarity): 73.3%
Still unmatched after fuzzy matching: 26.7% (~3,041 names)
Questions:

Is this spelling variation intentional? (e.g., different scholarly conventions)
Is there a recommended way to use the lexicon for name verification/correction?
Are there any additional resources that map between these spelling variants?

### Comments
- URL: https://www.kaggle.com/competitions/deep-past-initiative-machine-translation/discussion/664905#3382925
- 投稿者: @deeppast
- 投稿日時: 2025-12-29
- upvote: 1
- 本文:Yes, Angantyr is correct, and your questions are worth addressing one by one:

(1) Spelling variation exists at both the transliteration and normalization (unfortunately). For example we find: Ahu-waqar = A-hu-wa-qar & A-hu-qar Ahuwaqar = A-hu-wa-qar & A-hu-qar

This discrepency is because there are many scholars all over the world doing their best to normalize the names on these texts, but there are not yet firmly established conventions for every name encountered on the texts. I realize this is a big issue, since most of the OOV (out of vocabulary) words are going to be proper nouns / names. So I'm working on getting a list of spellings and normalizations together for the supplemental data.

(2) Most of the names are provided in the OA_Lexicon_eBL.csv and given a "PN" type (instead of "Word"). And I will share a more robust onomasticon (list of names) shortly.

(3) All the resources we provided are what is currently available in digital format. There are lists of personal names in book publications in the index of the major text editions, and specialist studies (e.g. https://archive.org/details/veenhof-1972-assyrian-trade/page/n515/mode/2up). But these are rarely accessible online as far as I'm aware.