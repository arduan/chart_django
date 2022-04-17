from chart.models import GDP
from django.shortcuts import render
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.models import ColumnarDataSource
import pandas
import plotly.express as px


def chart(request):
    gdp = GDP.objects.order_by('date')

    fig = px.line(
        x=gdp.values_list('date', flat=True),
        y=gdp.values_list('average', flat=True)
    )

    chart = fig.to_html()
    context = {'chart': chart}
    return render(request, 'line.html', context)

#
# def line(request):
#     country = request.GET.get('country', 'Germany')
#     gdps = GDP.objects.filter(country=country).order_by('year')
#
#     country_years = [d.year for d in gdps]
#     country_gdps = [d.gdp for d in gdps]
#     cds = ColumnarDataSource(data=dict(country_years=country_years, country_gdps=country_gdps))
#
#     fig = figure(height=500, title=f"{country} GDP")
#
#     fig.line(x='country_years', y='country_gdps', source=cds, line_width=2)
#
#     scrip, div = components(fig)
#
#     context = {
#         'scrip': scrip,
#         'div': div
#     }
#     return render(request, 'line.html', context)
