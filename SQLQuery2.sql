select * from [portfolio project].dbo.['covid death)]
where continent is not null
order by 3,4


--select * from [portfolio project].dbo.['covid vaccinations$']
--order by 3,4


select location,date,total_cases, new_cases,total_deaths,population
from [portfolio project].dbo.['covid death)]


select location,date,total_cases,total_deaths, (total_deaths/total_cases)*100 as death_percentage
from [portfolio project].dbo.['covid death)]
where location like '%india%'
order by 1,2


select location,date,population,total_cases, (total_cases/population) *100 as case_percentage
from [portfolio project].dbo.['covid death)]
where location like '%india%'
order by 1,2

select location, Max(cast( total_deaths as int)) as totaldeathcount
 from[portfolio project].dbo.['covid death)]
 group by location
 order by totaldeathcount desc

 
 select location, Max(cast( total_cases as int)) as totalcasecount
 from[portfolio project].dbo.['covid death)]
 group by location
 order by totalcasecount desc

 ---showing continent with highest count of total case of covid

  select continent, Max(cast( total_cases as int)) as totalcasecount
 from[portfolio project].dbo.['covid death)]
 where continent is not null
 group by continent
 order by totalcasecount desc



 

 select date,location,sum(total_cases) as t_cases
 from [portfolio project].dbo.['covid death)]
 group by date,location
 


 select date,location, sum(new_cases) as n_cases
 from [portfolio project].dbo.['covid death)]
 group by date,location
 order by 1,2

 select sum(new_cases) as n_case,sum(cast(new_deaths as int) )as n_death,sum(cast(new_deaths as int) ) /sum(new_cases) *100 as death_percentage
 from [portfolio project].dbo.['covid death)]
 
 --TABLE 2--
 SELECT * FROM [portfolio project].dbo.['covid vaccinations$']
 
 select dea.continent,dea.location, dea.date,  dea.population, vacc.new_vaccinations
 ,sum(convert(int,vacc.new_vaccinations )) 
 over (partition by dea.location order by dea.location,dea.date) as book
 from[portfolio project].dbo.['covid death)] dea
  join[portfolio project].dbo.['covid vaccinations$'] vacc
 on   dea.location=vacc.location
 and  dea.date=vacc.date
 where dea.continent is not null
 order by 2,3
 
 
















