import HTML_Gen as H
import Month_DF
import calendar
import LogGen as log
class Dataframe_converter:

    def Df_to_list(self,dataframe,monthNum):
        tempDF=dataframe
        try:
            dtMonths=Month_DF.SQLToDataFrames().monthDF(tempDF,monthNum)
        except Exception:
            log.logger.info("Month dataframe for %s generation Error",calendar.month_name[monthNum])
        else:
            log.logger.info("Month dataframe for %s generated", calendar.month_name[monthNum])
        header = list(dtMonths.columns.values)
        row_data = dtMonths.values.tolist()
        row_data.insert(0,header)
        return H.CreateHTMLTable().createHTML(row_data, calendar.month_name[monthNum])
