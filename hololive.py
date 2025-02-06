import streamlit as st
from Vertex import Vertex
from Graph import Graph

holo = {
    "Generation 0": ['Hoshimachi Suisei', 'Sakura Miko', 'AZKi', 'Tokino Sora', 'Robocosan'],
    "Generation 1": ['Aki Rosenthal', 'Akai Haato', 'Natsuiro Matsuri'],
    "Generation 2": ['Murasaki Shion', 'Nakiri Ayame', 'Yuzuki Choco', 'Ōzora Subaru',],
    "GAMERS": ["Shirakami Fubuki", "Ōkami Mio", "Nekomata Okayu", "Inugami Korone"],
    "Generation 3": ['Usada Pekora', 'Shiranui Flare', 'Shirogane Noel', 'Houshou Marine'],
    "Generation 4": ['Amane Kanata', 'Tsunomaki Watame', 'Tokoyami Towa', 'Himemori Luna'],
    "Generation 5": ['Yukihana Lamy', 'Momosuzu Nene', "Shishiro Botan", 'Omaru Polka'],
    "holoX": ['La+ Darknesss', "Takane Lui", "Hakui Koyori", "Kazama Iroha"],
    "AREA15": ['Ayunda Risu', 'Moona Hoshinova', 'Airani Iofifteen'],
    "holoro": ["Kureiji Ollie", 'Anya Melfissa', 'Pavolia Reine'],
    'holoh3ro': ['Vestia Zeta', 'Kaela Kovalskia', 'Kobo Kanaeru'],
    'Myth': ['Mori Calliope', 'Takanashi Kiara', "Ninomae Ina'nis", 'Gawr Gura'],
    'Promise': ['IRyS', 'Ouro Kronii', 'Nanashi Mumei', "Hakos Baelz"],
    'Advent': ['Shiori Novella', "Koseki Bijou", 'Nerissa Ravencroft', 'Fuwawa and Mococo Abyssgard'],
    'Justice': ['Elizabeth Rose Bloodflame', 'Cecilia Immergreen', 'Raora Panthera', 'Gigi Murin'],
    'ReGLOSS': ['Hiodoshi Ao', 'Otonose Kanade', 'Ichijou Ririka', 'Juufuutei Raden', 'Todoroki Hajime'],
    'FLOW GLOW': ['Isaki Riona', 'Koganei Niko', 'Mizumiya Su', 'Rindo Chihaya', 'Kikirara Vivi']
}
