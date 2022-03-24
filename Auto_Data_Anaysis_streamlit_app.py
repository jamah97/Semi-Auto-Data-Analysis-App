# Core Pkgs
import streamlit as st


# EDA pkgs
import pandas as pd
import numpy as np


# Data Viz Pkg
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)

def main():

	st.title("Semi Auto Data Analysis App")

	activites = ["About","EDA"]

	choice = st.sidebar.selectbox("Select Activity",activites)

	if choice == 'About':
		st.subheader("About Section")
		st.write("Creator of Application Hassan Jama. The purpose of the application is to perform basic exploratory data analysis along with visualization that may be useful to the end-user. The application is intended to help non-technical personnel gain meaningful insights from their data. The application takes in CSV files only, after uploading files the end-user will be able to analyze the data.")


	if choice == 'EDA':
		st.subheader("Exploratory Data Analysis")

		data = st.file_uploader("Upload Dataset",type=["csv"])
		if data is not None:
			df = pd.read_csv(data)

			if st.checkbox("Preview Dataset"):
				try:
					st.dataframe(df.head(int(st.text_input("Select Number of Rows To View"))))
				except ValueError:
					pass

			if st.checkbox("Show data types"):
				st.write(df.info())
				#st.write(df.dtypes.value_counts())

			if st.checkbox("Show missing data"):
				st.write(df.isnull().sum())

			if st.checkbox("Show shape"):
				st.write(df.shape)

			if st.checkbox("Show Columns"):
				all_columns = df.columns.to_list()
				st.write(all_columns)

			if st.checkbox("Select Columns To Show"):
				all_columns2 = df.columns.to_list()
				selected_columns = st.multiselect("Select Columns",all_columns2)
				new_df =  df[selected_columns]
				st.dataframe(new_df)

			if st.checkbox("Show Summary of statistical data"):
				st.write(df.describe())

			if st.checkbox("Value counts"):
				cv= df.columns.tolist()
				columnsx = st.selectbox("Select Categorical Column",cv)
				for i in df.columns:
						if columnsx == i:
							st.dataframe(df[i].value_counts())

			if st.checkbox("Correlation of dataset"):
				st.write(df.corr())
				st.write(sns.heatmap(df.corr(),annot=True))
				st.pyplot()



			cv2= df.columns.tolist()
			
			if st.checkbox('Scatterplot'):
				columnsx = st.selectbox("Select X Column",cv2)
				columnsy = st.selectbox("Select Y Column",cv2)
				st.write(sns.regplot(x = columnsx, y = columnsy, data = df))
				st.pyplot()


			type_of_plot = st.selectbox("Select Type of Plot for categorical variable",["Pie plot","Bar plot"])
			selected_columns_names = st.selectbox("Select Columns To Plot",cv2)


			if st.button("Generate Plot"):
				st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))

				# Plot By Streamlit
				if type_of_plot == 'Pie plot':
					cust_data = df[selected_columns_names]
					pie_plot = cust_data.value_counts().plot.pie(autopct="%1.1f%%")
					st.write(pie_plot)
					st.pyplot()

				# Plot By Streamlit
				if type_of_plot == 'Bar plot':
			#cust_data = df[selected_columns_names]
					st.write(sns.countplot(x=selected_columns_names, data = df, palette = 'deep'))
					st.pyplot()



if __name__ == '__main__':
	main()
