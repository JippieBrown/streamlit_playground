import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
from toolbox.db_tools import read_db
from st_aggrid import AgGrid



import numpy as np
import plotly.figure_factory as ff


st.set_page_config(page_title="Test",
                   page_icon="",
                   layout="wide"
)




df = [dict(Task="Zamosc-Installation", Start='2023-01-09', Finish='2023-02-17', Resource='Tudor Manolache'),
      dict(Task="Zamosc-Commissioning", Start='2023-01-30', Finish='2023-02-17', Resource='Martin Langenhuizen'),
      dict(Task="Czechnica Tauron - Installation", Start='2023-01-24', Finish='2023-04-30', Resource='Lech Kozuba'),
      dict(Task="Czechnica Tauron - Commissioning", Start='2023-02-20', Finish='2023-02-17', Resource='Complete'),
      dict(Task="Abramowice - Installation", Start='2023-02-15', Finish='2023-04-30', Resource='Tudor Manolache'),
      dict(Task="Abramowice - Commissioning", Start='2023-04-01', Finish='2023-04-20', Resource='Martin Langenhuizen'),
      dict(Task="EC Czechnica (Kraftwerk) - Installation", Start='2023-02-15', Finish='2023-06-18', Resource='Complete'),
      dict(Task="EC Czechnica (Kraftwerk) - Commissioning", Start='2023-01-14', Finish='2023-03-14', Resource='Martin Langenhuizen')
      ]

colors = {'Tudor Manolache': 'rgb(220, 0, 0)',
          'Martin Langenhuizen': (1, 0.9, 0.16),
          'Lech Kozuba': 'rgb(0, 255, 100)',
          'Complete': 'rgb(0, 255, 100)'}

fig = ff.create_gantt(df, colors=colors, index_col='Resource', show_colorbar=True,
                      group_tasks=True,showgrid_x=True, showgrid_y=True)
# fig.show()




# Plot!
st.plotly_chart(fig)#, use_container_width=True)







# # Add histogram data
# x1 = np.random.randn(200) - 2
# x2 = np.random.randn(200)
# x3 = np.random.randn(200) + 2

# # Group data together
# hist_data = [x1, x2, x3]

# group_labels = ['Group 1', 'Group 2', 'Group 3']

# # Create distplot with custom bin_size
# fig = ff.create_distplot(
#         hist_data, group_labels, bin_size=[.1, .25, .5])








# st.set_page_config(page_title="Test",
#                    page_icon=":poop:",
#                    layout="wide"
# )


# test = read_db('static_content.db','dropdown_elements','plant_type')
# test2 = read_db('static_content.db','dropdown_elements','hv_plug_size')
# # gis_type = st.selectbox("Menu",test)

# df_planner = pd.DataFrame(
#     np.array([["scope", "", "", ""]]),
#     columns=['Scope', 'Scope_description','Start','Finish'])

# df_planner['Start'] = df_planner['Start'].astype('datetime64')
# df_planner['Finish'] = df_planner['Finish'].astype('datetime64')

# # st.table(df)
# grid_response = AgGrid(
#     df_planner,
#     editable=True, 
#     height=300, 
#     width='100%',
#     )

# updated = grid_response['data']
# df = pd.DataFrame(updated) 

# # AgGrid(df_planner,editable=True)

# # with st.container():
# # col1, col2, col3 = st.columns([1,2,1])

# # col1.markdown("")

# # col2.markdown(st.selectbox("",test))

# # col3.markdown(st.selectbox("",test2))





# gantt_css = open("html/gantt_css.html", 'r', encoding='utf-8')
# gantt_html = open("html/gantt.html", 'r', encoding='utf-8')

# gantt_chart = components.html(gantt_css.read() + gantt_html.read(),height=1200)

