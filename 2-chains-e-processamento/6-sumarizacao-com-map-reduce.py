from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
import json
from dotenv import load_dotenv
load_dotenv()

def format_as_json(result):
    return {
        "output_text": result["output_text"],
        "input_documents": [
            {
                "page_content": doc.page_content,
                "metadata": doc.metadata
            }
            for doc in result["input_documents"]
        ]
    }


long_text = """
Dawn threads a pale gold through the alley of glass.
The city yawns in a chorus of brakes and distant sirens.
Windows blink awake, one by one, like sleepy eyes.
Streetcloth of steam curls from manholes, a quiet river.
Coffee steam spirals above a newspaper's pale print.
Pedestrians sketch light on sidewalks, hurried, loud with umbrellas.
Buses swallow the morning with their loud yawns.
A sparrow perches on a steel beam, surveying the grid.
The subway sighs somewhere underground, a heartbeat rising.
Neon still glows in the corners where night refused to retire.
A cyclist cuts through the chorus, bright with chrome and momentum.
The city clears its throat, the air turning a little less electric.
Shoes hiss on concrete, a thousand small verbs of arriving.
Dawn keeps its promises in the quiet rhythm of a waking metropolis.
The morning light cascades through towering windows of steel and glass,
casting geometric shadows on busy streets below.
Traffic flows like rivers of metal and light,
while pedestrians weave through crosswalks with purpose.
Coffee shops exhale warmth and the aroma of fresh bread,
as commuters clutch their cups like talismans against the cold.
Street vendors call out in a symphony of languages,
their voices mixing with the distant hum of construction.
Pigeons dance between the feet of hurried workers,
finding crumbs of breakfast pastries on concrete sidewalks.
The city breathes in rhythm with a million heartbeats,
each person carrying dreams and deadlines in equal measure.
Skyscrapers reach toward clouds that drift like cotton,
while far below, subway trains rumble through tunnels.
This urban orchestra plays from dawn until dusk,
a endless song of ambition, struggle, and hope.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=250, chunk_overlap=70,
)

parts = splitter.create_documents([long_text])

# for part in parts:
#     print(part.page_content)
#     print("-"*30)

llm = ChatOpenAI(model="gpt-5-nano", temperature=0)

chain_sumarize = load_summarize_chain(llm, chain_type="map_reduce", verbose=False)

result = chain_sumarize.invoke({"input_documents": parts})
print(json.dumps(format_as_json(result), indent=2, ensure_ascii=False))

"""
Result:
{'input_documents': [Document(metadata={}, page_content='Dawn threads a pale gold through the alley of glass.\nThe city yawns in a chorus of brakes and distant sirens.\nWindows blink awake, one by one, like sleepy eyes.\nStreetcloth of steam curls from manholes, a quiet river.'), Document(metadata={}, page_content="Streetcloth of steam curls from manholes, a quiet river.\nCoffee steam spirals above a newspaper's pale print.\nPedestrians sketch light on sidewalks, hurried, loud with umbrellas.\nBuses swallow the morning with their loud yawns."), Document(metadata={}, page_content='Buses swallow the morning with their loud yawns.\nA sparrow perches on a steel beam, surveying the grid.\nThe subway sighs somewhere underground, a heartbeat rising.\nNeon still glows in the corners where night refused to retire.'), Document(metadata={}, page_content='Neon still glows in the corners where night refused to retire.\nA cyclist cuts through the chorus, bright with chrome and momentum.\nThe city clears its throat, the air turning a little less electric.'), Document(metadata={}, page_content='The city clears its throat, the air turning a little less electric.\nShoes hiss on concrete, a thousand small verbs of arriving.\nDawn keeps its promises in the quiet rhythm of a waking metropolis.'), Document(metadata={}, page_content='Dawn keeps its promises in the quiet rhythm of a waking metropolis.\nThe morning light cascades through towering windows of steel and glass,\ncasting geometric shadows on busy streets below.\nTraffic flows like rivers of metal and light,'), Documescades through towering windows of steel and glass,\ncasting geometric shadows on busy streets below.\nTraffic flows like rivers of metal and light,'), Document(metadata={}, page_content='Traffic flows like rivers of metal and light,\nwhile pedestrians weave through crosswalks with purpose.\nCoffee shops exhale warmth and the aroma of fresh bread,\nas commuters clutch their cups like talismans against the cold.'), Document(metadata={}, page_content='as commuters clutch their cups like talismans against the cold.\nStreet vendors call out in a symphony of languages,\ntheir voices mixing with the distant hum of construction.\nPigeons dance between the feet of hurried workers,'), Document(metadata={}, page_content='Pigeons dance between the feet of hurried workers,\nfinding crumbs of breakfast pastries on concrete sidewalks.\nThe city breathes in rhythm with a million heartbeats,\neach person carrying dreams and deadlines in equal measure.'), Document(metadata={}, page_content='each person carrying dreams and deadlines in equal measure.\nSkyscrapers reach toward clouds that drift like cotton,\nwhile far below, subway trains rumble through tunnels.\nThis urban orchestra plays from dawn until dusk,'), Document(metadata={}, page_content='This urban orchestra plays from dawn until dusk,\na endless song of ambition, struggle, and hope.')], 'output_text': 'From dawn to dusk, the city wakes in a continuous rhythm: steam rises from manholes and neon glows over glass towers as buses, subways, and pedestrians fill the streets. Vendors, cyclists, and pigeons weave through a cold, coffee-warm urban landscape where dreams crush against deadlines in a nonstop symphony of ambition, struggle, and hope.'}

(Readable)
input: Dawn threads a pale gold through the alley of glass.\nThe city yawns in a chorus of brakes and distant sirens.\nWindows blink awake, one by one, like sleepy eyes.\nStreetcloth of steam curls from manholes, a quiet river.'
input: Streetcloth of steam curls from manholes, a quiet river.\nCoffee steam spirals above a newspaper's pale print.\nPedestrians sketch light on sidewalks, hurried, loud with umbrellas.\nBuses swallow the morning with their loud yawns."
input: Buses swallow the morning with their loud yawns.\nA sparrow perches on a steel beam, surveying the grid.\nThe subway sighs somewhere underground, a heartbeat rising.\nNeon still glows in the corners where night refused to retire.'
input: Neon still glows in the corners where night refused to retire.\nA cyclist cuts through the chorus, bright with chrome and momentum.\nThe city clears its throat, the air turning a little less electric.'
input: The city clears its throat, the air turning a little less electric.\nShoes hiss on concrete, a thousand small verbs of arriving.\nDawn keeps its promises in the quiet rhythm of a waking metropolis.'
input: Dawn keeps its promises in the quiet rhythm of a waking metropolis.\nThe morning light cascades through towering windows of steel and glass,\ncasting geometric shadows on busy streets below.\nTraffic flows like rivers of metal and light,'
input: Traffic flows like rivers of metal and light,\nwhile pedestrians weave through crosswalks with purpose.\nCoffee shops exhale warmth and the aroma of fresh bread,\nas commuters clutch their cups like talismans against the cold.'
input: as commuters clutch their cups like talismans against the cold.\nStreet vendors call out in a symphony of languages,\ntheir voices mixing with the distant hum of construction.\nPigeons dance between the feet of hurried workers,'
input: Pigeons dance between the feet of hurried workers,\nfinding crumbs of breakfast pastries on concrete sidewalks.\nThe city breathes in rhythm with a million heartbeats,\neach person carrying dreams and deadlines in equal measure.'
input: each person carrying dreams and deadlines in equal measure.\nSkyscrapers reach toward clouds that drift like cotton,\nwhile far below, subway trains rumble through tunnels.\nThis urban orchestra plays from dawn until dusk,'
input: This urban orchestra plays from dawn until dusk,\na endless song of ambition, struggle, and hope.'

output: From dawn to dusk, the city wakes in a continuous rhythm: steam rises from manholes and neon glows over glass towers as buses, subways, and pedestrians fill the streets. Vendors, cyclists, and pigeons weave through a cold, coffee-warm urban landscape where dreams crush against deadlines in a nonstop symphony of ambition, struggle, and hope.
"""
