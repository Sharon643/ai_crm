import Header from "../components/Header";
import { useAppSelector } from "../redux/hooks";
import "./VisitPlanner.css";

export default function VisitPlanner() {

    const visits = useAppSelector(
        state => state.planner.visits
    );

    return (
        <>
            <Header />

            <main className="visit-page">

                <h2>Today's Visit Plan</h2>

                {visits.map((v,index)=>(
                    <div
                        key={v.hcp_id}
                        className="visit-card"
                    >

                        <span>
                            #{index+1}
                        </span>

                        <h3>
                            {v.hcp_name}
                        </h3>

                        <p>
                            {v.hospital}
                        </p>

                        <div className={v.priority.toLowerCase()}>
                            {v.priority}
                        </div>

                        <p>

                            Score : {v.score}

                        </p>

                        <p>

                            {v.reason}

                        </p>

                    </div>
                ))}

            </main>
        </>
    );
}