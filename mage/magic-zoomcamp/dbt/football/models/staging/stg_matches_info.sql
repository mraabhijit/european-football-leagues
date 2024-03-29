with 

source as (

    select * from {{ source('staging', 'matches_info') }}

),

renamed as (

    select
        league,
        league_id,
        matchday,
        match_id,
        match_date,
        match_referee

    from source

)

select * from renamed
