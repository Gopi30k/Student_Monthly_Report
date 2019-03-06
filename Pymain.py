import Queries_FileHandling as H_GA
import Query_Extract as QE
import DataFrame_converter as DC
import Month_DF as MD
import LogGen as logging
import sys
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")


if  __name__ == '__main__':
    try:
        queryObj=QE.Query_To_List()
        sql_cmds=queryObj.getQuery_as_List('Queries.sql')
    except Exception:
        logging.logger.error("Query List generation error")
    else:
        logging.logger.info("Query List Generated ")
    dataFrameObj=MD.SQLToDataFrames()
    try:

        list_of_DFS= dataFrameObj.createDF(sql_cmds)
    except Exception:
        logging.logger.error("Dataframe could not be generated")
    else:
        logging.logger.info("Dataframe created out of SQL Data")


    htmlcode=""
    for i in range(1,13):
        htmlcode+=DC.Dataframe_converter().Df_to_list(list_of_DFS[0],i)

    HtmlFileName="Student_monthly_report.html"
    FileWriteObj=H_GA.FILE_handling()
    try:

        FileWriteObj.writeToFile(HtmlFileName,htmlcode)
    except Exception:
        logging.logger.error("Writing to File %s Err",HtmlFileName)
    else:
        logging.logger.info("Html File Report : %s created",HtmlFileName)


