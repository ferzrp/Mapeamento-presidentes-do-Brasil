import pandas as pd
import folium
import webbrowser

# Map to show where Brazilian Presidents were born
brazil_data = [
    # República Velha (1889-1930)
    {"President": "Deodoro da Fonseca", "State": "Rio de Janeiro"},
    {"President": "Floriano Peixoto", "State": "Alagoas"},
    {"President": "Prudente de Morais", "State": "São Paulo"},
     {"President": "Campos Sales", "State": "São Paulo"},
     {"President": "Rodrigues Alves", "State": "São Paulo"},
     {"President": "Afonso Pena", "State": "Minas Gerais"},
     {"President": "Nilo Peçanha", "State": "Rio de Janeiro"},
     {"President": "Hermes da Fonseca", "State": "Rio Grande do Sul"},
     {"President": "Venceslau Brás", "State": "Minas Gerais"},
     {"President": "Delfim Moreira", "State": "Minas Gerais"},
     {"President": "Epitácio Pessoa", "State": "Paraíba"},
     {"President": "Artur Bernardes", "State": "Minas Gerais"},
     {"President": "Washington Luís", "State": "Rio de Janeiro"},    
     {"President": "Júlio Prestes", "State": "São Paulo"}, 

    # Segunda República (1930 - 1937)
    {"President": "Tasso Fragoso", "State": "Rio de Janeiro"},
    {"President": "Isaías de Noronha", "State": "Rio de Janeiro"},
    {"President": "João de Deus Mena Barreto", "State": "Rio Grande do Sul"},
    {"President": "Getúlio Vargas (x1)", "State": "Rio Grande do Sul"},

# Terceira República (1937 - 1945)
    {"President": "Getúlio Vargas (x2)", "State": "Rio Grande do Sul"},
    {"President": "José Linhares", "State": "Ceará"},
# Quarta República (1945 - 1964)
    {"President": "Gaspar Dutra", "State": "Mato Grosso"},
    {"President": "Getúlio Vargas (x3)", "State": "Rio Grande do Sul"},
    {"President": "Café Filho", "State": "Rio Grande do Norte"},
    {"President": "Carlos Luz", "State": "Minas Gerais"},
    {"President": "Nereu Ramos", "State": "Santa Catarina"},
    {"President": "Juscelino Kubitschek", "State": "Minas Gerais"},
    {"President": "Jânio Quadros", "State": "Mato Grosso"},
    {"President": "Ranieri Mazzilli (x1)", "State": "São Paulo"},
    {"President": "João Goulart", "State": "Rio Grande do Sul"},

# Ditadura Militar (1964 - 1985)
    {"President": "Ranieri Mazzilli (x2)", "State": "São Paulo"},
    {"President": "Castelo Branco", "State": "Ceará"},
    {"President": "Costa e Silva", "State": "Rio de Janeiro"},
    {"President": "Pedro Aleixo", "State": "Minas Gerais"},
    {"President": "Aurélio de Lira Tavares", "State": "Paraíba"},
    {"President": "Augusto Rademaker", "State": "Rio de Janeiro"},
    {"President": "Márcio de Sousa Melo", "State": "Santa Catarina"},  
    {"President": "Emílio Médici", "State": "Rio Grande do Sul"},
    {"President": "Ernesto Geisel", "State": "Rio Grande do Sul"},
    {"President": "João Figueiredo", "State": "Rio de Janeiro"},

    # Sexta República (1985 - Present)
    {"President": "Tancredo Neves", "State": "Minas Gerais"},
    {"President": "José Sarney", "State": "Maranhão"},
    {"President": "Fernando Collor", "State": "Rio de Janeiro"},
    {"President": "Itamar Franco", "State": "Minas Gerais"},
    {"President": "Fernando Henrique Cardoso", "State": "Rio de Janeiro"},
    {"President": "Luiz Inácio Lula da Silva (x1)", "State": "Pernambuco"},
    {"President": "Dilma Rousseff", "State": "Minas Gerais"},
    {"President": "Michel Temer", "State": "São Paulo"},
    {"President": "Jair Bolsonaro", "State": "São Paulo"},
    {"President": "Luiz Inácio Lula da Silva (x2)", "State": "Pernambuco"}
] 

df = pd.DataFrame(brazil_data)

# Sort and group by state
df = df.sort_values(by=["State", "President"])
state_groups = df.groupby("State")["President"].apply(list).reset_index()

# Complete geographic coordinate map covering all included states
geo_coords = {
    "Acre": [-9.0238, -70.8120],
    "Pará": [-1.9981, -54.9306],
    "Distrito Federal": [-15.7938, -47.8828],
    "Paraíba": [-7.2400, -36.7820],
    "Bahia": [-12.9714, -38.5014],
    "Pernambuco": [-8.0543, -34.8813],
    "Alagoas": [-9.5713, -36.7820],
    "São Paulo": [-23.5505, -46.6333],
    "Rio de Janeiro": [-22.9068, -43.1729],
    "Minas Gerais": [-19.9167, -43.9345],
    "Rio Grande do Sul": [-30.0346, -51.2177],
    "Santa Catarina": [-27.5954, -48.5480],
    "Paraná": [-25.4290, -49.2671],
    "Mato Grosso": [-12.6819, -56.9211],
    "Ceará": [-3.7172, -38.5434],
    "Maranhão": [-2.5297, -44.3028],
    "Rio Grande do Norte": [-5.7945, -35.2110],
    "Mato Grosso do Sul": [-20.4697, -54.6201],
    "Espírito Santo": [-20.3155, -40.3128], 
    
}

# Base map centered on Brazil's core geographic mass
m = folium.Map(
    location=[-14.2350, -51.9253], 
    zoom_start=4, 
    tiles="CartoDB positron",
    min_zoom=3,
    max_zoom=7
)

for _, row in state_groups.iterrows():
    state = row["State"]
    presidents = row["President"]
    count = len(presidents)
    
    if state in geo_coords:
        president_list_html = "".join([f"<li style='margin-bottom:2px;'>{p}</li>" for p in presidents])
        popup_content = f"""
        <div style='font-family: Arial, sans-serif; font-size: 12px; width: 220px;'>
            <h4 style='margin:0 0 5px 0; color:#2e7d32; border-bottom: 1px solid #ddd; padding-bottom:3px;'>{state} State</h4>
            <b>Total Selected Presidentes:</b> {count}<br><br>
            <b>Presidentes Born Here:</b>
            <ul style='padding-left:15px; margin:5px 0 0 0; max-height: 180px; overflow-y: auto;'>{president_list_html}</ul>
        </div>
        """
        
        folium.CircleMarker(
            location=geo_coords[state],
            radius=12 + (count * 1.0),
            popup=folium.Popup(popup_content, max_width=260),
            tooltip=f"{state}: {count} Presidentes",
            color="#1b5e20", 
            fill=True,
            fill_color="#fbc02d", 
            fill_opacity=0.7,
            weight=2
        ).add_to(m)

output_file = "brazil_complete_regions_map.html"
m.save(output_file)
print(f"Complete map generated! Opening '{output_file}' right now.")

webbrowser.open(output_file)