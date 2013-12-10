#!/usr/bin/env python
from __future__ import print_function
from alchemyapi import AlchemyAPI
import json

demo_text = 'Tesla Motors was one of the market movers last week, with the stock touching a low of $123.93 on Monday, Dec. 2, only to close the week about 11% higher on Friday at $137. Last Tuesday was a particularly busy day for shares of Tesla, as the stock climbed on unusually high volume of 25,625,400. Let's take a closer look at what caused the move last week, and what investors can anticipate in the week ahead. Last week's defining "Tesla" moments
More than 25 million Tesla shares traded hands last Tuesday, pushing the stock higher by 17% that day. Good news from German investigators, as well as an analyst upgrade from Morgan Stanley, was to thank. First, a German probe into recent Tesla Model S fires found "no manufacturer-related defects." While a U.S. investigation by the NHTSA is still under way, the seal of approval from the German Federal Motor Transport Authority was nonetheless encouraging.
On top of this, Morgan Stanley analyst Adam Jonas reiterated his support for the stock by naming Tesla his top pick among stocks within the auto sector. Commenting on the Model S fire incidents, Jonas said his firm is "impressed there have only been three fires since the car has gone on sale over 17 months, 22,000 units and some 130 million miles driven ago." As a result, Morgan Stanley now has a price target of $153 on shares of Tesla.
Tesla gained even more attention later in the week, after SolarCity announced a new solar-powered storage system that uses Tesla's lithium-ion batteries. This is a perfect fit for the electric-car maker, particularly because Tesla's CEO, Elon Musk, is already a majority shareholder in SolarCity. It also helps that Musk is cousins with SolarCity's CEO Lyndon Rive.'
#demo_text = 'In Moulmein, in lower Burma, I was hated by large numbers of people, the only time in my life that I have been important enough for this to happen to me. I was sub-divisional police officer of the town, and in an aimless, petty kind of way anti-European feeling was very bitter. No one had the guts to raise a riot, but if a European woman went through the bazaars alone somebody would probably spit betel juice over her dress. As a police officer I was an obvious target and was baited whenever it seemed safe to do so. When a nimble Burman tripped me up on the football field and the referee (another Burman) looked the other way, the crowd yelled with hideous laughter. This happened more than once. In the end the sneering yellow faces of young men that met me everywhere, the insults hooted after me when I was at a safe distance, got badly on my nerves. The young Buddhist priests were the worst of all. There were several thousands of them in the town and none of them seemed to have anything to do except stand on street corners and jeer at Europeans.'
demo_url = 'http://blog.programmableweb.com/2011/09/16/new-api-billionaire-text-extractor-alchemy/'
demo_html = '<html><head><title>Python Demo | AlchemyAPI</title></head><body><h1>Did you know that AlchemyAPI works on HTML?</h1><p>Well, you do now.</p></body></html>'


print('')
print('')
print('            ,                                                                                                                              ') 
print('      .I7777~                                                                                                                              ')
print('     .I7777777                                                                                                                             ')
print('   +.  77777777                                                                                                                            ')
print(' =???,  I7777777=                                                                                                                          ')
print('=??????   7777777?   ,:::===?                                                                                                              ')
print('=???????.  777777777777777777~         .77:    ??           :7                                              =$,     :$$$$$$+  =$?          ')
print(' ????????: .777777777777777777         II77    ??           :7                                              $$7     :$?   7$7 =$?          ')
print('  .???????=  +7777777777777777        .7 =7:   ??   :7777+  :7:I777?    ?777I=  77~777? ,777I I7      77   +$?$:    :$?    $$ =$?          ')
print('    ???????+  ~777???+===:::         :7+  ~7   ?? .77    +7 :7?.   II  7~   ,I7 77+   I77   ~7 ?7    =7:  .$, =$    :$?  ,$$? =$?          ')
print('    ,???????~                        77    7:  ?? ?I.     7 :7     :7 ~7      7 77    =7:    7  7    7~   7$   $=   :$$$$$$~  =$?          ')
print('    .???????  ,???I77777777777~     :77777777~ ?? 7:        :7     :7 777777777:77    =7     7  +7  ~7   $$$$$$$$I  :$?       =$?          ')
print('   .???????  ,7777777777777777      7=      77 ?? I+      7 :7     :7 ??      7,77    =7     7   7~ 7,  =$7     $$, :$?       =$?          ')
print('  .???????. I77777777777777777     +7       ,7???  77    I7 :7     :7  7~   .?7 77    =7     7   ,77I   $+       7$ :$?       =$?          ')
print(' ,???????= :77777777777777777~     7=        ~7??  ~I77777  :7     :7  ,777777. 77    =7     7    77,  +$        .$::$?       =$?          ')
print(',???????  :7777777                                                                                77                                       ')
print(' =?????  ,7777777                                                                               77=                                        ')
print('   +?+  7777777?                                                                                                                           ')
print('    +  ~7777777                                                                                                                            ')
print('       I777777                                                                                                                             ')
print('          :~                                                                                                                               ')
	 

alchemyapi = AlchemyAPI()

print('')
print('')
print('############################################')
print('#   Entity Extraction Example              #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.entities('text',demo_text, { 'sentiment':1 })

if response['status'] == 'OK':
	print('## Response Object ##')
	print(json.dumps(response, indent=4))


	print('')
	print('## Entities ##')
	for entity in response['entities']:
		print('text: ', entity['text'])
		print('type: ', entity['type'])
		print('relevance: ', entity['relevance'])
		print('sentiment: ', entity['sentiment']['type'] + ' (' + entity['sentiment']['score'] + ')')
		print('')
else:
	print('Error in entity extraction call: ', response['statusInfo'])



print('')
print('')
print('')
print('############################################')
print('#   Sentiment Analysis Example             #')
print('############################################')
print('')
print('')

print('Processing html: ', demo_html)
print('')

response = alchemyapi.sentiment('html',demo_html)

if response['status'] == 'OK':
	print('## Response Object ##')
	print(json.dumps(response, indent=4))

	print('')
	print('## Document Sentiment ##')
	print('type: ', response['docSentiment']['type'])
	print('score: ', response['docSentiment']['score'])
else:
	print('Error in sentiment analysis call: ', response['statusInfo'])



print('')
print('')
print('')
print('############################################')
print('#   Keyword Extraction Example             #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.keywords('text',demo_text, { 'sentiment':1 })

if response['status'] == 'OK':
	print('## Response Object ##')
	print(json.dumps(response, indent=4))


	print('')
	print('## Keywords ##')
	for keyword in response['keywords']:
		print('text: ', keyword['text'])
		print('relevance: ', keyword['relevance'])
		print('sentiment: ', keyword['sentiment']['type'] + ' (' + keyword['sentiment']['score'] + ')')
		print('')
else:
	print('Error in keyword extaction call: ', response['statusInfo'])



print('')
print('')
print('')
print('############################################')
print('#   Concept Tagging Example                #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.concepts('text',demo_text)

if response['status'] == 'OK':
	print('## Object ##')
	print(json.dumps(response, indent=4))


	print('')
	print('## Concepts ##')
	for concept in response['concepts']:
		print('text: ', concept['text'])
		print('relevance: ', concept['relevance'])
		print('')
else:
	print('Error in concept tagging call: ', response['statusInfo'])



print('')
print('')
print('')
print('############################################')
print('#   Relation Extraction Example            #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.relations('text',demo_text)

if response['status'] == 'OK':
	print('## Object ##')
	print(json.dumps(response, indent=4))


	print('')
	print('## Relations ##')
	for relation in response['relations']:
		if 'subject' in relation:
			print('Subject: ', relation['subject']['text'] )
		
		if 'action' in relation:
			print('Action: ', relation['action']['text'])
		
		if 'object' in relation:
			print('Object: ', relation['object']['text'])
		
		print('')
else:
	print('Error in relation extaction call: ', response['statusInfo'])



print('')
print('')
print('')
print('############################################')
print('#   Text Categorization Example            #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.category('text',demo_text)

if response['status'] == 'OK':
	print('## Response Object ##')
	print(json.dumps(response, indent=4))


	print('')
	print('## Category ##')
	print('text: ', response['category'])
	print('score: ', response['score'])
	print('')
else:
	print('Error in text categorization call: ', response['statusInfo'])



print('')
print('')
print('')
print('############################################')
print('#   Language Detection Example             #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.language('text',demo_text)

if response['status'] == 'OK':
	print('## Response Object ##')
	print(json.dumps(response, indent=4))


	print('')
	print('## Language ##')
	print('language: ', response['language'])
	print('iso-639-1: ', response['iso-639-1'])
	print('native speakers: ', response['native-speakers'])
	print('')
else:
	print('Error in language detection call: ', response['statusInfo'])



print('')
print('')
print('')
print('############################################')
print('#   Author Extraction Example              #')
print('############################################')
print('')
print('')

print('Processing url: ', demo_url)
print('')

response = alchemyapi.author('url',demo_url)

if response['status'] == 'OK':
	print('## Response Object ##')
	print(json.dumps(response, indent=4))

	print('')
	print('## Author ##')
	print('author: ', response['author'])
	print('')
else:
	print('Error in author extraction call: ', response['statusInfo'])



print('')
print('')
print('')
print('############################################')
print('#   Feed Detection Example                 #')
print('############################################')
print('')
print('')

print('Processing url: ', demo_url)
print('')

response = alchemyapi.feeds('url',demo_url)

if response['status'] == 'OK':
	print('## Response Object ##')
	print(json.dumps(response, indent=4))

	print('')
	print('## Feeds ##')
	for feed in response['feeds']:
		print('feed: ', feed['feed'])
else:
	print('Error in feed detection call: ', response['statusInfo'])

print('')
print('')

