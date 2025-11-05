from dash import html, dcc

def create_header():
    return html.Div(
        style={
            "backgroundColor": "#1f4788",
            "padding": "15px 40px",
            "display": "flex",
            "justifyContent": "space-between",
            "alignItems": "center",
            "color": "white",
            "fontFamily": "Arial, sans-serif",
            "boxShadow": "0 3px 6px rgba(0,0,0,0.15)",
            "position": "sticky",
            "top": "0",
            "zIndex": "1000"
        },
        children=[

            # === LOGO + HOME BUTTON ===
            html.A(
                "🏠 Dashboard Égalité Professionnelle",
                href="/",
                style={
                    "color": "white",
                    "textDecoration": "none",
                    "fontSize": "26px",
                    "fontWeight": "bold"
                }
            ),

            # === MENU DÉROULANT POUR LA NAVIGATION ===
            dcc.Dropdown(
                id="page-selector",
                options=[
                    {"label": "Distrib. des Notes", "value": "/page1"},
                    {"label": "Notes Moyennes par Taille", "value": "/page2"},
                    {"label": "Évolution Temporelle par Région", "value": "/page3"},
                    {"label": "Évolution par Taille d'Entreprise", "value": "/page4"},
                    {"label": "Statistiques Clés", "value": "/page5"},
                ],
                placeholder="📂 Aller à une page...",
                style={
                    "width": "260px",
                    "color": "#000"
                }
            )
        ]
    )
