import pandas as pd
import streamlit as st
import plotly.express as px


APP_TITLE = 'Electoral Bonds Dashboard'
APP_SUBTITLE = 'Source: State Bank of India'

with open("styles.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


def main():

    st.title(APP_TITLE)
    st.caption(APP_SUBTITLE)

    img = st.image(
        'CCI_UDHindu_KSL_URO5O15EU_R1555596349_0_cec15fbe-6287-4ffa-80d2-58a64c787a79.jpg', use_column_width=True)

    df = pd.read_csv('bonds.csv')

    dist = st.markdown('### Distribution of Bonds ₹')
    # cap = st.caption('Among Parties')

# The Tree Map Visulation
    fig = px.treemap(df, path=[px.Constant('All Parties'), 'pol_party'], values='price',
                     color='price',
                     color_continuous_scale=px.colors.sequential.Mint,
                     hover_data=['pol_party', 'price']
                     )
    fig.update_traces(marker=dict(cornerradius=5))
    fig.update_traces(root_color="lightgrey")
    st.plotly_chart(figure_or_data=fig, use_container_width=True)


# Side bar

    unique = df.pol_party.unique()
    side_sel_party = st.sidebar.radio(
        "Select the Political Party", options=unique)

    df = df[df['pol_party'] == side_sel_party]
    metric_total = df['price'].sum()
    avg_total = metric_total/df.price.count()

    st.write(f'{side_sel_party}')

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label='Total Amount of Bonds Purchased in ₹', value="{:,}".format(metric_total))
    with col3:
        st.metric(label='Avg Amount in ₹',
                  value="{:,}".format(round(avg_total)))

    st.markdown('### Data in CSV')
    st.dataframe(df,
                 column_config={
                     "encashment_date": "Date of Cashing",
                     "pol_party": "Political Party",
                     "purchased_date": "Date of Purchasing",
                     "purchaser_name": "Purchaser Name",
                     "price": "Price"
                 }, use_container_width=True)


if __name__ == '__main__':
    main()
