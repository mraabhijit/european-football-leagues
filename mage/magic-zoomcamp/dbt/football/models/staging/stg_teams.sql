with 

source as (

    select * from {{ source('staging', 'teams') }}

),

renamed as (

    select
        team_id,
        team,
        full_name,
        abbv,
        team_crest,
        address,
        country,
        year_founded,
        stadium,
        coach,
        coach_nationality

    from source

)

select * from renamed
