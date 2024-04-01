import pandas as pd
import streamlit as st
import plotly.express as px

APP_TITLE = 'Electoral Bonds Dashboard'
APP_SUBTITLE = 'Source: State Bank of India'


def main():

    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUBTITLE)

    df = pd.read_csv('bonds.csv')

    st.markdown('### Distribution of Bonds $')
    st.caption('Among Parties')

# The Tree Map Visulation
    fig = px.treemap(df, path=[px.Constant('All Parties'), 'pol_party'], values='price',
                     color='price',
                     color_continuous_scale=px.colors.sequential.Mint,
                     hover_data=['pol_party', 'price']
                     )
    fig.update_traces(marker=dict(cornerradius=5))
    fig.update_traces(root_color="lightgrey")
    st.plotly_chart(figure_or_data=fig, use_container_width=True)

    # write(df[df['pol_party'] == sel_party].head())

# Side bar

    side_sel_party = st.sidebar.selectbox(
        "Select the Political Party", options=df.pol_party.unique())

    st.write(df[df['pol_party'] == side_sel_party])


if __name__ == '__main__':
    main()
