import sqlite3
import time
from datetime import datetime


def bot_fala(texto, delay=0.03):
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def criar_banco():
    conexao = sqlite3.connect("academia.db")
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS historico (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            nivel TEXT,
            objetivo TEXT,
            data_treino TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exercicios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nivel TEXT,
            objetivo TEXT,
            grupo TEXT,
            nome_exercicio TEXT
        )
    ''')

    # Verificar se já existem exercícios cadastrados
    cursor.execute("SELECT COUNT(*) FROM exercicios")
    count = cursor.fetchone()[0]

    # Se não houver exercícios, adicionar a lista padrão
    if count == 0:
        exercicios_padrao = [
            # INICIANTE - HIPERTROFIA
            ("iniciante", "hipertrofia", "A", "Supino reto com halteres - 3x12"),
            ("iniciante", "hipertrofia", "A", "Crucifixo inclinado - 3x12"),
            ("iniciante", "hipertrofia", "A", "Desenvolvimento com halteres - 3x12"),
            ("iniciante", "hipertrofia", "A", "Elevacao lateral - 3x15"),
            ("iniciante", "hipertrofia", "A", "Elevacao frontal - 3x12"),
            ("iniciante", "hipertrofia", "A", "Triceps pulley - 3x15"),
            ("iniciante", "hipertrofia", "A", "Triceps coice - 3x12"),
            ("iniciante", "hipertrofia", "A", "Flexao de bracos - 3x10"),

            ("iniciante", "hipertrofia", "B", "Agachamento livre - 3x12"),
            ("iniciante", "hipertrofia", "B", "Leg press 45 graus - 3x12"),
            ("iniciante", "hipertrofia", "B", "Cadeira extensora - 3x15"),
            ("iniciante", "hipertrofia", "B", "Cadeira flexora - 3x15"),
            ("iniciante", "hipertrofia", "B", "Afundo - 3x10 cada"),
            ("iniciante", "hipertrofia", "B", "Cadeira abdutora - 3x15"),
            ("iniciante", "hipertrofia", "B", "Cadeira adutora - 3x15"),
            ("iniciante", "hipertrofia", "B", "Panturrilha no leg - 4x20"),
            ("iniciante", "hipertrofia", "B", "Agachamento sumô - 3x12"),

            ("iniciante", "hipertrofia", "C", "Puxada frontal - 3x12"),
            ("iniciante", "hipertrofia", "C", "Remada curvada - 3x12"),
            ("iniciante", "hipertrofia", "C", "Remada baixa - 3x12"),
            ("iniciante", "hipertrofia", "C", "Pullover - 3x12"),
            ("iniciante", "hipertrofia", "C", "Encolhimento de ombros - 3x15"),
            ("iniciante", "hipertrofia", "C", "Rosca direta - 3x12"),
            ("iniciante", "hipertrofia", "C", "Rosca martelo - 3x12"),
            ("iniciante", "hipertrofia", "C", "Rosca concentrada - 3x12"),
            ("iniciante", "hipertrofia", "C", "Abdominal supra - 3x15"),

            # INICIANTE - EMAGRECIMENTO
            ("iniciante", "emagrecimento", "A", "Burpees - 3x10"),
            ("iniciante", "emagrecimento", "A", "Jumping jacks - 3x30 seg"),
            ("iniciante", "emagrecimento", "A", "Flexao de bracos - 3x10"),
            ("iniciante", "emagrecimento", "A", "Mountain climbers - 3x20"),
            ("iniciante", "emagrecimento", "A", "Prancha - 3x30 seg"),
            ("iniciante", "emagrecimento", "A", "Polichinelos - 3x30"),
            ("iniciante", "emagrecimento", "A", "High knees - 3x30 seg"),
            ("iniciante", "emagrecimento", "A", "Skipping - 3x30 seg"),

            ("iniciante", "emagrecimento", "B", "Agachamento - 4x15"),
            ("iniciante", "emagrecimento", "B", "Afundo alternado - 3x12 cada"),
            ("iniciante", "emagrecimento", "B", "Stiff - 3x15"),
            ("iniciante", "emagrecimento", "B", "Agachamento sumô - 3x15"),
            ("iniciante", "emagrecimento", "B", "Elevacao pelvica - 3x15"),
            ("iniciante", "emagrecimento", "B", "Panturrilha em pe - 4x20"),
            ("iniciante", "emagrecimento", "B", "Abdominal bicicleta - 3x20"),
            ("iniciante", "emagrecimento", "B", "Abdominal canivete - 3x15"),

            ("iniciante", "emagrecimento", "C", "Corrida esteira - 20 min"),
            ("iniciante", "emagrecimento", "C", "Polichinelos - 3x30"),
            ("iniciante", "emagrecimento", "C", "Pular corda - 3x1 min"),
            ("iniciante", "emagrecimento", "C", "Abdominal remador - 3x15"),
            ("iniciante", "emagrecimento", "C", "Prancha lateral - 3x30 seg cada"),
            ("iniciante", "emagrecimento", "C", "Bike ergometrica - 15 min"),
            ("iniciante", "emagrecimento", "C", "Step basico - 15 min"),
            ("iniciante", "emagrecimento", "C", "Caminhada inclinada - 15 min"),

            # INICIANTE - RESISTENCIA
            ("iniciante", "resistencia", "A", "Corrida leve - 25 min"),
            ("iniciante", "resistencia", "A", "Flexao de bracos - 3x15"),
            ("iniciante", "resistencia", "A", "Abdominal supra - 3x20"),
            ("iniciante", "resistencia", "A", "Prancha frontal - 3x40 seg"),
            ("iniciante", "resistencia", "A", "Burpees leves - 3x8"),
            ("iniciante", "resistencia", "A", "Polichinelos - 3x40"),
            ("iniciante", "resistencia", "A", "Alongamento - 10 min"),

            ("iniciante", "resistencia", "B", "Bike ergometrica - 30 min"),
            ("iniciante", "resistencia", "B", "Agachamento livre - 4x20"),
            ("iniciante", "resistencia", "B", "Afundo - 3x15 cada"),
            ("iniciante", "resistencia", "B", "Stiff - 3x15"),
            ("iniciante", "resistencia", "B", "Elevacao pelvica - 3x20"),
            ("iniciante", "resistencia", "B", "Panturrilha - 4x25"),
            ("iniciante", "resistencia", "B", "Alongamento MMII - 10 min"),

            ("iniciante", "resistencia", "C", "Natacao ou remo - 20 min"),
            ("iniciante", "resistencia", "C", "Puxada frontal - 3x20"),
            ("iniciante", "resistencia", "C", "Remada baixa - 3x20"),
            ("iniciante", "resistencia", "C", "Desenvolvimento - 3x15"),
            ("iniciante", "resistencia", "C", "Elevacao lateral - 3x15"),
            ("iniciante", "resistencia", "C", "Prancha lateral - 3x30 seg cada"),
            ("iniciante", "resistencia", "C", "Abdominal infra - 3x20"),
            ("iniciante", "resistencia", "C", "Caminhada rapida - 15 min"),

            # INTERMEDIARIO - HIPERTROFIA
            ("intermediario", "hipertrofia", "A", "Supino reto - 4x10"),
            ("intermediario", "hipertrofia", "A", "Supino inclinado - 4x10"),
            ("intermediario", "hipertrofia", "A", "Supino declinado - 3x12"),
            ("intermediario", "hipertrofia", "A", "Crucifixo - 3x12"),
            ("intermediario", "hipertrofia", "A", "Crucifixo inclinado - 3x12"),
            ("intermediario", "hipertrofia", "A", "Desenvolvimento militar - 4x10"),
            ("intermediario", "hipertrofia", "A", "Desenvolvimento Arnold - 3x12"),
            ("intermediario", "hipertrofia", "A", "Elevacao lateral - 3x12"),
            ("intermediario", "hipertrofia", "A", "Elevacao frontal - 3x12"),
            ("intermediario", "hipertrofia", "A", "Elevacao posterior - 3x15"),
            ("intermediario", "hipertrofia", "A", "Triceps testa - 3x12"),
            ("intermediario", "hipertrofia", "A", "Triceps corda - 3x12"),
            ("intermediario", "hipertrofia", "A", "Triceps frances - 3x12"),
            ("intermediario", "hipertrofia", "A", "Flexao diamante - 3x10"),

            ("intermediario", "hipertrofia", "B", "Agachamento livre - 4x10"),
            ("intermediario", "hipertrofia", "B", "Agachamento frontal - 4x12"),
            ("intermediario", "hipertrofia", "B", "Agachamento sumô - 4x12"),
            ("intermediario", "hipertrofia", "B", "Agachamento bulgaro - 3x10 cada"),
            ("intermediario", "hipertrofia", "B", "Leg press - 4x12"),
            ("intermediario", "hipertrofia", "B", "Hack machine - 4x12"),
            ("intermediario", "hipertrofia", "B", "Cadeira extensora - 3x15"),
            ("intermediario", "hipertrofia", "B", "Mesa flexora - 4x12"),
            ("intermediario", "hipertrofia", "B", "Stiff - 4x12"),
            ("intermediario", "hipertrofia", "B", "Cadeira abdutora - 3x15"),
            ("intermediario", "hipertrofia", "B", "Cadeira adutora - 3x15"),
            ("intermediario", "hipertrofia", "B", "Afundo caminhando - 3x12 cada"),
            ("intermediario", "hipertrofia", "B", "Panturrilha sentado - 4x15"),
            ("intermediario", "hipertrofia", "B", "Panturrilha em pe - 4x15"),

            ("intermediario", "hipertrofia", "C", "Barra fixa - 4x max"),
            ("intermediario", "hipertrofia", "C", "Puxada frontal - 4x10"),
            ("intermediario", "hipertrofia", "C", "Puxada triangulo - 4x12"),
            ("intermediario", "hipertrofia", "C", "Puxada supinada - 3x12"),
            ("intermediario", "hipertrofia", "C", "Remada curvada - 4x10"),
            ("intermediario", "hipertrofia", "C", "Remada cavalinho - 3x12"),
            ("intermediario", "hipertrofia", "C", "Remada unilateral - 3x12 cada"),
            ("intermediario", "hipertrofia", "C", "Remada baixa - 4x12"),
            ("intermediario", "hipertrofia", "C", "Pullover - 3x12"),
            ("intermediario", "hipertrofia", "C", "Encolhimento de ombros - 4x15"),
            ("intermediario", "hipertrofia", "C", "Rosca direta - 4x10"),
            ("intermediario", "hipertrofia", "C", "Rosca alternada - 3x12"),
            ("intermediario", "hipertrofia", "C", "Rosca scott - 3x12"),
            ("intermediario", "hipertrofia", "C", "Rosca martelo - 3x12"),
            ("intermediario", "hipertrofia", "C", "Rosca concentrada - 3x12"),

            # INTERMEDIARIO - EMAGRECIMENTO
            ("intermediario", "emagrecimento", "A", "Burpees - 4x15"),
            ("intermediario", "emagrecimento", "A", "Flexao com palmas - 4x10"),
            ("intermediario", "emagrecimento", "A", "Mountain climbers - 4x30"),
            ("intermediario", "emagrecimento", "A", "Prancha dinamica - 3x45 seg"),
            ("intermediario", "emagrecimento", "A", "High knees - 4x40 seg"),
            ("intermediario", "emagrecimento", "A", "Jumping jacks - 4x45 seg"),
            ("intermediario", "emagrecimento", "A", "Skater jumps - 3x20"),
            ("intermediario", "emagrecimento", "A", "Corrida alta intensidade - 15 min"),

            ("intermediario", "emagrecimento", "B", "Agachamento jump - 4x15"),
            ("intermediario", "emagrecimento", "B", "Afundo com salto - 3x12 cada"),
            ("intermediario", "emagrecimento", "B", "Stiff - 4x15"),
            ("intermediario", "emagrecimento", "B", "Swing kettlebell - 4x20"),
            ("intermediario", "emagrecimento", "B", "Box jump - 3x12"),
            ("intermediario", "emagrecimento", "B", "Agachamento pistol - 3x8 cada"),
            ("intermediario", "emagrecimento", "B", "Wall ball - 4x15"),
            ("intermediario", "emagrecimento", "B", "Farmer walk - 3x50m"),

            ("intermediario", "emagrecimento", "C", "HIIT esteira - 20 min"),
            ("intermediario", "emagrecimento", "C", "Bike sprint - 15 min"),
            ("intermediario", "emagrecimento", "C", "Pular corda - 5x2 min"),
            ("intermediario", "emagrecimento", "C", "Abdominal complexo - 4x20"),
            ("intermediario", "emagrecimento", "C", "Prancha spider - 3x15 cada"),
            ("intermediario", "emagrecimento", "C", "Battle rope - 4x45 seg"),
            ("intermediario", "emagrecimento", "C", "Sled push - 4x20m"),
            ("intermediario", "emagrecimento", "C", "Circuito funcional - 20 min"),

            # INTERMEDIARIO - RESISTENCIA
            ("intermediario", "resistencia", "A", "Corrida moderada - 35 min"),
            ("intermediario", "resistencia", "A", "Circuito de forca - 3 series"),
            ("intermediario", "resistencia", "A", "Prancha com variacao - 4x1 min"),
            ("intermediario", "resistencia", "A", "Abdominal infra - 4x20"),
            ("intermediario", "resistencia", "A", "Burpees - 4x12"),
            ("intermediario", "resistencia", "A", "Flexao de bracos - 4x20"),
            ("intermediario", "resistencia", "A", "Mountain climbers - 4x30"),
            ("intermediario", "resistencia", "A", "Alongamento completo - 15 min"),

            ("intermediario", "resistencia", "B", "Bike longa distancia - 45 min"),
            ("intermediario", "resistencia", "B", "Agachamento - 4x25"),
            ("intermediario", "resistencia", "B", "Afundo caminhando - 3x20 cada"),
            ("intermediario", "resistencia", "B", "Step up - 4x15 cada"),
            ("intermediario", "resistencia", "B", "Stiff - 4x20"),
            ("intermediario", "resistencia", "B", "Wall sit - 4x1 min"),
            ("intermediario", "resistencia", "B", "Elevacao pelvica - 4x25"),
            ("intermediario", "resistencia", "B", "Panturrilha - 5x30"),

            ("intermediario", "resistencia", "C", "Natacao continua - 30 min"),
            ("intermediario", "resistencia", "C", "Remada na maquina - 4x25"),
            ("intermediario", "resistencia", "C", "Puxada frontal - 4x20"),
            ("intermediario", "resistencia", "C", "Desenvolvimento - 4x20"),
            ("intermediario", "resistencia", "C", "Elevacao lateral - 4x20"),
            ("intermediario", "resistencia", "C", "Prancha lateral - 4x45 seg cada"),
            ("intermediario", "resistencia", "C", "Circuito core - 20 min"),
            ("intermediario", "resistencia", "C", "Caminhada inclinada - 20 min"),

            # AVANCADO - HIPERTROFIA
            ("avancado", "hipertrofia", "A", "Supino reto - 5x8"),
            ("avancado", "hipertrofia", "A", "Supino inclinado - 4x8"),
            ("avancado", "hipertrofia", "A", "Supino declinado - 4x10"),
            ("avancado", "hipertrofia", "A", "Supino guilhotina - 3x12"),
            ("avancado", "hipertrofia", "A", "Crucifixo inclinado - 4x12"),
            ("avancado", "hipertrofia", "A", "Crucifixo na polia - 3x15"),
            ("avancado", "hipertrofia", "A", "Desenvolvimento militar - 4x8"),
            ("avancado", "hipertrofia", "A", "Desenvolvimento Arnold - 4x10"),
            ("avancado", "hipertrofia", "A", "Desenvolvimento com pegada neutra - 3x12"),
            ("avancado", "hipertrofia", "A", "Elevacao lateral - 4x12"),
            ("avancado", "hipertrofia", "A", "Elevacao frontal - 3x12"),
            ("avancado", "hipertrofia", "A", "Elevacao posterior - 4x15"),
            ("avancado", "hipertrofia", "A", "Remada alta - 3x12"),
            ("avancado", "hipertrofia", "A", "Triceps testa - 4x10"),
            ("avancado", "hipertrofia", "A", "Triceps frances - 4x12"),
            ("avancado", "hipertrofia", "A", "Triceps mergulho - 3x max"),
            ("avancado", "hipertrofia", "A", "Triceps coice - 3x15"),
            ("avancado", "hipertrofia", "A", "Triceps polia invertida - 3x12"),

            ("avancado", "hipertrofia", "B", "Agachamento livre - 5x8"),
            ("avancado", "hipertrofia", "B", "Agachamento frontal - 4x10"),
            ("avancado", "hipertrofia", "B", "Agachamento sumô - 4x12"),
            ("avancado", "hipertrofia", "B", "Agachamento bulgaro - 4x10 cada"),
            ("avancado", "hipertrofia", "B", "Hack machine - 4x10"),
            ("avancado", "hipertrofia", "B", "Leg press - 4x12"),
            ("avancado", "hipertrofia", "B", "Leg press unilateral - 3x12 cada"),
            ("avancado", "hipertrofia", "B", "Cadeira extensora - 4x15 (drop set)"),
            ("avancado", "hipertrofia", "B", "Mesa flexora - 4x12"),
            ("avancado", "hipertrofia", "B", "Flexora em pe - 3x15 cada"),
            ("avancado", "hipertrofia", "B", "Stiff - 4x10"),
            ("avancado", "hipertrofia", "B", "Stiff unilateral - 3x12 cada"),
            ("avancado", "hipertrofia", "B", "Afundo caminhando - 4x12 cada"),
            ("avancado", "hipertrofia", "B", "Afundo reverso - 3x15 cada"),
            ("avancado", "hipertrofia", "B", "Cadeira abdutora - 4x15"),
            ("avancado", "hipertrofia", "B", "Cadeira adutora - 4x15"),
            ("avancado", "hipertrofia", "B", "Elevacao pelvica com barra - 4x12"),
            ("avancado", "hipertrofia", "B", "Panturrilha em pe - 5x15"),
            ("avancado", "hipertrofia", "B", "Panturrilha sentado - 4x20"),
            ("avancado", "hipertrofia", "B", "Panturrilha no leg - 4x20"),

            ("avancado", "hipertrofia", "C", "Barra fixa pronada - 5x max"),
            ("avancado", "hipertrofia", "C", "Barra fixa supinada - 4x max"),
            ("avancado", "hipertrofia", "C", "Puxada frontal - 4x8"),
            ("avancado", "hipertrofia", "C", "Puxada triangulo - 4x10"),
            ("avancado", "hipertrofia", "C", "Puxada supinada - 4x10"),
            ("avancado", "hipertrofia", "C", "Puxada unilateral - 3x12 cada"),
            ("avancado", "hipertrofia", "C", "Remada curvada - 4x8"),
            ("avancado", "hipertrofia", "C", "Remada curvada supinada - 4x10"),
            ("avancado", "hipertrofia", "C", "Remada cavalinho - 4x10"),
            ("avancado", "hipertrofia", "C", "Remada unilateral - 3x12 cada"),
            ("avancado", "hipertrofia", "C", "Remada T - 4x10"),
            ("avancado", "hipertrofia", "C", "Remada serrote - 3x12 cada"),
            ("avancado", "hipertrofia", "C", "Pullover - 3x12"),
            ("avancado", "hipertrofia", "C", "Pullover na polia - 3x15"),
            ("avancado", "hipertrofia", "C", "Encolhimento de ombros - 4x15"),
            ("avancado", "hipertrofia", "C", "Encolhimento posterior - 3x15"),
            ("avancado", "hipertrofia", "C", "Rosca direta barra - 4x8"),
            ("avancado", "hipertrofia", "C", "Rosca direta barra W - 4x10"),
            ("avancado", "hipertrofia", "C", "Rosca alternada - 4x10"),
            ("avancado", "hipertrofia", "C", "Rosca scott - 3x12"),
            ("avancado", "hipertrofia", "C", "Rosca martelo - 3x12"),
            ("avancado", "hipertrofia", "C", "Rosca concentrada - 3x12"),
            ("avancado", "hipertrofia", "C", "Rosca invertida - 3x15"),
            ("avancado", "hipertrofia", "C", "Rosca 21 - 3x21"),

            # AVANCADO - EMAGRECIMENTO
            ("avancado", "emagrecimento", "A", "Burpees com flexao - 5x20"),
            ("avancado", "emagrecimento", "A", "Burpees com box jump - 4x15"),
            ("avancado", "emagrecimento", "A", "Thruster - 5x15"),
            ("avancado", "emagrecimento", "A", "Man makers - 4x12"),
            ("avancado", "emagrecimento", "A", "Box jump alto - 4x15"),
            ("avancado", "emagrecimento", "A", "Kettlebell snatch - 4x12 cada"),
            ("avancado", "emagrecimento", "A", "Kettlebell clean - 4x15 cada"),
            ("avancado", "emagrecimento", "A", "Prancha com peso - 4x1 min"),
            ("avancado", "emagrecimento", "A", "Devil press - 4x12"),
            ("avancado", "emagrecimento", "A", "HIIT avancado - 20 min"),

            ("avancado", "emagrecimento", "B", "Agachamento pistol - 4x10 cada"),
            ("avancado", "emagrecimento", "B", "Agachamento com salto - 5x15"),
            ("avancado", "emagrecimento", "B", "Afundo bulgaro com salto - 4x12 cada"),
            ("avancado", "emagrecimento", "B", "Swing pesado - 5x25"),
            ("avancado", "emagrecimento", "B", "Swing unilateral - 4x20 cada"),
            ("avancado", "emagrecimento", "B", "Leg press explosivo - 4x15"),
            ("avancado", "emagrecimento", "B", "Turkish get up - 3x8 cada"),
            ("avancado", "emagrecimento", "B", "Wall ball - 5x20"),
            ("avancado", "emagrecimento", "B", "Sled push pesado - 5x20m"),
            ("avancado", "emagrecimento", "B", "Corrida intervalada - 25 min"),

            ("avancado", "emagrecimento", "C", "Crossfit WOD - 30 min"),
            ("avancado", "emagrecimento", "C", "Complexo de barra - 5 rounds"),
            ("avancado", "emagrecimento", "C", "Battle rope - 5x1 min"),
            ("avancado", "emagrecimento", "C", "Battle rope alternado - 5x45 seg"),
            ("avancado", "emagrecimento", "C", "Bike Tabata - 20 min"),
            ("avancado", "emagrecimento", "C", "Remo Tabata - 20 min"),
            ("avancado", "emagrecimento", "C", "Rope climb - 5x subidas"),
            ("avancado", "emagrecimento", "C", "Muscle up - 5x max"),
            ("avancado", "emagrecimento", "C", "Circuito metabolico - 25 min"),

            # AVANCADO - RESISTENCIA
            ("avancado", "resistencia", "A", "Corrida longa - 50 min"),
            ("avancado", "resistencia", "A", "Corrida fartlek - 45 min"),
            ("avancado", "resistencia", "A", "Circuito forca resistencia - 4 series"),
            ("avancado", "resistencia", "A", "Prancha complexa - 5x1.5 min"),
            ("avancado", "resistencia", "A", "Prancha RKC - 5x1 min"),
            ("avancado", "resistencia", "A", "L-sit - 5x30 seg"),
            ("avancado", "resistencia", "A", "Core avancado - 25 min"),
            ("avancado", "resistencia", "A", "Hollow body hold - 5x45 seg"),
            ("avancado", "resistencia", "A", "Alongamento profundo - 20 min"),

            ("avancado", "resistencia", "B", "Bike resistencia - 60 min"),
            ("avancado", "resistencia", "B", "Bike intervalada longa - 50 min"),
            ("avancado", "resistencia", "B", "Agachamento alta repeticao - 5x30"),
            ("avancado", "resistencia", "B", "Agachamento isometrico - 5x1 min"),
            ("avancado", "resistencia", "B", "Afundo caminhando - 4x25 cada"),
            ("avancado", "resistencia", "B", "Step up com peso - 4x20 cada"),
            ("avancado", "resistencia", "B", "Wall sit - 5x2 min"),
            ("avancado", "resistencia", "B", "Pistol squat - 4x15 cada"),
            ("avancado", "resistencia", "B", "Jumping lunges - 4x20 cada"),
            ("avancado", "resistencia", "B", "Circuito MMII - 30 min"),

            ("avancado", "resistencia", "C", "Natacao longa distancia - 45 min"),
            ("avancado", "resistencia", "C", "Natacao intervalada - 40 min"),
            ("avancado", "resistencia", "C", "Remada ergometro - 5000m"),
            ("avancado", "resistencia", "C", "Remada intervalada - 4000m"),
            ("avancado", "resistencia", "C", "Barra fixa alta repeticao - 5x20"),
            ("avancado", "resistencia", "C", "Puxada frontal - 5x25"),
            ("avancado", "resistencia", "C", "Circuito tronco - 30 min"),
            ("avancado", "resistencia", "C", "Treino funcional - 35 min"),
            ("avancado", "resistencia", "C", "Crossfit Cindy - 20 min"),
            ("avancado", "resistencia", "C", "Yoga ou pilates - 30 min"),

            # INICIANTE - CARDIO
            ("iniciante", "cardio", "A", "Caminhada rapida - 30 min"),
            ("iniciante", "cardio", "A", "Bike leve - 25 min"),
            ("iniciante", "cardio", "A", "Eliptico - 20 min"),
            ("iniciante", "cardio", "A", "Polichinelos - 3x30 seg"),
            ("iniciante", "cardio", "A", "Alongamento - 10 min"),

            ("iniciante", "cardio", "B", "Corrida leve - 20 min"),
            ("iniciante", "cardio", "B", "Transport - 15 min"),
            ("iniciante", "cardio", "B", "Pular corda - 3x1 min"),
            ("iniciante", "cardio", "B", "Step basico - 20 min"),
            ("iniciante", "cardio", "B", "Caminhada inclinada - 15 min"),

            ("iniciante", "cardio", "C", "Natacao livre - 20 min"),
            ("iniciante", "cardio", "C", "Hidroginastica - 30 min"),
            ("iniciante", "cardio", "C", "Danca aerobica - 25 min"),
            ("iniciante", "cardio", "C", "Remada ergometro - 15 min"),
            ("iniciante", "cardio", "C", "Caminhada ao ar livre - 30 min"),

            # INTERMEDIARIO - CARDIO
            ("intermediario", "cardio", "A", "Corrida moderada - 35 min"),
            ("intermediario", "cardio", "A", "Bike HIIT - 25 min"),
            ("intermediario", "cardio", "A", "Eliptico intervalado - 30 min"),
            ("intermediario", "cardio", "A", "Pular corda avancado - 5x2 min"),
            ("intermediario", "cardio", "A", "Circuito aerobico - 20 min"),

            ("intermediario", "cardio", "B", "Corrida intervalada - 30 min"),
            ("intermediario", "cardio", "B", "Transport inclinado - 25 min"),
            ("intermediario", "cardio", "B", "Bike spinning - 35 min"),
            ("intermediario", "cardio", "B", "Step coreografado - 30 min"),
            ("intermediario", "cardio", "B", "Box cardio - 20 min"),

            ("intermediario", "cardio", "C", "Natacao crawl - 30 min"),
            ("intermediario", "cardio", "C", "Circuito aquatico - 35 min"),
            ("intermediario", "cardio", "C", "Zumba - 40 min"),
            ("intermediario", "cardio", "C", "Remada 3000m - 20 min"),
            ("intermediario", "cardio", "C", "Trekking - 45 min"),

            # AVANCADO - CARDIO
            ("avancado", "cardio", "A", "Corrida intensa - 45 min"),
            ("avancado", "cardio", "A", "Bike Tabata - 30 min"),
            ("avancado", "cardio", "A", "HIIT extremo - 25 min"),
            ("avancado", "cardio", "A", "Burpees cardio - 5x20"),
            ("avancado", "cardio", "A", "Escadaria - 30 min"),
            ("avancado", "cardio", "A", "Battle rope cardio - 6x1 min"),

            ("avancado", "cardio", "B", "Corrida de velocidade - 40 min"),
            ("avancado", "cardio", "B", "Transport sprint - 35 min"),
            ("avancado", "cardio", "B", "Spinning avancado - 45 min"),
            ("avancado", "cardio", "B", "Crossfit cardio WOD - 30 min"),
            ("avancado", "cardio", "B", "Box jump cardio - 25 min"),

            ("avancado", "cardio", "C", "Natacao competitiva - 45 min"),
            ("avancado", "cardio", "C", "Triatlon simulado - 60 min"),
            ("avancado", "cardio", "C", "Circuito metabolico - 40 min"),
            ("avancado", "cardio", "C", "Remada 5000m - 30 min"),
            ("avancado", "cardio", "C", "Trail running - 60 min"),
        ]

        cursor.executemany(
            "INSERT INTO exercicios (nivel, objetivo, grupo, nome_exercicio) VALUES (?, ?, ?, ?)",
            exercicios_padrao
        )
        print("Base de exercicios carregada com sucesso!")

    conexao.commit()
    conexao.close()


def mostrar_historico(nome):
    conexao = sqlite3.connect("academia.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT nivel, objetivo, data_treino FROM historico WHERE nome = ? ORDER BY id DESC LIMIT 3",
                   (nome,))
    historico = cursor.fetchall()
    conexao.close()

    if not historico:
        bot_fala("Você ainda não possui histórico de treinos.")
    else:
        bot_fala("\nÚltimos treinos registrados:")
        for nivel, objetivo, data in historico:
            bot_fala(f"- {data} | Nível: {nivel.capitalize()} | Objetivo: {objetivo.capitalize()}")


def adicionar_exercicio():
    bot_fala("\nVamos adicionar um novo exercício ao banco de dados!")
    nivel = input("Digite o nível (iniciante/intermediario/avancado): ").strip().lower()
    objetivo = input("Digite o objetivo (hipertrofia/emagrecimento/resistencia/cardio): ").strip().lower()
    grupo = input("Digite o grupo (A/B/C): ").strip().upper()
    nome_exercicio = input("Digite o nome do exercício e a série (ex: Supino reto - 3x10): ").strip()

    if nivel not in ["iniciante", "intermediario", "avancado"] or \
            objetivo not in ["hipertrofia", "emagrecimento", "resistencia", "cardio"] or \
            grupo not in ["A", "B", "C"]:
        bot_fala("Dados inválidos! Verifique se digitou corretamente.")
        return

    conexao = sqlite3.connect("academia.db")
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO exercicios (nivel, objetivo, grupo, nome_exercicio) VALUES (?, ?, ?, ?)",
        (nivel, objetivo, grupo, nome_exercicio)
    )
    conexao.commit()
    conexao.close()

    bot_fala("Exercício adicionado com sucesso ao banco de dados!")


def listar_exercicios():
    conexao = sqlite3.connect("academia.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nivel, objetivo, grupo, nome_exercicio FROM exercicios ORDER BY nivel, objetivo, grupo")
    exercicios = cursor.fetchall()
    conexao.close()

    if not exercicios:
        bot_fala("Nenhum exercício cadastrado ainda.")
        return

    bot_fala("\nLista de exercícios cadastrados:\n")
    for ex in exercicios:
        bot_fala(f"ID {ex[0]} | {ex[1].capitalize()} | {ex[2].capitalize()} | Grupo {ex[3]} | {ex[4]}")


def editar_exercicio():
    listar_exercicios()
    id_ex = input("\nDigite o ID do exercício que deseja editar: ").strip()

    conexao = sqlite3.connect("academia.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM exercicios WHERE id = ?", (id_ex,))
    exercicio = cursor.fetchone()

    if not exercicio:
        bot_fala("ID não encontrado.")
        conexao.close()
        return

    bot_fala(f"Editando: {exercicio[4]}")
    novo_nome = input("Novo nome do exercício (ou pressione ENTER para manter o mesmo): ").strip()
    if novo_nome == "":
        novo_nome = exercicio[4]

    cursor.execute("UPDATE exercicios SET nome_exercicio = ? WHERE id = ?", (novo_nome, id_ex))
    conexao.commit()
    conexao.close()

    bot_fala("Exercício atualizado com sucesso!")


def excluir_exercicio():
    listar_exercicios()
    id_ex = input("\nDigite o ID do exercício que deseja excluir: ").strip()

    conexao = sqlite3.connect("academia.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM exercicios WHERE id = ?", (id_ex,))
    exercicio = cursor.fetchone()

    if not exercicio:
        bot_fala("ID não encontrado.")
        conexao.close()
        return

    confirm = input(f"Tem certeza que deseja excluir '{exercicio[4]}'? (s/n): ").strip().lower()
    if confirm == "s":
        cursor.execute("DELETE FROM exercicios WHERE id = ?", (id_ex,))
        conexao.commit()
        bot_fala("Exercício excluído com sucesso!")
    else:
        bot_fala("Exclusão cancelada.")
    conexao.close()


def mostrar_treino(nome, nivel, objetivo):
    conexao = sqlite3.connect("academia.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT grupo, nome_exercicio FROM exercicios WHERE nivel = ? AND objetivo = ?", (nivel, objetivo))
    resultados = cursor.fetchall()
    conexao.close()

    if not resultados:
        bot_fala("Nenhum treino encontrado para essa combinação de nível e objetivo.")
        return

    planos = {}
    for grupo, exercicio in resultados:
        planos.setdefault(grupo, []).append(exercicio)

    bot_fala(f"\n{nome}, aqui está seu plano {nivel.capitalize()} focado em {objetivo.capitalize()}:\n")
    for grupo, exercicios in planos.items():
        bot_fala(f"--- Treino {grupo} ---")
        for ex in exercicios:
            bot_fala(f"- {ex}")
            time.sleep(0.2)
        print()

    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
    conexao = sqlite3.connect("academia.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO historico (nome, nivel, objetivo, data_treino) VALUES (?, ?, ?, ?)",
                   (nome, nivel, objetivo, data_atual))
    conexao.commit()
    conexao.close()

    bot_fala("Treino registrado no histórico com sucesso!")


def bot_academia():
    criar_banco()
    bot_fala("Olá! Eu sou o Aton_Bot-1.0, seu assistente de treinos inteligentes!")
    nome = input("Qual é o seu nome? ").strip().capitalize()

    while True:
        bot_fala(f"\nO que deseja fazer, {nome}?")
        bot_fala("1. Ver treino personalizado")
        bot_fala("2. Ver histórico de treinos")
        bot_fala("3. Gerenciar exercícios (adicionar, listar, editar, excluir)")
        bot_fala("4. Sair")
        opcao = input("Escolha uma opção (1-4): ").strip()

        if opcao == "1":
            nivel = input("Digite seu nível (iniciante/intermediario/avancado): ").strip().lower()
            objetivo = input("Digite seu objetivo (hipertrofia/emagrecimento/resistencia/cardio): ").strip().lower()
            mostrar_treino(nome, nivel, objetivo)

        elif opcao == "2":
            mostrar_historico(nome)

        elif opcao == "3":
            while True:
                bot_fala("\nMenu de Gerenciamento de Exercícios:")
                bot_fala("1. Adicionar novo exercício")
                bot_fala("2. Listar exercícios")
                bot_fala("3. Editar exercício")
                bot_fala("4. Excluir exercício")
                bot_fala("5. Voltar ao menu principal")
                sub = input("Escolha uma opção (1-5): ").strip()

                if sub == "1":
                    adicionar_exercicio()
                elif sub == "2":
                    listar_exercicios()
                elif sub == "3":
                    editar_exercicio()
                elif sub == "4":
                    excluir_exercicio()
                elif sub == "5":
                    break
                else:
                    bot_fala("Opção inválida.")

        elif opcao == "4":
            bot_fala("Até a próxima! Continue firme nos treinos!")
            break

        else:
            bot_fala("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    bot_academia()
