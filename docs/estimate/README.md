# estimate

## Description
Estimate the cost of a single or multi-component LLM project

## Synopsis
```
{-f|-d}
```

## Options

`-f FILE_PATH`
> Load the JSON project definition from path FILE_PATH

`-d JSON_STRING`
> Use the JSON project definition string JSON_STRING

## Project Definition JSON
```
{
   "project_name": "string",
   "components": [
      {
         "component_name": "string",
         "component_index": int,
         "model_id": "string",
         "n_input_tokens": int,
         "n_output_tokens": int,
         "recurrence": Optional[literal]
      },
   ]
}
```

- *project_name* **_(str)_**: Name for the project
- *components* **_(list[object])_**:  
  - *component_name* **_(str)_**: Name for the component
  - *component_index* **_(int)_**: Index of component within project
  - *model_id* **_(str)_**: Unique model identifier for component model
  - *n_input_tokens* **_(int)_**: Number of input tokens for component
  - *n_output_tokens* **_(int)_**: Number of output tokens for component
  - *occurrence* **_(Optional[literal])_**: How often this component will be run with the given parameters. One of {'daily', 'weekly', 'monthly', 'yearly'}. Components with this parameter omitted will be treated as one-time costs

    
**Response**:
```
{
    "estimate": {
        "project_name": "string",
        "components":[
            {
                 "component_index": int,
                 "component_name":"string",
                 "n_input_tokens": int,
                 "n_output_tokens": int,
                 "llm":{
                    "provider_id": "string",
                    "provider_name_pretty": "string",
                    "model_id": "string",
                    "model_name_pretty": "string",
                    "cost_per_1k_input_tokens": float,
                    "cost_per_1k_output_tokens": float
                 },
                 "recurrence": "string",
                 "cost":{
                    "daily_input_cost": float,
                    "weekly_input_cost": float,
                    "monthly_input_cost": float,
                    "yearly_input_cost": float,
                    "one_time_input_cost": float,
                    "daily_output_cost": float,
                    "weekly_output_cost": float,
                    "monthly_output_cost": float,
                    "yearly_output_cost": float,
                    "one_time_output_cost": float,
                    "daily_total_cost": float,
                    "weekly_total_cost": float,
                    "monthly_total_cost": float,
                    "yearly_total_cost": float,
                    "one_time_total_cost": float
                 }
            },
        ],
        "cost":{
          "daily_input_cost": float,
          "weekly_input_cost": float,
          "monthly_input_cost": float,
          "yearly_input_cost": float,
          "one_time_input_cost": float,
          "daily_output_cost": float,
          "weekly_output_cost": float,
          "monthly_output_cost": float,
          "yearly_output_cost": float,
          "one_time_output_cost": float,
          "daily_total_cost": float,
          "weekly_total_cost": float,
          "monthly_total_cost": float,
          "yearly_total_cost": float,
          "one_time_total_cost": float
        }
    }
}
```
- *project_name* **_(str)_**: Name for the project
- *components* **_(list[object])_**:  
  - *component_name* **_(string)_**: Name for the component  
  - *component_index* **_(int)_**: Index of component within project
  - *n_input_tokens* **_(int)_**: Number of input tokens for component
  - *n_output_tokens* **_(int)_**: Number of output tokens for component
  - *llm* **_(object)_**:
    - *provider_id* **_(str)_**: Unique provider identifier
    - *provider_name_pretty* **_(str)_**: Provider display name
    - *model_id* **_(str)_**: Unique model identifier 
    - *model_name_pretty* **_(str)_**: Model display name
    - *cost_per_1k_input_tokens* **_(float)_**: Model cost per 1000 input tokens
    - *cost_per_1k_output_tokens* **_(float)_**: Model cost per 1000 output tokens
  - *recurrence* **_(literal)_**: How often this component will be run with the given parameters. One of {'daily', 'weekly', 'monthly', 'yearly'}. Components with this parameter omitted will be treated as one-time costs
  - *cost* **_(object)_**: 
    - *daily_input_cost* **_(float)_**: daily cost for token input
    - *weekly_input_cost* **_(float)_**: weekly cost for token input
    - *monthly_input_cost* **_(float)_**: monthly cost for token input
    - *yearly_input_cost* **_(float)_**: yearly cost for token input
    - *one_time_input_cost* **_(float)_**: one-time token input cost
    - *daily_output_cost* **_(float)_**: daily cost for token output
    - *weekly_output_cost* **_(float)_**: weekly cost for token output
    - *monthly_output_cost* **_(float)_**: monthly cost for token output
    - *yearly_output_cost* **_(float)_**: yearly cost for token output
    - *one_time_output_cost* **_(float)_**: one-time token output cost
    - *daily_total_cost* **_(float)_**: daily total cost 
    - *weekly_total_cost* **_(float)_**: weekly total cost
    - *monthly_total_cost* **_(float)_**: monthly total cost
    - *yearly_total_cost* **_(float)_**: yearly total cost
    - *one_time_total_cost* **_(float)_**: one-time total cost
- *cost* **_(object)_**: 
    - *daily_input_cost* **_(float)_**: project daily cost for token input
    - *weekly_input_cost* **_(float)_**: project weekly cost for token input
    - *monthly_input_cost* **_(float)_**: project monthly cost for token input
    - *yearly_input_cost* **_(float)_**: project yearly cost for token input
    - *one_time_input_cost* **_(float)_**: project one-time token input cost
    - *daily_output_cost* **_(float)_**: project daily cost for token output
    - *weekly_output_cost* **_(float)_**: project weekly cost for token output
    - *monthly_output_cost* **_(float)_**: project monthly cost for token output
    - *yearly_output_cost* **_(float)_**: project yearly cost for token output
    - *one_time_output_cost* **_(float)_**: project one-time token output cost
    - *daily_total_cost* **_(float)_**: project daily total cost 
    - *weekly_total_cost* **_(float)_**: project weekly total cost
    - *monthly_total_cost* **_(float)_**: project monthly total cost
    - *yearly_total_cost* **_(float)_**: project yearly total cost
    - *one_time_total_cost* **_(float)_**: project one-time total cost
  

## Examples
**Body**:  
```
{
   "project_name": "my llm project",
   "components":[
      {
         "component_name": "my-component-00",
         "component_index": 0,
         "model_id": "openai.text-embedding-3-small",
         "n_input_tokens": 10000000,
         "n_output_tokens": 0
      },
      {
         "component_name": "my-component-01",
         "component_index": 1,
         "model_id": "anthropic.claude-3.5-sonnet.bedrock",
         "n_input_tokens": 10000000,
         "n_output_tokens": 50000000,
         "recurrence": "monthly"
      }
   ]
}
```

**Response**:
```
{
   "estimate":{
      "project_name":"my llm project",
      "components":[
         {
            "component_index":0,
            "component_name":"my-component-00",
            "n_input_tokens":10000000,
            "n_output_tokens":0,
            "llm":{
               "provider_id":"openai",
               "provider_name_pretty":"OpenAI",
               "model_id":"openai.text-embedding-3-small",
               "model_name_pretty":"Text Embedding 3 Small",
               "cost_per_1k_input_tokens":2e-05,
               "cost_per_1k_output_tokens":0.0
            },
            "recurrence":"None",
            "cost":{
               "daily_input_cost":0.0,
               "weekly_input_cost":0.0,
               "monthly_input_cost":0.0,
               "yearly_input_cost":0.0,
               "one_time_input_cost":0.2,
               "daily_output_cost":0.0,
               "weekly_output_cost":0.0,
               "monthly_output_cost":0.0,
               "yearly_output_cost":0.0,
               "one_time_output_cost":0.0,
               "daily_total_cost":0.0,
               "weekly_total_cost":0.0,
               "monthly_total_cost":0.0,
               "yearly_total_cost":0.0,
               "one_time_total_cost":0.2
            }
         },
         {
            "component_index":1,
            "component_name":"my-component-01",
            "n_input_tokens":10000000,
            "n_output_tokens":50000000,
            "llm":{
               "provider_id":"anthropic",
               "provider_name_pretty":"Anthropic",
               "model_id":"anthropic.claude-3.5-sonnet.bedrock",
               "model_name_pretty":"Claude 3.5 Sonnet (AWS Bedrock)",
               "cost_per_1k_input_tokens":0.003,
               "cost_per_1k_output_tokens":0.015
            },
            "recurrence":"monthly",
            "cost":{
               "daily_input_cost":0.9856262833675564,
               "weekly_input_cost":6.8993839835728945,
               "monthly_input_cost":30.0,
               "yearly_input_cost":360.0,
               "one_time_input_cost":0.0,
               "daily_output_cost":24.640657084188913,
               "weekly_output_cost":172.48459958932239,
               "monthly_output_cost":750.0,
               "yearly_output_cost":9000.0,
               "one_time_output_cost":0.0,
               "daily_total_cost":25.626283367556468,
               "weekly_total_cost":179.38398357289526,
               "monthly_total_cost":780.0,
               "yearly_total_cost":9360.0,
               "one_time_total_cost":0.0
            }
         }
      ],
      "cost":{
         "daily_input_cost":0.9856262833675564,
         "weekly_input_cost":6.8993839835728945,
         "monthly_input_cost":30.0,
         "yearly_input_cost":360.0,
         "one_time_input_cost":0.2,
         "daily_output_cost":24.640657084188913,
         "weekly_output_cost":172.48459958932239,
         "monthly_output_cost":750.0,
         "yearly_output_cost":9000.0,
         "one_time_output_cost":0.0,
         "daily_total_cost":25.626283367556468,
         "weekly_total_cost":179.38398357289526,
         "monthly_total_cost":780.0,
         "yearly_total_cost":9360.0,
         "one_time_total_cost":0.2
      }
   }
}
```