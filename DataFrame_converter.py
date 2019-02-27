import HTML_Gen as H
import Month_DF
import calendar

class Dataframe_converter:

    def Df_to_list(self,dataframe,monthNum):

        dtMonths=Month_DF.SQLToDataFrames().monthDF(dataframe,monthNum)
        header = list(dtMonths.columns.values)
        row_data = dtMonths.values.tolist()
        row_data.insert(0,header)
        return H.CreateHTMLTable().createHTML(row_data, calendar.month_name[monthNum])
