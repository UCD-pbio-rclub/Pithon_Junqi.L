def online_fa_seq_count (url):
    import urllib.request
    response = urllib.request.urlopen(url)
    lines = response.readlines()
    name_list = lines [0::2] # The 1st name appears on the 0th line, then it appears on every 2nd line.
    seq_list = lines [1::2] # The 1st seq appears on the 1st line, then it appears on every 2nd line.

    true_name_list = []
    true_seq_list = []
    for i in range (len (name_list)):
        true_name_list.append (str(name_list [i]).replace ("b'",'').replace ("\\r\\n'",'')) 
        true_seq_list.append (str(seq_list [i]).replace ("b'",'').replace ("\\r\\n",'').replace ("'",'')) 
    name_seq = dict(zip(true_name_list, true_seq_list))

    print ('>>> Your name-seq dictionary (fasta file) looks like: ')
    print (name_seq)
    print ('>>> The number of sequences in this fasta file is ' + str (len (name_seq)))
