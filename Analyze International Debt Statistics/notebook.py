#!/usr/bin/env python
# coding: utf-8

# ## 1. The World Bank's international debt data
# <p>It's not that we humans only take debts to manage our necessities. A country may also take debt to manage its economy. For example, infrastructure spending is one costly ingredient required for a country's citizens to lead comfortable lives. <a href="https://www.worldbank.org">The World Bank</a> is the organization that provides debt to countries.</p>
# <p>In this notebook, we are going to analyze international debt data collected by The World Bank. The dataset contains information about the amount of debt (in USD) owed by developing countries across several categories. We are going to find the answers to questions like: </p>
# <ul>
# <li>What is the total amount of debt that is owed by the countries listed in the dataset?</li>
# <li>Which country owns the maximum amount of debt and what does that amount look like?</li>
# <li>What is the average amount of debt owed by countries across different debt indicators?</li>
# </ul>
# <p><img src="https://assets.datacamp.com/production/project_754/img/image.jpg" alt></p>
# <p>The first line of code connects us to the <code>international_debt</code> database where the table <code>international_debt</code> is residing. Let's first <code>SELECT</code> <em>all</em> of the columns from the <code>international_debt</code> table. Also, we'll limit the output to the first ten rows to keep the output clean.</p>

# In[111]:


get_ipython().run_cell_magic('sql', '', 'postgresql:///international_debt\n\n--Returns 10 rows of all the columns for the international debt table \nSELECT *\nFROM international_debt\nLIMIT 10;')


# In[112]:


get_ipython().run_cell_magic('nose', '', '# %%nose needs to be included at the beginning of every @tests cell\n\nlast_output = _\n\ndef test_output():\n    correct_result_string = \'  country_name country_code                                     indicator_name  indicator_code                 debt\\n0  Afghanistan          AFG  Disbursements on external debt, long-term (DIS...  DT.DIS.DLXF.CD   72894453.700000003\\n1  Afghanistan          AFG  Interest payments on external debt, long-term ...  DT.INT.DLXF.CD   53239440.100000001\\n2  Afghanistan          AFG                  PPG, bilateral (AMT, current US$)  DT.AMT.BLAT.CD   61739336.899999999\\n3  Afghanistan          AFG                  PPG, bilateral (DIS, current US$)  DT.DIS.BLAT.CD   49114729.399999999\\n4  Afghanistan          AFG                  PPG, bilateral (INT, current US$)  DT.INT.BLAT.CD   39903620.100000001\\n5  Afghanistan          AFG               PPG, multilateral (AMT, current US$)  DT.AMT.MLAT.CD             39107845\\n6  Afghanistan          AFG               PPG, multilateral (DIS, current US$)  DT.DIS.MLAT.CD   23779724.300000001\\n7  Afghanistan          AFG               PPG, multilateral (INT, current US$)  DT.INT.MLAT.CD             13335820\\n8  Afghanistan          AFG         PPG, official creditors (AMT, current US$)  DT.AMT.OFFT.CD  100847181.900000006\\n9  Afghanistan          AFG         PPG, official creditors (DIS, current US$)  DT.DIS.OFFT.CD   72894453.700000003\'\n    try:\n        assert last_output.DataFrame().to_string() == correct_result_string\n    except AttributeError:\n        assert False, "Please ensure a SQL ResultSet is the output of the code cell."\n    except AssertionError:\n        assert False, "The results of the query are incorrect. Please review the instructions and check the hint if necessary."')


# ## 2. Finding the number of distinct countries
# <p>From the first ten rows, we can see the amount of debt owed by <em>Afghanistan</em> in the different debt indicators. But we do not know the number of different countries we have on the table. There are repetitions in the country names because a country is most likely to have debt in more than one debt indicator. </p>
# <p>Without a count of unique countries, we will not be able to perform our statistical analyses holistically. In this section, we are going to extract the number of unique countries present in the table. </p>

# In[113]:


get_ipython().run_cell_magic('sql', '', '\n--Returns the total count of countries \nSELECT \n    COUNT(DISTINCT country_name) AS total_distinct_countries\nFROM international_debt;')


# In[114]:


get_ipython().run_cell_magic('nose', '', '# %%nose needs to be included at the beginning of every @tests cell\n\nlast_output = _\n\ndef test_output():\n    correct_result_string = \'   total_distinct_countries\\n0                       124\'\n    try:\n        assert last_output.DataFrame().to_string() == correct_result_string\n    except AttributeError:\n        assert False, "Please ensure a SQL ResultSet is the output of the code cell."\n    except AssertionError:\n        assert False, "The results of the query are incorrect. Please review the instructions and check the hint if necessary."')


# ## 3. Finding out the distinct debt indicators
# <p>We can see there are a total of 124 countries present on the table. As we saw in the first section, there is a column called <code>indicator_name</code> that briefly specifies the purpose of taking the debt. Just beside that column, there is another column called <code>indicator_code</code> which symbolizes the category of these debts. Knowing about these various debt indicators will help us to understand the areas in which a country can possibly be indebted to. </p>

# In[115]:


get_ipython().run_cell_magic('sql', '', '\n--Shows all the unique indicator codes \nSELECT\n    DISTINCT indicator_code AS distinct_debt_indicators\nFROM international_debt\nORDER BY distinct_debt_indicators;')


# In[116]:


get_ipython().run_cell_magic('nose', '', '# %%nose needs to be included at the beginning of every @tests cell\n\nlast_output = _\n\ndef test_output():\n    correct_result_string = \'   distinct_debt_indicators\\n0            DT.AMT.BLAT.CD\\n1            DT.AMT.DLXF.CD\\n2            DT.AMT.DPNG.CD\\n3            DT.AMT.MLAT.CD\\n4            DT.AMT.OFFT.CD\\n5            DT.AMT.PBND.CD\\n6            DT.AMT.PCBK.CD\\n7            DT.AMT.PROP.CD\\n8            DT.AMT.PRVT.CD\\n9            DT.DIS.BLAT.CD\\n10           DT.DIS.DLXF.CD\\n11           DT.DIS.MLAT.CD\\n12           DT.DIS.OFFT.CD\\n13           DT.DIS.PCBK.CD\\n14           DT.DIS.PROP.CD\\n15           DT.DIS.PRVT.CD\\n16           DT.INT.BLAT.CD\\n17           DT.INT.DLXF.CD\\n18           DT.INT.DPNG.CD\\n19           DT.INT.MLAT.CD\\n20           DT.INT.OFFT.CD\\n21           DT.INT.PBND.CD\\n22           DT.INT.PCBK.CD\\n23           DT.INT.PROP.CD\\n24           DT.INT.PRVT.CD\'\n    try:    \n        assert last_output.DataFrame().to_string() == correct_result_string\n    except AttributeError:\n        assert False, "Please ensure a SQL ResultSet is the output of the code cell."\n    except AssertionError:\n        assert False, "The results of the query are incorrect. Please review the instructions and check the hint if necessary."')


# ## 4. Totaling the amount of debt owed by the countries
# <p>As mentioned earlier, the financial debt of a particular country represents its economic state. But if we were to project this on an overall global scale, how will we approach it?</p>
# <p>Let's switch gears from the debt indicators now and find out the total amount of debt (in USD) that is owed by the different countries. This will give us a sense of how the overall economy of the entire world is holding up.</p>

# In[117]:


get_ipython().run_cell_magic('sql', '', '\n--Shows the total amount of debt in dollars owe by each country\nSELECT \n    ROUND(SUM(debt)/1000000, 2) AS total_debt\nFROM international_debt;')


# In[118]:


get_ipython().run_cell_magic('nose', '', '# %%nose needs to be included at the beginning of every @tests cell\n\nlast_output = _\n\ndef test_output():\n    correct_result_string = \'   total_debt\\n0  3079734.49\'\n    try:\n        assert last_output.DataFrame().to_string() == correct_result_string\n    except AttributeError:\n        assert False, "Please ensure a SQL ResultSet is the output of the code cell."\n    except AssertionError:\n        assert False, "The results of the query are incorrect. Please review the instructions and check the hint if necessary."')


# ## 5. Country with the highest debt
# <p>"Human beings cannot comprehend very large or very small numbers. It would be useful for us to acknowledge that fact." - <a href="https://en.wikipedia.org/wiki/Daniel_Kahneman">Daniel Kahneman</a>. That is more than <em>3 million <strong>million</strong></em> USD, an amount which is really hard for us to fathom. </p>
# <p>Now that we have the exact total of the amounts of debt owed by several countries, let's now find out the country that owns the highest amount of debt along with the amount. <strong>Note</strong> that this debt is the sum of different debts owed by a country across several categories. This will help to understand more about the country in terms of its socio-economic scenarios. We can also find out the category in which the country owns its highest debt. But we will leave that for now. </p>

# In[119]:


get_ipython().run_cell_magic('sql', '', '\n--Shows the country with the highest total amount of debt \nSELECT \n    country_name, \n    SUM(debt) AS total_debt\nFROM international_debt\nGROUP BY country_name\nORDER BY total_debt DESC\nLIMIT 1;')


# In[120]:


get_ipython().run_cell_magic('nose', '', '# %%nose needs to be included at the beginning of every @tests cell\n\nlast_output = _\n\ndef test_output():\n    correct_result_string = \'  country_name              total_debt\\n0        China  285793494734.200001568\'\n    try:\n        assert last_output.DataFrame().to_string() == correct_result_string\n    except AttributeError:\n        assert False, "Please ensure a SQL ResultSet is the output of the code cell."\n    except AssertionError:\n        assert False, "The results of the query are incorrect. Please review the instructions and check the hint if necessary."')


# ## 6. Average amount of debt across indicators
# <p>So, it was <em>China</em>. A more in-depth breakdown of China's debts can be found <a href="https://datatopics.worldbank.org/debt/ids/country/CHN">here</a>. </p>
# <p>We now have a brief overview of the dataset and a few of its summary statistics. We already have an idea of the different debt indicators in which the countries owe their debts. We can dig even further to find out on an average how much debt a country owes? This will give us a better sense of the distribution of the amount of debt across different indicators.</p>

# In[121]:


get_ipython().run_cell_magic('sql', '', '\n--This query returns top 10 countries with the highest average amount of debt.\nSELECT \n    indicator_code AS debt_indicator,\n    indicator_name,\n    AVG(debt) AS average_debt\nFROM international_debt\nGROUP BY debt_indicator, indicator_name\nORDER BY average_debt DESC\nLIMIT 10;')


# In[122]:


get_ipython().run_cell_magic('nose', '', '# %%nose needs to be included at the beginning of every @tests cell\n\nlast_output = _\n\ndef test_output():\n    correct_result_string = \'   debt_indicator                                     indicator_name          average_debt\\n0  DT.AMT.DLXF.CD  Principal repayments on external debt, long-te...  5904868401.499193612\\n1  DT.AMT.DPNG.CD  Principal repayments on external debt, private...  5161194333.812658349\\n2  DT.DIS.DLXF.CD  Disbursements on external debt, long-term (DIS...  2152041216.890243888\\n3  DT.DIS.OFFT.CD         PPG, official creditors (DIS, current US$)  1958983452.859836046\\n4  DT.AMT.PRVT.CD          PPG, private creditors (AMT, current US$)  1803694101.963265321\\n5  DT.INT.DLXF.CD  Interest payments on external debt, long-term ...  1644024067.650806481\\n6  DT.DIS.BLAT.CD                  PPG, bilateral (DIS, current US$)  1223139290.398230108\\n7  DT.INT.DPNG.CD  Interest payments on external debt, private no...  1220410844.421518983\\n8  DT.AMT.OFFT.CD         PPG, official creditors (AMT, current US$)  1191187963.083064523\\n9  DT.AMT.PBND.CD                      PPG, bonds (AMT, current US$)  1082623947.653623188\'\n    try:\n        assert last_output.DataFrame().to_string() == correct_result_string\n    except AttributeError:\n        assert False, "Please ensure a SQL ResultSet is the output of the code cell."\n    except AssertionError:\n        assert False, "The results of the query are incorrect. Please review the instructions and check the hint if necessary."')


# ## 7. The highest amount of principal repayments
# <p>We can see that the indicator <code>DT.AMT.DLXF.CD</code> tops the chart of average debt. This category includes repayment of long term debts. Countries take on long-term debt to acquire immediate capital. More information about this category can be found <a href="https://datacatalog.worldbank.org/principal-repayments-external-debt-long-term-amt-current-us-0">here</a>. </p>
# <p>An interesting observation in the above finding is that there is a huge difference in the amounts of the indicators after the second one. This indicates that the first two indicators might be the most severe categories in which the countries owe their debts.</p>
# <p>We can investigate this a bit more so as to find out which country owes the highest amount of debt in the category of long term debts (<code>DT.AMT.DLXF.CD</code>). Since not all the countries suffer from the same kind of economic disturbances, this finding will allow us to understand that particular country's economic condition a bit more specifically. </p>

# In[123]:


get_ipython().run_cell_magic('sql', '', "\n--Select a country with the highes amount of principal repayments\nSELECT \n    country_name, \n    indicator_name\nFROM international_debt\nWHERE debt = (SELECT \n                 MAX(debt)\n             FROM international_debt\n             WHERE indicator_code = 'DT.AMT.DLXF.CD');")


# In[124]:


get_ipython().run_cell_magic('nose', '', '# %%nose needs to be included at the beginning of every @tests cell\n\nlast_output = _\n\ndef test_output():\n    correct_result_string = \'  country_name                                     indicator_name\\n0        China  Principal repayments on external debt, long-te...\'\n    try:\n        assert last_output.DataFrame().to_string() == correct_result_string\n    except AttributeError:\n        assert False, "Please ensure a SQL ResultSet is the output of the code cell."\n    except AssertionError:\n        assert False, "The results of the query are incorrect. Please review the instructions and check the hint if necessary."')


# ## 8. The most common debt indicator
# <p>China has the highest amount of debt in the long-term debt (<code>DT.AMT.DLXF.CD</code>) category. This is verified by <a href="https://data.worldbank.org/indicator/DT.AMT.DLXF.CD?end=2018&most_recent_value_desc=true">The World Bank</a>. It is often a good idea to verify our analyses like this since it validates that our investigations are correct. </p>
# <p>We saw that long-term debt is the topmost category when it comes to the average amount of debt. But is it the most common indicator in which the countries owe their debt? Let's find that out. </p>

# In[125]:


get_ipython().run_cell_magic('sql', '', '\n--This query shows the most frequent debt indicator\nSELECT\n    indicator_code,\n    COUNT(indicator_code) AS indicator_count\nFROM international_debt\nGROUP BY indicator_code\nORDER BY indicator_count DESC, indicator_code DESC\nLIMIT 20;')


# In[126]:


get_ipython().run_cell_magic('nose', '', '# %%nose needs to be included at the beginning of every @tests cell\n\nlast_output = _\n\ndef test_output():\n    correct_result_string = \'    indicator_code  indicator_count\\n0   DT.INT.OFFT.CD              124\\n1   DT.INT.MLAT.CD              124\\n2   DT.INT.DLXF.CD              124\\n3   DT.AMT.OFFT.CD              124\\n4   DT.AMT.MLAT.CD              124\\n5   DT.AMT.DLXF.CD              124\\n6   DT.DIS.DLXF.CD              123\\n7   DT.INT.BLAT.CD              122\\n8   DT.DIS.OFFT.CD              122\\n9   DT.AMT.BLAT.CD              122\\n10  DT.DIS.MLAT.CD              120\\n11  DT.DIS.BLAT.CD              113\\n12  DT.INT.PRVT.CD               98\\n13  DT.AMT.PRVT.CD               98\\n14  DT.INT.PCBK.CD               84\\n15  DT.AMT.PCBK.CD               84\\n16  DT.INT.DPNG.CD               79\\n17  DT.AMT.DPNG.CD               79\\n18  DT.INT.PBND.CD               69\\n19  DT.AMT.PBND.CD               69\'\n    try:\n        assert last_output.DataFrame().to_string() == correct_result_string\n    except AttributeError:\n        assert False, "Please ensure a SQL ResultSet is the output of the code cell."\n    except AssertionError:\n        assert False, "The results of the query are incorrect. Please review the instructions and check the hint if necessary."')


# ## 9. Other viable debt issues and conclusion
# <p>There are a total of six debt indicators in which all the countries listed in our dataset have taken debt. The indicator <code>DT.AMT.DLXF.CD</code> is also there in the list. So, this gives us a clue that all these countries are suffering from a common economic issue. But that is not the end of the story, but just a part of the story.</p>
# <p>Let's change tracks from <code>debt_indicator</code>s now and focus on the amount of debt again. Let's find out the maximum amount of debt that each country has. With this, we will be in a position to identify the other plausible economic issues a country might be going through.</p>
# <p>In this notebook, we took a look at debt owed by countries across the globe. We extracted a few summary statistics from the data and unraveled some interesting facts and figures. We also validated our findings to make sure the investigations are correct.</p>

# In[127]:


get_ipython().run_cell_magic('sql', '', '\n--This query shows the top 10 countries with the maximum debt\nSELECT \n    country_name,\n    MAX(debt) AS maximum_debt\nFROM international_debt\nGROUP BY country_name\nORDER BY maximum_debt DESC\nLIMIT 10;\n')


# In[128]:


get_ipython().run_cell_magic('nose', '', '# %%nose needs to be included at the beginning of every @tests cell\n\nlast_output = _\n\ndef test_output():\n    correct_result_string = \'                                   country_name           maximum_debt\\n0                                         China  96218620835.699996948\\n1                                        Brazil  90041840304.100006104\\n2                            Russian Federation          66589761833.5\\n3                                        Turkey  51555031005.800003052\\n4                                    South Asia  48756295898.199996948\\n5  Least developed countries: UN classification  40160766261.599998474\\n6                                      IDA only  34531188113.199996948\\n7                                         India  31923507000.799999237\\n8                                     Indonesia  30916112653.799999237\\n9                                    Kazakhstan  27482093686.400001526\'\n    try:\n        assert last_output.DataFrame().to_string() == correct_result_string\n    except AttributeError:\n        assert False, "Please ensure a SQL ResultSet is the output of the code cell."\n    except AssertionError:\n        assert False, "The results of the query are incorrect. Please review the instructions and check the hint if necessary."')

