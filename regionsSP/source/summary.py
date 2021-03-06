    if districtRegion1=="DRS 05 - Barretos":
        date="2020-04-01"
        #initial condition for susceptible
        s0=10.0e3
        #initial condition for exposed   
        e0=1e-4
        #initial condition for infectious   
        i0=1e-4
        #initial condition for recovered
        r0=1e-4
        #initial condition for deaths   
        k0=1e-4
        #initial condition for asymptomatic   
        a0=1e-4
        #start fitting when the number of cases >= start
        start=0
        #how many days is the prediction
        prediction_days=70
        #as recovered data is not available, so recovered is in function of death
        ratioRecovered=.08
        #weigth for fitting data
        weigthCases=0.4
        weigthRecov=0.0
        #weightDeaths = 1 - weigthCases - weigthRecov

    if districtRegion1=="DRS 01 - Grande São Paulo":
        date="2020-03-15"
        #initial condition for susceptible
        s0=280.0e3
        #initial condition for exposed   
        e0=1e-4
        #initial condition for infectious   
        i0=1e-4
        #initial condition for recovered
        r0=1e-4
        #initial condition for deaths   
        k0=80
        #initial condition for asymptomatic   
        a0=1e-4
        #start fitting when the number of cases >= start
        start=1500
        #how many days is the prediction
        prediction_days=70
        #as recovered data is not available, so recovered is in function of infected
        ratioRecovered=0.1
        #weigth for fitting data
        weigthCases=0.6
        weigthRecov=0.1
        #weightDeaths = 1 - weigthCases - weigthRecov

    if districtRegion1=="DRS 04 - Baixada Santista":
        date="2020-04-01"
        #initial condition for susceptible
        s0=8.0e3
        #initial condition for exposed   
        e0=1e-4
        #initial condition for infectious   
        i0=1e-4
        #initial condition for recovered
        r0=1e-4
        #initial condition for deaths   
        k0=1e-4
        #initial condition for asymptomatic   
        a0=1e-4
        #start fitting when the number of cases >= start
        start=0
        #how many days is the prediction
        prediction_days=150
        #as recovered data is not available, so recovered is in function of death
        ratioRecovered=.1
        #weigth for fitting data
        weigthCases=0.4
        weigthRecov=0.1
        #weightDeaths = 1 - weigthCases - weigthRecov

    if districtRegion1=="DRS 06 - Bauru":
        date="2020-04-01"
        #initial condition for susceptible
        s0=10.0e3
        #initial condition for exposed   
        e0=1e-4
        #initial condition for infectious   
        i0=4
        #initial condition for recovered
        r0=1e-4
        #initial condition for deaths   
        k0=1e-4
        #initial condition for asymptomatic   
        a0=1e-4
        #start fitting when the number of cases >= start
        start=0
        #how many days is the prediction
        prediction_days=70
        #as recovered data is not available, so recovered is in function of death
        ratioRecovered=.1
        #weigth for fitting data
        weigthCases=0.4
        weigthRecov=0.0
        #weightDeaths = 1 - weigthCases - weigthRecov

    if districtRegion1=="DRS 17 - Taubaté":
        date="2020-04-01"
        #initial condition for susceptible
        s0=10.0e3
        #initial condition for exposed   
        e0=1e-4
        #initial condition for infectious   
        i0=17
        #initial condition for recovered
        r0=1e-4
        #initial condition for deaths   
        k0=2
        #initial condition for asymptomatic   
        a0=1e-4
        #start fitting when the number of cases >= start
        start=0
        #how many days is the prediction
        prediction_days=70
        #as recovered data is not available, so recovered is in function of death
        ratioRecovered=.08
        #weigth for fitting data
        weigthCases=0.4
        weigthRecov=0.0
        #weightDeaths = 1 - weigthCases - weigthRecov

if districtRegion1=="DRS 06 - Bauru":
        date="2020-04-01"
        #initial condition for susceptible
        s0=10.0e3
        #initial condition for exposed   
        e0=1e-4
        #initial condition for infectious   
        i0=4
        #initial condition for recovered
        r0=1e-4
        #initial condition for deaths   
        k0=1e-4
        #initial condition for asymptomatic   
        a0=1e-4
        #start fitting when the number of cases >= start
        start=0
        #how many days is the prediction
        prediction_days=70
        #as recovered data is not available, so recovered is in function of death
        ratioRecovered=.1
        #weigth for fitting data
        weigthCases=0.4
        weigthRecov=0.0
        #weightDeaths = 1 - weigthCases - weigthRecov

    if districtRegion1=="DRS 13 - Ribeirão Preto":
        date="2020-03-25"
        #initial condition for susceptible
        s0=5.0e3
        #initial condition for exposed   
        e0=1e-4
        #initial condition for infectious   
        i0=1e-4
        #initial condition for recovered
        r0=1e-4
        #initial condition for deaths   
        k0=1e-4
        #initial condition for asymptomatic   
        a0=1e-4
        #start fitting when the number of cases >= start
        start=5
        #how many days is the prediction
        prediction_days=60
        #as recovered data is not available, so recovered is in function of death
        ratioRecovered=.1
        #weigth for fitting data
        weigthCases=0.3
        weigthRecov=0.1
        #weightDeaths = 1 - weigthCases - weigthRecov

    if districtRegion1=="DRS 02 - Araçatuba":
        date="2020-04-01"
        #initial condition for susceptible
        s0=10.0e3
        #initial condition for exposed   
        e0=1e-4
        #initial condition for infectious   
        i0=2
        #initial condition for recovered
        r0=1e-4
        #initial condition for deaths   
        k0=1
        #initial condition for asymptomatic   
        a0=1e-4
        #start fitting when the number of cases >= start
        start=0
        #how many days is the prediction
        prediction_days=70
        #as recovered data is not available, so recovered is in function of death
        ratioRecovered=.1
        #weigth for fitting data
        weigthCases=0.4
        weigthRecov=0.0
        #weightDeaths = 1 - weigthCases - weigthRecov

    if districtRegion1=="DRS 09 - Marília":
        date="2020-04-01"
        #initial condition for susceptible
        s0=5.0e3
        #initial condition for exposed   
        e0=1e-4
        #initial condition for infectious   
        i0=1e-4
        #initial condition for recovered
        r0=1e-4
        #initial condition for deaths   
        k0=1e-4
        #initial condition for asymptomatic   
        a0=1e-4
        #start fitting when the number of cases >= start
        start=0
        #how many days is the prediction
        prediction_days=60
        #as recovered data is not available, so recovered is in function of death
        ratioRecovered=.08
        #weigth for fitting data
        weigthCases=0.4
        weigthRecov=0.0
        #weightDeaths = 1 - weigthCases - weigthRecov


    if districtRegion1=="DRS 07 - Campinas":
        date="2020-04-01"
        #initial condition for susceptible
        s0=20.0e3
        #initial condition for exposed   
        e0=1e-4
        #initial condition for infectious   
        i0=40
        #initial condition for recovered
        r0=1e-4
        #initial condition for deaths   
        k0=1e-4
        #initial condition for asymptomatic   
        a0=1e-4
        #start fitting when the number of cases >= start
        start=0
        #how many days is the prediction
        prediction_days=70
        #as recovered data is not available, so recovered is in function of death
        ratioRecovered=.1
        #weigth for fitting data
        weigthCases=0.5
        weigthRecov=0.1
        #weightDeaths = 1 - weigthCases - weigthRecov

    if districtRegion1=="DRS 11 - Presidente Prudente":
        date="2020-04-01"
        #initial condition for susceptible
        s0=5.0e3
        #initial condition for exposed   
        e0=1e-4
        #initial condition for infectious   
        i0=1e-4
        #initial condition for recovered
        r0=1e-4
        #initial condition for deaths   
        k0=1e-4
        #initial condition for asymptomatic   
        a0=1e-4
        #start fitting when the number of cases >= start
        start=0
        #how many days is the prediction
        prediction_days=60
        #as recovered data is not available, so recovered is in function of death
        ratioRecovered=.08
        #weigth for fitting data
        weigthCases=0.4
        weigthRecov=0.0
        #weightDeaths = 1 - weigthCases - weigthRecov

    if districtRegion1=="DRS 10 - Piracicaba":
        date="2020-04-01"
        #initial condition for susceptible
        s0=10.0e3
        #initial condition for exposed   
        e0=1e-4
        #initial condition for infectious   
        i0=2
        #initial condition for recovered
        r0=1e-4
        #initial condition for deaths   
        k0=1
        #initial condition for asymptomatic   
        a0=1e-4
        #start fitting when the number of cases >= start
        start=0
        #how many days is the prediction
        prediction_days=70
        #as recovered data is not available, so recovered is in function of death
        ratioRecovered=.1
        #weigth for fitting data
        weigthCases=0.4
        weigthRecov=0.0
        #weightDeaths = 1 - weigthCases - weigthRecov

    if districtRegion1=="DRS 12 - Registro":
        date="2020-04-01"
        #initial condition for susceptible
        s0=10.0e3
        #initial condition for exposed   
        e0=1e-4
        #initial condition for infectious   
        i0=1e-4
        #initial condition for recovered
        r0=1e-4
        #initial condition for deaths   
        k0=1e-4
        #initial condition for asymptomatic   
        a0=1e-4
        #start fitting when the number of cases >= start
        start=0
        #how many days is the prediction
        prediction_days=70
        #as recovered data is not available, so recovered is in function of death
        ratioRecovered=.08
        #weigth for fitting data
        weigthCases=0.4
        weigthRecov=0.0
        #weightDeaths = 1 - weigthCases - weigthRecov

    if districtRegion1=="DRS 14 - São João da Boa Vista":
        date="2020-04-01"
        #initial condition for susceptible
        s0=5.0e3
        #initial condition for exposed   
        e0=1e-4
        #initial condition for infectious   
        i0=1e-4
        #initial condition for recovered
        r0=1e-4
        #initial condition for deaths   
        k0=1e-4
        #initial condition for asymptomatic   
        a0=1e-4
        #start fitting when the number of cases >= start
        start=0
        #how many days is the prediction
        prediction_days=60
        #as recovered data is not available, so recovered is in function of death
        ratioRecovered=.08
        #weigth for fitting data
        weigthCases=0.4
        weigthRecov=0.0
        #weightDeaths = 1 - weigthCases - weigthRecov

    if districtRegion1=="DRS 15 - São José do Rio Preto":
        date="2020-04-01"
        #initial condition for susceptible
        s0=10.0e3
        #initial condition for exposed   
        e0=1e-4
        #initial condition for infectious   
        i0=1e-4
        #initial condition for recovered
        r0=1e-4
        #initial condition for deaths   
        k0=1e-4
        #initial condition for asymptomatic   
        a0=1e-4
        #start fitting when the number of cases >= start
        start=0
        #how many days is the prediction
        prediction_days=70
        #as recovered data is not available, so recovered is in function of death
        ratioRecovered=.08
        #weigth for fitting data
        weigthCases=0.4
        weigthRecov=0.0
        #weightDeaths = 1 - weigthCases - weigthRecov

    if districtRegion1=="DRS 14 - São João da Boa Vista":
        date="2020-04-01"
        #initial condition for susceptible
        s0=5.0e3
        #initial condition for exposed   
        e0=1e-4
        #initial condition for infectious   
        i0=1e-4
        #initial condition for recovered
        r0=1e-4
        #initial condition for deaths   
        k0=1e-4
        #initial condition for asymptomatic   
        a0=1e-4
        #start fitting when the number of cases >= start
        start=0
        #how many days is the prediction
        prediction_days=60
        #as recovered data is not available, so recovered is in function of death
        ratioRecovered=.08
        #weigth for fitting data
        weigthCases=0.4
        weigthRecov=0.0
        #weightDeaths = 1 - weigthCases - weigthRecov

    if districtRegion1=="DRS 16 - Sorocaba":
        date="2020-04-01"
        #initial condition for susceptible
        s0=1.0e3
        #initial condition for exposed   
        e0=1e-4
        #initial condition for infectious   
        i0=2
        #initial condition for recovered
        r0=1e-4
        #initial condition for deaths   
        k0=1
        #initial condition for asymptomatic   
        a0=1e-4
        #start fitting when the number of cases >= start
        start=0
        #how many days is the prediction
        prediction_days=70
        #as recovered data is not available, so recovered is in function of death
        ratioRecovered=.1
        #weigth for fitting data
        weigthCases=0.4
        weigthRecov=0.1
        #weightDeaths = 1 - weigthCases - weigthRecov

    if districtRegion1=="DRS 03 - Araraquara":
        date="2020-03-25"
        #initial condition for susceptible
        s0=5.0e3
        #initial condition for exposed   
        e0=1e-4
        #initial condition for infectious   
        i0=0
        #initial condition for recovered
        r0=1e-4
        #initial condition for deaths   
        k0=1e-4
        #initial condition for asymptomatic   
        a0=1e-4
        #start fitting when the number of cases >= start
        start=0
        #how many days is the prediction
        prediction_days=70
        #as recovered data is not available, so recovered is in function of death
        ratioRecovered=.1
        #weigth for fitting data
        weigthCases=0.4 
        weigthRecov=0.1
        #weightDeaths = 1 - weigthCases - weigthRecov

    if districtRegion1=="DRS 03 - Araraquara":
        date="2020-03-25"
        #initial condition for susceptible
        s0=2.0e3
        #initial condition for exposed   
        e0=1e-4
        #initial condition for infectious   
        i0=0
        #initial condition for recovered
        r0=1e-4
        #initial condition for deaths   
        k0=1e-4
        #initial condition for asymptomatic   
        a0=1e-4
        #start fitting when the number of cases >= start
        start=0
        #how many days is the prediction
        prediction_days=70
        #as recovered data is not available, so recovered is in function of death
        ratioRecovered=.1
        #weigth for fitting data
        weigthCases=0.5 
        weigthRecov=0.1
        #weightDeaths = 1 - weigthCases - weigthRecov

