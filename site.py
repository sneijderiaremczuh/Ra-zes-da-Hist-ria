import random
import streamlit as st

st.set_page_config(
    page_title="Consciência Negra | História e Resistência",
    page_icon="✊🏿",
    layout="wide",
)

# -------------------------
# ESTILO
# -------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #101010 0%, #211d16 100%);
    color: #f5f5f5;
}
h1, h2, h3 { color: #F5BD36 !important; }
section[data-testid="stSidebar"] {
    background: #171717;
}
div[data-testid="stMetric"] {
    background: #292929;
    border: 1px solid #49402f;
    padding: 14px;
    border-radius: 14px;
}
.hero {
    padding: 28px;
    border-radius: 18px;
    border: 1px solid #514326;
    background: linear-gradient(120deg, #282116, #1d1d1d);
}
.card {
    background: #242424;
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #403a2f;
    margin-bottom: 12px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# HISTÓRIAS
# -------------------------
pessoas = {
    "Zumbi dos Palmares": {
        "periodo": "Século XVII",
        "area": "Resistência e liberdade",
        "historia": """Zumbi foi uma das principais lideranças do Quilombo dos Palmares,
comunidade formada por pessoas que buscavam viver livres da escravidão.
Palmares tornou-se um importante símbolo de resistência. Zumbi morreu em
20 de novembro de 1695 e sua memória permanece associada à luta por liberdade.""",
        "legado": "Símbolo da resistência negra e da luta por liberdade.",
    },
    "Dandara dos Palmares": {
        "periodo": "Século XVII",
        "area": "Resistência",
        "historia": """Dandara é lembrada por sua ligação com o Quilombo dos Palmares
e com a resistência à escravidão. Os registros históricos detalhados sobre
sua vida são limitados, mas ela se tornou uma figura importante na memória
da participação das mulheres negras na luta por liberdade.""",
        "legado": "Representa a participação das mulheres negras na resistência.",
    },
    "Machado de Assis": {
        "periodo": "1839–1908",
        "area": "Literatura",
        "historia": """Joaquim Maria Machado de Assis nasceu no Rio de Janeiro, em 1839,
e construiu uma carreira literária extraordinária em uma sociedade marcada
pela escravidão e pelo racismo. Escreveu obras como Dom Casmurro e
Memórias Póstumas de Brás Cubas. Foi um dos fundadores e o primeiro
presidente da Academia Brasileira de Letras.""",
        "legado": "Transformou a literatura brasileira e tornou-se um de seus maiores escritores.",
    },
    "Carolina Maria de Jesus": {
        "periodo": "1914–1977",
        "area": "Literatura e desigualdade social",
        "historia": """Carolina Maria de Jesus nasceu em Minas Gerais e viveu em São Paulo.
Trabalhou como catadora de papel e registrou em seus cadernos a vida na
favela do Canindé. Seu livro Quarto de Despejo, publicado em 1960,
revelou ao público experiências de pobreza e desigualdade social.""",
        "legado": "Deu visibilidade à vida nas periferias e tornou-se uma escritora reconhecida.",
    },
    "Luiz Gama": {
        "periodo": "1830–1882",
        "area": "Justiça e abolicionismo",
        "historia": """Luiz Gama foi escritor, jornalista, abolicionista e advogado autodidata.
Depois de ser escravizado ilegalmente durante parte da juventude, dedicou-se
à defesa jurídica de pessoas escravizadas. Sua atuação ajudou muitas pessoas
a buscar a liberdade e contribuiu para o movimento abolicionista.""",
        "legado": "Usou a escrita e o conhecimento jurídico para combater a escravidão.",
    },
    "Antonieta de Barros": {
        "periodo": "1901–1952",
        "area": "Educação e política",
        "historia": """Antonieta de Barros foi professora, jornalista e política catarinense.
Defendeu a educação pública e a participação das mulheres na sociedade.
Em 1934, tornou-se deputada estadual em Santa Catarina, sendo reconhecida
como uma pioneira na política brasileira.""",
        "legado": "Abriu caminhos para a participação de mulheres negras na política.",
    },
    "Milton Santos": {
        "periodo": "1926–2001",
        "area": "Geografia e pensamento social",
        "historia": """Milton Santos foi um geógrafo baiano de reconhecimento internacional.
Estudou cidades, território, globalização e desigualdades. Em 1994,
recebeu o Prêmio Vautrin Lud, uma das distinções internacionais mais
importantes da Geografia.""",
        "legado": "Influenciou a Geografia e o pensamento sobre as desigualdades no mundo.",
    },
    "Lélia Gonzalez": {
        "periodo": "1935–1994",
        "area": "Pensamento social e movimento negro",
        "historia": """Lélia Gonzalez foi intelectual, professora e ativista brasileira.
Seus estudos abordaram racismo, sexismo e as experiências das mulheres
negras no Brasil. Participou do movimento negro e ajudou a ampliar o debate
sobre desigualdade racial e de gênero.""",
        "legado": "Sua obra continua influenciando estudos sociais e movimentos por igualdade.",
    },
    "Conceição Evaristo": {
        "periodo": "1946–",
        "area": "Literatura",
        "historia": """Conceição Evaristo é escritora e professora brasileira. Sua obra aborda
memória, identidade, desigualdade e experiências da população negra.
O conceito de escrevivência, associado à sua produção, conecta escrita
e experiências vividas.""",
        "legado": "Ampliou a presença de vozes negras na literatura brasileira.",
    },
    "Abdias do Nascimento": {
        "periodo": "1914–2011",
        "area": "Teatro, política e movimento negro",
        "historia": """Abdias do Nascimento foi ator, dramaturgo, artista, político e ativista.
Fundou o Teatro Experimental do Negro, que buscava ampliar a participação
de artistas negros e questionar o racismo na cultura brasileira.""",
        "legado": "Foi uma referência na luta antirracista e na valorização da cultura negra.",
    },
}

# -------------------------
# BANCO DE PERGUNTAS
# -------------------------
perguntas = [
    {"pergunta": "Quem foi uma das principais lideranças de Palmares?",
     "opcoes": ["Zumbi dos Palmares", "Machado de Assis", "Milton Santos", "Antonieta de Barros"],
     "correta": "Zumbi dos Palmares", "explicacao": "Zumbi tornou-se um símbolo da resistência à escravidão."},
    {"pergunta": "Quem escreveu Quarto de Despejo?",
     "opcoes": ["Carolina Maria de Jesus", "Lélia Gonzalez", "Dandara dos Palmares", "Antonieta de Barros"],
     "correta": "Carolina Maria de Jesus", "explicacao": "O livro registra experiências de pobreza e desigualdade."},
    {"pergunta": "Quem atuou na defesa jurídica de pessoas escravizadas?",
     "opcoes": ["Milton Santos", "Machado de Assis", "Luiz Gama", "Zumbi dos Palmares"],
     "correta": "Luiz Gama", "explicacao": "Luiz Gama usou seus conhecimentos jurídicos na luta abolicionista."},
    {"pergunta": "Quem foi uma pioneira negra na política de Santa Catarina?",
     "opcoes": ["Dandara dos Palmares", "Antonieta de Barros", "Carolina Maria de Jesus", "Lélia Gonzalez"],
     "correta": "Antonieta de Barros", "explicacao": "Antonieta foi professora, jornalista e deputada estadual."},
    {"pergunta": "Qual personalidade ficou conhecida internacionalmente pela Geografia?",
     "opcoes": ["Milton Santos", "Luiz Gama", "Zumbi dos Palmares", "Machado de Assis"],
     "correta": "Milton Santos", "explicacao": "Milton Santos foi um geógrafo brasileiro reconhecido internacionalmente."},
    {"pergunta": "Quem escreveu Dom Casmurro?",
     "opcoes": ["Carolina Maria de Jesus", "Machado de Assis", "Lélia Gonzalez", "Antonieta de Barros"],
     "correta": "Machado de Assis", "explicacao": "Machado de Assis é um dos maiores nomes da literatura brasileira."},
    {"pergunta": "Quem estudou as relações entre racismo e sexismo no Brasil?",
     "opcoes": ["Dandara dos Palmares", "Milton Santos", "Lélia Gonzalez", "Luiz Gama"],
     "correta": "Lélia Gonzalez", "explicacao": "Lélia foi uma intelectual e ativista fundamental nesses debates."},
    {"pergunta": "Em que data é celebrado o Dia da Consciência Negra?",
     "opcoes": ["20 de novembro", "13 de maio", "7 de setembro", "15 de novembro"],
     "correta": "20 de novembro", "explicacao": "A data está associada à memória de Zumbi dos Palmares."},
    {"pergunta": "Em que ano foi assinada a Lei Áurea?",
     "opcoes": ["1888", "1822", "1889", "1930"],
     "correta": "1888", "explicacao": "A Lei Áurea foi assinada em 13 de maio de 1888."},
    {"pergunta": "Qual lei tornou obrigatório o ensino de história e cultura afro-brasileira nas escolas?",
     "opcoes": ["Lei 10.639/2003", "Lei Áurea", "Lei do Ventre Livre", "Lei Eusébio de Queirós"],
     "correta": "Lei 10.639/2003", "explicacao": "A lei de 2003 alterou a legislação educacional brasileira."},
    {"pergunta": "Qual comunidade se tornou símbolo de resistência à escravidão?",
     "opcoes": ["Quilombo dos Palmares", "Missão Francesa", "Inconfidência Mineira", "Corte portuguesa"],
     "correta": "Quilombo dos Palmares", "explicacao": "Palmares reuniu pessoas que resistiam à escravidão."},
    {"pergunta": "Dandara dos Palmares é lembrada por sua ligação com qual comunidade?",
     "opcoes": ["Quilombo dos Palmares", "Academia Brasileira de Letras", "Teatro Experimental do Negro", "Academia Imperial"],
     "correta": "Quilombo dos Palmares", "explicacao": "Dandara é lembrada na memória da resistência de Palmares."},
    {"pergunta": "Quem foi o primeiro presidente da Academia Brasileira de Letras?",
     "opcoes": ["Machado de Assis", "José de Alencar", "Rui Barbosa", "Castro Alves"],
     "correta": "Machado de Assis", "explicacao": "Machado foi um dos fundadores e o primeiro presidente da instituição."},
    {"pergunta": "Quem registrou em seus escritos a vida na favela do Canindé?",
     "opcoes": ["Carolina Maria de Jesus", "Lélia Gonzalez", "Rachel de Queiroz", "Clarice Lispector"],
     "correta": "Carolina Maria de Jesus", "explicacao": "Seus escritos deram visibilidade à pobreza e à desigualdade."},
    {"pergunta": "Qual destas é uma manifestação cultural afro-brasileira?",
     "opcoes": ["Capoeira", "Esgrima medieval", "Ópera italiana", "Flamenco espanhol"],
     "correta": "Capoeira", "explicacao": "A capoeira combina luta, música, movimento e tradição."},
    {"pergunta": "Qual prato está ligado à culinária afro-brasileira?",
     "opcoes": ["Acarajé", "Croissant", "Sushi", "Taco mexicano"],
     "correta": "Acarajé", "explicacao": "O acarajé tem raízes na tradição culinária africana e afro-brasileira."},
    {"pergunta": "Qual era uma das profissões de Antonieta de Barros?",
     "opcoes": ["Professora", "Astronauta", "Piloto de corrida", "Imperatriz"],
     "correta": "Professora", "explicacao": "Antonieta atuou como educadora, jornalista e política."},
    {"pergunta": "Em qual cidade nasceu Luiz Gama?",
     "opcoes": ["Salvador", "Curitiba", "Manaus", "Goiânia"],
     "correta": "Salvador", "explicacao": "Luiz Gama nasceu em Salvador, na Bahia, em 1830."},
    {"pergunta": "Qual era a principal luta do movimento abolicionista?",
     "opcoes": ["Acabar com a escravidão", "Ampliar a escravidão", "Impedir a educação", "Restaurar o colonialismo"],
     "correta": "Acabar com a escravidão", "explicacao": "O abolicionismo defendia o fim da escravidão."},
    {"pergunta": "Quem escreveu Ponciá Vicêncio?",
     "opcoes": ["Conceição Evaristo", "Dandara", "Antonieta de Barros", "Chiquinha Gonzaga"],
     "correta": "Conceição Evaristo", "explicacao": "Conceição Evaristo aborda memória, identidade e desigualdade em sua obra."},
    {"pergunta": "Qual jogador ficou conhecido como Rei do Futebol?",
     "opcoes": ["Pelé", "Zico", "Romário", "Sócrates"],
     "correta": "Pelé", "explicacao": "Pelé foi um dos maiores jogadores da história do futebol."},
    {"pergunta": "Qual foi uma contribuição importante de Luiz Gama?",
     "opcoes": ["Lutar juridicamente pela liberdade", "Criar a Lei Áurea", "Fundar Palmares", "Escrever Dom Casmurro"],
     "correta": "Lutar juridicamente pela liberdade", "explicacao": "Luiz Gama ajudou pessoas escravizadas a buscar liberdade na Justiça."},
    {"pergunta": "O que significa combater o racismo?",
     "opcoes": ["Enfrentar a discriminação racial", "Ignorar desigualdades", "Reforçar estereótipos", "Excluir pessoas"],
     "correta": "Enfrentar a discriminação racial", "explicacao": "Combater o racismo envolve respeito, igualdade e ação contra a discriminação."},
    {"pergunta": "Por que é importante valorizar a história afro-brasileira?",
     "opcoes": ["Reconhecer contribuições e histórias", "Apagar a história", "Promover preconceitos", "Negar a diversidade"],
     "correta": "Reconhecer contribuições e histórias", "explicacao": "Conhecer essas histórias amplia a compreensão da sociedade brasileira."},
    {"pergunta": "Quem fundou o Teatro Experimental do Negro?",
     "opcoes": ["Abdias do Nascimento", "Milton Santos", "Machado de Assis", "Luiz Gama"],
     "correta": "Abdias do Nascimento", "explicacao": "Abdias foi artista, ativista e fundador do Teatro Experimental do Negro."},
    {"pergunta": "O que foi o Quilombo dos Palmares?",
     "opcoes": ["Uma comunidade de resistência", "Uma universidade portuguesa", "Uma expedição marítima", "Uma lei imperial"],
     "correta": "Uma comunidade de resistência", "explicacao": "Palmares foi uma comunidade formada por pessoas que buscavam liberdade."},
    {"pergunta": "Qual destas áreas foi importante na atuação de Lélia Gonzalez?",
     "opcoes": ["Pensamento social e ativismo", "Engenharia aeronáutica", "Física nuclear", "Navegação comercial"],
     "correta": "Pensamento social e ativismo", "explicacao": "Lélia contribuiu para debates sobre racismo, gênero e sociedade."},
    {"pergunta": "A abolição de 1888 resolveu todas as desigualdades raciais no Brasil?",
     "opcoes": ["Não, as desigualdades continuaram", "Sim, imediatamente", "Sim, antes da lei", "Não existiam desigualdades"],
     "correta": "Não, as desigualdades continuaram", "explicacao": "O fim legal da escravidão não garantiu igualdade social ou econômica."},
    {"pergunta": "Qual atitude ajuda a construir uma sociedade antirracista?",
     "opcoes": ["Respeitar diferenças e enfrentar preconceitos", "Compartilhar insultos racistas", "Excluir colegas", "Ignorar discriminação"],
     "correta": "Respeitar diferenças e enfrentar preconceitos", "explicacao": "Uma sociedade antirracista exige compromisso com a igualdade."},
    {"pergunta": "Qual foi uma área importante da atuação de Abdias do Nascimento?",
     "opcoes": ["Teatro e movimento negro", "Exploração espacial", "Aviação comercial", "Futebol profissional"],
     "correta": "Teatro e movimento negro", "explicacao": "Abdias usou a arte e a política para valorizar a cultura negra."},
]

# -------------------------
# ESTADO DO JOGO
# -------------------------
def iniciar_partida():
    st.session_state.partida_ids = random.sample(
        range(len(perguntas)), min(10, len(perguntas))
    )
    st.session_state.jogo_indice = 0
    st.session_state.jogo_pontos = 0
    st.session_state.jogo_terminou = False
    st.session_state.jogo_resposta = None
    st.session_state.jogo_acertou = False
    st.session_state.alternativas_partida = {}
    st.session_state.partida_iniciada = True

if "partida_iniciada" not in st.session_state:
    iniciar_partida()

# -------------------------
# MENU
# -------------------------
st.sidebar.title("✊🏿 CONSCIÊNCIA NEGRA")
st.sidebar.caption("História • Cultura • Resistência")

pagina = st.sidebar.radio(
    "Navegue pelo projeto",
    ["🏠 Início", "📚 Histórias", "🗓️ Linha do tempo", "🎮 Mini game", "💡 Aprenda mais"],
)

st.sidebar.markdown("---")
st.sidebar.write("**20 de novembro**")
st.sidebar.caption("Memória, respeito e igualdade.")

# -------------------------
# INÍCIO
# -------------------------
if pagina == "🏠 Início":
    st.markdown("""
    <div class="hero">
        <h1>✊🏿 Heróis que Mudaram o Brasil</h1>
        <h3>Uma história de coragem, inteligência, cultura e resistência.</h3>
        <p>Conheça pessoas negras que transformaram a literatura, a educação,
        a ciência, a política e a luta por direitos.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Explore o projeto")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="card"><h3>📚 Histórias</h3>Conheça trajetórias e legados.</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><h3>🗓️ Linha do tempo</h3>Descubra datas importantes.</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="card"><h3>🎮 Mini game</h3>Teste seus conhecimentos e marque pontos.</div>', unsafe_allow_html=True)

    st.markdown("### Por que 20 de novembro?")
    st.write("""O Dia Nacional de Zumbi e da Consciência Negra é celebrado em 20 de novembro,
data associada à morte de Zumbi dos Palmares, em 1695. O dia tornou-se feriado nacional em 2023.""")
    st.info("Consciência Negra é valorizar a história, reconhecer desigualdades e promover uma sociedade antirracista.")

# -------------------------
# HISTÓRIAS
# -------------------------
elif pagina == "📚 Histórias":
    st.title("📚 Pessoas que fizeram história")
    st.write("Escolha uma personalidade para conhecer sua trajetória.")
    nome = st.selectbox("Selecione uma pessoa:", list(pessoas.keys()))
    pessoa = pessoas[nome]
    st.caption(f"{pessoa['periodo']} • {pessoa['area']}")
    st.markdown(f"## {nome}")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Sua história")
    st.write(pessoa["historia"])
    st.markdown("### Seu legado")
    st.write(pessoa["legado"])
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("---")
    st.write("**Reflita:** que desafios essa pessoa enfrentou e que mudanças ajudou a construir?")

# -------------------------
# LINHA DO TEMPO
# -------------------------
elif pagina == "🗓️ Linha do tempo":
    st.title("🗓️ Linha do tempo")
    st.write("Alguns marcos da história da população negra no Brasil.")
    eventos = [
        ("1695", "Morte de Zumbi", "Zumbi dos Palmares morre em 20 de novembro."),
        ("1830", "Nascimento de Luiz Gama", "Futuro abolicionista que atuaria na defesa da liberdade."),
        ("1888", "Abolição da escravidão", "A Lei Áurea é assinada em 13 de maio, sem garantir igualdade social."),
        ("1934", "Antonieta na política", "Antonieta de Barros é eleita deputada estadual em Santa Catarina."),
        ("1960", "Quarto de Despejo", "É publicado o livro de Carolina Maria de Jesus."),
        ("1988", "Constituição Federal", "A Constituição estabelece o racismo como crime inafiançável e imprescritível."),
        ("2003", "Lei 10.639", "O ensino de história e cultura afro-brasileira torna-se obrigatório nas escolas."),
        ("2023", "Feriado nacional", "O dia 20 de novembro passa a ser feriado nacional."),
    ]
    for ano, titulo, descricao in eventos:
        with st.expander(f"📍 {ano} — {titulo}"):
            st.write(descricao)

# -------------------------
# MINI GAME
# -------------------------
elif pagina == "🎮 Mini game":
    st.title("🎮 Desafio da Consciência Negra")
    st.write("10 perguntas sorteadas por partida. Cada acerto vale 100 pontos!")

    total = len(st.session_state.partida_ids)

    if not st.session_state.jogo_terminou:
        indice = st.session_state.jogo_indice
        pergunta = perguntas[st.session_state.partida_ids[indice]]

        if indice not in st.session_state.alternativas_partida:
            st.session_state.alternativas_partida[indice] = random.sample(
                pergunta["opcoes"], len(pergunta["opcoes"])
            )

        st.progress((indice + 1) / total)
        col1, col2 = st.columns(2)
        col1.metric("Pergunta", f"{indice + 1}/{total}")
        col2.metric("Pontuação", st.session_state.jogo_pontos)
        st.markdown("---")
        st.subheader(pergunta["pergunta"])

        if st.session_state.jogo_resposta is None:
            resposta = st.radio(
                "Escolha uma alternativa:",
                st.session_state.alternativas_partida[indice],
                index=None,
                key=f"resposta_partida_{indice}",
            )

            if st.button("Confirmar resposta", type="primary"):
                if resposta is None:
                    st.warning("Escolha uma alternativa antes de confirmar.")
                else:
                    st.session_state.jogo_resposta = resposta
                    st.session_state.jogo_acertou = resposta == pergunta["correta"]
                    if st.session_state.jogo_acertou:
                        st.session_state.jogo_pontos += 100
                    st.rerun()
        else:
            if st.session_state.jogo_acertou:
                st.success("🎉 Correto! Você ganhou 100 pontos!")
            else:
                st.error(f"Resposta correta: {pergunta['correta']}")
            st.info(pergunta["explicacao"])

            if st.button("Próxima pergunta", type="primary"):
                if indice + 1 >= total:
                    st.session_state.jogo_terminou = True
                else:
                    st.session_state.jogo_indice += 1
                st.session_state.jogo_resposta = None
                st.rerun()
    else:
        pontos = st.session_state.jogo_pontos
        st.balloons()
        st.title("🏆 Fim de jogo!")
        st.metric("Pontuação final", f"{pontos} / {total * 100}")
        if pontos == total * 100:
            st.success("Lenda da Consciência Negra! Você acertou todas!")
        elif pontos >= 700:
            st.success("Excelente! Você conhece muito sobre essas histórias.")
        elif pontos >= 400:
            st.info("Muito bem! Continue aprendendo.")
        else:
            st.warning("Explore as histórias e tente novamente.")

        if st.button("🔄 Nova partida", type="primary"):
            iniciar_partida()
            st.rerun()

# -------------------------
# APRENDA MAIS
# -------------------------
elif pagina == "💡 Aprenda mais":
    st.title("💡 Conhecimento para transformar")
    st.subheader("O que é racismo?")
    st.write("""Racismo é a discriminação baseada em raça ou cor. Pode aparecer em atitudes
individuais e também em estruturas e instituições que produzem desigualdades.""")
    st.subheader("Como podemos contribuir?")
    st.markdown("""
    - Conhecer a história da população negra.
    - Valorizar autores, cientistas e artistas negros.
    - Combater piadas e atitudes racistas.
    - Respeitar as diferenças.
    - Denunciar situações de discriminação.
    - Aprender sobre a contribuição africana e afro-brasileira.
    """)
    st.subheader("Desafio final")
    reflexao = st.text_area("O que você aprendeu com este projeto?")
    if st.button("Registrar minha reflexão"):
        if reflexao.strip():
            st.success("Reflexão registrada nesta sessão!")
            st.write(reflexao)
        else:
            st.warning("Escreva sua reflexão primeiro.")

st.markdown("---")
st.caption("Projeto educativo sobre história, cultura afro-brasileira e combate ao racismo.")
