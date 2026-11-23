# -*- coding: utf-8 -*-
"""Conteúdo MODELO ILUSTRATIVO das páginas legais.

⚠️  Este arquivo NÃO contém informações jurídicas reais da farmácia.
    Campos entre [COLCHETES] devem ser preenchidos pelo proprietário e o texto
    deve ser revisado por profissional competente ANTES de publicar.
    As páginas exibem um aviso visível dizendo que são modelos.
"""

LEGAL_PAGES = [
    {
        'file': 'politica-de-privacidade.html',
        'title': 'Política de Privacidade',
        'script': 'Privacidade, cookies e LGPD',
        'desc': 'Modelo ilustrativo de Política de Privacidade, com orientações gerais sobre dados, cookies e direitos do titular.',
        'crumb': 'Política de Privacidade',
        'lead': 'Esta política explica, em termos gerais, como a Farma Popular Ouro Preto trata '
                'informações pessoais no âmbito deste site informativo. É um modelo: os dados '
                'entre colchetes precisam ser preenchidos e o texto revisado antes da publicação.',
        'sections': [
            {
                'h': '1. Quem é o responsável pelo tratamento',
                'p': [
                    'O responsável pelo tratamento dos dados é [RAZÃO SOCIAL], inscrita no CNPJ '
                    '[CNPJ], com sede na Rua Diogo de Vasconcelos, 39, Ouro Preto – MG, 35400-000. '
                    'Contato: (31) 3551-5271 e [E-MAIL DE CONTATO].',
                    'O encarregado pelo tratamento de dados pessoais (DPO), quando designado, '
                    'pode ser contatado em [E-MAIL DO ENCARREGADO].'
                ],
                'ul': []
            },
            {
                'h': '2. Quais dados são coletados neste site',
                'p': [
                    'Este site não possui cadastro, formulário de compra nem área restrita. '
                    'Não solicitamos nome, CPF, e-mail ou dados de pagamento para navegar.'
                ],
                'ul': [
                    'Dados de navegação: podem ser coletados por ferramentas de análise somente '
                    'se você aceitar os cookies opcionais no aviso exibido no site.',
                    'Conversa pelo WhatsApp: ao clicar em um botão de consulta, você é direcionado '
                    'ao aplicativo WhatsApp, que é operado por terceiro. As mensagens que você '
                    'enviar ficam sob as regras daquele serviço e são tratadas pela farmácia apenas '
                    'para responder à sua consulta.',
                    'Ligações telefônicas: os dados da chamada são tratados pela operadora e não '
                    'são armazenados por este site.'
                ]
            },
            {
                'h': '3. Para que os dados são usados',
                'p': ['Os dados eventualmente recebidos são usados exclusivamente para responder '
                      'consultas sobre produtos, disponibilidade e orientações gerais, além de '
                      'melhorar a experiência de navegação quando houver consentimento para análise.'],
                'ul': []
            },
            {
                'h': '4. Compartilhamento com terceiros',
                'p': [
                    'A farmácia não vende, não aluga e não compartilha dados pessoais com terceiros '
                    'para fins de marketing. O site inclui links para serviços externos (WhatsApp, '
                    'Google Maps e redes sociais); ao acessá-los, aplicam-se as políticas desses serviços.'
                ],
                'ul': []
            },
            {
                'h': '5. Armazenamento e exclusão',
                'p': [
                    'A preferência de cookies ficará salva no seu navegador (armazenamento local) '
                    'para lembrar a escolha nas próximas visitas. Os dados de uma conversa são '
                    'mantidos apenas pelo tempo necessário para responder e para cumprir '
                    'obrigações legais aplicáveis.'
                ],
                'ul': []
            },
            {
                'h': '6. Seus direitos (LGPD – Lei nº 13.709/2018)',
                'p': ['Você pode solicitar, conforme a lei:'],
                'ul': [
                    'confirmação da existência de tratamento e acesso aos dados;',
                    'correção de dados incompletos, inexatos ou desatualizados;',
                    'anonimização, bloqueio ou eliminação de dados desnecessários;',
                    'portabilidade e informações sobre compartilhamentos;',
                    'revogação do consentimento e oposição a tratamento fundado em outras bases legais.'
                ]
            },
            {
                'h': '7. Cookies e como alterar sua escolha',
                'p': [
                    'Você pode aceitar ou rejeitar os cookies opcionais no aviso exibido na primeira '
                    'visita e alterar a decisão a qualquer momento pelo link “Preferências de cookies” '
                    'no rodapé. Detalhes estão na Política de Cookies.'
                ],
                'ul': []
            },
            {
                'h': '8. Alterações nesta política',
                'p': ['Esta página pode ser atualizada. A versão vigente será sempre a publicada neste endereço, com a data de revisão indicada: [DATA DA ÚLTIMA REVISÃO].'],
                'ul': []
            },
        ],
    },
    {
        'file': 'termos-de-uso.html',
        'title': 'Termos de Uso',
        'script': 'Regras gerais de utilização do site',
        'desc': 'Modelo ilustrativo de Termos de Uso do site informativo da Farma Popular Ouro Preto.',
        'crumb': 'Termos de Uso',
        'lead': 'Ao navegar neste site, você concorda com as orientações abaixo. Este é um modelo '
                'ilustrativo, que deve ser revisado e adaptado à realidade da farmácia antes de '
                'entrar em vigor.',
        'sections': [
            {
                'h': '1. Natureza informativa',
                'p': [
                    'Este site é uma vitrine informativa. Não realiza vendas, não possui carrinho, '
                    'checkout ou pagamento online e não publica preços, estoque ou disponibilidade '
                    'de produtos. Toda consulta é encaminhada à farmácia por WhatsApp ou telefone.'
                ],
                'ul': []
            },
            {
                'h': '2. Informações sobre medicamentos',
                'p': [
                    'Os dados cadastrais (nome, princípio ativo, registro e detentor) foram obtidos '
                    'da base de dados abertos da Anvisa. Apresentação, concentração, forma '
                    'farmacêutica e quantidade da embalagem não estão confirmados para a maioria '
                    'dos itens e são tratados como pendentes nas fichas.'
                ],
                'ul': []
            },
            {
                'h': '3. Uso permitido',
                'p': ['Você pode navegar, consultar as fichas e usar os botões de contato desde que:'],
                'ul': [
                    'não tente alterar, bloquear ou explorar o funcionamento do site;',
                    'não use as informações para autodiagnóstico ou automedicação;',
                    'não represente este conteúdo como prescrição ou orientação médica.'
                ]
            },
            {
                'h': '4. Propriedade intelectual',
                'p': [
                    'Os textos, a identidade visual e os arquivos deste site pertencem à farmácia '
                    'ou foram licenciados para uso neste projeto. Marcas e logotipos de terceiros '
                    'são de seus respectivos titulares. Fotos de produtos são exemplos e podem '
                    'mostrar marcas diferentes das disponíveis na loja.'
                ],
                'ul': []
            },
            {
                'h': '5. Links externos',
                'p': [
                    'O site contém links para WhatsApp, Google Maps e redes sociais. A farmácia '
                    'não controla e não se responsabiliza pelo conteúdo ou pelas práticas desses serviços.'
                ],
                'ul': []
            },
            {
                'h': '6. Limitação de responsabilidade',
                'p': [
                    'As informações são fornecidas “como estão”. A farmácia não garante que o '
                    'conteúdo esteja livre de erros nem que um produto esteja disponível em '
                    'determinado momento. A decisão de compra deve ser tomada após confirmação '
                    'direta com a loja e leitura da bula.'
                ],
                'ul': []
            },
            {
                'h': '7. Lei aplicável',
                'p': ['Estes termos são regidos pela legislação brasileira, inclusive o Código de Defesa do Consumidor e a LGPD.'],
                'ul': []
            },
        ],
    },
    {
        'file': 'politica-de-cookies.html',
        'title': 'Política de Cookies',
        'script': 'Cookies e preferências de navegação',
        'desc': 'Modelo ilustrativo de Política de Cookies, com explicação sobre cookies essenciais e opcionais.',
        'crumb': 'Política de Cookies',
        'lead': 'Esta página explica como o site usa cookies e tecnologias semelhantes. É um modelo '
                'ilustrativo: quando ferramentas de análise ou propaganda forem adicionadas, '
                'este texto e a lista de cookies devem ser atualizados.',
        'sections': [
            {
                'h': '1. O que são cookies',
                'p': ['Cookies são pequenos arquivos armazenados pelo navegador que ajudam a lembrar preferências e a entender como a página é utilizada. Tecnologias semelhantes incluem armazenamento local (localStorage) e pixels.'],
                'ul': []
            },
            {
                'h': '2. O que este site usa hoje',
                'p': [
                    'Atualmente, o site não carrega ferramentas de análise, publicidade ou rastreamento. '
                    'A única tecnologia utilizada é o armazenamento local da sua preferência de '
                    'cookies, para que o aviso não apareça novamente e para respeitar a sua escolha.'
                ],
                'ul': [
                    'Essenciais: a preferência de consentimento (aceitar ou rejeitar opcionais).',
                    'Opcionais: nenhuma ferramenta opcional está ativa neste momento. Seeds para '
                    'futuras ferramentas de análise ficam desativados até que você aceite.'
                ]
            },
            {
                'h': '3. Como aceitar ou rejeitar',
                'p': [
                    'Na primeira visita, um aviso oferece “Aceitar cookies” e “Rejeitar opcionais”. '
                    'Sua escolha é salva no navegador. Você pode mudar a decisão a qualquer momento '
                    'pelo link “Preferências de cookies” no rodapé.'
                ],
                'ul': []
            },
            {
                'h': '4. Cookies de terceiros',
                'p': [
                    'Ao clicar em links externos (WhatsApp, Google Maps ou redes sociais), você pode '
                    'receber cookies desses serviços, que possuem políticas próprias. O site não '
                    'insere esses cookies automaticamente na sua visita.'
                ],
                'ul': []
            },
            {
                'h': '5. Como gerenciar no navegador',
                'p': ['Você também pode bloquear ou apagar cookies nas configurações do seu navegador. Bloquear cookies essenciais pode impedir que a preferência seja lembrada, fazendo o aviso aparecer novamente.'],
                'ul': []
            },
            {
                'h': '6. Atualizações',
                'p': ['Se novas ferramentas forem adicionadas, esta política será atualizada e o consentimento será solicitado novamente quando necessário. Última revisão do modelo: [DATA DA ÚLTIMA REVISÃO].'],
                'ul': []
            },
        ],
    },
    {
        'file': 'responsabilidade.html',
        'title': 'Aviso de Responsabilidade',
        'script': 'Avisos e limitações do conteúdo',
        'desc': 'Modelo ilustrativo de aviso de responsabilidade: o site não presta assistência médica nem faz vendas online.',
        'crumb': 'Aviso de Responsabilidade',
        'lead': 'Este aviso esclarece os limites das informações publicadas. Trata-se de um modelo '
                'ilustrativo, sujeito à revisão antes da publicação.',
        'sections': [
            {
                'h': '1. Não é serviço médico',
                'p': [
                    'Este site não presta assistência médica, não faz diagnóstico, prescrição, '
                    'telemedicina nem dispensação de medicamentos. As fichas são meramente '
                    'informativas e não substituem a orientação de um profissional de saúde.'
                ],
                'ul': []
            },
            {
                'h': '2. Bula e automedicação',
                'p': ['Sempre leia a bula do produto antes de usar. Não pratique automedicação. Em caso de dúvida, procure um farmacêutico ou médico.'],
                'ul': []
            },
            {
                'h': '3. Dados regulatórios',
                'p': [
                    'Registros e princípios ativos foram conferidos na base de dados abertos da '
                    'Anvisa em 16/11/2026. Situações podem mudar; a verificação definitiva deve '
                    'ser feita no Bulário Eletrônico da Anvisa pelo número de registro.'
                ],
                'ul': []
            },
            {
                'h': '4. Imagens e apresentações',
                'p': ['As fotos são exemplos de produtos e podem apresentar marca, fabricante ou embalagem diferentes do item efetivamente disponível na loja. A imagem não representa uma oferta.'],
                'ul': []
            },
            {
                'h': '5. Preço, estoque e disponibilidade',
                'p': ['Nenhum valor, quantidade em estoque ou garantia de disponibilidade é publicado. Todas as condições devem ser confirmadas diretamente com a farmácia.'],
                'ul': []
            },
            {
                'h': '6. Medicamentos controlados',
                'p': ['Medicamentos sujeitos a controle especial não são comercializados, reservados ou entregues por meio deste site. A aquisição ocorre exclusivamente na loja, com apresentação de receita quando exigida.'],
                'ul': []
            },
            {
                'h': '7. Contato',
                'p': ['Fale com a Farma Popular Ouro Preto pelo telefone (31) 3551-5271, pelo WhatsApp informado no site ou pela página de contato.'],
                'ul': []
            },
        ],
    },
    {
        'file': 'entrega-e-troca.html',
        'title': 'Entrega e Troca',
        'script': 'Condições comerciais gerais (modelo)',
        'desc': 'Modelo ilustrativo de política de entrega e troca para uma farmácia física, sem venda online.',
        'crumb': 'Entrega e Troca',
        'lead': 'Como o site não realiza vendas, as condições abaixo são um modelo ilustrativo para '
                'o atendimento presencial e devem ser confirmadas pela farmácia antes de qualquer '
                'publicação definitiva.',
        'sections': [
            {
                'h': '1. Local de compra',
                'p': ['As compras são realizadas presencialmente na loja: Rua Diogo de Vasconcelos, 39, Ouro Preto – MG, 35400-000. O site apenas encaminha consultas por WhatsApp e telefone.'],
                'ul': []
            },
            {
                'h': '2. Entrega',
                'p': [
                    'A farmácia pode oferecer entrega local conforme combinado diretamente com o '
                    'cliente. [DESCREVER AQUI AS CONDIÇÕES REAIS: áreas atendidas, horários, '
                    'taxas e forma de solicitação.] Não há promessa de entrega neste site.'
                ],
                'ul': []
            },
            {
                'h': '3. Trocas e devoluções',
                'p': [
                    'Para compras presenciais, aplicam-se a política interna da loja e o Código de '
                    'Defesa do Consumidor. Para compras realizadas fora do estabelecimento, a lei '
                    'garante, em regra, o direito de arrependimento em até 7 dias. [CONFIRMAR '
                    'A POLÍTICA INTERNA DA FARMÁCIA.]'
                ],
                'ul': [
                    'Solicitações devem ser feitas na loja ou pelos canais de contato informados.',
                    'É necessário apresentar nota fiscal ou comprovante da compra.',
                    'O produto deve estar intacto, com embalagem original e lacres preservados.'
                ]
            },
            {
                'h': '4. Exceções',
                'p': [
                    'Medicamentos, produtos controlados, itens com prazo de validade curto, '
                    'higiene íntima e produtos personalizados podem não admitir troca por motivos '
                    'de segurança e higiene, conforme a legislação e a política da loja.'
                ],
                'ul': []
            },
            {
                'h': '5. Reembolso',
                'p': ['A forma e o prazo de reembolso dependem do meio de pagamento e devem ser acordados com a farmácia no momento da solicitação. [PREENCHER COM A POLÍTICA REAL.]'],
                'ul': []
            },
            {
                'h': '6. Contato',
                'p': ['Telefone (31) 3551-5271, WhatsApp informado no site ou página de contato.'],
                'ul': []
            },
        ],
    },
]
