---
name: Farma Popular Ouro Preto
description: Vitrine informativa de farmácia com identidade vermelha e amarela, tipografia Poppins e toque local de Ouro Preto.
colors:
  primary: "#c8102e"
  primary-deep: "#a50b1f"
  primary-dark: "#8e0a18"
  accent: "#ffc20e"
  accent-soft: "#ffe083"
  whatsapp: "#0f7a3a"
  whatsapp-hover: "#0d6b33"
  ink: "#2b1a1a"
  paper: "#ffffff"
  surface-tint: "#fff6f7"
  surface-warm: "#fff8e1"
  promo-gold: "#ffbf00"
  muted: "#6f6161"
typography:
  display:
    fontFamily: "Yellowtail, cursive"
    fontSize: "3.25rem"
    fontWeight: 400
    lineHeight: 0.95
  headline:
    fontFamily: "Poppins, Arial, sans-serif"
    fontSize: "2.75rem"
    fontWeight: 800
    lineHeight: 1.06
  title:
    fontFamily: "Poppins, Arial, sans-serif"
    fontSize: "1.5rem"
    fontWeight: 700
    lineHeight: 1.25
  body:
    fontFamily: "Poppins, Arial, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Poppins, Arial, sans-serif"
    fontSize: "0.6875rem"
    fontWeight: 800
    letterSpacing: "0.06em"
rounded:
  sm: "10px"
  md: "16px"
  lg: "22px"
  pill: "30px"
spacing:
  xs: "8px"
  sm: "12px"
  md: "16px"
  lg: "24px"
  xl: "34px"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.paper}"
    typography: "Poppins 700 15px"
    rounded: "{rounded.pill}"
    padding: "14px 26px"
  button-primary-hover:
    backgroundColor: "{colors.primary-deep}"
    textColor: "{colors.paper}"
    rounded: "{rounded.pill}"
    padding: "14px 26px"
  button-whatsapp:
    backgroundColor: "{colors.whatsapp}"
    textColor: "{colors.paper}"
    rounded: "{rounded.pill}"
    padding: "14px 26px"
  button-whatsapp-hover:
    backgroundColor: "{colors.whatsapp-hover}"
    textColor: "{colors.paper}"
    rounded: "{rounded.pill}"
    padding: "14px 26px"
  card:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "24px"
  chip:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.primary-deep}"
    rounded: "{rounded.pill}"
    padding: "10px 16px"
  input-search:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "12px 26px"
---

# Design System: Farma Popular Ouro Preto

## Overview

**Creative North Star: "A Farmácia da Esquina"**

O sistema visual se comporta como uma farmácia de bairro de Ouro Preto: direta,
acolhedora e reconhecível à distância. O vermelho assume a autoridade da marca, o
amarelo traz o calor e a assinatura cursiva "Ouro Preto" dá o toque local. Não há
pretensão de minimalismo clínico: a página é informativa, densa e otimista.

Hierarquia é construída por peso e cor, não por variações sutis de cinza. Cartões
arredondados e sombras suaves organizam a informação sem criar "cards dentro de cards".
O movimento é discreto e restrito a transform e opacity.

**Key Characteristics:**
- Vermelho `#c8102e` como voz primária e amarelo `#ffc20e` como assinatura
- Tipografia Poppins para tudo; Yellowtail apenas para a assinatura de cidade
- Superfícies brancas com tints quentes e cantos generosos
- Chamadas para ação em pílula, com o verde do WhatsApp em tom profundo

## Colors

A paleta é quente, de farmácia popular brasileira: vermelho de confiança, amarelo
de proximidade, verde de conversa.

### Primary
- **Vermelho Farma** (#c8102e): botões principais, cabeçalhos, destaques e links.
- **Vermelho Profundo** (#a50b1f): hover de botões e fundos de rodapé.
- **Vermelho Vinho** (#8e0a18): topbar e gradientes do cabeçalho.

### Secondary
- **Amarelo Farma** (#ffc20e): assinatura "Ouro Preto", ícones e faixas promocionais.
- **Amarelo Claro** (#ffe083): microtexto sobre fundo vermelho, onde o amarelo puro não alcança contraste.

### Tertiary
- **Verde Conversa** (#0f7a3a): botões de WhatsApp e botão flutuante; 5,4:1 com texto branco.
- **Verde Conversa Hover** (#0d6b33): estado de hover.

### Neutral
- **Tinta Quente** (#2b1a1a): texto principal.
- **Papel** (#ffffff): fundo padrão.
- **Tinta Suave** (#6f6161): metadados e avisos secundários.
- **Tint Rosa** (#fff6f7) e **Tint Creme** (#fff8e1): fundos de mídia e avisos.

### Named Rules
**The Red Voice Rule.** O vermelho primário aparece em CTAs, títulos e marcadores;
o vinho fica reservado a fundos. Amarelo nunca substitui vermelho em CTA.

**The Deep Green Rule.** O verde dos botões de WhatsApp é `#0f7a3a`, não o verde
claro de logos. Contraste com texto branco é requisito, não preferência.

## Typography

**Display Font:** Yellowtail (cursive)
**Body Font:** Poppins (Arial, sans-serif)
**Label/Mono Font:** Barlow Condensed (uso pontual na faixa promocional)

**Character:** Poppins mantém a clareza institucional; Yellowtail quebra a
monotonia apenas na assinatura da cidade. Barlow Condensed aparece só no
"Genéricos" promocional.

### Hierarchy
- **Display** (400, clamp 2.75rem–5.75rem, line-height 0.95): "Ouro Preto" em script.
- **Headline** (800, 2.75rem no desktop / clamp 1.75rem–2.75rem no mobile, line-height 1.06): H1 das páginas.
- **Title** (700, 1.5rem): cards e seções.
- **Body** (400, 0.9375rem, line-height 1.6): textos e descrições; measure máxima de 68–72ch.
- **Label** (800, 0.6875rem, letter-spacing 0.06em): badges "ILUSTRAÇÃO" e.meta.

### Named Rules
**The Script-Only Rule.** Yellowtail é usado apenas na assinatura "Ouro Preto".
Nenhum outro texto recebe a fonte cursiva.

## Layout

Container único `.wrap` com `max-width:1248px` e padding lateral de 24 px (16 px em
telas ≤380 px). Grades fluidas com `minmax(0,1fr)` para evitar estouro. Breakpoints:
1024 px (duas colunas), 820 px (menu mobile, coluna única), 560 px (produtos em uma
coluna, categorias com rolagem horizontal), 380 px (espaçamento reduzido). A home
usa ainda 480 px para tipografia fluida. Espaçamento vertical típico entre seções:
34 px; entre cards, 20 px.

## Elevation & Depth

Profundidade é suave e difusa: sombras com offset vertical e blur amplo, usadas em
cards, busca e botão flutuante. Não há sombras de contorno duro.

### Shadow Vocabulary
- **Card** (`box-shadow: 0 4px 16px rgba(80,0,10,.10)`): repouso dos cards.
- **Hover** (`box-shadow: 0 16px 30px rgba(120,0,16,.18)`): elevação em cards.
- **Busca** (`box-shadow: 0 12px 32px rgba(120,0,16,.16)`): destaque da busca.
- **Flutuante** (`box-shadow: 0 6px 20px rgba(15,107,51,.5)`): botão de WhatsApp.

### Named Rules
**The Flat-Until-Touched Rule.** Superfícies ficam planas em repouso; sombra
mais forte só em hover ou elevação funcional.

## Shapes

Cantos generosos e consistentes: pills (30 px) para botões, chips e busca; 22 px
para cards e banners; 16 px para painéis internos; 10 px para detalhes. Bordas
quando existem são claras (`#f3e8e8`) e não competem com o conteúdo. A onda amarela
no topo do rodapé e o recorte diagonal da foto do hero são as duas silhuetas
assinatura.

## Components

### Buttons
- **Shape:** pílula (30 px), min-height 48 px.
- **Primary:** vermelho `#c8102e` com texto branco, padding 14×26 px.
- **WhatsApp:** verde profundo `#0f7a3a` com texto branco; hover `#0d6b33`.
- **Hover / Focus:** translateY(-2 px), sombra maior; foco com outline de 3 px em `#ffc20e`.

### Chips
- **Style:** fundo branco, borda `#f0c9c9`, texto `#8e0a18`, contador interno.
- **State:** selecionado vira vermelho com texto branco.

### Cards / Containers
- **Corner Style:** 22 px.
- **Background:** branco ou tint quente; borda clara.
- **Shadow Strategy:** ver Elevation.
- **Internal Padding:** 20–24 px.

### Inputs / Fields
- **Style:** pílula branca, ícone à esquerda, placeholder `#666666`.
- **Focus:** outline visível; sem borda própria.

### Navigation
- **Style:** pílula branca dentro do hero vermelho; item ativo em vermelho.
- **Mobile:** hamburger com submenu recuado; itens com no mínimo 44 px de altura.

### Signature Component
** Faixa promocional:** gradiente amarelo com raios em conic-gradient, título em
Barlow Condensed 800 e recorte da embalagem ilustrativa à direita.

## Do's and Don'ts

### Do:
- **Do** manter o verde dos CTAs em `#0f7a3a` (5,4:1 com branco).
- **Do** usar `clamp()` e `minmax(0,1fr)` em layouts responsivos.
- **Do** rotular as fotos dos 7 medicamentos como "FOTO DO PRODUTO" e manter o aviso de
  que a embalagem fotografada pode diferir da apresentação recebida na loja.
- **Do** rotular as fotos das cinco vitrines como "FOTO DO PRODUTO" e avisar que
  marca e apresentação podem diferir do item disponível na loja.
- **Do** preservar o submenu de Medicamentos e a seta apenas onde há subcategorias reais.

### Don't:
- **Don't** usar o verde claro `#25d366` em botão com texto branco (1,98:1).
- **Don't** aplicar Yellowtail fora da assinatura "Ouro Preto".
- **Don't** criar categorias vazias só para preencher o menu.
- **Don't** publicar preço, estoque, indicação terapêutica ou link `wa.me` não validado.
