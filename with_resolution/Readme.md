Some scripts which are taking into account the resolution of structures and the best resolution  of each domain structures
<b>check3.py</b> and <b>uniprotintpfam4.py</b> calculate <i> interaction mode </i> of domains and the number of structures belonging to each domain;<br>
 <b>checkfamilies3.py</b> and<b> familiesintpfam.py</b> calculate <i>interaction class</i> of families and the number of structures belonging to each  domain;<br>
<br>
<b>sqlcountcorrone_fam.py</b> - the template for calculating the number of  families for each <i>interaction class</i> (class) <br>
<b>sqlcountcorronedom.py</b> - the template for calculating the number of  domains for each <i>interaction mode</i> (class) <br>
<b>sqlcountcorrone_structs.py</b> - the template for calculating the number of  structures for each <i>interaction mode</i> (class) <br>
<b>tablestructs.py, tablestructs_run.py</b> for each <i>interaction class</i> calculates the number of structures and the number of domains belonging to families with this <i>interaction class</i> <br>
<b>tablestructs.py, tablestructsrun.py</b> for each <i>interaction class</i> calculates the number of structures and the number of domains belonging to families with this <i>interaction class</i> <br>
<b>tablestructsdom.py, tablestructsrundom.py</b> for each <i>interaction mode</i> calculates the number of structures and the number of families belonging to domains with this <i>interaction mode</i> <br>
<b>tablestructs2.py, tablestructsrun2.py</b> for each <i>interaction mode</i>  calculates the number of families and the number of domains belonging to structures with this <i>interaction mode</i> <br>
 <b>res.py</b>  - calculates resolutions for structures<br>
 <b> listresdomains.py</b> chooses domains with a good resolution<br>
 <b>listresstructs.py</b> chooses structures with a good resolution<br>
  <b> pdball.py</b> calculates the number of structures obtained with electron microscopy, nmr and x-ray<br>
 <b>throw.py</b> adds NULL to families that don't have three domains with non-empty <i>interaction modes</i> and throws them away for further calculations<br>
 <b>sort.py</b> sorts the file with <i>interaction modes</i> for structures<br>
 <b>xray.py</b> makes a file with a structure of complex and the way it was obtained (nmr, electron microscopy, xray diffraction) in one line<br>
 <b> PF00046xray.py</b> calculates the number with nmr and xray ways of obtaining the structure for the family with the Pfam identificator PF00046(homeodomain)<br>
 <b> PF00046.py</b> calculates the number of domains and structures represented in NPIDB for the family with the Pfam identificator PF00046(homeodomain)<br>
