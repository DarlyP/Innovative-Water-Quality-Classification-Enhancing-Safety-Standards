import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.models.formatters import NumeralTickFormatter
from bokeh.plotting import figure
from bokeh.models import HoverTool, NumeralTickFormatter
from bokeh.layouts import gridplot
from bokeh.palettes import Category20
import seaborn as sns

# Fungsi EDA Scatterplot dengan Regresi menggunakan Bokeh
def scatter_plot_regression(df, x_col='Year', y_col='Salary', x_label='Tahun', y_label='Gaji Rata-rata', title='Diagram Sebaran dengan Garis Regresi'):
    # Konversi data menjadi array numpy
    x_data = df[x_col].values
    y_data = df[y_col].values
    
    # Membuat model regresi linier
    model = np.polyfit(x_data, y_data, 1)
    y_pred = np.polyval(model, x_data)
    
    # Buat ColumnDataSource
    source = ColumnDataSource(data={x_col: x_data, y_col: y_data, 'regression_line': y_pred})
    
    # Buat plot baru dengan judul dan label sumbu
    p = figure(title=title, x_axis_label=x_label, y_axis_label=y_label, width=800, height=400,
               tools="pan,box_zoom,wheel_zoom,reset,save")

    # Tambahkan diagram sebaran
    p.circle(x_col, y_col, source=source, size=8, color="navy", alpha=0.5, legend_label=y_label)

    # Tambahkan garis regresi
    p.line(x_col, 'regression_line', source=source, line_width=2, line_color="red", legend_label="Garis Regresi")
    
    # Tambahkan alat hover untuk menampilkan nilai data
    hover = HoverTool()
    hover.tooltips = [(x_label, f"@{x_col}"), (y_label, f"@{y_col}")]
    p.add_tools(hover)
    
    # Sesuaikan gaya label sumbu
    p.xaxis.axis_label_text_font_style = "bold"
    p.yaxis.axis_label_text_font_style = "bold"
    
    # Atur format untuk sumbu Y agar menampilkan nilai tanpa notasi ilmiah
    p.yaxis.formatter = NumeralTickFormatter(format="0")
    
    # Sesuaikan plot
    p.legend.location = "top_left"
    p.legend.click_policy = "hide"
    
    # Tampilkan plot menggunakan st.bokeh_chart()
    st.bokeh_chart(p)

# Fungsi EDA untuk IQR plot & Histogram 1 Kolom
def histogram_boxplot(df, nama_kolom, judul="Contoh Bar Plot"):
    # Ekstrak data kolom
    data_kolom = df[nama_kolom]

    # Plot histogram
    hist, edges = np.histogram(data_kolom, bins=20)

    # Generate random colors for the bars
    colors = random.choices(Category20[20], k=len(hist))

    p1 = figure(title=f"{judul} (Histogram)", tools="save,hover", background_fill_color="#fafafa",
                width=600, height=400, tooltips=[("Jumlah", "@top"), ("Interval", "@left{0.00} hingga @right{0.00}")],
                x_axis_label=judul, y_axis_label="Frequency")

    p1.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], 
            fill_color=colors, line_color="white", alpha=0.7)

    # Box plot
    q1 = data_kolom.quantile(0.25)
    q2 = data_kolom.quantile(0.50)
    q3 = data_kolom.quantile(0.75)
    iqr = q3 - q1

    lower_whisker = data_kolom[data_kolom >= (q1 - 1.5 * iqr)].min()
    upper_whisker = data_kolom[data_kolom <= (q3 + 1.5 * iqr)].max()

    outliers = data_kolom[(data_kolom > upper_whisker) | (data_kolom < lower_whisker)]

    p2 = figure(title=f"{judul} (Boxplot)", tools="save,hover", background_fill_color="#fafafa",
                width=400, height=400, tooltips=[("Nilai", "@y"), ("Q1", f"{q1:.2f}"), 
                                                 ("Q2 (Median)", f"{q2:.2f}"), ("Q3", f"{q3:.2f}"), 
                                                 ("Lower Whisker", f"{lower_whisker:.2f}"), 
                                                 ("Upper Whisker", f"{upper_whisker:.2f}")])

    # Menambahkan elemen diagram kotak
    p2.segment(1, lower_whisker, 1, q1, line_color="black")
    p2.segment(1, q3, 1, upper_whisker, line_color="black")
    p2.vbar(1, 0.7, q1, q3, fill_color="navy", line_color="black")
    p2.vbar(1, 0.7, q2, q2, line_color="black")

    # Whiskers
    p2.rect(1, lower_whisker, 0.2, 0.01, line_color="black")
    p2.rect(1, upper_whisker, 0.2, 0.01, line_color="black")

    # Outliers
    p2.scatter([1]*len(outliers), outliers, size=6, color="red", fill_alpha=0.6)

    # Menghapus label sumbu dan tanda sumbu pada boxplot
    p2.xaxis.axis_label = ""
    p2.yaxis.axis_label = ""
    p2.xaxis.visible = False
    p2.yaxis.visible = False

    # Set gaya label sumbu dan tanda sumbu
    p1.xaxis.axis_label_text_font_style = "bold"
    p1.xaxis.axis_label_text_font_size = "10pt"
    p1.xaxis.major_label_text_font_style = "bold"
    p1.xaxis.major_label_text_font_size = "8pt"
    p1.yaxis.axis_label_text_font_style = "bold"
    p1.yaxis.axis_label_text_font_size = "10pt"
    p1.yaxis.major_label_text_font_style = "bold"
    p1.yaxis.major_label_text_font_size = "8pt"

    # Menghapus garis grid
    p1.grid.grid_line_color = None
    p2.grid.grid_line_color = None

    # Mengatur formatter sumbu agar tidak menggunakan notasi ilmiah
    p1.yaxis.formatter.use_scientific = False
    p1.xaxis.formatter.use_scientific = False

    # Menata plot dalam grid
    grid = gridplot([[p1, p2]])

    # Tampilkan plot menggunakan st.bokeh_chart()
    st.bokeh_chart(grid)


def run():
    # Membuat judul
    st.title('Water Quality')

    # Membuat Sub Header
    st.header('Water Quality Data Visualization', divider='gray')

    # Menambahkan Gambar
    image = Image.open('water.jpg')
    st.image(image, caption = 'Water Pollution (wallpapers.com)', channels='RGB')

    # Menambahkan Divider
    st.divider()

    # Menampilkan Dataframe
    st.header('Dataframe', divider='gray')
    df = pd.read_csv('water_quality.csv')
    st.dataframe(df)
    st.divider()

    # Display descriptive statistics for all numeric columns
    # Fungsi Untuk Menghitung Mean, Median, Mode dan Mengevaluasi Distribusi
    def evaluate_distribution(col):
        mean = col.mean()
        median = col.median()
        mode = col.mode()[0]  # Ambil mode pertama jika ada beberapa mode
        if (abs(mean - median) / mean <= 0.05 and abs(mean - mode) / mean <= 0.05):
            evaluasi = 'Normal Distribution'
        elif mean > median:
            evaluasi = 'Positive Skewness'
        else:
            evaluasi = 'Negative Skewness'
        return pd.Series({'Mean': mean, 'Median': median, 'Mode': mode, 'Evaluasi': evaluasi})

    # Memilih Hanya Kolom Numerik
    numerical_cols = df.select_dtypes(include=[np.number])

    # Terapkan Fungsi ke Setiap Kolom Numerik dalam DataFrame
    result = numerical_cols.apply(evaluate_distribution)
    st.header('Descriptive Statistics', divider='gray')
    st.write(result)
    st.divider()

    st.header('Correlation Bacteria and Viruses', divider='gray')
    scatter_plot_regression(df, x_col='bacteria', y_col='viruses', x_label='Bacteria', y_label='Viruses', title='Correlation Bacteria and Viruses')
    st.divider()

    st.header('Correlation Arsenic and Selenium', divider='gray')
    scatter_plot_regression(df, x_col='arsenic', y_col='selenium', x_label='Arsenic', y_label='Selenium', title='Correlation Arsenic and Selenium')
    st.divider()

    st.header('Correlation Lead and Copper', divider='gray')
    scatter_plot_regression(df, x_col='lead', y_col='copper', x_label='Lead', y_label='copper', title='Correlation Lead and Copper')
    st.divider()

    st.header('Correlation Lead and Copper', divider='gray')
    scatter_plot_regression(df, x_col='chloramine', y_col='bacteria', x_label='Chloramine', y_label='Bacteria', title='Correlation Chloramine and Bacteria')
    st.divider()


    # Fungsi untuk menghitung korelasi dan menampilkan hasilnya di Streamlit
    def tampilkan_korelasi(df):
        # Hitung korelasi
        cor = df.corr()
        
        # Membuat DataFrame dari Matriks Korelasi
        cor_df = pd.DataFrame(cor.stack(), columns=['Correlation'])
        
        # Menambahkan Kolom Baris dan Kolom
        cor_df.reset_index(inplace=True)
        cor_df.columns = ['Variable 1', 'Variable 2', 'Correlation']
        
        # Menambahkan Kolom Interpretasi
        cor_df['Interpretation'] = np.where(cor_df['Correlation'] < 0.05, 'Ada korelasi', 'Tidak ada korelasi')
        
        # Menampilkan DataFrame menggunakan Streamlit
        st.dataframe(cor_df)

        # Menampilkan heatmap korelasi
        st.write("Heatmap Korelasi:")
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(cor, annot=True, fmt=".2f", cmap='coolwarm', ax=ax)
        st.pyplot(fig)

    # Implementasi Streamlit
    def main():
        # Tombol untuk menghitung dan menampilkan korelasi
        if st.button('Hitung Korelasi'):
            tampilkan_korelasi(df)

    st.divider()

    st.header('Aluminium Bar Plot', divider='gray')
    histogram_boxplot(df, 'aluminium', judul="Aluminium Plot")
    st.divider()

    st.header('Arsenic Bar Plot', divider='gray')
    histogram_boxplot(df, 'arsenic', judul="Arsenic Plot")
    st.divider()

    # Fungsi untuk membuat pie chart
    def plot_pie_chart(df, column):
        # Menghitung distribusi nilai dalam kolom
        value_counts = df[column].value_counts()
        
        # Set up the matplotlib figure
        fig, ax = plt.subplots(figsize=(8, 8))

        # Create the pie chart
        ax.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)

        # Set title
        plt.title(f'Pie Chart for {column}')

        # Display the plot
        st.pyplot(fig)

    # Menambahkan Gambar
    image2 = Image.open('output.png')
    st.header('Feature Selection', divider='gray')
    st.image(image2, caption = 'Feature Selection', channels='RGB')

    # Menampilkan gambar menggunakan tombol
    if st.button('Show Image'):
        # Gantilah 'image2.png' dengan jalur ke file gambar Anda
        image_path = 'water1.jpeg'
        st.image(image_path, caption='Nickel Processing Factory (Smelter) in the Obi Island Industrial Area, North Maluku Province.', channels='RGB')

if __name__ == '__main__':
   run()
